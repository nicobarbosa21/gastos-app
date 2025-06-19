from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.categoria import Categoria

class Gasto(Base):
    __tablename__ = "gastos"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String, index=True, nullable=False)
    monto = Column(Integer, nullable=False)
    fecha = Column(DateTime, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"),nullable=False)

    categoria = relationship("Categoria", backref="gastos")