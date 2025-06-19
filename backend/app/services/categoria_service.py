from sqlalchemy.orm import Session
from app.models.categoria import Categoria
from app.dtos.categoria_dto import CategoriaCreateDTO, CategoriaUpdateDTO, CategoriaResponseDTO

def create_categoria(db: Session, categoria: CategoriaCreateDTO) -> CategoriaResponseDTO:
    db_categoria = Categoria(**categoria.model_dump())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return CategoriaResponseDTO.model_validate(db_categoria)

def update_categoria(db: Session, categoria_id: int, categoria: CategoriaUpdateDTO) -> CategoriaResponseDTO:
    db_categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if not db_categoria:
        return None
    for key, value in categoria.model_dump().items():
        setattr(db_categoria, key, value)
    db.commit()
    db.refresh(db_categoria)
    return CategoriaResponseDTO.model_validate(db_categoria)

def delete_categoria(db: Session, categoria_id: int) -> None:
    db_categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if db_categoria:
        db.delete(db_categoria)
        db.commit()

def get_categoria(db: Session, categoria_id: int) -> CategoriaResponseDTO:
    db_categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if not db_categoria:
        return None
    return CategoriaResponseDTO.model_validate(db_categoria)

def get_all_categorias(db: Session) -> list[CategoriaResponseDTO]:
    return [CategoriaResponseDTO.model_validate(categoria) for categoria in db.query(Categoria).all()]

def get_categorias_by_name(db: Session, name: str) -> list[CategoriaResponseDTO]:
    db_categorias = db.query(Categoria).filter(Categoria.nombre.ilike(f"%{name}%")).all()
    return [CategoriaResponseDTO.model_validate(categoria) for categoria in db_categorias] if db_categorias else []