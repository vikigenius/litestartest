# -*- coding: utf-8 -*-
from __future__ import annotations

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy.orm import Mapped, mapped_column


class User(UUIDAuditBase):
    __tablename__ = "user_account"

    email: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    name: Mapped[str | None] = mapped_column(nullable=True, default=None)
