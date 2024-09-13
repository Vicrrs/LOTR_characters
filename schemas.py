from pydantic import BaseModel


class CharacterBase(BaseModel):
    name: str
    race_id: int
    class_id: int
    city_id: int

class CharacterCreate(CharacterBase):
    pass

class Character(CharacterBase):
    id: int

    class Config:
        orm_mode = True 

class RaceBase(BaseModel):
    name: str

class Race(RaceBase):
    id: int

    class Config:
        orm_mode = True

class ClassBase(BaseModel):
    name: str

class Class(ClassBase):
    id: int

    class Config:
        orm_mode = True

class CityBase(BaseModel):
    name: str

class City(CityBase):
    id: int

    class Config:
        orm_mode = True

