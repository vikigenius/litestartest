# -*- coding: utf-8 -*-
from advanced_alchemy.extensions.litestar.dto import SQLAlchemyDTO, SQLAlchemyDTOConfig
from .model import User


class UserDTO(SQLAlchemyDTO[User]):
    """DTO for creating users."""
    config = SQLAlchemyDTOConfig(max_nested_depth=0, exclude={'id', 'created_at', 'updated_at', 'chat_thread', 'roles'})


class UserCreateDTO(SQLAlchemyDTO[User]):
    """DTO for creating users."""
    config = SQLAlchemyDTOConfig(max_nested_depth=0, exclude={'id', 'created_at', 'updated_at', 'chat_thread', 'roles'}, rename_fields={'hashed_password': 'password'})


class UserUpdateDTO(SQLAlchemyDTO[User]):
    """DTO for creating users."""
    config = SQLAlchemyDTOConfig(
        max_nested_depth=0,
        exclude={'id', 'created_at', 'updated_at', 'chat_thread', 'roles'},
        rename_fields={'hashed_password': 'password'},
        partial=True,
    )
