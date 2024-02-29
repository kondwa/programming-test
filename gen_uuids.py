import uuid
import json

num_uuids = 5
uuids = [str(uuid.uuid4()) for _ in range(num_uuids)]

output_file = "uuids\\sub\\one.json"
with open(output_file, 'w') as f:
    json.dump(uuids, f, indent=4)