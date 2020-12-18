import json

VALUES_ATTR = 'Values'

def json_reader(filename, collection):
    with open(filename, 'r', encoding='utf-8-sig') as json_file:
        json_data = json.load(json_file)

    values = json_data[VALUES_ATTR]
    for value in values:
        collection.append(value)