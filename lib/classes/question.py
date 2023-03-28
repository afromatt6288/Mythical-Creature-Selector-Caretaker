#!/usr/bin/env python3
from datetime import datetime
from sqlalchemy import Column, Integer, String, create_engine, func, desc, ForeignKey, PrimaryKeyConstraint, DateTime
from sqlalchemy.orm import Session, relationship, validates, backref
from .base import Base

class Question(Base):
    __tablename__ ="questions"

    id = Column(Integer(), primary_key=True)
    content = Column(String())
    
    def __repr__(self):
        return f"Question ID: {self.id}" \
            + f"Question Content: {self.content}"

    




    

    def create_table(base, engine):
        base.metadata.create_all(engine)

    def save(session, question):
        session.add(question)
        session.commit()

    def get_all(session):
        return session.query(Question).all()

    def find_by_id(session, id):
        return session.query(Question).filter(Question.id == id).first()

    def update_content(session, answer, content):
        answer.content = content
        session.add(answer)
        session.commit()

    def update_question(session, question, ):
        question.breed = breed
        session.add(question)
        session.commit()