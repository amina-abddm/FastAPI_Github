import json

# 🔽 Charger les données sur les utilisateurs depuis le fichier JSON
filepath = "data/filtered_users.json"

with open(filepath, "r", encoding="utf-8") as f:
    USERS = json.load(f)
    print(f"✅ {len(USERS)} utilisateurs chargés depuis {filepath}")

