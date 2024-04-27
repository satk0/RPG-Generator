from typing import List, TYPE_CHECKING
from sqlalchemy.types import DateTime
import datetime

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.shared.models import db

# https://github.com/sqlalchemy/sqlalchemy/discussions/9576
if TYPE_CHECKING:
    from app.account.models import User

class Name(db.Model):
    id: Mapped[str] = mapped_column(String(60), primary_key=True)
    name: Mapped[str] = mapped_column(String(60), nullable=False)

class Character(db.Model):
    timestamp: Mapped[datetime.datetime]  = mapped_column(DateTime, primary_key=True)

    user_id: Mapped[str] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="characters")

    name_id: Mapped[str] = mapped_column(ForeignKey("name.id"))
    name: Mapped["Name"] = relationship()

    attributes: Mapped[List["Attribute"]] = relationship(back_populates="character")
    skills: Mapped[List["Skill"]] = relationship(back_populates="character")
    items: Mapped[List["Item"]] = relationship(back_populates="character")

class Attribute(db.Model):
    id: Mapped[str] = mapped_column(String(60), primary_key=True)
    name: Mapped[str]  = mapped_column(String(50), nullable=False)

    character_id: Mapped[str] = mapped_column(ForeignKey("character.timestamp"))
    character: Mapped["Character"] = relationship(back_populates="attributes")

class Skill(db.Model):
    id: Mapped[str] = mapped_column(String(60), primary_key=True)
    name: Mapped[str]  = mapped_column(String(50), nullable=False)

    character_id: Mapped[str] = mapped_column(ForeignKey("character.timestamp"))
    character: Mapped["Character"] = relationship(back_populates="skills")

class Item(db.Model):
    id: Mapped[str] = mapped_column(String(60), primary_key=True)
    name: Mapped[str]  = mapped_column(String(50), nullable=False)

    character_id: Mapped[str] = mapped_column(ForeignKey("character.timestamp"))
    character: Mapped["Character"] = relationship(back_populates="items")

