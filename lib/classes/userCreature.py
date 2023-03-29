#!/usr/bin/env python3
from datetime import datetime
from sqlalchemy import Column, Integer, String, create_engine, func, desc, ForeignKey, PrimaryKeyConstraint, DateTime
from sqlalchemy.orm import Session, relationship, validates, backref
from .base import Base

class UserCreature(Base):
    __tablename__="userCreatures"

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id'))
    creature_id = Column(Integer(), ForeignKey('creatures.id'))
    creature_species = Column(String())
    creature_name = Column(String())
    happiness = Column(Integer())
    health = Column(Integer())
    adoption_day = Column(DateTime(), default=datetime.now())
    last_interaction = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f"UserCreature ID: {self.id}" \
            + f"User ID: {self.user_id}" \
            + f"Creature ID: {self.creature_id}" \
            + f"Species: {self.creature_species}" \
            + f"Name: {self.creature_name}" \
            + f"Happiness: {self.happiness}" \
            + f"Health: {self.health}" \
            + f"Adoption Day: {self.adoption_day}" \
            + f"Last Interaction: {self.last_interaction}"








    def create_table(base, engine):
        base.metadata.create_all(engine)

    def save(session, answer):
        session.add(answer)
        session.commit()

    def get_all(session):
        return session.query(Answer).all()

    def find_by_name(session, name):
        return session.query(Answer).filter(Answer.name == name).first()

    def find_by_id(session, id):
        return session.query(Answer).filter(Answer.id == id).first()

    def find_by_name_and_breed(session, name, breed):
        return session.query(Answer).filter(Answer.name == name and Answer.breed == breed).first()

    def update_breed(session, answer, breed):
        answer.breed = breed
        session.add(answer)
        session.commit()