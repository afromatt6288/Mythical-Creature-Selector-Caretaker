#!/usr/bin/env python3
from datetime import datetime
from sqlalchemy import Column, Integer, String, create_engine, func, desc, ForeignKey, PrimaryKeyConstraint, DateTime
from sqlalchemy.orm import Session, relationship, validates, backref
from .base import Base

class Creature(Base):
    __tablename__ ="creatures"

    id = Column(Integer(), primary_key=True)
    species = Column(String())
    origin = Column(String())
    description = Column(String())
    care_instructions = Column(String())
    ascii_art = Column(String())
    
    def __repr__(self):
        return f"Creature ID: {self.id}" \
            + f"Creature Species: {self.species}" \
            + f"Creature Origin: {self.origin}" \
            + f"Creature Description: {self.description}" \
            + f"Care Instructions: {self.care_instructions}" \
            + f"ASCII Art: {self.ascii_art}"








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