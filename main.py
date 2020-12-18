import json
import os
import xmltodict
from collections import Counter

VALUES_ATTR = 'Values'
VALUE_ATTR = 'Value'
ROOT_ATTR = 'Root'

collection = []

def json_reader(filename):
    with open(filename, 'r', encoding='utf-8-sig') as json_file:
        json_data = json.load(json_file)

    values = json_data[VALUES_ATTR]
    for value in values:
        collection.append(value)


def xml_reader(filename):
    with open(filename, 'r', encoding='utf-8-sig') as myfile:
        obj = xmltodict.parse(myfile.read())
    json_data = json.dumps(obj)

    json_data1 = json.loads(json_data)

    values = json_data1[ROOT_ATTR][VALUES_ATTR][VALUE_ATTR]
    for value in values:
        collection.append(value)


def main():
    files = os.listdir()
    for file in files:
        if (file.endswith('.json')):
            json_reader(file)

        if (file.endswith('.xml')):
            xml_reader(file)

    print(Counter(collection))


if __name__ == '__main__':
    main()