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
    name: Mapped[str] = mapped_column(String(60), nullable=False, unique=True)

class Character(db.Model):
    id: Mapped[str]  = mapped_column(String, primary_key=True)
    timestamp: Mapped[datetime.datetime]  = mapped_column(DateTime, primary_key=True)

    user_id: Mapped[str] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="characters")

    name_id: Mapped[str] = mapped_column(ForeignKey("name.id"))
    name: Mapped["Name"] = relationship()

    attributes: Mapped[List["Attribute"]] = relationship(secondary='character_attribute')
    skills: Mapped[List["Skill"]] = relationship(back_populates="character")
    items: Mapped[List["Item"]] = relationship(back_populates="character")

class Attribute(db.Model):
    id: Mapped[str] = mapped_column(String(60), primary_key=True)
    name: Mapped[str]  = mapped_column(String(50), nullable=False)

# https://stackoverflow.com/a/69995324
class CharacterAtribute(db.Model):
    __tablename__ = 'character_attribute'

    character_timestamp: Mapped[datetime.datetime] = mapped_column(ForeignKey("character.id"), primary_key=True)
    attribute_id: Mapped[str] = mapped_column(ForeignKey("attribute.id"), primary_key=True)

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


