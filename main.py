from fastapi import APIRouter
from api.routes import router  # import des router défini dans routes.py
from api.security import verify_token  # import de la fonction de vérification du token
from api.models import User  # import du modèle User

app = APIRouter()

# 🔗 Enregistre les routes
app.include_router(router)
