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
        return f"Creature ID: {self.id} / " \
            + f"Creature Species: {self.species} / " \
            + f"Creature Origin: {self.origin} / " \
            + f"Creature Description: {self.description} / " \
            + f"Care Instructions: {self.care_instructions} / " \
            + f"ASCII Art: {self.ascii_art}"








    def create_table(base, engine):
        base.metadata.create_all(engine)

    def add_to_creatures_db(session, creature):
        session.add(creature)
        session.commit()

    def get_all(session):
        return session.query(Creature).all()

    def find_by_name(session, name):
        return session.query(Creature).filter(Creature.name == name).first()

    def find_by_id(session, id):
        return session.query(Creature).filter(Creature.id == id).first()

    def find_by_name_and_breed(session, name, breed):
        return session.query(Creature).filter(Creature.name == name and Creature.breed == breed).first()

    def update_breed(session, creature, breed):
        creature.breed = breed
        session.add(creature)
        session.commit()