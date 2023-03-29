#!/usr/bin/env python3
from datetime import datetime
from sqlalchemy import Column, Integer, String, create_engine, func, desc, ForeignKey, PrimaryKeyConstraint, DateTime
from sqlalchemy.orm import Session, relationship, validates, backref
from .base import Base

class CreatureInteraction(Base):
    __tablename__ ="creatureInteractions"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    effect_on_happiness = Column(String())
    effect_on_health = Column(String())
    effect_on_obedience = Column(String())
    
    def __repr__(self):
        return f"Interaction ID: {self.id}" \
            + f"Interaction Name: {self.name}" \
            + f"Interaction Happiness: {self.effect_on_happiness}" \
            + f"Interaction Health: {self.effect_on_health}" \
            + f"Interaction Obedience: {self.effect_on_obedience}"







    def create_table(base, engine):
        base.metadata.create_all(engine)

    def add_to_creatureInteractions_db(session, creatureInteraction):
        session.add(creatureInteraction)
        session.commit()

    def get_all(session):
        return session.query(CreatureInteraction).all()

    def find_by_name(session, name):
        return session.query(CreatureInteraction).filter(CreatureInteraction.name == name).first()

    def find_by_id(session, id):
        return session.query(CreatureInteraction).filter(CreatureInteraction.id == id).first()

    def find_by_name_and_breed(session, name, breed):
        return session.query(CreatureInteraction).filter(CreatureInteraction.name == name and CreatureInteraction.breed == breed).first()

    def update_breed(session, creatureInteraction, breed):
        creatureInteraction.breed = breed
        session.add(creatureInteraction)
        session.commit()