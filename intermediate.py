



with open('inputs/input.csv', encoding='utf-8-sig') as csv_file: 
        reader = csv.DictReader(csvfile, delimiter=',')
        
        for row in reader:
            patent_id = row['patent_id']
            
            local_lat = row['local_cluster']