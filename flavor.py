import json

with open('AllSets.json', encoding='latin-1') as json_data:
    all_sets = json.load(json_data)
    print (all_sets["UNH"]["cards"][2]['name'])
    print (all_sets["UNH"]["cards"][2]['flavor'])
        
