from typing import List, TYPE_CHECKING

from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.shared.models import db

if TYPE_CHECKING:
    from app.generator.models import Character

class User(db.Model):
    id: Mapped[str] = mapped_column(String(60), primary_key=True)
    name: Mapped[str] = mapped_column(String(60), unique=True)
    password: Mapped[str] = mapped_column(String(255))
    moderator: Mapped[bool] = mapped_column(Boolean)

    characters: Mapped[List["Character"]] = relationship(back_populates="user")

