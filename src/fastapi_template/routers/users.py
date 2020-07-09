import fastapi
from starlette import status
import pydantic

from fastapi_template.core import security, service_factory
from fastapi_template.domain.users import user_schemas

router = fastapi.APIRouter()


@router.get("/", response_model=user_schemas.Paginated)
async def get_users(page_size: pydantic.conint(ge=1, le=100) = 20,
                    page: pydantic.conint(ge=1) = 1,
                    service=fastapi.Depends(service_factory.get_user_services)):
    return await service.get_list(page=page, page_size=page_size)


@router.post("/", response_model=user_schemas.DB)
async def add_user(user: user_schemas.Create,
                   service=fastapi.Depends(service_factory.get_user_services)):
    return await service.create(user=user)


@router.get("/{identifier}", response_model=user_schemas.DB)
async def get_user(identifier: pydantic.UUID4,
                   service=fastapi.Depends(service_factory.get_user_services)):
    user = await service.get_by_id(identifier=identifier)
    if user:
        return user
    raise fastapi.HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"A user with id: '{identifier} was not found.",
    )


@router.delete("/{identifier}", response_model=user_schemas.DB)
async def delete_user(identifier: pydantic.UUID4,
                      service=fastapi.Depends(
                          service_factory.get_user_services)):
    return await service.delete(identifier=identifier)
