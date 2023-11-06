import json

with open("openapi.json", "r") as f:
    data = json.load(f)

with open("openapi.json", "w") as f:
    json.dump(data, f, indent=2)
