#!/usr/bin/env python3
from datetime import datetime
from sqlalchemy import Column, Integer, String, create_engine, func, desc, ForeignKey, PrimaryKeyConstraint, DateTime
from sqlalchemy.orm import Session, relationship, validates, backref
from .base import Base

class CreatureInteraction(Base):
    __tablename__ ="creatureInteractions"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    effect_on_happiness = Column(Integer())
    effect_on_health = Column(Integer())
    effect_on_obedience = Column(Integer())
    effect_on_loyalty = Column(Integer())
    
    def __repr__(self):
        return f"Interaction ID: {self.id} / " \
            + f"Interaction Name: {self.name} / " \
            + f"Interaction Happiness: {self.effect_on_happiness} / " \
            + f"Interaction Health: {self.effect_on_health} / " \
            + f"Interaction Obedience: {self.effect_on_obedience} / " \
            + f"Interaction Loyalty: {self.effect_on_loyalty}"

    def find_by_id(session, id):
        return session.query(CreatureInteraction).filter(CreatureInteraction.id == id).first()

    def interact(session, userCreature, interact_id):
        from .creature import Creature
        creatureDetails = Creature.find_by_creature_id(session, userCreature.creature_id)
        interaction = CreatureInteraction.find_by_id(session, interact_id)
        print(interaction)
        if interact_id == "1":
            print(f'''
Did some hard, but rewarding, {creatureDetails.species} 
Training with {userCreature.creature_name}!
            ''')
        elif interact_id == "2":
            print(f'''
{creatureDetails.species} feeding time is always a hit with 
{userCreature.creature_name}!
        ''')
        elif interact_id == "3":
            print(f'''
Praised {userCreature.creature_name} for being a good 
{creatureDetails.species}!
        ''')
        elif interact_id == "4":
            print(f'''
Petted {userCreature.creature_name}, as a good 
{creatureDetails.species} deserves!
        ''')
        elif interact_id == "5":
            print(f'''
Playing with a {creatureDetails.species} can be dicey. 
Luckily {userCreature.creature_name} is gentle!
        ''')
        elif interact_id == "6":
            print(f'''
{creatureDetails.species} grooming is not something that 
{userCreature.creature_name} enjoys!
        ''')
        elif interact_id == "7":
            print(f'''
Went to a Vet specializing in {creatureDetails.species}. 
{userCreature.creature_name} was not ammused, but does feel better!
        ''')
        elif interact_id == "8":
            print(f'''
{userCreature.creature_name} was misbehaving... 
but Disciplining a {creatureDetails.species} is not for the faint of heart!
        ''')
        from .userCreature import UserCreature
        UserCreature.update_happiness(session, userCreature, userCreature.happiness + interaction.effect_on_happiness)
        UserCreature.update_health(session, userCreature, userCreature.health + interaction.effect_on_health)
        UserCreature.update_obedience(session, userCreature, userCreature.obedience + interaction.effect_on_obedience)
        UserCreature.update_loyalty(session, userCreature, userCreature.loyalty + interaction.effect_on_loyalty)
        UserCreature.update_last_interaction(session, userCreature)


## Extra Commands that could prove useful in a future update

    def create_table(base, engine):
        base.metadata.create_all(engine)

    def add_to_creatureInteractions_db(session, newCreatureInteraction):
        session.add(newCreatureInteraction)
        session.commit()

    def get_all_creatureInteractions(session):
        return session.query(CreatureInteraction).all()

    def find_by_name(session, name):
        return session.query(CreatureInteraction).filter(CreatureInteraction.name == name).first()

    def update_creatureInteraction_name(session, creatureInteraction, newName):
        creatureInteraction.newName = newName
        session.add(creatureInteraction)
        session.commit()