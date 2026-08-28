import json

with open("databse.json", "r") as f:
    website = json.load(f)

with open("apps.json", "r") as f:
    apps = json.load(f)

#combine the two dictionaries
database = {
    "websites": website,
    "apps": apps
}

with open("database.json", "w") as f:
    json.dump(database, f)

print("Database merged and saved to database.json")    