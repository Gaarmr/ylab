from fastapi import APIRouter, Depends
from src.services.users import UserServis, get_user_service
from src.api.v1.schemas.users import UserModel
from src.api.v1.schemas.auth import Login, Signup, Tokens

router = APIRouter()


@router.post(
    path="/signup",
    response_model=UserModel,
    summary="Регистрация пользователя",
    tags=["auth"],
)
def signup(
    signup_data: Signup,
    user_service: UserServis = Depends(get_user_service)
) -> UserModel:
    user = user_service.create_user(user=signup_data)
    return user


@router.post(
    path="/login",
    response_model=Tokens,
    summary="Авторизация пользователя",
    tags=["auth"],
)
def login(
    login_data: Login,
    user_service: UserServis = Depends(get_user_service)
) -> UserModel:
    user = user_service.create_user(user=signup_data)
    return user
