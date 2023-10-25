import json

with open("openapi.json", "r") as f:
    data = json.load(f)

data["components"]["securitySchemes"]["OAuth2PasswordBearer"] = {
    "type": "http",
    "scheme": "bearer",
}

with open("openapi.json", "w") as f:
    json.dump(data, f, indent=2)
