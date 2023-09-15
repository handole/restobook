from pydantic import BaseModel

class MenuBase(BaseModel):
    name: str
    stock: int
    resto_id: int

class MenuOut(MenuBase):
    pass

class MenuCreate(MenuBase):
    pass

class MenuEdit(MenuBase):
    pass

class Menu(MenuBase):
    id: int
    is_active: bool
    
    class Config:
        orm_mode = True