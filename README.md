# Mythical-Creature-Selector-Caretaker

## Overview
TBD


## Setup / Running the Project (on Windows)
Enter you terminal (however you have set up to do so.)

### Check Python version
Type: python --version
If you are running Python 3.9.2 or higher you can skip the next section

### Install the correct python. 
Navigate to the following website and follow the instructions to install Python 3 on your system
For Windows:
https://docs.python.org/3/using/windows.html
For Mac:
https://docs.python.org/3/using/mac.html
For Unix (ie: Linux):
https://docs.python.org/3/using/unix.html

### Install the Virtual Environment
In your terminal, navigate to the root directory of this project:
Type: pipenv install
(it can take a little while, so please be patient)
Type: pipenvshell to enter the virtual environment

Congrats, you are now configured and ready to run this program!

## Instructions:
### How to Start the program
From the root folder of this project, in the command line of your terminal...
Type: chmod +x lib/main.py (to unlock permisions)
Type: lib/main.py

And it begins!
If at any time you get stuck, you can always press <ctrl-c> to exit the program.

### How to access the programs Functions:
Follow the instructions to navigate the program. 
Other than the username and password, most other entries will be a number key.
You can type "back" to go up a menu at any point.
You can type "exit" to leave the program at any point.

## Assignment Goals
As per the Project Pitch Template:

Done... You must make a project using SQL and Python
    Primarily Python, with SQLAlchemy mixed in

Done... Include 1 CLI
    The whole thing is CLI

Done... Use any ORM to connect SQL to Python (SqlAlchemy, Sqlite3)
    Used SQLAlchemy

Done... Include 3 related tables
    7 tables in total.
    answers, creatures, creatureInteractions, questions, users, userAnswers, userCreatures.

Done... Have a Many-to-Many Relationship
    The userCreatures table acts as a join table to let Users have many Creatures, and Creatures to have many users. 

Include a ReadMe file that has 
    An Overview about what your project is about
    Instructions for running your project
    Instructions for using your project

As per Vocal Instructions:

Done... Full CRUD
    Create:
        users can be created and added to the users table
        creatures can be added into the userCreatures db
    Read:
        answers are pulled from the answers table for the quiz
        creatures are pulled from the creatures table for selection
        creatures are pulled from the creatures table for details in UserCreature
        creatureInteractions are pulled from the creatureInteractions table for interactions in USerCreatures
        questions are pulled from the questions table for the quiz
        users are pulled for logging in
        userCreatures are pulled by name for verification
    Update:
        happiness, health, and obedience are updated when certain conditions are met.
        $other functions exist in each module to allow for an update of any table, but they are currently not being utilized.
    Delete:
        UserCreatures get deleted when their happiness, health, or obedience is too low. 
        UserCreatures can be manually deleted by the user. 
        UserAnswers are deleted at quiz start to start fresh.




## Initial Project Pitch/Ideas (just in case you were curious about how it started)

Mythical Creature Selector

A CLI-based application built with Python and SQL project where you take a list of questions with four answers and use those answers to determine the user's animal type.

Tables:

Questions (question_id, content)
Answers (answer_id, question_id, content, creature_id, creature_id, creature_id)
Creatures (creature_id, name, origin, description, care_instructions, ascii_art)
Users (user_id, username, password)
UserCreatures (user_id, creature_id, creature_name, happiness, health, last_interaction)
CreatureInteractions (interaction_id, name, effect_on_happiness, effect_on_health)

Many-to-many relationships:

UserAnswers: To associate multiple answers with a single user and a single answer with multiple users.
UserAnimals: To associate multiple animals with a single user and a single animal with multiple users.

Features:

Users can browse mythical creatures to see name, origin, and type.
The application can display ASCII art for each creature.
Users can answer a series of questions, realted to their preferences and personailty, and let the system match them to a mythological creature.
Users can select a short quiz (10 questions) or a longer quiz (50 questions).
Users can see a counter as they answer questions, so they know how may questions are left. 
Users can go back to change an answer before submitting the quiz (Stretch Goal).
Users will be able to view a detailed description and ASCII art of the mythological creature I've been matched with, so I can learn more about it and its traits.
Users can retake the quiz to see if they get a different creature result with different answers.

################################################################################################

Mythical Creature Caretaker:

A CLI-based application built with Python and SQL project that allows users to adopt, care for, and interact with various mythical creatures from folklore and popular culture. The application should manage creature data, user profiles, and user-creature interactions.

Tables:

Creatures (creature_id, name, origin, description, care_instructions, ascii_art)
Users (user_id, username, password)
UserCreatures (user_id, creature_id, creature_name, happiness, health, last_interaction)
CreatureInteractions (interaction_id, name, effect_on_happiness, effect_on_health)

Many-to-many relationships:

UserCreatures: To associate multiple creatures with a single user and a single creature with multiple users.

Features:

Users can browse mythical creatures to see name, origin, and type.
The application can display ASCII art for each creature.
Users can either directly select their creature from a list, or can take the optional Mythical Creature Selector Quiz below.
Users can adopt creatures and give them a custom name, with each user allowed to adopt multiple creatures.
Users can interact with their creatures in various ways (e.g., feeding, playing, grooming), with each interaction affecting the creature's happiness and health.
The application can track the time since the last interaction for each creature and adjust its happiness and health accordingly. Potentially with different levels of difficulty that the user can select for their creatures.
Users can create and manage their own profiles, including their adopted creatures and their creatures' happiness and health levels.

#############################################################################################

Merged Mythical Creature Caretaker & Selector:

A CLI-based application built with Python and SQL project that allows users to find their ideal mythical creature by taking a quiz and then adopt, care for, and interact with various mythical creatures from folklore and popular culture. The application should manage creature data, user profiles, user-creature interactions, and user-creature matches.

Tables:

Creatures (creature_id, name, origin, description, care_instructions, ascii_art)
Users (user_id, username, password)
Questions (question_id, content)
Answers (answer_id, question_id, content, creature_id)
UserAnswers (user_id, answer_id)
UserCreatures (user_id, creature_id, creature_name, happiness, health, last_interaction)
CreatureInteractions (interaction_id, name, effect_on_happiness, effect_on_health)

Many-to-many relationships:

UserAnswers: To associate multiple answers with a single user and a single answer with multiple users.
UserCreatures: To associate multiple creatures with a single user and a single creature with multiple users.

Features:

Users can browse mythical creatures to see the name, origin, and type.
The application can display ASCII art for each creature.
Users can answer a series of questions related to their preferences and personality to find their ideal mythological creature match.
Users can select a short quiz (10 questions) or a longer quiz (50 questions).
Users can see a counter as they answer questions, so they know how many questions are left.
Users can go back to change an answer before submitting the quiz (Stretch Goal).
Users will be able to view a detailed description and ASCII art of the mythological creature they've been matched with, so they can learn more about it and its traits.
Users can retake the quiz to see if they get a different creature result with different answers.
Users can adopt creatures and give them a custom name, with each user allowed to adopt multiple creatures.
Users can interact with their creatures in various ways (e.g., feeding, playing, grooming), with each interaction affecting the creature's happiness and health.
The application can track the time since the last interaction for each creature and adjust its happiness and health accordingly. Potentially with different levels of difficulty that the user can select for their creatures.
Users can create and manage their own profiles, including their adopted creatures and their creatures' happiness and health levels.
Users can view their quiz results and adopted creatures, as well as share their results with friends on social media (Stretch Goal).
