from fastapi import FastAPI
from api.routes import router  # import des router défini dans routes.py

app = FastAPI()

# 🔗 Enregistre les routes
app.include_router(router)
