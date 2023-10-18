from typing import List

from fastapi import APIRouter, Depends

from ..models.questions import Question, QuestionCreate
from ..services.questions import QuestionsService

router = APIRouter(
    prefix='/questions',
    tags=['questions']
)


@router.post('/', response_model=List[Question], summary='Create questions')
def create_questions(
        questions_data: QuestionCreate,
        service: QuestionsService = Depends()
):
    """
    Creating a certain number of unique questions.

    - **questions_num**: number of questions

    :param questions_data:
    :param service:
    :return:
    """
    return service.create_questions(questions_data)
