from pydantic import BaseModel, Field

class CategoriaDTO(BaseModel):
    model_config = {
        "from_attributes": True,
    }

    nombre: str = Field(..., description="Nombre de la categoría")

class CategoriaResponseDTO(CategoriaDTO):
    id: int = Field(..., description="ID de la categoría")

    class Config:
        orm_mode = True

class CategoriaUpdateDTO(BaseModel):
    nombre: str = Field(..., description="Nombre de la categoría")

    class Config:
        orm_mode = True

class CategoriaCreateDTO(CategoriaDTO):
    pass

class CategoriaDeleteDTO(BaseModel):
    id: int = Field(..., description="ID de la categoría a eliminar")
    confirmacion: bool = Field(..., description="Confirmación de eliminación")

    class Config:
        orm_mode = True

