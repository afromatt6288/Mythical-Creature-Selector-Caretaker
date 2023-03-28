#!/usr/bin/env python3
import random
import time
import copy
from sqlalchemy import *
from sqlalchemy.orm import *
from classes.answer import Answer
from classes.creature import Creature
from classes.creatureInteraction import CreatureInteraction
from classes.question import Question
from classes.userCreature import UserCreature
from classes.user import User
from classes.base import Base

if __name__ == '__main__':
    # answer = Answer('myth.db')
    # creature = Creature('myth.db')
    # creatureInteraction = CreatureInteraction('myth.db')
    # question = Question('myth.db')
    # user = User('myth.db')
    # userCreature = UserCreature('myth.db')
    engine = create_engine('sqlite:///myth.db')

    print('''
             ▄▄▄▄███▄▄▄▄   ▄██   ▄       ███        ▄█    █▄     ▄█   ▄████████    ▄████████  ▄█       
           ▄██▀▀▀███▀▀▀██▄ ███   ██▄ ▀█████████▄   ███    ███   ███  ███    ███   ███    ███ ███       
           ███   ███   ███ ███▄▄▄███    ▀███▀▀██   ███    ███   ███▌ ███    █▀    ███    ███ ███       
           ███   ███   ███ ▀▀▀▀▀▀███     ███   ▀  ▄███▄▄▄▄███▄▄ ███▌ ███          ███    ███ ███       
           ███   ███   ███ ▄██   ███     ███     ▀▀███▀▀▀▀███▀  ███▌ ███        ▀███████████ ███       
           ███   ███   ███ ███   ███     ███       ███    ███   ███  ███    █▄    ███    ███ ███       
           ███   ███   ███ ███   ███     ███       ███    ███   ███  ███    ███   ███    ███ ███▌    ▄ 
            ▀█   ███   █▀   ▀█████▀     ▄████▀     ███    █▀    █▀   ████████▀    ███    █▀  █████▄▄██ 
                                                                                   ▀        
       ▄████████    ▄████████    ▄████████    ▄████████     ███     ███    █▄     ▄████████    ▄████████ 
       ███    ███   ███    ███   ███    ███   ███    ███ ▀█████████▄ ███    ███   ███    ███   ███    ███ 
       ███    █▀    ███    ███   ███    █▀    ███    ███    ▀███▀▀██ ███    ███   ███    ███   ███    █▀  
       ███         ▄███▄▄▄▄██▀  ▄███▄▄▄       ███    ███     ███   ▀ ███    ███  ▄███▄▄▄▄██▀  ▄███▄▄▄     
       ███        ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ▀███████████     ███     ███    ███ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     
       ███    █▄  ▀███████████   ███    █▄    ███    ███     ███     ███    ███ ▀███████████   ███    █▄  
       ███    ███   ███    ███   ███    ███   ███    ███     ███     ███    ███   ███    ███   ███    ███ 
       ████████▀    ███    ███   ██████████   ███    █▀     ▄████▀   ████████▀    ███    ███   ██████████ 
                    ███    ███                                                    ███    ███             
             
 ▄████████    ▄████████    ▄████████    ▄████████     ███        ▄████████    ▄█   ▄█▄    ▄████████    ▄████████ 
███    ███   ███    ███   ███    ███   ███    ███ ▀█████████▄   ███    ███   ███ ▄███▀   ███    ███   ███    ███ 
███    █▀    ███    ███   ███    ███   ███    █▀     ▀███▀▀██   ███    ███   ███▐██▀     ███    █▀    ███    ███ 
███          ███    ███  ▄███▄▄▄▄██▀  ▄███▄▄▄         ███   ▀   ███    ███  ▄█████▀     ▄███▄▄▄      ▄███▄▄▄▄██▀ 
███        ▀███████████ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀         ███     ▀███████████ ▀▀█████▄    ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
███    █▄    ███    ███ ▀███████████   ███    █▄      ███       ███    ███   ███▐██▄     ███    █▄  ▀███████████ 
███    ███   ███    ███   ███    ███   ███    ███     ███       ███    ███   ███ ▀███▄   ███    ███   ███    ███ 
████████▀    ███    █▀    ███    ███   ██████████    ▄████▀     ███    █▀    ███   ▀█▀   ██████████   ███    ███ 
                          ███    ███                                         ▀                        ███    ███
'''
    )

    # Checks for new or returning user
    with Session(engine) as session:
        inprogram = True
        while inprogram:
            userinput1 = input("Are you a New or Returning Caretaker:")


