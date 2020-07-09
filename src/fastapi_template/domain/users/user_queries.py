import datetime
from typing import List, Tuple

import pydantic

from fastapi_template.core.db import DB
from fastapi_template.domain.users import user_model, user_schemas

CreateSchema = user_schemas.Create
UpdateSchema = user_schemas.Update
Model = user_model.Model


class Queries():

    async def create(self, user: CreateSchema) -> Model:
        return await Model.create(**user.__dict__)

    async def get_list(self, page_size: int,
                       page: int) -> Tuple[List[Model], int]:
        users: List[Model] = await Model.query.order_by(
            Model.email.asc()).offset(page_size * (page - 1)
                                     ).limit(page_size).gino.all()

        count = await DB.func.count(Model.identifier).gino.scalar()
        return users, count

    async def get_by_id(self, identifier: pydantic.UUID4) -> Model:
        return await Model.get(identifier)

    async def delete(self, identifier: pydantic.UUID4) -> Model:
        user = await self.get_by_id(identifier)
        await user.delete()
        return user
