from sqlalchemy.orm import Session
from app.dtos.categoria_dto import CategoriaCreateDTO, CategoriaUpdateDTO, CategoriaResponseDTO
import app.services.categoria_service as categoria_service

def create_categoria(db: Session, categoria: CategoriaCreateDTO) -> CategoriaResponseDTO:
    return categoria_service.create_categoria(db, categoria)

def update_categoria(db: Session, categoria_id: int, categoria: CategoriaUpdateDTO) -> CategoriaResponseDTO:
    return categoria_service.update_categoria(db, categoria_id, categoria)

def delete_categoria(db: Session, categoria_id: int) -> None:
    categoria_service.delete_categoria(db, categoria_id)

def get_categoria(db: Session, categoria_id: int) -> CategoriaResponseDTO:
    return categoria_service.get_categoria(db, categoria_id)

def get_all_categorias(db: Session) -> list[CategoriaResponseDTO]:
    return categoria_service.get_all_categorias(db)

def get_categorias_by_name(db: Session, name: str) -> list[CategoriaResponseDTO]:
    return categoria_service.get_categorias_by_name(db, name)
