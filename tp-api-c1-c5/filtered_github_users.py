import json
from datetime import datetime

# 🧩 Étape 1 — Charger les données JSON
def load_users(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        users = json.load(f)
    print(f"✅ {len(users)} utilisateurs chargés depuis {filepath}")
    return users

# Appel de la fonction avec le chemin du fichier JSON
load_users("tp-api-c1-c5/users.json")

# 🧹 Étape 2 — Suppression des doublons (id unique)
def remove_duplicates(users):
    unique = {}
    for user in users:
        unique[user['id']] = user
    print(f"🗑️ {len(users) - len(unique)} doublons supprimés.")
    return list(unique.values())


# 🚦 Étape 3 — Filtrer les utilisateurs valides
def filter_users(users):
    date_limit = datetime(2015, 1, 1)
    filtered = []
    
    count_bio = 0
    count_avatar = 0
    count_date = 0
    
    for user in users:
        bio = user.get("bio")
        avatar_url = user.get("avatar_url")
        created_at_str = user.get("created_at")
        
        
        
    # Vérifier que bio et avatar_url existent
        if bio:
            count_bio += 1
        else:
            continue
        
        if avatar_url:
            count_avatar += 1
        else:
            continue

    # Vérifier la date de création
        try:
            created_at = datetime.strptime(created_at_str, "%Y-%m-%dT%H:%M:%SZ")
            if created_at > date_limit:
                count_date += 1
            
        # Conserver uniquement les champs utiles et postérieur à 2015
                filtered.append({
                "login": user["login"],
                "id": user["id"],
                "created_at": user["created_at"],
                "avatar_url": user["avatar_url"],
                "bio": user["bio"]
        })
        except Exception :
            continue  # Ignorer les dates mal formatées
            
    print(f"Utilisateur avec bio : {count_bio}")
    print(f"Utilisateur avec avatar : {count_avatar}")
    print(f"Utilisateur avec date de création postérieure à 2015 : {count_date}")
        
        
    print(f"✅ {len(filtered)} utilisateurs conservés après filtrage.")
    return filtered

# 💾 Étape 4 — Sauvegarder dans un fichier JSON propre
def save_filtered_users(users, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)
    print(f"📁 Fichier enregistré dans {output_path}")

# 📊 Étape 5 — Résumé final
def summarize(original_count, unique_count, filtered_count):
    print("\n📊 Résumé :")
    print(f"Utilisateurs chargés        : {original_count}")
    print(f"Doublons supprimés          : {original_count - unique_count}")
    print(f"Utilisateurs après filtrage : {filtered_count}")

# 🧪 Fonction principale
def main():
    filepath = "tp-api-c1-c5/users.json"  
    output_path = "data/filtered_users.json"
    
    users = load_users(filepath)
    original_count = len(users)

    users = remove_duplicates(users)
    unique_count = len(users)

    filtered = filter_users(users)
    filtered_count = len(filtered)

    save_filtered_users(filtered, output_path)
    summarize(original_count, unique_count, filtered_count)

# ✅ Exécution du script
if __name__ == "__main__":
    main()