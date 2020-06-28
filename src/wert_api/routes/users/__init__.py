from typing import List
import fastapi
import pydantic

from wert_api.models.users import User
from wert_api import schemas

router = fastapi.APIRouter()


@router.get("/users", response_model=List[schemas.User])
async def get_users():
    users = await User.query.gino.all()
    return users


@router.post("/users", response_model=schemas.User)
async def add_user(user: schemas.UserCreate):
    user = await User.create(name=user.name, email=user.email)
    return user


@router.get("/users/{email}", response_model=schemas.User)
async def get_user(email: str):
    user = await User.get_or_404(email)
    return user


@router.delete("/users/{email}")
async def delete_user(email: str):
    user = await User.get_or_404(email)
    await user.delete()
    return dict(email=email)
