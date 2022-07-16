import jwt

from functools import lru_cache
from fastapi import Depends
from passlib.hash import pbkdf2_sha256
from sqlmodel import Session


from src.db import AbstractCache, get_cache, get_session
from src.models import User
from src.services import ServiceMixin
from src.api.v1.schemas.auth import Login, Signup


class UserServis(ServiceMixin):
    def create_user(self, user: Signup):
        """Создать пользователя."""
        new_user = User(
            username=user.username,
            email=user.email,
            password_hash=pbkdf2_sha256.hash(user.password)
        )
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user

    def login_user(self, login_data: Login):
        user = self.session.query(User).filter(
            User.username == login_data.username
        ).first()
        if not user:
            raise ValueError
        if not pbkdf2_sha256.verify(login_data.password, user.password_hash):
            raise ValueError
        encoding_jwt = jwt.encode(
            {"username": user.username},
            "secret",
            algorithm="HS256"
        ) 



@lru_cache()
def get_user_service(
    cache: AbstractCache = Depends(get_cache),
    session: Session = Depends(get_session),
) -> UserServis:
    return UserServis(cache=cache, session=session)
