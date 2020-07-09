import pydantic
"""Example Google style docstrings.

"""

from typing import Optional, List
from fastapi_template.domain import base_schemas
from fastapi_template.domain.users import user_schemas, user_queries


class Service:
    """Service.
    """

    def __init__(self, queries: user_queries.Queries):
        """__init__.

        Args:
            queries (user_queries.Queries): queries
        """
        self._queries = queries

    async def create(self, user: user_schemas.Create) -> user_schemas.DB:
        """create.

        Args:
            user (user_schemas.Create): user

        Returns:
            user_schemas.DB:
        """
        new_user = await self._queries.create(user=user)
        return user_schemas.DB.from_orm(new_user)

    async def get_by_id(
            self, identifier: pydantic.UUID4) -> Optional[user_schemas.DB]:
        """get_by_id.

        Args:
            identifier (pydantic.UUID4): identifier

        Returns:
            Optional[user_schemas.DB]:
        """
        user = await self._queries.get_by_id(identifier=identifier)
        return user_schemas.DB.from_orm(user)

    async def get_list(
            self,
            page: pydantic.conint(ge=1),
            page_size: pydantic.conint(ge=1, le=100),
    ) -> user_schemas.Paginated:
        """get_list.

        Args:
            page (pydantic.conint(ge=1)): page
            page_size (pydantic.conint(ge=1, le=100)): page_size

        Returns:
            user_schemas.Paginated:
        """
        users, total = await self._queries.get_list(page=page,
                                                    page_size=page_size)
        more = ((total / page_size) - page) > 0
        results = [user_schemas.DB.from_orm(user) for user in users]
        print(more)
        print(results)
        pagination = base_schemas.Pagination(total=total, more=more)
        return user_schemas.Paginated(results=results, pagination=pagination)

    async def update(self, identifier: pydantic.UUID4,
                     new_user: user_schemas.Update) -> user_schemas.DB:
        """update.

        Args:
            identifier (pydantic.UUID4): identifier
            new_user (user_schemas.Update): new_user

        Returns:
            user_schemas.DB:
        """
        old_user = await self._queries.get_by_id(identifier=identifier)
        updated_user = await self._queries.update(old_user=old_user,
                                                  new_user=new_user)
        return user_schemas.DB.from_orm(updated_user)

    async def delete(self, identifier: pydantic.UUID4) -> user_schemas.DB:
        """delete.

        Args:
            identifier (pydantic.UUID4): identifier

        Returns:
            user_schemas.DB:
        """
        deleted_user = await self._queries.delete(identifier=identifier)
        return user_schemas.DB.from_orm(deleted_user)
