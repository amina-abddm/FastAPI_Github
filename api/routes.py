import json
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from .models import User
from .security import verify_token

# 🔽 Charger les données sur les utilisateurs depuis le fichier JSON
filepath = "data/filtered_users.json"

with open(filepath, "r", encoding="utf-8") as f:
    USERS = json.load(f)
    print(f"✅ {len(USERS)} utilisateurs chargés depuis {filepath}")

router = APIRouter(dependencies=[Depends(verify_token)]) 

# ✅ Route 1 : GET /users/
@router.get("/users")

def get_all_users(user:str = Depends(verify_token)):
    print("📥 Requête reçue : liste complète des utilisateurs")
    return USERS

# 🔍 Route 2 : GET /users/{login}
@router.get("/users/{login}")

def get_user_by_login(login: str, user:str = Depends(verify_token)):
    for user in USERS:
        print(f"🔍 Requête reçue : recherche de l'utilisateur avec le login '{login}'")
        if user["login"].lower() == login.lower():
            print(f"✅ Utilisateur trouvé : {user['login']}")
            return user
    print(f"❌ Utilisateur non trouvé : {login}")
    raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

#🧠 Route 3 : GET /users/search?q=...
@router.get("/users/search")

def search_users(q: str, user:str = Depends(verify_token)):
    print(f"🔍 Requête reçue : recherche du mot-clé '{q}' dans login, bio, created_at")
    q_lower = q.lower()
    results = []
    
    # Recherche dans login, bio et created_at
    for user in USERS:      
        if (q_lower in user.get("login","").lower() or 
            q_lower in user.get("bio", "").lower() or 
            q_lower in user.get("created_at", "").lower()):
            
            results.append(user)
    print(f"✅ {len(results)} utilisateurs trouvés pour '{q}'")
    
    if not results:
        print(f"❌ Aucun utilisateur trouvé pour '{q}'")
        raise HTTPException(status_code=404, detail="Aucun utilisateur trouvé")
    
    return results
