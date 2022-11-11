from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/sets/", response_model=list[schemas.Set])
def read_sets(db: Session = Depends(get_db)):
    sets = crud.read_sets(db)
    return sets

@app.get("/sets/{set_id}", response_model=schemas.Set)
def read_set(set_id: int, db: Session = Depends(get_db)):
    db_set = crud.read_set(db, set_id=set_id)
    if db_set is None:
        raise HTTPException(status_code=404, detail="Set not found")
    return db_set

#add authentication
@app.post("/sets/", response_model=schemas.Set)
def create_set(set: schemas.SetCreate, db: Session = Depends(get_db)):
    return crud.create_set(db=db, set=set)

@app.delete("/sets/{set_id}", response_model=schemas.Set)
def remove_set(set_id: int, db: Session = Depends(get_db)):
    db_set = crud.remove_set(db, set_id=set_id)
    if db_set is None:
        raise HTTPException(status_code=404, detail="Set not found")
    return db_set


@app.post("/sets/{set_id}/questions", response_model=schemas.Question)
def create_question(question: schemas.QuestionCreate, set_id: int, db: Session = Depends(get_db)):
    return crud.create_question(db=db, question=question, set_id=set_id)

@app.get("/questions/{question_id}", response_model=schemas.Question)
def read_question(question_id: int, db: Session = Depends(get_db)):
    db_question = crud.read_question(db, question_id=question_id)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question

@app.delete("/questions/{question_id}", response_model=schemas.Question)
def remove_question(question_id: int, db: Session = Depends(get_db)):
    db_question = crud.remove_question(db, question_id=question_id)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question



@app.post("/questions/{question_id}/answers", response_model=schemas.Answer)
def create_answer(answer: schemas.AnswerCreate, question_id: int, db: Session = Depends(get_db)):
    return crud.create_answer(db=db, answer=answer, question_id=question_id)

@app.delete("/answers/{answer_id}", response_model=schemas.Answer)
def remove_answer(answer_id: int, db: Session = Depends(get_db)):
    db_answer = crud.remove_answer(db, answer_id=answer_id)
    if db_answer is None:
        raise HTTPException(status_code=404, detail="Answer not found")
    return db_answer