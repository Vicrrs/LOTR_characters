from enum import unique
from operator import index
from re import I
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    race_id = Column(Integer, ForeignKey("races.id"))
    class_id = Column(Integer, ForeignKey("classes.id"))
    city_id = Column(Integer, ForeignKey("cities.id"))

    race = relationship("Race")
    char_class = relationship("Class")
    city = relationship("City")

class Race(Base):
    __tablename__ = "races"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class Class(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

