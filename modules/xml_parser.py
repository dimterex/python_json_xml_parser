import xmltodict
import json

VALUES_ATTR = 'Values'
VALUE_ATTR = 'Value'
ROOT_ATTR = 'Root'


def xml_reader(filename, collection):
    with open(filename, 'r', encoding='utf-8-sig') as myfile:
        obj = xmltodict.parse(myfile.read())
    json_data = json.dumps(obj)

    json_obj = json.loads(json_data)

    values = json_obj[ROOT_ATTR][VALUES_ATTR][VALUE_ATTR]
    for value in values:
        collection.append(value)