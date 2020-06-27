import fastapi
import pydantic

from wert_api.models.users import User

router = fastapi.APIRouter()


class UserModel(pydantic.BaseModel):
    email: str
    name: str


@router.get("/users/{email}")
async def get_user(email: str):
    user = await User.get_or_404(email)
    return user.to_dict()


@router.post("/users")
async def add_user(user: UserModel):
    user = await User.create(name=user.name, email=user.email)
    return user.to_dict()


@router.delete("/usrs/{email}")
async def delete_user(email: str):
    user = await User.get_or_404(email)
    await user.delete()
    return dict(email=email)
