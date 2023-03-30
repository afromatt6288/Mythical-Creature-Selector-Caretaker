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

    def add_to_userAnswers_db(self, session):
        session.add(self)
        session.commit()

    def find_all_userAnswer_by_user_id(session, user_id):
        return session.query(UserAnswer).filter(UserAnswer.user_id == user_id).all()

    def delete_userAnswers(session, answer_to_delete):
        session.delete(answer_to_delete)
        session.commit()
    
    def tabulate_quiz(session, currentUser):
        creature_id_list = []
        userAnswers = UserAnswer.find_all_userAnswer_by_user_id(session, currentUser.id)
        from .answer import Answer
        for useranswer in userAnswers:
            answersIds = []
            answersIds.append(useranswer.answer_id)
            for answerId in answersIds:
                answers = []
                answers.append(answerId)
                for answer in answers:
                    query = Answer.find_by_answer_id(session, answerId)
                    creature_id_list.append(query.creature_id1)
                    creature_id_list.append(query.creature_id2)
                    creature_id_list.append(query.creature_id3)
        print(creature_id_list)


        

## Extra Commands that could prove useful in a future update

    def create_table(base, engine):
        base.metadata.create_all(engine)

    def get_all(session):
        return session.query(UserAnswer).all()

    def find_by_userAnswer_id(session, id):
        return session.query(UserAnswer).filter(UserAnswer.id == id).all()

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