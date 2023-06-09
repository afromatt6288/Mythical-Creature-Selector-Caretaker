#!/usr/bin/env python3
from sqlalchemy import *
from sqlalchemy.orm import *
from .base import Base

class Answer(Base):
    __tablename__ ="answers"
    id = Column(Integer(), primary_key=True)
    content = Column(String())
    question_id = Column(Integer(), ForeignKey('questions.id'))
    creature_id1 = Column(Integer(), ForeignKey('creatures.id'))
    creature_id2 = Column(Integer(), ForeignKey('creatures.id'))
    creature_id3 = Column(Integer(), ForeignKey('creatures.id'))
    
    def __repr__(self):
        return f"Answer ID: {self.id} / " \
            + f"Answer Content: {self.content} / " \
            + f"Question ID: {self.content} / " \
            + f"Answer Creature 1: {self.creature_id1} / " \
            + f"Answer Creature 2: {self.creature_id2} / " \
            + f"Answer Creature 3: {self.creature_id3} / "

    def find_by_answer_id(session, id):
        return session.query(Answer).filter(Answer.id == id).first()


## Extra Commands that could prove useful in a future update

    def create_table(base, engine):
        base.metadata.create_all(engine)

    def add_to_answers_db(session, answer):
        session.add(answer)
        session.commit()

    def get_all_answers(session):
        return session.query(Answer).all()

    def find_by_question_id(session, question_id):
        return session.query(Answer).filter(Answer.question_id == question_id).all()

    def update_answer_content(session, answer, content):
        answer.content = content
        session.add(answer)
        session.commit()

    def update_question_id(session, answer, question_id):
        answer.question_id = question_id
        session.add(answer)
        session.commit()

    def update_creature_id1(session, answer, creature_id1):
        answer.creature_id1 = creature_id1
        session.add(answer)
        session.commit()

    def update_creature_id2(session, answer, creature_id2):
        answer.creature_id2 = creature_id2
        session.add(answer)
        session.commit()

    def update_creature_id3(session, answer, creature_id3):
        answer.creature_id3 = creature_id3
        session.add(answer)
        session.commit()

