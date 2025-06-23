from fastapi import FastAPI
from app.views import gasto_views
from app.views import categoria_views
from fastapi.middleware.cors import CORSMiddleware
from app.views import chat_view

#Archivo de prueba para swagger
app = FastAPI()

# Middleware CORS (habilita llamadas desde el frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Podés reemplazar con ["http://localhost:3000"] si querés limitarlo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar las rutas del chat
app.include_router(chat_view.router, prefix="")
app.include_router(gasto_views.router)
app.include_router(categoria_views.router)

# Opción opcional de ruta base para probar que funciona
@app.get("/")
def read_root():
    return {"status": "online", "message": "API de chat financiero lista"}
