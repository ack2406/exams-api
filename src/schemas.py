from pydantic import BaseModel

class AnswerBase(BaseModel):
    content: str
    is_correct: bool

class AnswerCreate(AnswerBase):
    pass

class AnswerUpdate(AnswerBase):
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

class QuestionUpdate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int
    answers: list[Answer] = []

    class Config:
        orm_mode = True


class TestBase(BaseModel):
    name: str
    description: str
    picture_path: str

class TestCreate(TestBase):
    pass

class TestUpdate(TestBase):
    pass

class Test(TestBase):
    id: int
    questions: list[Question] = []

    class Config:
        orm_mode = True
