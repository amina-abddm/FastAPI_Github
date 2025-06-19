import json

filepath = "data/filtered_users.json"

# Charger les utilisateurs depuis le fichier JSON
with open(filepath, "r", encoding="utf-8") as f:
    USERS = json.load(f)
    print(f"✅ {len(USERS)} utilisateurs chargés depuis {filepath}")

