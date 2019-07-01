import csv
import ast
import json
import Group

# list of cluster list with local cluster as first element
all_cluster_lists = []
# update airport radius
airport_radius = 0
try:
    with open('inputs/arguments.csv', encoding='utf-8-sig') as csvfile: 
        reader = csv.DictReader(csvfile, delimiter=',')
        #create the list of ungrouped addresses
        for row in reader:
            airport_radius = row['airport_radius']
    with open('inputs/groupings.csv', encoding='utf-8-sig') as csvfile: 
            reader = csv.DictReader(csvfile, delimiter=',')
            
            for row in reader:
                print(reader.line_num)
                if row['remote_cluster'] == 'N/A':
                    continue
                else:
                    cluster_list = []
                    patent_id = row['patent_id']
                    # local cluster
                    local_dict = ast.literal_eval(row['local_cluster'])
                    local_lat = local_dict['center_lat']
                    local_lon = local_dict['center_lng']
            
                    is_local = True
                    local_cluster = Group.group(is_local, patent_id, airport_radius, local_lat, local_lon)
                    cluster_list.append(local_cluster)
                    
                    # remote clusters
                    
                    remote_dict_list = ast.literal_eval(row['remote_cluster'])
               
                    for remote_dict in remote_dict_list:
                        remote_lat = remote_dict['center_lat']
                        remote_lon = remote_dict['center_lng']
                        is_local = False
                        remote_cluster = Group.group(is_local, patent_id, airport_radius, remote_lat, remote_lon)
                     
                        cluster_list.append(remote_cluster)
                    all_cluster_lists.append(cluster_list)
except:
    # when no arguments updated for arguments.csv
    try:
        with open('inputs/groupings.csv', encoding='utf-8-sig') as csvfile: 
            reader = csv.DictReader(csvfile, delimiter=',')
            
            for row in reader:
                if row['remote_cluster'] == 'N/A':
                    continue
                else:
                    cluster_list = []
                    patent_id = row['patent_id']
                    airport_radius = row['airport_radius']
                    # local cluster
                    local_dict = ast.literal_eval(row['local_cluster'])
                    local_lat = local_dict['center_lat']
                    local_lon = local_dict['center_lng']
                    is_local = True
                    local_cluster = Group.group(is_local, patent_id, airport_radius, local_lat, local_lon)
                    cluster_list.append(local_cluster)
                    
                    # remote clusters
                    remote_dict_list = ast.literal_eval(row['remote_cluster'])
               
                    for remote_dict in remote_dict_list:
                        remote_lat = remote_dict['center_lat']
                        remote_lon = remote_dict['center_lng']
                        is_local = False
                        remote_cluster = Group.group(is_local, patent_id, airport_radius, local_lat, local_lon)
                        cluster_list.append(remote_cluster)
                    all_cluster_lists.append(cluster_list)
            
    except:
        print("enter airport radius")
        
with open('outputs/pairings.csv', 'w', newline="\n", encoding = 'utf-8-sig') as output_csv:
    writer = csv.writer(output_csv, delimiter=',')
    header = ['a', 'b', 'a_radius', 'b_radius', 'a_lat', 'a_lng', 'b_lat', 'b_lng', 'local_remote']
    writer.writerow(header)
    
    for cluster_list in all_cluster_lists:
        local_cluster = cluster_list[0]
        for i in range(1, len(cluster_list)):
            #this will match all remotes with the local cluster
            writer.writerow([local_cluster.get_name() + '_L',
                            cluster_list[i].get_name() + '_R' + str(i),
                            local_cluster.get_airport_radius(),
                            cluster_list[i].get_airport_radius(),
                            local_cluster.get_coordinates()[0],
                            local_cluster.get_coordinates()[1],
                            cluster_list[i].get_coordinates()[0],
                            cluster_list[i].get_coordinates()[1],
                            "1"])
            
        for i in range(1, len(cluster_list)-1):
            #this will match all remotes with each other
            remote_cluster1 = cluster_list[i]
            
            for j in range(i+1, len(cluster_list)):
                remote_cluster2 = cluster_list[j]
                
                writer.writerow([remote_cluster1.get_name() + '_R' + str(i),
                            remote_cluster2.get_name() + '_R' + str(j),
                            remote_cluster1.get_airport_radius(),
                            remote_cluster2.get_airport_radius(),
                            remote_cluster1.get_coordinates()[0],
                            remote_cluster1.get_coordinates()[1],
                            remote_cluster2.get_coordinates()[0],
                            remote_cluster2.get_coordinates()[1],
                            "0"])
                

