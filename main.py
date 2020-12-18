import os

from collections import Counter
from modules.json_parser import *
from modules.xml_parser import *


collection = []


def main():
    files = os.listdir()
    for file in files:
        if (file.endswith('.json')):
            json_reader(file, collection)

        if (file.endswith('.xml')):
            xml_reader(file, collection)

    print(Counter(collection))


if __name__ == '__main__':
    main()