import json

with open('AllSets.json', encoding='latin-1') as json_data:
    all_sets = json.load(json_data)
    for set_code in all_sets:
        for a_card in all_sets[set_code]['cards']:
            if 'power' in a_card:
                print(a_card['name'])
                print(a_card['power'])
