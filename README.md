# Mythical-Creature-Selector-Caretaker

## Overview


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

## Instructions to Use


### Project Pitch/Ideas 

Mythical Creature Selector

A CLI-based application built with Python and SQL project where you take a list of questions with four answers and use those answers to determine the user's animal type.

Tables:

Questions (question_id, content)
Answers (answer_id, question_id, content, creature_id, creature_id, creature_id)
Creatures (creature_id, name, origin, description, care_instructions, ascii_art)
Users (user_id, username, email)
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
Users (user_id, username, email)
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
Users (user_id, username, email)
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
