from typing import List
from fastapi import APIRouter, Depends, Request, Response

from app.db.models import User
from app.db.schemas.resto import Resto
from app.db.crud.resto import get_resto, get_restos
from app.db.schemas.table import TableOut
from app.db.crud.table import get_table, get_tables
from app.db.schemas.menu import Menu
from app.db.crud.menu import get_menu, get_menus
from app.db.schemas.reservate import Reservate, ReservateBase, ReservateEdit
from app.db.crud.reservate import create_reservate, edit_reservate
from app.db.crud.reservate import get_reservate, get_reservates
from app.db.schemas.ticket import TicketBase, TicketEdit, TicketCreate, Ticket
from app.db.crud.ticket import create_ticket, edit_ticket
from app.db.crud.ticket import get_ticket, get_tickets

from app.utils.auth import get_current_active_user

from app.db import get_db


router = APIRouter(prefix="/api/customer", tags=["Customers"])


@router.get("/resto/", response_model=List[Resto])
async def resto_list(
    response: Response, db=Depends(get_db),
    user: User = Depends(get_current_active_user)
):
    resto = get_restos(db)
    return resto


@router.get("/resto/{resto_id}", response_model=Resto)
async def resto_details(
    request: Request, resto_id: int,
    db=Depends(get_db),
    user: User = Depends(get_current_active_user)
):
    resto = get_resto(db, resto_id)
    return resto


@router.get("/table/{resto_id}", response_model=List[TableOut])
async def table_list(
    request: Request, resto_id: int,
    response: Response, db=Depends(get_db), 
    user: User = Depends(get_current_active_user)
):
    table = get_tables(db=db, resto_id=resto_id)
    print(table)
    return table


@router.get("/table/{table_id}", response_model=TableOut)
async def table_details(
    request: Request, table_id: int,
    db=Depends(get_db),
    user: User = Depends(get_current_active_user)
):
    table = get_table(db, table_id)
    return table


@router.get("/menu/{resto_id}", response_model=List[Menu])
async def menu_list(
    request: Request, resto_id: int,
    response: Response, db=Depends(get_db),
    user: User = Depends(get_current_active_user)
):
    menu = get_menus(db, resto_id)
    return menu


@router.get("/menu/{menu_id}", response_model=Menu)
async def menu_details(
    request: Request, menu_id: int,
    db=Depends(get_db),
    user: User = Depends(get_current_active_user)
):
    menu = get_menu(db, menu_id)
    return menu


@router.post("/booking/")
async def reservate_create(
    request: Request, reservate: ReservateBase, db=Depends(get_db),
    user: User = Depends(get_current_active_user)    
):
    return create_reservate(db, reservate, user.id)


@router.put("/booking/{reservate_id}")
async def reservate_edit(
    request: Request, reservate_id: int,
    reservate: ReservateEdit, db=Depends(get_db),
    user: User = Depends(get_current_active_user)
):
    return edit_reservate(db, reservate_id, reservate)


@router.get("/booking/", response_model=List[Reservate])
async def reservate_list(
    response: Response, db=Depends(get_db),
    user: User = Depends(get_current_active_user),
):
    reservate = get_reservates(db, user.id)
    return reservate


@router.get("/booking/{reservate_id}", response_model=Reservate)
async def reservate_details(
    request: Request, reservate_id: int,
    db=Depends(get_db),
    user: User = Depends(get_current_active_user)
):
    reservate = get_reservate(db, reservate_id)
    return reservate



@router.post("/ticket/")
async def ticket_create(
    request: Request, ticket: TicketCreate, db=Depends(get_db),
    user: User = Depends(get_current_active_user)    
):
    return create_ticket(db, ticket, user.id)


@router.put("/ticket/{ticket_id}")
async def ticket_edit(
    request: Request, ticket_id: int,
    ticket: TicketEdit, db=Depends(get_db),
    user: User = Depends(get_current_active_user)
):
    return edit_ticket(db, ticket_id, ticket)


@router.get("/ticket/", response_model=List[Ticket])
async def ticket_list(
    response: Response, db=Depends(get_db),
    user: User = Depends(get_current_active_user)
):
    ticket = get_tickets(db, user.id)
    return ticket


@router.get("/ticket/{ticket_id}", response_model=TicketBase)
async def ticket_details(
    request: Request, ticket_id: int,
    db=Depends(get_db),
    user: User = Depends(get_current_active_user)
):
    ticket = get_ticket(db, ticket_id)
    return ticket