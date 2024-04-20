from typing import List

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.shared.models import db

class Character(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(60), unique=True)

    attributes: Mapped[List["Attribute"]] = relationship(back_populates="character")
    skills: Mapped[List["Skill"]] = relationship(back_populates="character")
    items: Mapped[List["Item"]] = relationship(back_populates="character")

class Attribute(db.Model):
    id: Mapped[str] = mapped_column(String(60), primary_key=True)
    name: Mapped[str]  = mapped_column(String(50), nullable=False)

    character_id: Mapped[str] = mapped_column(ForeignKey("character.id"))
    character: Mapped["Character"] = relationship(back_populates="attributes")

class Skill(db.Model):
    id: Mapped[str] = mapped_column(String(60), primary_key=True)
    name: Mapped[str]  = mapped_column(String(50), nullable=False)

    character_id: Mapped[str] = mapped_column(ForeignKey("character.id"))
    character: Mapped["Character"] = relationship(back_populates="skills")

class Item(db.Model):
    id: Mapped[str] = mapped_column(String(60), primary_key=True)
    name: Mapped[str]  = mapped_column(String(50), nullable=False)

    character_id: Mapped[str] = mapped_column(ForeignKey("character.id"))
    character: Mapped["Character"] = relationship(back_populates="items")

