from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer

import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def api_key_auth(api_key: str = Depends(oauth2_scheme)):
    if api_key not in os.getenv("API_KEYS"):
        raise HTTPException(status_code=400, detail="Invalid API key")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/token/")
def read_token(token: str):
    if token not in os.getenv("API_KEYS"):
        raise HTTPException(status_code=400, detail="Invalid API key")
    return {"token": token}



@app.get("/tests/", response_model=list[schemas.Test])
def read_tests(db: Session = Depends(get_db)):
    tests = crud.read_tests(db)
    return tests

@app.get("/tests/{test_id}", response_model=schemas.Test)
def read_test(test_id: int, db: Session = Depends(get_db)):
    db_test = crud.read_test(db, test_id=test_id)
    if db_test is None:
        raise HTTPException(status_code=404, detail="Test not found")
    return db_test


@app.post("/tests/", response_model=schemas.Test, dependencies=[Depends(api_key_auth)])
def create_test(test: schemas.TestCreate, db: Session = Depends(get_db)):
    return crud.create_test(db=db, test=test)

@app.delete("/tests/{test_id}", response_model=schemas.Test, dependencies=[Depends(api_key_auth)])
def remove_test(test_id: int, db: Session = Depends(get_db)):
    db_test = crud.remove_test(db, test_id=test_id)
    if db_test is None:
        raise HTTPException(status_code=404, detail="Test not found")
    return db_test

@app.put("/tests/{test_id}", response_model=schemas.Test, dependencies=[Depends(api_key_auth)])
def update_test(test_id: int, test: schemas.TestUpdate, db: Session = Depends(get_db)):
    db_test = crud.update_test(db, test_id=test_id, test=test)
    if db_test is None:
        raise HTTPException(status_code=404, detail="Test not found")
    return db_test


@app.get("/tests/{test_id}/questions/", response_model=list[schemas.Question])
def read_questions(test_id: int, db: Session = Depends(get_db)):
    db_test = crud.read_test(db, test_id=test_id)
    if db_test is None:
        raise HTTPException(status_code=404, detail="Test not found")
    return db_test.questions

@app.post("/tests/{test_id}/questions/", response_model=schemas.Question, dependencies=[Depends(api_key_auth)])
def create_question(question: schemas.QuestionCreate, test_id: int, db: Session = Depends(get_db)):
    return crud.create_question(db=db, question=question, test_id=test_id)

@app.get("/questions/{question_id}", response_model=schemas.Question)
def read_question(question_id: int, db: Session = Depends(get_db)):
    db_question = crud.read_question(db, question_id=question_id)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question

@app.delete("/questions/{question_id}", response_model=schemas.Question, dependencies=[Depends(api_key_auth)])
def remove_question(question_id: int, db: Session = Depends(get_db)):
    db_question = crud.remove_question(db, question_id=question_id)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question

@app.put("/questions/{question_id}", response_model=schemas.Question, dependencies=[Depends(api_key_auth)])
def update_question(question_id: int, question: schemas.QuestionUpdate, db: Session = Depends(get_db)):
    db_question = crud.update_question(db, question_id=question_id, question=question)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question


@app.get("/questions/{question_id}/answers/", response_model=list[schemas.Answer])
def read_answers(question_id: int, db: Session = Depends(get_db)):
    db_question = crud.read_question(db, question_id=question_id)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question.answers

@app.post("/questions/{question_id}/answers/", response_model=schemas.Answer, dependencies=[Depends(api_key_auth)])
def create_answer(answer: schemas.AnswerCreate, question_id: int, db: Session = Depends(get_db)):
    return crud.create_answer(db=db, answer=answer, question_id=question_id)

@app.delete("/answers/{answer_id}", response_model=schemas.Answer, dependencies=[Depends(api_key_auth)])
def remove_answer(answer_id: int, db: Session = Depends(get_db)):
    db_answer = crud.remove_answer(db, answer_id=answer_id)
    if db_answer is None:
        raise HTTPException(status_code=404, detail="Answer not found")
    return db_answer

@app.put("/answers/{answer_id}", response_model=schemas.Answer, dependencies=[Depends(api_key_auth)])
def update_answer(answer_id: int, answer: schemas.AnswerUpdate, db: Session = Depends(get_db)):
    db_answer = crud.update_answer(db, answer_id=answer_id, answer=answer)
    if db_answer is None:
        raise HTTPException(status_code=404, detail="Answer not found")
    return db_answer