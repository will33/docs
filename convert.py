import json

with open("openapi.json", "r") as f:
    data = json.load(f)

# Remove trailing slash from servers
for server in data["servers"]:
    if server["url"][-1] == '/':
        server["url"] = server["url"][:-1]

with open("openapi.json", "w") as f:
    json.dump(data, f, indent=2)
