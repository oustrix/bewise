from datetime import datetime
from typing import List

import requests
from fastapi import Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette import status

from src.proxy import tables
from src.proxy.database import get_session
from src.proxy.models.questions import QuestionCreate


class QuestionsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
        self.endpoint = 'https://jservice.io/api/random'

    def create_questions(self, data: QuestionCreate) -> List[tables.Question]:
        questions: List[tables.Question] = []

        url = f'{self.endpoint}?count={data.questions_num}'

        while True:
            res = requests.get(url).json()

            for raw_question in res:
                question = tables.Question(
                    question=raw_question['question'],
                    answer=raw_question['answer'],
                    created=datetime.utcnow()
                )
                questions.append(question)

            self.session.add_all(questions)
            try:
                self.session.commit()
                break
            except IntegrityError:
                self.session.rollback()
                self.session.flush()
                questions = []
            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=e
                )

        return questions
