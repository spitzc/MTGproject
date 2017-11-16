import json

with open('AllSets-x.json', encoding='latin-1') as json_data:
    all_sets = json.load(json_data)
    for set_code in all_sets:
        for element_name in all_sets[set_code]: 
            print(element_name)
        
