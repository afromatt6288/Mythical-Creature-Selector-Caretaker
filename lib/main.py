#!/usr/bin/env python3
# import random
# import copy
import sys
import schedule
import time
from datetime import datetime
from sqlalchemy import *
from sqlalchemy.orm import *
## Classes to import from modules
from classes.answer import Answer
from classes.creature import Creature
# from classes.creatureInteraction import CreatureInteraction
from classes.question import Question
from classes.user import User
from classes.userAnswer import UserAnswer
from classes.userCreature import UserCreature
from classes.base import Base

if __name__ == '__main__':
    engine = create_engine('sqlite:///myth.db')
    Session = sessionmaker(bind=engine)
    session = Session()

## game_start() is being called at the very end of main.
## This allows it to start the game as a called function. 
## It also wraps the other functions and can call them 
## even if they are declared "after" they are called.


    def game_start():

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

        currentUser = None
        inprogram = True
        while inprogram:
            # Checks for new or returning user
            userinput = input('''
Welcome to Mythical Creature Caretaker! We here at MCC are glad you are here. 
Just a few notes... 
When you can, enter the numbers or letters to the left of any options you might see. 
Also, you can type "back" at any prompt to go back to a previous menu or option, 
or "exit" to end the program.

            Please enjoy!
            
Are you a New or Returning Caretaker? 

1) New Caretaker
2) Returning Caretaker
            
Select: ''')
            # user input
            if userinput == "1":
                User.new_user(session)
                currentUser=User.currentUser
                if currentUser != None:
                    main_menu(currentUser)
            elif userinput == "2":
                User.returning_user(session)
                currentUser=User.currentUser
                if currentUser != None:
                    main_menu(currentUser)
            elif userinput == "back":
                print("Back to the Beginning!")
                game_start()
            elif userinput == "exit":
                sys.exit(0)
            elif userinput == "Mythical":
                print("Welcome to the Secret Gallery")
            else:
                print("Invalid Entry. Please try again!")

    def main_menu(currentUser):
        mainMenu = True
        while mainMenu:
            print(f"main 87 {currentUser}")
            option = input(f'''
Main Menu

What would you like to do today {currentUser.username}?

1) New Creature (select from list)
2) Better Suited Creature (short quiz - 10 creatures available)
3) Best Suited Creature (extended quiz - 25 creatures available)
4) Visit Current Creatures

Selection : ''')
            if option == "1":
                print("New Creature (select from list)")
                select_creature(currentUser)
            elif option == "2":
                print("Better Suited Creature (short quiz - 10 creatures available)")
                short_quiz(currentUser)
            elif option == "3":
                print("Best Suited Creature (extended quiz - 25 creatures available)")
                long_quiz(currentUser)
            elif option == "4":
                print("Visit Current Creatures")
                UserCreature.view_userCreature_list(session, currentUser)
            elif option == "back":
                print("Back to the Beginning!")
                game_start()
            elif option == "exit":
                sys.exit(0)
            elif option == "countdown":
                UserCreature.countdown(session)
            else:
                print("Invalid Entry. Please try again!")
    
    def select_creature(currentUser):
        creatureSelect = True
        creatures = Creature.get_all_creatures(session)
        while creatureSelect:
            print(f'''
Welcome, {currentUser.username} to the Mythical Creature Selection Screen.
By being here it proves one of two things:
    Either, you know exactly who you are and what you want!
    Or... You were too lazy to take a short quiz
In either case, please select a creture of your choice from below!
            ''')
            n=1
            for creature in creatures:
                print(f"{n}) {creature.species}")
                n += 1
            option = input(f'''
Select:  ''')
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
                elif type(newUserCreatureName) is str and 4 <= len(newUserCreatureName):
                    UserCreature(user_id = currentUser.id, creature_id = creature.id, creature_name = newUserCreatureName).add_to_userCreatures_db(session)
                    newUserCreature = UserCreature.find_by_userCreature_name(session, newUserCreatureName)        
                    UserCreature.hang_with_creature(session, currentUser, newUserCreature)
                else:
                    print("Creature name must be 4 letters or longer!")
            elif option == "back":
                print("Back to Main Menu!")
                creatureSelect = False
            elif option == "exit":
                sys.exit(0)
            else:
                print("Invalid option. Please try again!")
    
    def short_quiz(currentUser):
        shortQuiz = True
        while shortQuiz:
            option = input(f'''
                              Welcome to the Short Quiz! 
These 10 questions will help you pick a creature that BETTER suits your temperment and interests. 
Once you complete this quiz you will see a ranking of 10 creatures, and how you relate with them. 
You can then select which creature you wish (ie, you are not stuck with the creature you have the highest compatability with.)
Also, you can type exit at any time in the quiz to return to this menu... but your progress will not be saved. 

         1) Proceed with quiz            OR             2) Back to main menu

                                Selection :  ''')
            if option == "2" or option == "back":
                print("Back to the Main Menu")
                main_menu(currentUser)
            elif option == "exit":
                sys.exit(0)
            elif option == "1":
                inQuiz=True
                while inQuiz:
                    n=1
                    while n <= 10:
                        question = Question.find_by_question_id(session, n)
                        answer1 = Answer.find_by_answer_id(session, 1+(n-1)*4)
                        answer2 = Answer.find_by_answer_id(session, 2+(n-1)*4)
                        answer3 = Answer.find_by_answer_id(session, 3+(n-1)*4)
                        answer4 = Answer.find_by_answer_id(session, 4+(n-1)*4)
                        option = input(f'''
                        Question {n} of 10:

                        {n}: {question.content}

                        1) {answer1.content}
                        2) {answer2.content}
                        3) {answer3.content}
                        4) {answer4.content}

                        Answer: ''')
                        if option == "1":
                            print("Answer 1")
                            n += 1
                        elif option == "2":
                            print("Answer 2")
                            n += 1
                        elif option == "3":
                            print("Answer 3")
                            n += 1
                        elif option == "4":
                            print("Answer 4")
                            n += 1
                        elif option == "back":
                            print("Back to the start of the Short Quiz!")
                            short_quiz(currentUser)
                        elif option == "exit":
                            sys.exit(0)
                    print("end of quiz")
                    inQuiz=False


    def long_quiz(currentUser):
        longQuiz = True
        while longQuiz:
            option = input(f'''
                              Welcome to the Extended Quiz! 
These 50 questions will help you pick a creature that BEST suits your temperment and interests. 
Once you complete this quiz you will see a ranking of 25 creatures, and how you relate with them. 
You can then select which creature you wish (ie, you are not stuck with the creature you have the highest compatability with.)
Also, you can type exit at any time in the quiz to return to this menu... but your progress will not be saved. 

         1) Proceed with quiz            OR             2) Back to main menu

                                Selection :  ''')
            if option == "2" or option == "back":
                print("Back to the Main Menu")
                main_menu(currentUser)
            elif option == "exit":
                sys.exit(0)
            elif option == "1" or option == "Proceed" or option =="Proceed with quiz":
                inQuiz=True
                while inQuiz:
                    n=1
                    while n <= 50:
                        question = Question.find_by_question_id(session, n)
                        answer1 = Answer.find_by_answer_id(session, 1+(n-1)*4)
                        answer2 = Answer.find_by_answer_id(session, 2+(n-1)*4)
                        answer3 = Answer.find_by_answer_id(session, 3+(n-1)*4)
                        answer4 = Answer.find_by_answer_id(session, 4+(n-1)*4)
                        option = input(f'''
                        Question {n} of 50:

                        {n}: {question.content}

                        1) {answer1.content}
                        2) {answer2.content}
                        3) {answer3.content}
                        4) {answer4.content}

                        Answer: ''')
                        if option == "1":
                            print("Answer 1")
                            n += 1
                        elif option == "2":
                            print("Answer 2")
                            n += 1
                        elif option == "3":
                            print("Answer 3")
                            n += 1
                        elif option == "4":
                            print("Answer 4")
                            n += 1
                        elif option == "back":
                            print("Back to the start of the Long Quiz!")
                            long_quiz(currentUser)
                        elif option == "exit":
                            sys.exit(0)
                    print("end of quiz")
                    inQuiz=False
                    
 
#     schedule.every(5).seconds.do(lambda: UserCreature.countdown(session))
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# ## The other way to have made the time run... 
#     while True:
#         now = datetime.now()
#         time_until_next_run = (30 - now.minute % 30) * 60 - now.second
#         time.sleep(time_until_next_run)
#         UserCreature.countdown(session)


game_start()