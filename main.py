from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import create_character, get_character, get_characters, create_race, create_class, create_city
from db_models import Base
from database import engine, get_db
from schemas import CharacterCreate, Character, RaceBase, ClassBase, CityBase

# Criação das tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/characters/", response_model=Character)
def create_character(character: CharacterCreate, db: Session = Depends(get_db)):
    return create_character(db=db, character=character)

@app.get("/characters/{character_id}", response_model=Character)
def read_character(character_id: int, db: Session = Depends(get_db)):
    db_character = get_character(db, character_id=character_id)
    if db_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return db_character

@app.get("/characters", response_model=list[Character])
def read_characters(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_characters(db, skip=skip, limit=limit)

@app.post("/races/", response_model=RaceBase)
def create_race(race: RaceBase, db: Session = Depends(get_db)):
    return create_race(db=db, race=race)

@app.post("/classes/", response_model=ClassBase)
def create_class(char_class: ClassBase, db: Session = Depends(get_db)):
    return create_class(db=db, char_class=char_class)

@app.post("/cities/", response_model=CityBase)
def create_city(city: CityBase, db: Session = Depends(get_db)):
    return create_city(db=db, city=city)
