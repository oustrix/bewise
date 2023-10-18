from datetime import datetime

from pydantic import BaseModel


class QuestionBase(BaseModel):
    pass


class Question(QuestionBase):
    id: int
    question: str
    answer: str
    created: datetime


class QuestionCreate(QuestionBase):
    questions_num: int
