from fastapi import FastAPI
from app.views import gasto_views
from app.views import categoria_views

#Archivo de prueba para swagger
app = FastAPI()
app.include_router(gasto_views.router)
app.include_router(categoria_views.router)