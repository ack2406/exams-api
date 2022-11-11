from pydantic import BaseModel

class AnswerBase(BaseModel):
    content: str
    is_correct: bool

class AnswerCreate(AnswerBase):
    pass

class Answer(AnswerBase):
    id: int
    question_id: int

    class Config:
        orm_mode = True

class QuestionBase(BaseModel):
    content: str
    picture_path: str

class QuestionCreate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int
    answers: list[Answer] = []

    class Config:
        orm_mode = True

class SetBase(BaseModel):
    name: str
    description: str
    picture_path: str

class SetCreate(SetBase):
    pass

class Set(SetBase):
    id: int
    questions: list[Question] = []

    class Config:
        orm_mode = True
        