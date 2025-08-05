from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID


class EnxadristaBase(BaseModel):
    nome: str = Field(..., example="José Silva")
    categoria: str = Field(..., example="Sub-18")
    federado: Optional[bool] = Field(default=False, example=True)


class EnxadristaCreate(EnxadristaBase):
    pass


class EnxadristaUpdate(EnxadristaBase):
    pass


class EnxadristaResponse(EnxadristaBase):
    id: UUID

    class Config:
        orm_mode = True
