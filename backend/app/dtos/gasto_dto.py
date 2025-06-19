from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class GastoDTO(BaseModel):
    model_config = {
        "from_attributes": True,
    }

    monto: float = Field(..., description="Monto del gasto")
    descripcion: str = Field(..., description="Descripción del gasto")
    fecha: date = Field(..., description="Fecha del gasto")
    categoria_id: int = Field(..., description="ID de la categoría del gasto")

class GastoResponseDTO(GastoDTO):
    id: int = Field(..., description="ID del gasto autogenerado")
    
    class Config:
        orm_mode = True

class GastoUpdateDTO(BaseModel):
    monto: Optional[float] = Field(None, description="Monto del gasto")
    descripcion: Optional[str] = Field(None, description="Descripción del gasto")
    fecha: Optional[date] = Field(None, description="Fecha del gasto")
    categoria_id: Optional[int] = Field(None, description="ID de la categoría del gasto")

    class Config:
        orm_mode = True

class GastoCreateDTO(GastoDTO):
    pass

class GastoDeleteDTO(BaseModel):
    id: int = Field(..., description="ID del gasto a eliminar")
    confirmacion: bool = Field(..., description="Confirmación de eliminación")
    
    class Config:
        orm_mode = True
