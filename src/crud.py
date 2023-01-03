from sqlalchemy.orm import Session

from . import models, schemas


#create_test
def create_test(db: Session, test: schemas.TestCreate):
    db_test = models.Test(**test.dict())
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test

#read_test
def read_test(db: Session, test_id: int):
    return db.query(models.Test).filter(models.Test.id == test_id).first()

#read_tests
def read_tests(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Test).offset(skip).limit(limit).all()

#remove_test
def remove_test(db: Session, test_id: int):
    db_test = db.query(models.Test).filter(models.Test.id == test_id).first()
    db.delete(db_test)
    db.commit()
    return db_test

#update_test
def update_test(db: Session, test_id: int, test: schemas.TestCreate):
    db_test = db.query(models.Test).filter(models.Test.id == test_id).first()
    db_test.title = test.title
    db_test.description = test.description
    db_test.time = test.time
    db_test.is_active = test.is_active
    db.commit()
    db.refresh(db_test)
    return db_test

#read_question
def read_question(db: Session, question_id: int):
    return db.query(models.Question).filter(models.Question.id == question_id).first()

#read_questions
def read_questions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Question).offset(skip).limit(limit).all()

#create_question
def create_question(db: Session, question: schemas.QuestionCreate, test_id: int):
    db_question = models.Question(**question.dict(), test_id=test_id)
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

#update_question
def update_question(db: Session, question_id: int, question: schemas.QuestionCreate):
    db_question = db.query(models.Question).filter(models.Question.id == question_id).first()
    db_question.title = question.title
    db_question.description = question.description
    db_question.time = question.time
    db.commit()
    db.refresh(db_question)
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

#update_answer
def update_answer(db: Session, answer_id: int, answer: schemas.AnswerCreate):
    db_answer = db.query(models.Answer).filter(models.Answer.id == answer_id).first()
    db_answer.title = answer.title
    db_answer.description = answer.description
    db_answer.is_correct = answer.is_correct
    db.commit()
    db.refresh(db_answer)
    return db_answer