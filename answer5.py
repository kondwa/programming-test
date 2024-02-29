import os
import json
import re

def find_uuids_in_json(file_path):
    uuids = set()
    with open(file_path, 'r') as file:
        data = json.load(file)
        if isinstance(data, list):
            for item in data:
                if isinstance(item, str) and re.match(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', item):
                    uuids.add(item)
    return uuids

def find_uuids_in_directory(directory):
    uuids = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                uuids.update(find_uuids_in_json(file_path))
    return uuids

directory_path = 'uuids'
all_uuids = find_uuids_in_directory(directory_path)

print("UUIDs found in JSON files:")
for uuid_str in all_uuids:
    print(uuid_str)
