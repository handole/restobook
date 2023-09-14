from typing import List
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status, Request
from datetime import timedelta

from app.db.schemas.user import UserCreate
from app.db.crud.user import create_user

from app.utils.security import create_access_token
from app.utils.auth import authenticate_user

from app import auth_settings
from app.db import get_db


router = APIRouter(prefix="/api/auth", tags=["Authentication"])

@router.post("/register")
async def register_user(
    request: Request, data: UserCreate, db=Depends(get_db)
):
    user = create_user(db, data)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Account already exists",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(
        minutes=auth_settings.jwt_expiry_time
    )
    if user.is_superuser:
        permissions = "admin"
    else:
        permissions = "user"
    access_token = create_access_token(
        data={"sub": user.email, "permissions": permissions},
        expires_delta=access_token_expires,
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/login")
async def login(
    db=Depends(get_db), data: OAuth2PasswordRequestForm = Depends()
):
    user = authenticate_user(db, data.username, data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(
        minutes=auth_settings.jwt_expiry_time
    )
    if user.is_superuser:
        permissions = "admin"
    else:
        permissions = "user"
    access_token = create_access_token(
        data={"sub": user.email, "permissions": permissions},
        expires_delta=access_token_expires,
    )

    return {"access_token": access_token, "token_type": "bearer"}