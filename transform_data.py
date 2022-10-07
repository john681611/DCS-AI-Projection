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
            "x": key_parts[0].replace("x:", ""),
            "y": key_parts[1].replace("z:", ""),
        },
        "input": contents[key],
    })
with gzip.open(f"Transformed_data/{file}.json.gz", 'wt') as f:
    f.write(json.dumps(lst))
