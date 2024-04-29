from typing import List, TYPE_CHECKING
from sqlalchemy.types import DateTime
import datetime

from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.shared.models import db

# https://github.com/sqlalchemy/sqlalchemy/discussions/9576
if TYPE_CHECKING:
    from app.account.models import User

class Name(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(60), nullable=False, unique=True)

class Character(db.Model):
    id: Mapped[int]  = mapped_column(Integer, primary_key=True)
    timestamp: Mapped[datetime.datetime]  = mapped_column(DateTime, nullable=False)

    user_id: Mapped[str] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="characters")

    name_id: Mapped[str] = mapped_column(ForeignKey("name.id"))
    name: Mapped["Name"] = relationship()

    attributes: Mapped[List["Attribute"]] = relationship(secondary='character_attribute')
    skills: Mapped[List["Skill"]] = relationship(secondary="character_skill")
    items: Mapped[List["Item"]] = relationship(secondary="character_item")

class Attribute(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str]  = mapped_column(String(50), nullable=False, unique=True)

# https://stackoverflow.com/a/69995324
class CharacterAtribute(db.Model):
    __tablename__ = 'character_attribute'

    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"), primary_key=True)
    attribute_id: Mapped[int] = mapped_column(ForeignKey("attribute.id"), primary_key=True)

class Skill(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str]  = mapped_column(String(50), nullable=False, unique=True)

class CharacterSkill(db.Model):
    __tablename__ = 'character_skill'

    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"), primary_key=True)
    skill_id: Mapped[int] = mapped_column(ForeignKey("skill.id"), primary_key=True)

class Item(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str]  = mapped_column(String(50), nullable=False, unique=True)

class CharacterItem(db.Model):
    __tablename__ = 'character_item'

    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"), primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("item.id"), primary_key=True)
