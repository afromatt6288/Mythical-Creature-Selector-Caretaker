#!/usr/bin/env python3
import sys
from datetime import datetime
from sqlalchemy import *
from sqlalchemy.orm import *
from .creature import Creature
from .creatureInteraction import CreatureInteraction
from .base import Base

engine = create_engine('sqlite:///myth.db')
Session = sessionmaker(bind=engine)
session = Session()

class UserCreature(Base):
    __tablename__="userCreatures"

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id'))
    creature_id = Column(Integer(), ForeignKey('creatures.id'))
    creature_name = Column(String())
    happiness = Column(Integer(), default=60)  # set default value to 60
    health = Column(Integer(), default=60)  # set default value to 60
    obedience = Column(Integer(), default=60)  # set default value to 60
    loyalty = Column(Integer(), default=60)  # set default value to 60
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
            + f"Loyalty: {self.loyalty} / " \
            + f"Adoption Day: {self.adoption_day} / " \
            + f"Last Interaction: {self.last_interaction}"

#############################################################################

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

    def update_loyalty(session, creature, newScore):
        creature.loyalty = newScore
        session.add(creature)
        session.commit()
    
    def update_last_interaction(session, creature):
        creature.last_interaction = datetime.now()
        session.add(creature)
        session.commit()        

    def delete_userCreature(session, creature):
        session.delete(creature)
        session.commit()

#########################################################################        

    def happiness_levels(session, creature, currentUser):
        if creature.happiness >= 100:
            UserCreature.update_happiness(session, creature, 99)
            print(f"Happiness: {creature.creature_name} feels Ecstatic, and is on top of the world!")
        elif creature.happiness >= 90:
            print(f"Happiness: {creature.creature_name} feels Joyful, and is really glad to see you!") 
        elif creature.happiness >=75:
            print(f"Happiness: {creature.creature_name} feels Good, and hopes you are too!") 
        elif creature.happiness >=50:
            print(f"Happiness: {creature.creature_name} feels Meh, and could be better!") 
        elif creature.happiness >=10:
            print(f"Happiness: {creature.creature_name} feels Unhappy, and desperately needs love!")
        elif creature.happiness <10:
            print(f'''
Happiness: Terrible News! {creature.creature_name} was feeling Miserable, Unloved, Unwanted, and Alone... 
{creature.creature_name} has ended their life... And it is all your fault!''')
            UserCreature.delete_userCreature(session, creature)
            UserCreature.view_userCreature_list(session, currentUser)

    def health_levels(session, creature, currentUser):
        if creature.health >= 100:
            UserCreature.update_health(session, creature, 99)
            print(f"Health: {creature.creature_name} feels Healthy and is extra Energetic!")
        elif creature.health >= 90:
            print(f"Health: {creature.creature_name} feels Darn Good!") 
        elif creature.health >=75:
            print(f"Health: {creature.creature_name} feels Mostly Okay, but is a bit fatigued.") 
        elif creature.health >=50:
            print(f"Health: {creature.creature_name} feels a bit under the weather, and could be better!") 
        elif creature.health >=10:
            print(f"Health: {creature.creature_name} feels Sick, and desperately needs Medical Attention!")
        elif creature.health <10:
            print(f'''
Health: Terrible News! {creature.creature_name} was very Sick and became terminal. 
Because you weren't there, {creature.creature_name} died in pain and very alone.
Oregon Trail Easter Egg: {creature.creature_name} has died of dysentary''')
            UserCreature.delete_userCreature(session, creature)
            UserCreature.view_userCreature_list(session, currentUser)

    def obedience_levels(session, creature, currentUser):
        if creature.obedience >= 100:
            UserCreature.update_obedience(session, creature, 99)
            print(f"Obedience: {creature.creature_name} is focused on you and ready to follow your command!")
        elif creature.obedience >= 90:
            print(f"Obedience: {creature.creature_name} is ready and willing to do as you say!") 
        elif creature.obedience >=75:
            print(f"Obedience: {creature.creature_name} is pretty responsive to your requests.") 
        elif creature.obedience >=50:
            print(f"Obedience: {creature.creature_name} might do what you say... when they feel like it.") 
        elif creature.obedience >=10:
            print(f"Obedience: {creature.creature_name} could care less what you ask, and just does what they want...")
        elif creature.obedience <10:
            print(f'''
Obedience: Terrible News! Due to lack of training, {creature.creature_name} ignored your commands and ran out into traffic.
{creature.creature_name} was crushed by a semi... if only you had trained them better...''')
            UserCreature.delete_userCreature(session, creature)
            UserCreature.view_userCreature_list(session, currentUser)
    
    def loyalty_levels(session, creature, currentUser):
        if creature.obedience >= 100:
            UserCreature.update_loyalty(session, creature, 99)
            print(f"Loyalty: {creature.creature_name} trusts you implicitly, and only wants to be near you!")
        elif creature.obedience >= 90:
            print(f"Loyalty: {creature.creature_name} is loyal and true, and would not betray you!") 
        elif creature.obedience >=75:
            print(f"Loyalty: {creature.creature_name} feels you are a good master, and wants to stick by your side!") 
        elif creature.obedience >=50:
            print(f"Loyalty: {creature.creature_name} feels you are not all that, and wouldn't be opposed to a better master.") 
        elif creature.obedience >=10:
            print(f"Loyalty: {creature.creature_name} feels Animosity towards you, and is actively planning to betray you!")
        elif creature.obedience <10:
            print(f'''
Loyalty: Terrible News! {creature.creature_name} couldn't hold it back any longer, and finally puth their plan of betrayal into action.
{creature.creature_name} left you for another master. But not before leaving a huge crap on your bed... Gross!''')
            UserCreature.delete_userCreature(session, creature)
            UserCreature.view_userCreature_list(session, currentUser)
        
####################################################################################

    def view_userCreature_list(session, currentUser):
        userCreaturesVisit = True
        userCreatures = session.query(UserCreature).filter(UserCreature.user_id == currentUser.id).all()
        while userCreaturesVisit:
            print(f'''
⠀⠀⢀⣠⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣴⣿⡿⠛⢿⣿⣷⠀⠀⣠⣤⠀⣀⣤⣄⡀⠀⠀⣀⣤⣄⡀⠀⢸⣿⣇⡀⣀⣀⠀⣀⡀⠀⢀⣠⣄⠀⣀⣤⣄⡀⠀⠀⠀⠀⣿⡿⠻⠛⠁⢀⣠⣤⣀⠀⠀⢀⣠⣄⠀⣀⣤⣀⣀⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⡀⠀⠀⣤⣤⠀⣾⣿⠛⢸⣿⢫⣽⣿⡆⣼⣿⠛⢻⣿⡄⢸⣿⡟⠃⣿⣿⠀⣿⡇⠀⣿⣿⠻⣾⣿⢩⣿⣿⠀⠀⠀⠀⣿⣷⡆⠀⢠⣿⡟⠛⣿⣧⠀⣾⣿⠛⢸⣿⡟⣿⣿⢻⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠹⣿⣷⣶⣾⣿⠟⠀⣿⣿⠀⠸⣿⣦⣦⡀⠀⢻⣿⣶⣾⣿⡇⠸⣿⣿⡆⢿⣿⣶⣿⠇⠀⣿⣿⠀⢿⣿⣦⣦⠀⠀⠀⠀⠀⣿⡏⠁⠀⠈⢿⣷⡆⣿⣿⠀⣿⣿⠀⢸⣿⡇⣿⣿⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠉⠛⠋⠁⠀⠀⠈⠉⠀⠀⠈⠉⠉⠁⠀⠀⠉⠉⠉⠉⠁⠀⠈⠉⠀⠀⠙⠛⠁⠀⠀⠉⠉⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠈⠉⠁⠉⠁⠀⠉⠉⠀⠈⠉⠀⠉⠁⠈⠉⠁⠀

Welcome to {currentUser.username}'s Creature Farm!
Which creature would you like to visit with today?
            ''')
            if len(userCreatures) > 0:
                n=1
                print("0) Back to Main Menu")
                for creature in userCreatures:
                    print(f"{n}) {creature.creature_name}")
                    n += 1
                option = input(f'''
Select: ''')
                if option.isdigit() and int(option) in range(1, len(userCreatures)+1):
                    index = int(option) - 1
                    creature = userCreatures[index]
                    print(f"You selected {creature.creature_name}")
                    UserCreature.hang_with_creature(session,currentUser, creature)
                elif option == "0" or option == "back":
                    userCreaturesVisit = False
                elif option == "exit":
                    sys.exit(0)
                else:
                    print("Invalid option. Please select a number from the list.")
                    input("Press Enter to continue... ")
            else:
                print("You currently have no Creatures. Time to Adopt!")
                option = input(f'''
0) Back to Main Menu

Select: ''')
                if option == "0" or option =="back":
                    userCreaturesVisit = False
                elif option == "exit":
                    sys.exit(0)

####################################################################################

    def hang_with_creature(session, currentUser, creature):
        # from .creature import Creature
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
            UserCreature.loyalty_levels(session, creature, currentUser)
            input("Press Enter to continue... ")
            option = input(f'''
You have the following options:
0) Back to Main Menu                        1) Train {creature.creature_name}           2) Feed {creature.creature_name}        
3) Praise {creature.creature_name}          4) Pet {creature.creature_name}             5) Play with {creature.creature_name}   
6) Groom {creature.creature_name}           7) Vet for {creature.creature_name}         8) Discipline {creature.creature_name}  
9) Release {creature.creature_name}         10) See {creature.creature_name}'s details 


Select: ''')
            if option == "1":
                CreatureInteraction.interact(session, creature, "1")
            elif option == "2":
                CreatureInteraction.interact(session, creature, "2")
            elif option == "3":
                CreatureInteraction.interact(session, creature, "3")
            elif option == "4":
                CreatureInteraction.interact(session, creature, "4")
            elif option == "5":
                CreatureInteraction.interact(session, creature, "5")
            elif option == "6":
                CreatureInteraction.interact(session, creature, "6")
            elif option == "7":
                CreatureInteraction.interact(session, creature, "7")
            elif option == "8":
                CreatureInteraction.interact(session, creature, "8")
            elif option == "9":
                UserCreature.delete_userCreature(session, creature)
                UserCreature.view_userCreature_list(session, currentUser)
            elif option == "10":
                print(f'''
{creatureDetails.description}
                ''')
                input("Press Enter to continue... ")
            elif option == "0" or option == "back":
                hanging=False
            elif option == "exit":
                sys.exit(0)

#####################################################################################
    
    def select_creature(currentUser, occurences, sorted_creature_id_dict = {}):
        from .creature import Creature
        creatureSelect = True
        while creatureSelect:
            if len(sorted_creature_id_dict) == 0:
                occurences = 1
                creatures = Creature.get_all_creatures(session)
                print(f'''
⠀⣴⢦⣴⣦⠀⣀⢀⡀⣴⡄⣴⣆⡀⢐⡆⠀⢀⡀⠀⠀⣀⠀⢠⣦⠀⠀⣠⡶⣶⣄⠀⢀⠀⢀⡀⠀⠀⣀⠀⢠⣦⠀⣀⢀⡀⠀⡀⠀⣀⠀⠀⠀⢠⣶⠀⠀⣀⠀⢰⡆⠀⣀⠀⠀⢀⡀⠀⣦⡀⣲⠀⢀⡀⠀⠀⢀⠀⠀⠀
⠀⣿⢸⣿⣿⡇⣿⢸⡇⣿⡟⣿⡟⣷⢸⡇⣼⡟⣛⡂⣾⠻⣷⢸⣿⠀⠀⣿⠁⢀⣭⢰⡿⢰⣿⣿⡆⣾⠛⣷⢸⣿⢻⣿⢸⡇⣸⡟⣾⣿⣿⠀⠀⠸⣷⢠⣿⢿⡧⢸⡇⣾⣽⣷⣴⡟⢛⡂⣿⠃⣿⣧⣿⠛⣧⢰⡟⣿⠀⠀
⠀⠿⠸⠟⠿⠇⠻⣿⡇⠙⠟⠿⠇⠿⠸⠇⠘⠿⠟⠁⠻⠇⠟⠸⠿⠀⠀⠙⠿⠿⠃⠸⠇⠈⠻⠗⠀⠙⠿⠿⠈⠻⠃⠻⠿⠁⠿⠃⠙⠿⠆⠀⠀⠿⠟⠈⠻⠷⠀⠸⠇⠙⠿⠆⠘⠿⠟⠁⠙⠇⠿⠋⠻⠿⠃⠸⠇⠿⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                                                

Welcome, {currentUser.username} to the Mythical Creature Selection Screen!

By being here proves one of two things:
Either, you know exactly who you are and what you want!
Or... You were too lazy to take a short quiz

In either case, please select a creature of your choice from below!
            ''')
                userinput = input("Press enter to continue... ")
                if userinput == "back" or userinput == "0":
                    print("Back to the Beginning!")
                    creatureSelect = False
                elif userinput == "exit":
                    sys.exit(0)
                elif userinput == "":
                    pass
                else:
                    print("Invalid Entry. Please try again!")
                # input("Press Enter to continue... ")
                n=1
                print("0) Back to Main Menu")
                for creature in creatures:
                    print(f"{n}) {creature.species}")
                    n += 1
            else:        
                n=1
                creatures = []
                print('''
⠀⠹⣷⣴⡿⠁⢀⣀⡀⠀⣀⡀⣀⡀⠀⢀⡀⠀⠀⣿⣿⢿⣷⠀⠀⣀⡀⠀⠀⢀⡀⢀⡀⢀⡀⢸⣿⢸⣿⣀⠀⠀⣀⠀⣿⡇⠀⠀⠀
⠀⠀⢹⣿⠀⢰⣿⠛⣿⡆⣿⡇⣿⡇⢰⣿⠇⠀⠀⣿⣿⣾⡟⢠⣿⢋⣿⡇⢰⣿⠟⢸⡇⣿⡇⢸⣿⢸⣿⠟⠀⣿⡿⠀⠿⠇⠀⠀⠀
⠀⠀⢸⣿⠀⠘⢿⣶⡿⠃⠹⣷⣿⠇⢸⣿⠀⠀⠀⣿⣿⢹⣿⡈⢿⣷⡦⠀⣿⡿⠀⠸⣷⣿⠇⢸⣿⠀⠻⣿⣾⡿⠃⠀⣿⡇⠀

Creature Compatibility:
                ''')
                print("0) Back to Main Menu")
                for key, value in sorted_creature_id_dict:
                    creature = Creature.find_by_creature_id(session, key)
                    creatures.append(creature)
                    print(f"{n}) {creature.species.ljust(22)} {int((value / occurences) * 100)}%")
                    n += 1
            option = input(f'''
Select your new Companion: ''')
            if option.isdigit() and int(option) in range(1, len(creatures)+1):
                index = int(option) - 1
                creature = creatures[index]
                print(f"You selected a {creature.species}")
                newUserCreatureName = input('''
Please name your new companion: ''')
                if newUserCreatureName == "back":
                    print("Back to Main Menu!")
                    creatureSelect = False
                elif newUserCreatureName == "exit":
                    sys.exit(0)
                elif UserCreature.find_by_userCreature_name(session, newUserCreatureName):
                    print("Username already exists. Please Try Again")
                    input("Press Enter to proceed...")
                elif type(newUserCreatureName) is str and 4 <= len(newUserCreatureName):
                    UserCreature(user_id = currentUser.id, creature_id = creature.id, creature_name = newUserCreatureName).add_to_userCreatures_db(session)
                    creatureSelect = False
                else:
                    print("Creature name must be 4 letters or longer!")
                    input("Press Enter to proceed...")
            elif option == "back" or option == "0":
                print("Back to Main Menu!")
                creatureSelect = False
            elif option == "exit":
                sys.exit(0)
            else:
                print("Invalid option. Please try again!")
                input("Press Enter to proceed...")

#####################################################################################

    def countdown(session):
        from .user import User
        currentUser=User.currentUser
        if currentUser != None:
            userCreatures = session.query(UserCreature).filter(UserCreature.user_id == currentUser.id).all()
            if len(userCreatures) == 0:
                pass
            else:
                print('''

Counting Down. Your creature(s) is/are missing you.
Their Happiness, Health, Obedience, and Loyalty have all decreased!
                ''')
                for creature in userCreatures:
                    UserCreature.update_happiness(session, creature, creature.happiness -2)
                    UserCreature.update_health(session, creature, creature.health -2)
                    UserCreature.update_obedience(session, creature, creature.obedience -2)
                    UserCreature.update_loyalty(session, creature, creature.loyalty -2)
        else:
            pass

########## Extra Commands that could prove useful in a future update ##############

    def get_all_userCreatures(session):
        return session.query(UserCreature).all()

    def find_by_userCreature_id(session, id):
        return session.query(UserCreature).filter(UserCreature.id == id).first()




            # else:        
            #     creatures = []
            #     for key, value in sorted_creature_id_dict:
            #         creature = Creature.find_by_creature_id(session, key)
            #         creatures.append(creature)
            #         print(f"{creature.species} appears {value} times")
            #     option = input("Press Enter to continue... ")
            #     if option == "exit":
            #         sys.exit(0)
            #     elif option == "back":
            #         creatureSelect = False        
            #     elif option == "":
            #         pass
            #     n=1
            #     for creature in creatures:
            #         print(f"{n}) {creature.species}")
            #         n += 1