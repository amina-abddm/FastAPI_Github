import os
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

# 🔒 Charger les variables d'environnement depuis le fichier .env
load_dotenv()
security = HTTPBasic()

# 🛡️ Fonction de vérification des identifiants de l'utilisateur
def verify_token(credentials: HTTPBasicCredentials = Depends(security)):
    """
    Vérifie les identifiants de l'utilisateur.
    """
    correct_username = os.getenv ("ADMIN_USERNAME")
    correct_password = os.getenv ("ADMIN_PASSWORD")

   
    if not (secrets.compare_digest(credentials.username, correct_username) and
            secrets.compare_digest(credentials.password, correct_password)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Identifiants incorrects",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


