#!/usr/bin/env python3
from datetime import datetime
from sqlalchemy import Column, Integer, String, create_engine, func, desc, ForeignKey, PrimaryKeyConstraint, DateTime
from sqlalchemy.orm import Session, relationship, validates, backref
from .base import Base

class UserAnswer(Base):
    __tablename__ ="userAnswers"
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id'))
    answer_id = Column(Integer(), ForeignKey('answers.id'))
    
    def __repr__(self):
        return f"UserAnswer ID: {self.id} / " \
            + f"User ID: {self.user_id} / " \
            + f"Answer ID: {self.answer_id} / " 


## Extra Commands that could prove useful in a future update

    def create_table(base, engine):
        base.metadata.create_all(engine)

    def add_to_userAnswers_db(session, userAnswer):
        session.add(userAnswer)
        session.commit()

    def get_all(session):
        return session.query(UserAnswer).all()

    def find_by_id(session, id):
        return session.query(UserAnswer).filter(UserAnswer.id == id).all()

    def find_by_question_id(session, user_id):
        return session.query(UserAnswer).filter(UserAnswer.user_id == user_id).all()

    def update_content(session, userAnswer, content):
        userAnswer.content = content
        session.add(userAnswer)
        session.commit()

    def update_question_id(session, userAnswer, user_id):
        userAnswer.user_id = user_id
        session.add(userAnswer)
        session.commit()

    def update_creature_id(session, userAnswer, answer_id):
        userAnswer.answer_id = answer_id
        session.add(userAnswer)
        session.commit()