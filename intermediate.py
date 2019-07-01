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
except:
    try:
        with open('inputs/input_test.csv', encoding='utf-8-sig') as csvfile: 
            reader = csv.DictReader(csvfile, delimiter=',')
            
            for row in reader:
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
        
    
                    