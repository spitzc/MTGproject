import json, re

with open('AllSets.json', encoding='latin-1') as json_data:
    all_sets = json.load(json_data)
    text_data = []
    for set_code in all_sets:
        for a_card in all_sets['ISD']['cards']:
            if 'flavor' in a_card:
                all_set_text = a_card['flavor'].lower()
                set_text = re.findall(r"[\w']+|[.,!?;]", all_set_text)
                text_data.append(set_text[0])
                

json.dump(text_data, open('Innistrad_data.json', 'w'),indent=4)