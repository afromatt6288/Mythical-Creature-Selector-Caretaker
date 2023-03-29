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
            userinput = input("Are you a New or Returning Caretaker: ")
            # user input
            if userinput == "New" or userinput == "N":
                User.new_user(session)
                currentUser=User.currentUser
                if currentUser != None:
                    main_menu(currentUser)
            elif userinput == "Returning" or userinput == "R":
                User.returning_user(session)
                currentUser=User.currentUser
                if currentUser != None:
                    main_menu(currentUser)
            elif userinput == "Mythical":
                print("Welcome to the Secret Gallery")
            else:
                print("Not a valid response. Please enter 'New' or 'Returning'.")

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
5) Logout

Selection : ''')
            if option == "New" or option == "New Creature" or option == "1":
                print("New Creature (select from list)")
            elif option == "Better" or option == "Better Suited Creature" or option == "2":
                print("Better Suited Creature (short quiz - 10 creatures available)")
                short_quiz(currentUser)
                # mainMenu=False
            elif option == "Best" or option == "Best Suited Creature" or option == "3":
                print("Best Suited Creature (extended quiz - 25 creatures available)")
            elif option == "Visit" or option == "Visit Current Creatures" or option == "4":
                print("Visit Current Creatures")
                pass
            elif option == "Logout" or option == "5":
                print("logout")
                game_start()
                # mainMenu=False
            else:
                print("Invalid Entry. Please try again!")
    
    def short_quiz(currentUser):
        shortQuiz = True
        while shortQuiz:
            option = input(f'''
                              Welcome to the Quiz! 
   These 10 questions will help you pick a creature that better suits your temperment 
and interests. Don't worry, you can change your mind afterwards. So, answer as you feel. 

         1) Proceed with quiz            OR             2) Back to main menu

                                Selection :  ''')
            if option == "2" or option == "Back" or option == "Back to main menu":
                main_menu(currentUser)
            elif option == "1" or option == "Proceed" or option =="Proceed with quiz":
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
                        elif option == "exit":
                            short_quiz(currentUser)
                    print("end of quiz")
                    inQuiz=False
                    


                







game_start()