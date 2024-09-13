from sqlalchemy.orm import Session
from db_models import Character, Race, Class, City
from schemas import CharacterCreate, RaceBase, ClassBase, CityBase

# CRUD characters
def get_character(db: Session, character_id: int):
    return db.query(Character).filter(Character.id == character_id).first()

def create_character(db: Session, character: CharacterCreate):
    db_character = Character(**character.dict())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character

def get_characters(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Character).offset(skip).limit(limit).all()

# CRUD Race
def get_race(db: Session, race_id: RaceBase):
    return db.query(Race).filter(Race.id == race_id).first()

def create_race(db: Session, race: RaceBase):
    db_race = Race(**race.dict())
    db.add(db_race)
    db.commit()
    db.refresh(db_race)
    return db_race

# CRUD Class
def get_class(db: Session, class_id: int):
    return db.query(Class).filter(Class.id == class_id).first()

def create_class(db: Session, char_class: ClassBase):
    db_class = Class(**char_class.dict())
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

# CRUD City
def get_city(db: Session, city_id: int):
    return db.query(City).filter(City.id == city_id).first()

def create_city(db: Session, city: CityBase):
    db_city = City(**city.dict())
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city
