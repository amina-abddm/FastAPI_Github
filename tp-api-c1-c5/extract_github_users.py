import requests
import time
import json
import os
from dotenv import load_dotenv

# Charger le token depuis .env
load_dotenv()
token = os.getenv ("GITHUB_TOKEN")

headers = {
    "Authorization": f"token {token}",
    "User-Agent": "GitHub API Script"
}

url = "https://api.github.com/users"
search_url = "https://api.github.com/search/users"


def get_user_details(login):
    try:
        response = requests.get(f"{url}/{login}", headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Erreur {response.status_code} pour {login}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur réseau : {e}")
    return None

def handle_rate_limit(response):
    if response.status_code == 403:
        reset_time = int(response.headers.get("X-RateLimit-Reset", time.time()))
        wait_time = max(0, reset_time - int(time.time()))
        print(f"⏳ Quota dépassé, pause de {wait_time}s...")
        time.sleep(wait_time + 1)

def get_all_users(target_count=300):
    all_users = []
    page = 1
    
    while len(all_users) < target_count:
        params = {
            "q":"created:>2015-01-01",
            "per_page": 30,
            "page": page
        }
        
        try:
                response = requests.get(search_url, headers=headers,params=params)
                handle_rate_limit(response)
        
                if response.status_code == 403:
                    handle_rate_limit(response)
                    continue

                if response.status_code != 200:
                    print(f"Erreur {response.status_code} lors de la récupération des utilisateurs")
                    break
                
                data = response.json()
                users = data.get("items", [])
                
        except requests.exceptions.RequestException as e:
            print(f"Erreur réseau pendant la recherche : {e}")
            break
        
        except ValueError:
                print("❌ Erreur de décodage JSON.")
                break
        
        if not users:
            print("Aucun utilisateur trouvé.")
            break

        for user in users:
            if len(all_users) >= target_count:
                break

            details = get_user_details(user["login"])
                    
            if details:
                all_users.append({
                    "login": details["login"],
                    "id": details["id"],
                    "avatar_url": details["avatar_url"],
                    "created_at": details["created_at"],
                    "bio": details["bio"]
                })
                
        print(f"📦 Page {page} traitée — total actuel : {len(all_users)}")
        page += 1  # Passer à la page suivante
            
    return all_users
    
    
def main():
    users = get_all_users(target_count = 300 )  # Récupérer 300 utilisateurs
    
    for user in users:
            
            print("Login:", user['login'])
            print("ID:", user['id'])
            print("Avatar URL:", user['avatar_url'])
            print("Date de création:", user['created_at'])
            print("Bio:", user['bio'])
            print("-" * 40)
                
# 💾 Sauvegarde des données brutes dans users.json
    with open("tp-api-c1-c5/users.json", "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)

    print("✅ Données sauvegardées dans users.json")
    
if __name__ == "__main__":
    main()