from fastapi import APIRouter, Depends, status
from fastapi.responses import Response
from sqlalchemy.orm import Session
from app.controllers import gasto_controller
from app.dtos.gasto_dto import GastoCreateDTO, GastoUpdateDTO, GastoResponseDTO, GastoDeleteDTO
from app.database import get_db

router = APIRouter(prefix="/gastos", tags=["Gastos"])

@router.post("/", response_model=GastoResponseDTO)
def create_gasto(gasto: GastoCreateDTO, db: Session = Depends(get_db)) -> GastoResponseDTO:
    return gasto_controller.create_gasto(db, gasto)

@router.put("/{gasto_id}", response_model=GastoResponseDTO)
def update_gasto(gasto_id: int, gasto: GastoUpdateDTO, db: Session = Depends(get_db)) -> GastoResponseDTO:
    return gasto_controller.update_gasto(db, gasto_id, gasto)

@router.delete("/{gasto_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_gasto(gasto_id: int, db: Session = Depends(get_db)) -> None:
    gasto_controller.delete_gasto(db, gasto_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get("/{gasto_id}", response_model=GastoResponseDTO)
def get_gasto(gasto_id: int, db: Session = Depends(get_db)) -> GastoResponseDTO:
    return gasto_controller.get_gasto(db, gasto_id)

@router.get("/", response_model=list[GastoResponseDTO])
def get_all_gastos(db: Session = Depends(get_db)) -> list[GastoResponseDTO  ]:
    return gasto_controller.get_all_gastos(db)

@router.get("/categoria/{categoria_id}", response_model=list[GastoResponseDTO])
def get_gastos_by_categoria(categoria_id: int, db: Session = Depends(get_db)) -> list[GastoResponseDTO]:
    return gasto_controller.get_gastos_by_categoria(db, categoria_id)