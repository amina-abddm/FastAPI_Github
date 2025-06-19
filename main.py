from fastapi import FastAPI
from api.routes import router  # import des router défini dans routes.py

app = FastAPI()

# 🔗 Enregistre les routes
app.include_router(router)

# 🏠 Route de base
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API des utilisateurs ! Utilisez /docs pour explorer les routes."}

