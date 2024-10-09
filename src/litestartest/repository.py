# -*- coding: utf-8 -*-
from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from .model import User


class UserRepository(SQLAlchemyAsyncRepository[User]):
    """User SQLAlchemy Repository."""

    model_type = User
