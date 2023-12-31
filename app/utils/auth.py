import jwt
from fastapi import Depends, HTTPException, status
from jwt import PyJWTError
from fastapi.security import OAuth2PasswordBearer

from app import auth_settings
from app.db import get_db
from app.db.models import User
from app.db.schemas import user as schemas
from app.db.crud.user import get_user_by_email, create_user
from app.utils import security

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login", auto_error=False)



async def get_current_user(
    db=Depends(get_db), token: str = Depends(oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, auth_settings.jwt_secret, algorithms=[auth_settings.jwt_algorithm]
        )
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        permissions: str = payload.get("permissions")
        token_data = schemas.TokenData(email=email, permissions=permissions)
    except PyJWTError:
        raise credentials_exception
    user = get_user_by_email(db, token_data.email)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


async def get_current_active_superuser(
    current_user: User = Depends(get_current_user),
) -> User:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="The user doesn't have enough privileges"
        )
    return current_user


def authenticate_user(db, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not security.verify_password(password, user.hashed_password):
        return False
    return user


def sign_up_new_user(db, email: str, password: str):
    user = get_user_by_email(db, email)
    if user:
        return False  # User already exists
    new_user = create_user(
        db,
        schemas.UserCreate(
            email=email,
            password=password,
            is_active=True,
            is_superuser=False,
        ),
    )
    return new_user
