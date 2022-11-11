from sqlalchemy.orm import Session

from . import models, schemas

#create_set
def create_set(db: Session, set: schemas.SetCreate):
    db_set = models.Set(**set.dict())
    db.add(db_set)
    db.commit()
    db.refresh(db_set)
    return db_set

#read_set
def read_set(db: Session, set_id: int):
    return db.query(models.Set).filter(models.Set.id == set_id).first()

#read_sets
def read_sets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Set).offset(skip).limit(limit).all()

#remove_set
def remove_set(db: Session, set_id: int):
    db_set = db.query(models.Set).filter(models.Set.id == set_id).first()
    db.delete(db_set)
    db.commit()
    return db_set

#read_question
def read_question(db: Session, question_id: int):
    return db.query(models.Question).filter(models.Question.id == question_id).first()

#read_questions
def read_questions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Question).offset(skip).limit(limit).all()

#create_question
def create_question(db: Session, question: schemas.QuestionCreate, set_id: int):
    db_question = models.Question(**question.dict(), set_id=set_id)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

#remove_question
def remove_question(db: Session, question_id: int):
    db_question = db.query(models.Question).filter(models.Question.id == question_id).first()
    db.delete(db_question)
    db.commit()
    return db_question


#read_answer
def read_answer(db: Session, answer_id: int):
    return db.query(models.Answer).filter(models.Answer.id == answer_id).first()

#read_answers
def read_answers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Answer).offset(skip).limit(limit).all()

#create_answer
def create_answer(db: Session, answer: schemas.AnswerCreate, question_id: int):
    db_answer = models.Answer(**answer.dict(), question_id=question_id)
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer

#remove_answer
def remove_answer(db: Session, answer_id: int):
    db_answer = db.query(models.Answer).filter(models.Answer.id == answer_id).first()
    db.delete(db_answer)
    db.commit()
    return db_answer