#!/usr/bin/env python3
from datetime import datetime
import sys
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
    
    def tabulate_quiz(session, currentUser, x):
        tabulating=True
        if x == 10:
            occurences = 12
        elif x == 50:
            occurences = 24
        while tabulating:
            creature_id_list = []
            creature_id_dict = {}
            userAnswers = UserAnswer.find_all_userAnswer_by_user_id(session, currentUser.id)
            from .answer import Answer
            for useranswer in userAnswers:
                query = Answer.find_by_answer_id(session, useranswer.answer_id)
                creature_id_list.append(query.creature_id1)
                creature_id_list.append(query.creature_id2)
                creature_id_list.append(query.creature_id3)
            print(creature_id_list)
            for creatureId in creature_id_list:
                if creatureId in creature_id_dict:
                    creature_id_dict[creatureId] += 1
                else:
                    creature_id_dict[creatureId] = 1
            print(creature_id_dict) 
            sorted_creature_id_dict = sorted(creature_id_dict.items(), key=lambda x: x[1], reverse=True)
            from .userCreature import UserCreature
            UserCreature.select_creature(currentUser, sorted_creature_id_dict)
            # for key, value in sorted_creature_id_dict:
            #     creature = Creature.find_by_creature_id(session, key)
            #     print(f"{creature.species} appears {value} times")
            # option = input("Press Enter to continue... ")
            # if option == "exit":
            #     sys.exit(0)
            # elif option == "back" or option == "":
            tabulating=False
            

## Extra Commands that could prove useful in a future update

    def create_table(base, engine):
        base.metadata.create_all(engine)

    def get_all_userAnswers(session):
        return session.query(UserAnswer).all()

    def find_by_userAnswer_id(session, id):
        return session.query(UserAnswer).filter(UserAnswer.id == id).all()

    def update_user_id(session, userAnswer, user_id):
        userAnswer.user_id = user_id
        session.add(userAnswer)
        session.commit()

    def update_answer_id(session, userAnswer, answer_id):
        userAnswer.answer_id = answer_id
        session.add(userAnswer)
        session.commit()