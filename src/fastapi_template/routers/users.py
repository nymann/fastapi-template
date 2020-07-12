"""Endpoints starting with /users/ are defined here.

This module contains all API endpoints which path contains '/users/'.
Not that no "business-logic" is defined in here, we simply pass in onto the
user service from the `service_factory`, by doing it this way the controller
only knows which methods it can call in User Service but nothing about the
database.
"""

import fastapi
import pydantic
from starlette import status

from fastapi_template.core import security, service_factory
from fastapi_template.domain.users import user_schemas

router = fastapi.APIRouter()


@router.get("/", response_model=user_schemas.Paginated)
async def get_users(page_size: pydantic.conint(ge=1, le=100) = 20,
                    page: pydantic.conint(ge=1) = 1,
                    service=fastapi.Depends(service_factory.get_user_services)):
    """get_users.

    Args:
        page_size (pydantic.conint(ge=1, le=100)): page_size
        page (pydantic.conint(ge=1)): page
        service:
    """
    return await service.get_list(page=page, page_size=page_size)


@router.post("/",
             response_model=user_schemas.DB,
             status_code=status.HTTP_201_CREATED)
async def add_user(user: user_schemas.Create,
                   service=fastapi.Depends(service_factory.get_user_services)):
    """add_user.

    Args:
        user (user_schemas.Create): user
        service:
    """
    return await service.create(user=user)


@router.put("/{identifier}", response_model=user_schemas.DB)
async def update_user(identifier: pydantic.UUID4,
                      user: user_schemas.Update,
                      service=fastapi.Depends(
                          service_factory.get_user_services)):
    """update_user.

    Args:
        identifier (pydantic.UUID4): identifier
        user (user_schemas.Update): user
        service:
    """
    user = await service.update(identifier=identifier, new_user=user)
    if user:
        return user
    raise fastapi.HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"A user with id: '{identifier} was not found.",
    )


@router.get("/{identifier}", response_model=user_schemas.DB)
async def get_user(identifier: pydantic.UUID4,
                   service=fastapi.Depends(service_factory.get_user_services)):
    """get_user.

    Args:
        identifier (pydantic.UUID4): identifier
        service:
    """
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
    """delete_user.

    Args:
        identifier (pydantic.UUID4): identifier
        service:
    """
    return await service.delete(identifier=identifier)
