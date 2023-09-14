from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.models import Tables
from app.db.schemas import table as table_schema


def get_table(db: Session, table_id: int):
    table = db.query(Tables).filter(Tables.id == table_id).first()
    if not table:
        raise HTTPException(status_code=404, detail="this table not found")
    return table


def get_tables(
    db: Session, resto_id: int
) -> List[table_schema.TableOut]:
    return db.query(Tables).filter(Tables.resto_id == resto_id)


def create_table(db: Session, table: table_schema.TableCreate):
    db_table = Tables(
        number=table.number,
        resto_id=table.resto_id,
        is_active=True,
    )
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table


def delete_table(db: Session, table_id: int):
    table = get_table(db, table_id)
    if not table:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="table not found")
    db.delete(table)
    db.commit()
    return table


def edit_table(
    db: Session, table_id: int, table: table_schema.TableEdit
) -> table_schema.Tables:
    db_table = get_table(db, table_id)
    if not db_table:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="table not found")
    update_data = table.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_table, key, value)

    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table
