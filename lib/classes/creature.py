#!/usr/bin/env python3
import sys
from sqlalchemy import *
from sqlalchemy.orm import *
from .base import Base

engine = create_engine('sqlite:///myth.db')
Session = sessionmaker(bind=engine)
session = Session()

class Creature(Base):
    __tablename__ ="creatures"

    id = Column(Integer(), primary_key=True)
    species = Column(String())
    origin = Column(String())
    description = Column(String())
    care_instructions = Column(String())
    ascii_art = Column(String())
    
    def __repr__(self):
        return f'''
Creature ID: {self.id}
ASCII Art: {self.ascii_art}

Creature Species: {self.species}   Creature Origin: {self.origin}

Creature Description: {self.description}

Care Instructions: {self.care_instructions}
        '''

    def find_by_creature_id(session, id):
        return session.query(Creature).filter(Creature.id == id).first()

    def get_all_creatures(session):
        return session.query(Creature).all()
    
##################################################################################### 

    def mythical_menagerie():
        print("Welcome to the Secret Gallery")
        menagerieSelect = True
        while menagerieSelect:
            creatures = Creature.get_all_creatures(session)
            print(f'''
⠀⣠⣄⣠⣄⠀⠀⠀⢀⣤⠀⣤⠀⠀⣤⠀⠀⠀⠀⠀⠀⠀⢠⡄⠀⠀⣀⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⠀⠀
⠀⣿⢹⡏⣿⢰⣶⣶⢸⣿⠆⣿⣶⡄⣶⢠⡶⠶⠄⣶⢶⡆⢸⡇⠀⢸⡟⠉⢛⡃⣴⠆⣶⣲⣆⣴⠶⣦⢸⡷⢰⡆⣶⠀⣶⢦⡶⣲⡄⠀⢸⡏⣿⢹⡇⣴⣖⣦⢠⡶⣶⢠⡶⢶⡄⣴⠶⣦⢰⣖⣶⡀⣶⢶⡆⣰⣖⣶⠀⠀
⠀⠿⠸⠇⠿⠈⣻⣿⠀⠛⠇⠿⠸⠇⠿⠈⠻⠟⠁⠻⠿⠇⠸⠇⠀⠈⠻⠿⠟⠁⠿⠀⠻⠶⠀⠙⠿⠿⠈⠻⠈⠿⠟⠀⠿⠈⠻⠖⠀⠀⠸⠇⠿⠸⠇⠙⠷⠂⠸⠇⠿⠈⠻⠿⠇⠙⣃⡿⠘⠳⠆⠀⠿⠸⠇⠘⠷⠆⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    
Welcome, to the Mythical Creature Menagerie!
Here you will see a list of all of the creatures available.
Selecting that creature lets you see all the creature details!
        ''')
            input("Press Enter to continue... ")
            n=1
            for creature in creatures:
                print(f"{n}) {creature.species}")
                n += 1
            option = input(f'''
Select a creature to View it's Details: ''')
            if option.isdigit() and int(option) in range(1, len(creatures)+1):
                index = int(option) - 1
                creature = creatures[index]
                print(f"You selected a {creature.species}")
                print(creature)
                input("Press Enter to continue")     
            elif option == "back":
                print("Back to Main Menu!")
                menagerieSelect = False
            elif option == "exit":
                sys.exit(0)
            else:
                print("Invalid option. Please try again!")
                input("Press Enter to proceed...")    

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