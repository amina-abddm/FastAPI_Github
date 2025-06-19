from fastapi import FastAPI
from routes import router  # <- importe le router défini dans routes.py

app = FastAPI()

# 🔗 Enregistre les routes
app.include_router(router)


