import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Question(Base):
    __tablename__ = 'questions'

    id = sa.Column(sa.Integer, primary_key=True)
    question = sa.Column(sa.String(255), unique=True)
    answer = sa.Column(sa.String(255))
    created = sa.Column(sa.Date)
