from app.database import Base, engine
from app.models.categoria import Categoria
from app.models.gasto import Gasto
from app.database import SessionLocal

Base.metadata.create_all(bind=engine)

categorias = [
  "Salud",
  "Farmacia",
  "Transporte",
  "Vehículo",
  "Deporte",
  "Supermercado",
  "Verdulería",
  "Carnes",
  "Panadería",
  "Snacks",
  "Comida Pedida",
  "Ropa",
  "Donaciones",
  "Servicios Básicos",
  "Servicios de Entretenimiento",
  "Belleza",
  "Viajes y turismo",
  "Ocio",
  "Hogar",
  "Educación",
  "Mascota",
  "Alquiler",
  "Ferretería",
  "Regalos",
  "Tecnología/Electrónica",
  "Otros / Varios"
]

db = SessionLocal()
for nombre in categorias:
    if not db.query(Categoria).filter(Categoria.nombre == nombre).first():
        db.add(Categoria(nombre=nombre))
db.commit()