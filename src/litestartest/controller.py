# -*- coding: utf-8 -*-
from __future__ import annotations

from typing import TYPE_CHECKING

from litestar import Controller, post
from .service import UserService
from .dto import UserCreateDTO, UserDTO
from .model import User


if TYPE_CHECKING:
    from litestar.dto import DTOData


class UserController(Controller):
    """User Account Controller."""
    dto = UserDTO

    @post(
        operation_id="CreateUser",
        name="users:create",
        summary="Create a new user.",
        cache_control=None,
        description="A user who can login and use the system.",
        path='/some/path',
        dto=UserCreateDTO,
    )
    async def create_user(
        self,
        users_service: UserService,
        data: DTOData[User],
    ) -> User:
        """Create a new user."""
        db_obj = await users_service.create(data)
        return users_service.to_schema(db_obj)
