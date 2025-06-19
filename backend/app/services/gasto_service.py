from sqlalchemy.orm import Session, declarative_base
from app.models.gasto import Gasto
from app.dtos.gasto_dto import GastoCreateDTO, GastoUpdateDTO, GastoResponseDTO

def create_gasto(db: Session, gasto: GastoCreateDTO) -> GastoResponseDTO:
    db_gasto = Gasto(**gasto.model_dump())
    db.add(db_gasto)
    db.commit()
    db.refresh(db_gasto)
    return GastoResponseDTO.model_validate(db_gasto)

def update_gasto(db: Session, gasto_id: int, gasto: GastoUpdateDTO) -> GastoResponseDTO:
    db_gasto = db.query(Gasto).filter(Gasto.id == gasto_id).first()
    if not db_gasto:
        return None
    for key, value in gasto.model_dump().items():
        setattr(db_gasto, key, value)
    db.commit()
    db.refresh(db_gasto)
    return GastoResponseDTO.model_validate(db_gasto)

def delete_gasto(db: Session, gasto_id: int) -> None:
    db_gasto = db.query(Gasto).filter(Gasto.id == gasto_id).first()
    if db_gasto:
        db.delete(db_gasto)
        db.commit()

def get_gasto(db: Session, gasto_id: int) -> GastoResponseDTO:
    db_gasto = db.query(Gasto).filter(Gasto.id == gasto_id).first()
    if not db_gasto:
        return None
    return GastoResponseDTO.model_validate(db_gasto)

def get_all_gastos(db: Session) -> list[GastoResponseDTO]:
    return [GastoResponseDTO.model_validate(gasto) for gasto in db.query(Gasto).all()]

def get_gastos_by_categoria(db: Session, categoria_id: int) -> list[GastoResponseDTO]:
    db_gastos = db.query(Gasto).filter(Gasto.categoria_id == categoria_id).all()
    return [GastoResponseDTO.model_validate(gasto) for gasto in db_gastos] if db_gastos else []