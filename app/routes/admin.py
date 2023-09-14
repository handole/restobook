from fastapi import APIRouter, Request, Depends

from app.db import get_db
from app.db.crud.resto import create_resto, delete_resto, edit_resto
from app.db.crud.table import create_table, delete_table, edit_table
from app.db.crud.menu import create_menu, delete_menu, edit_menu
from app.db.schemas.resto import Resto, RestoCreate, RestoEdit
from app.db.schemas.table import Tables, TableCreate, TableEdit
from app.db.schemas.menu import Menu, MenuCreate, MenuEdit
from app.db.models import User
from app.utils.auth import get_current_active_superuser


router = APIRouter(prefix="/api/admin", tags=["Admin"])


@router.post("/resto/", response_model=Resto)
async def resto_create(
    request: Request, resto: RestoCreate, db=Depends(get_db),
    user: User = Depends(get_current_active_superuser)    
):
    return create_resto(db, resto)


@router.put("/resto/{resto_id}", response_model=Resto)
async def resto_edit(
    request: Request, resto_id: int,
    resto: RestoEdit, db=Depends(get_db),
    user: User = Depends(get_current_active_superuser)
):
    return edit_resto(db, resto_id, resto)


@router.delete("/resto/{resto_id}", response_model=Resto)
async def resto_delete(
    request: Request, resto_id: int, db=Depends(get_db),
    user: User = Depends(get_current_active_superuser)    
):
    return delete_resto(db, resto_id)



@router.post("/table/", response_model=Tables)
async def table_create(
    request: Request, table: TableCreate, db=Depends(get_db),
    user: User = Depends(get_current_active_superuser)    
):
    return create_table(db, table)


@router.put("/table/{table_id}", response_model=Tables)
async def table_edit(
    request: Request, table_id: int,
    table: TableEdit, db=Depends(get_db),
    user: User = Depends(get_current_active_superuser)
):
    return edit_table(db, table_id, table)


@router.delete("/table/{table_id}", response_model=Tables)
async def table_delete(
    request: Request, table_id: int, db=Depends(get_db),
    user: User = Depends(get_current_active_superuser)    
):
    return delete_table(db, table_id)


@router.post("/menu/", response_model=Menu)
async def menu_create(
    request: Request, menu: MenuCreate, db=Depends(get_db),
    user: User = Depends(get_current_active_superuser)    
):
    return create_menu(db, menu)


@router.put("/menu/{menu_id}", response_model=Menu)
async def menu_edit(
    request: Request, menu_id: int,
    menu: MenuEdit, db=Depends(get_db),
    user: User = Depends(get_current_active_superuser)
):
    return edit_menu(db, menu_id, menu)


@router.delete("/menu/{menu_id}", response_model=Menu)
async def menu_delete(
    request: Request, menu_id: int, db=Depends(get_db),
    user: User = Depends(get_current_active_superuser)    
):
    return delete_menu(db, menu_id)