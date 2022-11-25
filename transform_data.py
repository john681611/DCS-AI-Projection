import gzip
import json

file = "Caucasus"
a_file = gzip.open(f"Original_data/{file}.json.gz", "rb")
contents = json.loads(a_file.read())

lst = []
for key in contents:
    key_parts = key.split(",")
    lst.append({
        "test": {
            "x": float(key_parts[0].replace("x:", "")),
            "y": float(key_parts[1].replace("z:", "")),
        },
        "input": {
            "x": float(contents[key]['x']),
            "y": float(contents[key]['y'])
        },
    })
with gzip.open(f"Transformed_data/{file}.json.gz", 'wt') as f:
    f.write(json.dumps(lst))
