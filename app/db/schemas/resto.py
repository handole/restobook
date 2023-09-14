from pydantic import BaseModel
from typing import Optional, List

from app.db.schemas.table import Tables
from app.db.schemas.menu import Menu


class RestoBase(BaseModel):
    name: str
    address: Optional[str]

class RestoOut(RestoBase):
    pass

class RestoCreate(RestoBase):
    pass

class RestoEdit(RestoBase):
    name: Optional[str]
    address: Optional[str]

    class Config:
        orm_mode = True

class Resto(RestoBase):
    id: int
    is_active: bool
    tables: List[Tables]
    menus: List[Menu]

    class Config:
        orm_mode = True