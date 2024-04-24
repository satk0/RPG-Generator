
from typing import List
from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import (sessionmaker, DeclarativeBase, relationship,
        mapped_column, Mapped)

  
engine = create_engine(DB_CONNECTION_STRING, echo = True)

class Base(DeclarativeBase):
    pass

class Character(Base):
    __tablename__ = 'character'

    id: Mapped[str] = mapped_column(String(60), primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    attributes: Mapped[List["Attribute"]] = relationship(back_populates="character")
    skills: Mapped[List["Skill"]] = relationship(back_populates="character")
    items: Mapped[List["Item"]] = relationship(back_populates="character")

class Attribute(Base):
    __tablename__ = 'attribute'

    id: Mapped[str] = mapped_column(String(60), primary_key=True)
    name: Mapped[str]  = mapped_column(String(50), nullable=False)

    character_id: Mapped[str] = mapped_column(ForeignKey("character.id"))
    character: Mapped["Character"] = relationship(back_populates="attributes")

class Skill(Base):
    __tablename__ = 'skill'

    id: Mapped[str] = mapped_column(String(60), primary_key=True)
    name: Mapped[str]  = mapped_column(String(50), nullable=False)

    character_id: Mapped[str] = mapped_column(ForeignKey("character.id"))
    character: Mapped["Character"] = relationship(back_populates="skills")

class Item(Base):
    __tablename__ = 'item'

    id: Mapped[str] = mapped_column(String(60), primary_key=True)
    name: Mapped[str]  = mapped_column(String(50), nullable=False)

    character_id: Mapped[str] = mapped_column(ForeignKey("character.id"))
    character: Mapped["Character"] = relationship(back_populates="items")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# flush db
session.query(Character).delete()
session.query(Attribute).delete()
session.query(Skill).delete()
session.query(Item).delete()

new_character = Character(id='1', name='c1')
new_attribute = Attribute(id='1', name='a1', character=new_character)
new_skill = Skill(id='1', name='s1', character=new_character)
new_item = Item(id='1', name='i1', character=new_character)

session.add_all([new_character, new_attribute, new_skill, new_item])
session.commit()

session.close()
