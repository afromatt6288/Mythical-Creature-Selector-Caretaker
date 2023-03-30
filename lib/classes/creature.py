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

    def find_by_creature_id(session, id):
        return session.query(Creature).filter(Creature.id == id).first()

    def get_all_creatures(session):
        return session.query(Creature).all()


## Extra Commands that could prove useful in a future update

    def create_table(base, engine):
        base.metadata.create_all(engine)

    def add_to_creatures_db(session, creature):
        session.add(creature)
        session.commit()

    def find_by_creature_species(session, species):
        return session.query(Creature).filter(Creature.species == species).first()

    def update_species(session, creature, species):
        creature.species = species
        session.add(creature)
        session.commit()