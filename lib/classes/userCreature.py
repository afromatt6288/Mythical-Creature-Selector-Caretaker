#!/usr/bin/env python3
import sys
from datetime import datetime
from sqlalchemy import Column, Integer, String, create_engine, func, desc, ForeignKey, PrimaryKeyConstraint, DateTime
from sqlalchemy.orm import Session, relationship, validates, backref
from .base import Base
from .creatureInteraction import CreatureInteraction

class UserCreature(Base):
    __tablename__="userCreatures"

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id'))
    creature_id = Column(Integer(), ForeignKey('creatures.id'))
    creature_name = Column(String())
    happiness = Column(Integer(), default=50)  # set default value to 50
    health = Column(Integer(), default=50)  # set default value to 50
    obedience = Column(Integer(), default=50)  # set default value to 50
    adoption_day = Column(DateTime(), default=datetime.now())
    last_interaction = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f"UserCreature ID: {self.id} / " \
            + f"User ID: {self.user_id} / " \
            + f"Creature ID: {self.creature_id} / " \
            + f"Name: {self.creature_name} / " \
            + f"Happiness: {self.happiness} / " \
            + f"Health: {self.health} / " \
            + f"Obedience: {self.obedience} / " \
            + f"Adoption Day: {self.adoption_day} / " \
            + f"Last Interaction: {self.last_interaction}"

    def add_to_userCreatures_db(self, session):
        session.add(self)
        session.commit()

    def find_by_userCreature_name(session, name):
        return session.query(UserCreature).filter(UserCreature.creature_name == name).first()

    def update_happiness(session, creature, newScore):
        creature.happiness = newScore
        session.add(creature)
        session.commit()

    def update_health(session, creature, newScore):
        creature.health = newScore
        session.add(creature)
        session.commit()

    def update_obedience(session, creature, newScore):
        creature.obedience = newScore
        session.add(creature)
        session.commit()

    def delete_userCreature(session, creature):
        session.delete(creature)
        session.commit()

    def happiness_levels(session, creature, currentUser):
        if creature.happiness >= 100:
            UserCreature.update_happiness(session, creature, 99)
            print(f"{creature.creature_name} feels Ecstatic, and is on top of the world!")
        elif creature.happiness >= 90:
            print(f"{creature.creature_name} feels Joyful, and is really glad to see you!") 
        elif creature.happiness >=75:
            print(f"{creature.creature_name} feels Good, and hopes you are too!") 
        elif creature.happiness >=50:
            print(f"{creature.creature_name} feels Meh, and could be better!") 
        elif creature.happiness >=25:
            print(f"{creature.creature_name} feels Unhappy, and desperately needs love!")
        elif creature.happiness <25:
            print(f'''
            Terrible News! {creature.creature_name} was feeling Miserable, Unloved, Unwanted, and Alone... 
            {creature.creature_name} has ended their life... And it is all your fault!''')
            UserCreature.delete_userCreature(session, creature)
            UserCreature.view_userCreature_list(session, currentUser)

    def health_levels(session, creature, currentUser):
        if creature.health >= 100:
            UserCreature.update_health(session, creature, 99)
            print(f"{creature.creature_name} feels Ecstatic, and is on top of the world!")
        elif creature.health >= 90:
            print(f"{creature.creature_name} feels Joyful, and is really glad to see you!") 
        elif creature.health >=75:
            print(f"{creature.creature_name} feels Good, and hopes you are too!") 
        elif creature.health >=50:
            print(f"{creature.creature_name} feels Meh, and could be better!") 
        elif creature.health >=25:
            print(f"{creature.creature_name} feels Unhappy, and desperately needs love!")
        elif creature.health <25:
            print(f'''
            Terrible News! {creature.creature_name} was feeling Miserable, Unloved, Unwanted, and Alone... 
            {creature.creature_name} has ended their life... And it is all your fault!''')
            UserCreature.delete_userCreature(session, creature)
            UserCreature.view_userCreature_list(session, currentUser)

    def obedience_levels(session, creature, currentUser):
        if creature.obedience >= 100:
            UserCreature.update_obedience(session, creature, 99)
            print(f"{creature.creature_name} feels Ecstatic, and is on top of the world!")
        elif creature.obedience >= 90:
            print(f"{creature.creature_name} feels Joyful, and is really glad to see you!") 
        elif creature.obedience >=75:
            print(f"{creature.creature_name} feels Good, and hopes you are too!") 
        elif creature.obedience >=50:
            print(f"{creature.creature_name} feels Meh, and could be better!") 
        elif creature.obedience >=25:
            print(f"{creature.creature_name} feels Unhappy, and desperately needs love!")
        elif creature.obedience <25:
            print(f'''
            Terrible News! {creature.creature_name} was feeling Miserable, Unloved, Unwanted, and Alone... 
            {creature.creature_name} has ended their life... And it is all your fault!''')
            UserCreature.delete_userCreature(session, creature)
            UserCreature.view_userCreature_list(session, currentUser)

    def view_userCreature_list(session, currentUser):
        userCreaturesVisit = True
        userCreatures = session.query(UserCreature).filter(UserCreature.user_id == currentUser.id).all()
        while userCreaturesVisit:
            print(f'''
Welcome to {currentUser.username}'s Creature Farm!
Which creature would you like to visit with today?
            ''')
            n=1
            for creature in userCreatures:
                print(f"{n}) {creature.creature_name}")
                n += 1
            option = input(f'''
Select:  ''')
            if option.isdigit() and int(option) in range(1, len(userCreatures)+1):
                index = int(option) - 1
                creature = userCreatures[index]
                print(f"You selected {creature.creature_name}")
                UserCreature.hang_with_creature(session,currentUser, creature)
            elif option == "back":
                userCreaturesVisit = False
            elif option == "exit":
                sys.exit(0)
            else:
                print("Invalid option. Please select a number from the list.")

    def hang_with_creature(session, currentUser, creature):
        from .creature import Creature
        creatureDetails = Creature.find_by_creature_id(session, creature.creature_id)
        hanging=True
        while hanging:
            print(f'''
{creatureDetails.ascii_art}
{currentUser.username}, you are currently hanging out with {creature.creature_name}!
{creature.creature_name} is a {creatureDetails.species} ''')
            UserCreature.happiness_levels(session, creature, currentUser)
            UserCreature.health_levels(session, creature, currentUser)
            UserCreature.obedience_levels(session, creature, currentUser)
            option = input(f'''
You have the following options:
1) Train {creature.creature_name}       2) Feed {creature.creature_name}        3) Praise {creature.creature_name}
4) Pet {creature.creature_name}         5) Play with {creature.creature_name}   6) Groom {creature.creature_name}
7) Vet for {creature.creature_name}     8) Discipline {creature.creature_name}  9) See {creature.creature_name}'s details
10) Release {creature.creature_name} 

Select: ''')
            if option == "1":
                print("Training")
            elif option == "2":
                print("Feeding")
            elif option == "3":
                print("Praising")
            elif option == "4":
                print("Peting")
            elif option == "5":
                print("Playing")
            elif option == "6":
                print("Grooming")
            elif option == "7":
                print("Went to the Vet")
            elif option == "8":
                print("Disciplining")
            elif option == "9":
                print(f'''
{creatureDetails.description}
                ''')
            elif option == "10":
                UserCreature.delete_userCreature(session, creature)
            elif option == "back":
                hanging=False
            elif option == "exit":
                sys.exit(0)


## Extra Commands that could prove useful in a future update

    def get_all(session):
        return session.query(UserCreature).all()

    def find_by_userCreature_id(session, id):
        return session.query(UserCreature).filter(UserCreature.id == id).first()