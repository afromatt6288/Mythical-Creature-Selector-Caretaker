#!/usr/bin/env python3
import threading
import sys
import os
os.environ['SDL_AUDIODRIVER'] = 'pulse'
import time
import pygame
from playsound import playsound
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
# from classes.base import Base

if __name__ == '__main__':
    engine = create_engine('sqlite:///myth.db')
    Session = sessionmaker(bind=engine)
    session = Session()

################################################################################################################

## A standalone function that counts down every `interval` seconds and
## runs the specified `func` function.
    def countdown_timer(interval, func):
        while True:
            time.sleep(interval)
            func(session)            

## Start the countdown timer in a separate thread from the rest of the program. So they can run at the same time.
    timer_thread = threading.Thread(target=countdown_timer, args=(60, UserCreature.countdown))
    timer_thread.daemon = True  # Set the thread as a daemon, so it exits when the main program exits
    timer_thread.start()

###################################################################################################################

## A standalone function that allows music to play in the background
    ## This Version allows for playing multiple songs in a loop. 
    def play_sound():
        pygame.mixer.init()
        song_list = [
            "/home/afromatt6288/development/code/phase-3/project/mythical-creature-selector-caretaker/lib/sound-deep-in-the-dell.mp3",
            "/home/afromatt6288/development/code/phase-3/project/mythical-creature-selector-caretaker/lib/sound-enchanted-kingdom.mp3",
            "/home/afromatt6288/development/code/phase-3/project/mythical-creature-selector-caretaker/lib/sound-fairy-tale-fantasy.mp3",
            "/home/afromatt6288/development/code/phase-3/project/mythical-creature-selector-caretaker/lib/sound-fairy-tale.mp3",
            "/home/afromatt6288/development/code/phase-3/project/mythical-creature-selector-caretaker/lib/sound-hiding-place-in-the-forest.mp3",
            "/home/afromatt6288/development/code/phase-3/project/mythical-creature-selector-caretaker/lib/sound-magic-in-the-air.mp3"
        ]
        while True:
            for song in song_list:
                pygame.mixer.music.load(song)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(5)  # To avoid high CPU usage, you can add a small delay
    
    ## This Version allows for playing a single song on loop
    # def play_sound():
    #     pygame.mixer.init()
    #     pygame.mixer.music.load("/home/afromatt6288/development/code/phase-3/project/mythical-creature-selector-caretaker/lib/sound-deep-in-the-dell.mp3")
    #     pygame.mixer.music.play(-1)  # The -1 argument indicates to loop the music indefinitely

    ## This version works for most people, but my computer gave it issues, so I had to switch to the abobve methods.
    # def play_sound():
    #     playsound("/home/afromatt6288/development/code/phase-3/project/mythical-creature-selector-caretaker/lib/sound-deep-in-the-dell.mp3")

## Start the music in a separate thread from the rest of the program. So they can run at the same time.    
    sound_thread = threading.Thread(target=play_sound)
    sound_thread.daemon = True # Set the thread as a daemon, so it exits when the main program exits
    sound_thread.start()

###################################################################################################################

## game_start() is being called at the very end of main.
## This allows it to start the game as a called function. 
## It also wraps the other functions and can call them 
## even if they are declared "after" they are called.


    def game_start():

        print('''
⠀⠀⠀⣀⣀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣴⣿⣿⣿⣷⣴⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⠛⣿⣿⣿⢻⣿⣿⣷⠀⢰⣶⣶⡆⢰⣶⣶⠀⢸⣿⣿⣧⡄⠀⣿⣿⣿⣴⣶⣦⡀⠀⢰⣶⣶⠀⠀⢀⣠⣴⣶⣦⣤⡀⠀⠀⢀⣤⣶⣶⣦⣄⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⠀⣿⣿⣿⢸⣿⣿⣿⠀⢸⣿⣿⡇⢸⣿⣿⠀⢸⣿⣿⣿⡇⠀⣿⣿⣿⠿⣿⣿⣷⠀⢸⣿⣿⠀⢀⣾⣿⣿⠿⣿⣿⣿⠀⢠⣿⣿⣿⠿⣿⣿⣷⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⠀⣿⣿⣿⢸⣿⣿⣿⠀⢸⣿⣿⣇⣸⣿⣿⠀⢸⣿⣿⣧⡀⠀⣿⣿⣿⠀⣿⣿⣿⠀⢸⣿⣿⠀⠸⣿⣿⣇⣀⣠⣤⣤⠄⢻⣿⣿⣇⡀⢹⣿⣿⡇⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⠀⣿⣿⣿⢸⣿⣿⣿⠀⠘⣿⣿⣿⣿⣿⣿⠀⠀⠻⣿⣿⡇⠀⣿⣿⣿⠀⣿⣿⣿⠀⢸⣿⣿⠀⠀⠻⣿⣿⣿⣿⣿⠟⠀⠈⢿⣿⣿⣿⢸⣿⣿⡇⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠉⠉⠉⠀⠉⠉⠉⠈⠉⠉⠉⠀⠀⢈⣉⣩⣿⣿⣿⠀⠀⠀⠈⠉⠁⠀⠉⠉⠉⠀⠉⠉⠉⠀⠈⠉⠉⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠈⠉⠉⠈⠉⠉⠁⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣤⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣿⣿⣿⠋⠀⠀⠙⣿⣿⡿⠄⠀⣠⣾⣿⣿⠀⣠⣾⣿⣿⣿⣶⡄⠀⢀⣴⣿⣿⣿⣿⣦⠀⠀⢸⣿⣿⣿⡇⢸⣿⣿⡇⢰⣿⣿⡇⠀⢠⣾⣿⣿⡇⢠⣶⣿⣿⣿⣷⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣧⠀⠀⠀⠀⣤⣤⣤⡄⢰⣿⣿⡟⠛⢸⣿⣿⢯⣤⣽⣿⣿⠀⣾⣿⣿⠛⠻⣿⣿⣷⠀⢸⣿⣿⠿⠇⢸⣿⣿⡇⢸⣿⣿⡇⠀⣼⣿⣿⠛⢣⣿⣿⡿⣡⣼⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢿⣿⣿⣶⣤⣤⣾⣿⣿⡟⠀⢸⣿⣿⡇⠀⢸⣿⣿⣎⣉⡉⠉⠉⠀⢿⣿⣿⣤⡄⣿⣿⣿⠀⢸⣿⣿⣦⡄⠘⣿⣿⣧⣸⣿⣿⠇⠀⣿⣿⣿⠀⠘⣿⣿⣷⣉⣉⡉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⠿⣿⣿⣿⣿⠿⠋⠀⠀⢸⣿⣿⡇⠀⠀⠛⠿⣿⣿⣿⠆⠀⠀⠈⠻⢿⣿⡇⣿⣿⡿⠀⠀⠙⢿⣿⡇⠀⠙⢿⣿⣿⡿⠟⠀⠀⣿⣿⣿⠀⠀⠈⠻⣿⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

⠀⠀⠀⢀⣤⣶⣶⣶⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣰⣿⣿⣿⠿⠿⢿⣿⣿⣧⠀⠀⠀⢀⣠⣤⣀⡀⠀⠀⠀⠀⢀⣠⣤⡀⠀⢀⣀⣤⣄⡀⠀⠀⢸⣿⣿⣀⡀⠀⠀⢀⣠⣤⣀⡀⠀⠀⠀⣿⣿⡇⠀⣀⣀⣀⠀⠀⠀⣀⣤⣤⣀⠀⠀⠀⠀⢀⣠⣤⠀⠀⠀⠀⠀⠀
 ⢰⣿⣿⣿⠁⠀⠀⠀⠛⠛⠛⠃⢀⣴⣿⣿⣿⣿⣿⣦⠀⠀⣴⣿⣿⣿⡇⣴⣿⣿⠿⣿⣿⣦⡀⢸⣿⣿⣿⡇⢀⣴⣿⣿⣿⣿⣿⣦⠀⠀⣿⣿⡇⣰⣿⣿⠏⠀⢠⣾⣿⡿⢿⣿⣷⡄⠀⣰⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠸⣿⣿⣿⡀⠀⠀⢀⣿⣿⣿⠇⢸⣿⣿⡏⠉⢻⣿⣿⡆⠀⣿⣿⡟⠉⢸⣿⣿⡇⠶⠾⠿⠿⠇⢸⣿⣿⡉⠁⢸⣿⣿⡏⠉⢻⣿⣿⡇⠀⣿⣿⡇⢻⣿⣿⡀⠀⣿⣿⣿⠰⠶⠿⠿⠿⠀⣿⣿⣿⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠹⣿⣿⣿⣶⣶⣿⣿⣿⠏⠀⠘⣿⣿⣿⣶⢸⣿⣿⡇⠀⣿⣿⡇⠀⠈⣿⣿⣷⣤⣦⡀⠀⠀⠘⣿⣿⣿⡆⠘⣿⣿⣿⣶⢸⣿⣿⡇⠀⣿⣿⡇⠈⢿⣿⣷⡀⢹⣿⣿⣦⣴⣄⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠙⠛⠿⠿⠟⠛⠁⠀⠀⠀⠈⠛⠻⠿⠘⠛⠛⠃⠀⠛⠛⠃⠀⠀⠀⠙⠛⠿⠛⠋⠀⠀⠀⠈⠛⠛⠃⠀⠀⠛⠛⠿⠘⠛⠛⠃⠀⠛⠛⠃⠀⠘⠛⠛⠃⠀⠉⠛⠻⠟⠛⠁⠀⠀⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀
''' )
        userinput = input("Press enter to continue... ")
        if userinput == "back":
            print("Back to the Beginning!")
            User.currentUser = None
            game_start()
        elif userinput == "exit":
            sys.exit(0)
        elif userinput == "":
            pass
        else:
            print("Invalid Entry. Please try again!")

        currentUser = None
        inprogram = True
        while inprogram:
            # Checks for new or returning user
            userinput = input('''
Welcome to Mythical Creature Caretaker! We here at the M.C.C. are glad you are here. 

Just a few notes... 
Type the Number to the left of any options you might see to proceed. 
Type "back" at (almost) any prompt to go back to a previous menu or option, 
Type "exit" to end the program... sometimes you might have to type it twice... or thrice... 

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
                User.currentUser = None
                game_start()
            elif userinput == "exit":
                sys.exit(0)
            elif userinput == "Mythical":
                Creature.mythical_menagerie()
            else:
                print("Invalid Entry. Please try again!")

    def main_menu(currentUser):
        mainMenu = True
        while mainMenu:
            # print(f"main 119 {currentUser}")
            option = input(f'''
⠀⣠⣄⣀⣠⣄⠀⠀⠀⠀⠀⠀⠀⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⢀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⢻⣿⡟⣿⡇⠀⣠⣤⣄⠀⠀⣭⡅⠀⣠⣤⡀⠀⠀⠀⣼⣿⢻⣿⡟⣿⡇⠀⣠⣤⣄⠀⠀⣠⣤⣄⠀⢠⣤⢠⣤⠀⠀⠀⠀⠀
⢸⣿⢸⣿⡇⣿⡇⢸⣿⠛⣿⡇⠀⣿⡇⢸⣿⢻⣿⠀⠀⠀⣿⣿⢸⣿⡇⣿⡇⢸⣿⢩⣿⡇⢸⣿⢻⣿⠀⢸⣿⢸⣿⠀⠀⠀⠀⠀
⢸⣿⢸⣿⡇⣿⡇⠘⢿⣷⣿⡇⠀⣿⡇⢸⣿⢸⣿⠀⠀⠀⣿⣿⢸⣿⡇⣿⡇⠘⢿⣶⡆⠀⢸⣿⢸⣿⠀⠸⣿⣾⠟⠀⠀

What would you like to do today {currentUser.username}?

1) Acquire Mythical Creature (select from list)
2) Aquire BETTER Suited Mythical Creature (short quiz - 10 creatures available)
3) Aquire BEST Suited Mythical Creature (extended quiz - 25 creatures available)
4) Visit Current Creatures

Select : ''')
            if option == "1":
                print("Acquire Mythical Creature (select from list)")
                UserCreature.select_creature(currentUser, 1, {})
            elif option == "2":
                print("Aquire BETTER Suited Mythical Creature (short quiz - 10 creatures available)")
                short_quiz(currentUser)
            elif option == "3":
                print("Aquire BEST Suited Mythical Creature (extended quiz - 25 creatures available)")
                long_quiz(currentUser)
            elif option == "4":
                print("Visit Current Creatures")
                UserCreature.view_userCreature_list(session, currentUser)
            elif option == "back":
                print("Back to the Beginning!")
                User.currentUser = None
                game_start()
            elif option == "exit":
                sys.exit(0)
            elif option == "countdown":
                UserCreature.countdown(session)
            else:
                print("Invalid Entry. Please try again!")
    
    def quiz_helper(currentUser, x):
        existing_answers_to_delete = UserAnswer.find_all_userAnswer_by_user_id(session, currentUser.id)
        for answer in existing_answers_to_delete:
            UserAnswer.delete_userAnswers(session, answer)                    
        inQuiz=True
        while inQuiz:
            n=1
            while n <= x:
                question = Question.find_by_question_id(session, n)
                answer1 = Answer.find_by_answer_id(session, 1+(n-1)*4)
                answer2 = Answer.find_by_answer_id(session, 2+(n-1)*4)
                answer3 = Answer.find_by_answer_id(session, 3+(n-1)*4)
                answer4 = Answer.find_by_answer_id(session, 4+(n-1)*4)
                option = input(f'''
Question {n} of {x}:

{question.content}

1) {answer1.content}
2) {answer2.content}
3) {answer3.content}
4) {answer4.content}

Answer: ''')
                if option == "1":
                    print(f"{answer1.content}")
                    UserAnswer(user_id = currentUser.id, answer_id = answer1.id).add_to_userAnswers_db(session)    
                    n += 1
                elif option == "2":
                    print(f"{answer2.content}")
                    UserAnswer(user_id = currentUser.id, answer_id = answer2.id).add_to_userAnswers_db(session)
                    n += 1
                elif option == "3":
                    print(f"{answer3.content}")
                    UserAnswer(user_id = currentUser.id, answer_id = answer3.id).add_to_userAnswers_db(session)
                    n += 1
                elif option == "4":
                    print(f"{answer4.content}")
                    UserAnswer(user_id = currentUser.id, answer_id = answer4.id).add_to_userAnswers_db(session)
                    n += 1
                elif option == "back":
                    print("Back to the Main Menu!")
                    main_menu(currentUser)
                elif option == "exit":
                    sys.exit(0)
            UserAnswer.tabulate_quiz(session, currentUser, x)
            print("end of quiz")
            inQuiz=False
    
    def short_quiz(currentUser):
        shortQuiz = True
        while shortQuiz:
            option = input(f'''
⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣾⡿⠇⣿⣿⣀⡀⠀⠀⣀⣀⠀⠀⢀⣀⢸⣿⡀⠀⠀⢀⣾⣿⠿⣿⣦⠀⢀⡀⢀⣀⠀⣛⡃⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢿⣷⡀⣿⣿⢻⣿⢠⣾⠟⢿⣷⠀⣿⡟⢸⣿⠇⠀⠀⢸⣿⡁⣀⢸⣿⡇⣿⡇⢸⣿⠀⣿⡇⠿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀
⠀⢰⣾⡿⠃⣿⣿⢸⣿⠈⢿⣷⣾⡟⠀⣿⡇⠘⢿⡆⠀⠀⠈⢿⣿⣿⣿⠟⠀⢻⣷⣾⡟⠀⣿⡇⢰⣿⣿⣶⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠁⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                            

Welcome to the Short Quiz! 
These 10 questions will help you pick a creature that BETTER suits your temperment and interests. 
Once you complete this quiz you will see a ranking of 10 creatures, and how you relate with them. 
You can then select which creature you wish (ie, you are not stuck with the creature you have the highest compatability with.)
Also, you can type exit at any time in the quiz to return to this menu... but your progress will not be saved. 

1) Proceed with quiz
2) Back to main menu

Select: ''')
            if option == "2" or option == "back":
                print("Back to the Main Menu")
                main_menu(currentUser)
            elif option == "exit":
                sys.exit(0)
            elif option == "1":
                quiz_helper(currentUser, 10)
                shortQuiz = False
            else:
                print("Invalid option. Please try again!")

    def long_quiz(currentUser):
        longQuiz = True
        while longQuiz:
            option = input(f'''
 ⠀⢀⣤⣤⠀⠀⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⠀⠀⠀⠀⠀⠀⠀⣤⡄⠀⠀⠀⣠⣤⣄⠀⠀⠀⠀⠀⢀⣤⠀⠀⠀⠀⠀
 ⠀⣿⣟⡛⢠⣤⢠⡄⢸⣧⡄⣠⣴⣤⡀⢀⣴⣤⠀⢀⣤⢸⣿⠀⣤⣦⣄⠀⣠⣤⣿⡇⠀⠀⣾⡟⠛⢿⣷⢠⣤⢠⣤⢠⣭⢠⣤⣤⡄⠀
 ⠀⣿⣟⣋⢈⣿⢾⡇⢸⣿⡁⣿⡑⠛⠃⣾⡏⣿⡇⣿⣏⣸⣿⢸⣿⠚⠛⢸⣿⣉⣿⡇⠀⠈⣿⣧⣤⣼⣿⢸⣿⢸⣿⢸⣿⠈⣹⣿⣁⠀
 ⠀⠙⠻⠿⠸⠟⠸⠇⠈⠛⠃⠙⠿⠗⠀⠻⠇⠿⠇⠈⠻⠟⠁⠈⠻⠿⠂⠀⠛⠿⠛⠀⠀⠀⠈⢻⣿⠛⠁⠀⠻⠿⠃⠸⠿⠠⠿⠿⠿⠀
                                                            
Welcome to the Extended Quiz! 
These 50 questions will help you pick a creature that BEST suits your temperment and interests. 
Once you complete this quiz you will see a ranking of 25 creatures, and how you relate with them. 
You can then select which creature you wish (ie, you are not stuck with the creature you have the highest compatability with.)
Also, you can type exit at any time in the quiz to return to this menu... but your progress will not be saved. 

1) Proceed with quiz
2) Back to main menu

Select: ''')
            if option == "2" or option == "back":
                print("Back to the Main Menu")
                main_menu(currentUser)
            elif option == "exit":
                sys.exit(0)
            elif option == "1":
                quiz_helper(currentUser, 50)
                longQuiz = False
            else:
                print("Invalid option. Please try again!")

game_start()