from sqlalchemy.orm import Session
from app.dtos.gasto_dto import GastoCreateDTO, GastoUpdateDTO, GastoResponseDTO
import app.services.gasto_service as gasto_service

def create_gasto(db: Session, gasto: GastoCreateDTO) -> GastoResponseDTO:
    return gasto_service.create_gasto(db, gasto)

def update_gasto(db: Session, gasto_id: int, gasto: GastoUpdateDTO) -> GastoResponseDTO:
    return gasto_service.update_gasto(db, gasto_id, gasto)

def delete_gasto(db: Session, gasto_id: int) -> None:
    gasto_service.delete_gasto(db, gasto_id)

def get_gasto(db: Session, gasto_id: int) -> GastoResponseDTO:
    return gasto_service.get_gasto(db, gasto_id)

def get_all_gastos(db: Session) -> list[GastoResponseDTO]:
    return gasto_service.get_all_gastos(db)

def get_gastos_by_categoria(db: Session, categoria_id: int) -> list[GastoResponseDTO]:
    return gasto_service.get_gastos_by_categoria(db, categoria_id)