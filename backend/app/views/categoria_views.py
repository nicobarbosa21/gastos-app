from fastapi import APIRouter, Depends, status
from fastapi.responses import Response
from sqlalchemy.orm import Session
from app.controllers import categoria_controller
from app.database import get_db
from app.dtos.categoria_dto import CategoriaCreateDTO, CategoriaUpdateDTO, CategoriaResponseDTO
from typing import List

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.post("/", response_model=categoria_controller.CategoriaResponseDTO)
def create_categoria(categoria: categoria_controller.CategoriaCreateDTO, db: Session = Depends(get_db)):
    return categoria_controller.create_categoria(db, categoria)

@router.put("/{categoria_id}", response_model=categoria_controller.CategoriaResponseDTO)
def update_categoria(categoria_id: int, categoria: categoria_controller.CategoriaUpdateDTO, db: Session = Depends(get_db)):
    return categoria_controller.update_categoria(db, categoria_id, categoria)

@router.delete("/{categoria_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria_controller.delete_categoria(db, categoria_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get("/search", response_model=List[CategoriaResponseDTO])
def search_categoria(nombre: str, db: Session = Depends(get_db)):
    return categoria_controller.get_categorias_by_name(db, nombre)

@router.get("/{categoria_id}", response_model=categoria_controller.CategoriaResponseDTO)
def get_categoria(categoria_id: int, db: Session = Depends(get_db)):
    return categoria_controller.get_categoria(db, categoria_id)

@router.get("/", response_model=list[categoria_controller.CategoriaResponseDTO])
def get_all_categorias(db: Session = Depends(get_db)):
    return categoria_controller.get_all_categorias(db)

