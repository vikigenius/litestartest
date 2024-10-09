# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import TYPE_CHECKING, override
from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService
from .model import User
from .repository import UserRepository


if TYPE_CHECKING:
    from advanced_alchemy.service import ModelDictT
    from advanced_alchemy.repository import Empty, EmptyType, ErrorMessages

class UserService(SQLAlchemyAsyncRepositoryService[User]):
    """Handles database operations for users."""
    repository_type = UserRepository

    @override
    async def create(
        self,
        data: ModelDictT[User],
        *,
        auto_commit: bool | None = None,
        auto_expunge: bool | None = None,
        auto_refresh: bool | None = None,
        error_messages: ErrorMessages | None | EmptyType = Empty,
    ) -> User:
        """Create."""
        raise NotImplementedError
