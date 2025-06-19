from fastapi import Header, HTTPException

# 🛡️ Mettre en place une sécurité de base avec token
def verify_token(authorization: str = Header(None)):
    if authorization != "mon_token_secret":
        raise HTTPException(status_code=401, detail="Unauthorized")
