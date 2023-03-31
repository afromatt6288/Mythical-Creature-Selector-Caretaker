#!/usr/bin/env python3
from sqlalchemy import *
from sqlalchemy.orm import *
from .base import Base

class Question(Base):
    __tablename__ ="questions"

    id = Column(Integer(), primary_key=True)
    content = Column(String())
    
    def __repr__(self):
        return f"Question ID: {self.id} / " \
            + f"Question Content: {self.content}"

    def find_by_question_id(session, id):
        return session.query(Question).filter(Question.id == id).first()
    

## Extra Commands that could prove useful in a future update

    def create_table(base, engine):
        base.metadata.create_all(engine)

    def add_to_questions_db(session, question):
        session.add(question)
        session.commit()

    def get_all_questions(session):
        return session.query(Question).all()

    def update_question_content(session, answer, content):
        answer.content = content
        session.add(answer)
        session.commit()