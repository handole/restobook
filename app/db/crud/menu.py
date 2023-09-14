from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.models import Menu
from app.db.schemas import menu as menu_schema


def get_menu(db: Session, menu_id: int):
    menu = db.query(Menu).filter(Menu.id == menu_id).first()
    if not menu:
        raise HTTPException(status_code=404, detail="this menu not found")
    return menu


def get_menus(
    db: Session, skip: int = 0, limit: int = 100
) -> List[menu_schema.MenuOut]:
    return db.query(Menu).offset(skip).limit(limit).all()


def create_menu(db: Session, menu: menu_schema.MenuCreate):
    db_menu = Menu(
        name=menu.name,
        stock=menu.stock,
        is_active=True,
    )
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu


def delete_menu(db: Session, menu_id: int):
    menu = get_menu(db, menu_id)
    if not menu:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="menu not found")
    db.delete(menu)
    db.commit()
    return menu


def edit_menu(
    db: Session, menu_id: int, menu: menu_schema.MenuEdit
) -> menu_schema.Menu:
    db_menu = get_menu(db, menu_id)
    if not db_menu:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="menu not found")
    update_data = menu.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_menu, key, value)

    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu
