#!/usr/bin/env python3
from sqlalchemy import *
from sqlalchemy.orm import *
from datetime import datetime
from classes.answer import Answer
from classes.creature import Creature
from classes.creatureInteraction import CreatureInteraction
from classes.question import Question
from classes.user import User
from classes.userAnswer import UserAnswer
from classes.userCreature import UserCreature
from classes.base import Base

engine = create_engine('sqlite:///myth.db')
Answer.__table__.drop(engine)
Creature.__table__.drop(engine)
CreatureInteraction.__table__.drop(engine)
Question.__table__.drop(engine)
User.__table__.drop(engine)
UserAnswer.__table__.drop(engine)
UserCreature.__table__.drop(engine)
Base.metadata.create_all(engine)
with Session(engine) as session:

    # enter in the following order!:

    # creature = Creature(name="TBD", origin="TBD", description="TBD", care_instructions="TBD", ascii_art=''' TBD ''')
    # creatureInteraction = CreatureInteraction(name="TBD", effect_on_happiness="TBD", effect_on_health="TBD")
    # question = Question(content="TBD")
    # user = User(username="TBD", password="TBD")
    # # userCreature = UserCreature(user_id="TBD", creature_id="TBD", creature_species="TBD", creature_name="TBD", happiness="TBD", health="TBD", adoption_day="TBD", last_interaction="TBD")
    # answer = Answer(content="TBD", question_id=1, creature_id1=1, creature_id2=2, creature_id3=3)


## Creature
    # creature = Creature(species="TBD", origin="TBD", description="TBD", care_instructions="TBD",ascii_art=''' TBD ''')

    creature1 = Creature(
        species="Dragon-Western", 
        origin="European", 
        description='''
        In European mythology, dragons are legendary creatures typically portrayed as large, fire-breathing 
        reptilian beasts with wings, sharp claws, and scaly skin. They are often depicted as fierce and 
        dangerous creatures that hoard treasure and demand tribute from nearby villages or towns. 
        In some stories, they are seen as agents of evil and chaos, wreaking havoc and destruction wherever 
        they go. However, in other tales, dragons can also be wise and powerful beings that possess magical 
        abilities and knowledge. In some European mythologies, dragons are also associated with royalty and 
        are depicted as protectors of kingdoms and important treasures. They have been a popular theme in 
        European literature and art for centuries and continue to be an iconic symbol of fantasy and adventure.
        ''', 
        care_instructions="TBD",
        ascii_art='''
                 ___====-_  _-====___
           _--^^^#####//      \\#####^^^--_
        _-^##########// (    ) \\##########^-_
       -############//  |\^^/|  \\############-
     _/############//   (@::@)   \\############\_
    /#############((     \\//     ))#############-
   -###############\\    (oo)    //###############-
  -#################\\  / VV \  //#################-
 -###################\\/      \//###################-
_#/|##########/\######(   /\   )######/\##########|\#_
|/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
   `   `  `      `   / | |  | | \   '      '  '   '
                    (  | |  | |  )
                   __\ | |  | | /__
                  (vvv(VVV)(VVV)vvv)
        '''
    )
    creature2 = Creature(
        species="Dragon-Eastern", 
        origin="Chinese, Japanese, Korean", 
        description='''
        Dragons in Chinese, Japanese, and Korean mythology are revered as powerful, benevolent creatures 
        associated with water, rain, and good fortune. They are typically depicted as long, serpentine 
        creatures with four legs, long whiskers, and a mane of hair or fur running down their backs. Unlike 
        the European dragon, these dragons are often portrayed without wings, and they are said to be able 
        to fly using their magical abilities. They are seen as symbols of strength, good fortune, and divine 
        power, and their images can be found on many cultural artifacts and decorations. Dragons in these 
        mythologies are regarded with great respect and are believed to bring luck and prosperity to those 
        who revere them.
        ''', 
        care_instructions="TBD",
        ascii_art='''
                           _,,,.._       ,_
                        .gMMMMMMMMMp,_    `/
                     .dMMP'       ``^YMb..dP
                    dMMP'
                    MMM:
                    YMMb.
                     YMMMb.
                      `YMM/|Mb.  ,__
                   _,,-~`--..-~-'_,/`--,,,____
               `\,_,/',_.-~_..-~/' ,/---~~~"""`/
          _,_,,,\q\q/'    \,,-~'_,/`````-,7.
         `@v@`\\,,,,__   \,,-~~"__/` ",,/MMMMb.
          `--''_..-~~\   \,-~~""  `\_,/ `^YMMMMMb..
           ,|``-~~--./_,,_  _,,-~~'/_      `YMMMMMMMb.
         ,/  `\,_,,/`\    `\,___,,,/M/'      `YMMMMMMMb
                     ;  _,,/__...|MMM/         YMMMMMMMb
                      .' /'      dMMM\         !MMMMMMMMb
                   ,-'.-'""~~~--/M|M' \        !MMMMMMMMM
                 ,/ .|...._____/MMM\   b       gMMMMMMMMM
              ,'/'\/          dMMP/'   M.     ,MMMMMMMMMP
             / `\;/~~~~----...MP'     ,MMb..,dMMMMMMMMM'
            / ,_  |          _/      dMMMMMMMMMMMMMMMMB
            \  |\,\,,,,___ _/    _,dMMMMMMMMMMMP".emmmb,
             `.\  gY.     /      7MMMMMMMMMMP"..emmMMMMM
                .dMMMb,-..|       `.~~"""```|dMMMMP'MMP'
               .MMMMP^"""/ .7 ,  _  \,---~""`^YMMP'MM;
             _dMMMP'   ,' / | |\ \\  }          PM^M^b
          _,' _,  \_.._`./  } ; \ \``'      __,'_` _  `._
      ,-~/'./'| 7`,,__,}`   ``   ``        // _/`| 7``-._`}
     |_,}__{  {,/'   ``                    `\{_  {,/'   ``
     ``  ```   ``                            ``   ``  
        '''
    )
    creature3 = Creature(
        species="Griffin/Gryphon", 
        origin="Greek, European", 
        description='''
        A Griffin, also known as a Gryphon, is a legendary creature from Greek and European mythology that 
        has the body of a lion and the head and wings of an eagle. These creatures are often portrayed as 
        fierce and powerful, with sharp talons and keen eyesight. In mythology, they are known to be 
        guardians of treasures and powerful protectors, and their images can be found in art and architecture 
        throughout history. The Griffin represents the combination of the strength and courage of the lion 
        with the grace and wisdom of the eagle, making it a symbol of power and intelligence in many cultures.
        ''', 
        care_instructions="TBD",
        ascii_art='''
                          _)\.-.
         .-.__,___,_.-=-. )\`  a`\_
     .-.__\__,__,__.-=-. `/  \     `>
     {~,-~-,-~.-~,-,;;;;\ |   '--;`)/
      \-,~_-~_-,~-,(_(_(;\/   ,;/
       ",-.~_,-~,-~,)_)_)'.  ;;(
         `~-,_-~,-~(_(_(_(_\  `;\_
   ,          `"~~--,)_)_)_)\_   \_
   |\              (_(_/_(_,   \  ;
   \ '-.       _.--'  /_/_/_)   | |
    '--.\    .'          /_/    | |
        ))  /       \      |   /.'
       //  /,        | __.'|  ||
      //   ||        /`    (  ||
     ||    ||      .'       \ \\
     ||    ||    .'_         \ \\
      \\   //   / _ `\        \ \\__
       \'-'/(   _  `\,;        \ '--:,
        `"`  `"` `-,,;         `"`",,;
        '''
    )
    creature4 = Creature(
        species="Phoenix", 
        origin="Greek, Egyptian, Chinese, Japanese", 
        description='''
        The Phoenix is a mythical bird that appears in Greek, Egyptian, Chinese, and Japanese mythology. 
        It is often depicted as a bird with bright and colorful feathers that are said to be reborn 
        from the ashes of its own funeral pyre. In Greek mythology, the Phoenix is a symbol of resurrection 
        and rebirth, while in Egyptian mythology it is associated with the sun and the cycle of life and death. 
        In Chinese and Japanese mythology, the Phoenix is associated with prosperity, good fortune, and feminine 
        grace. Overall, the Phoenix is a symbol of hope, renewal, and transformation, and its mythical qualities 
        have made it a popular symbol in art and literature throughout history.
        ''', 
        care_instructions="TBD",
        ascii_art='''
                (                           )
          ) )( (                           ( ) )( (
       ( ( ( )  ) )                     ( (   (  ) )(
      ) )     ,,\\\                     ///,,       ) (
   (  ((    (\\\\//                     \\////)      )
    ) )    (-(__//                       \\__)-)     (
   (((   ((-(__||                         ||__)-))    ) )
  ) )   ((-(-(_||           ```\__        ||_)-)-))   ((
  ((   ((-(-(/(/\\        ''; 9.- `      //\)\)-)-))    )
   )   (-(-(/(/(/\\      '';;;;-\~      //\)\)\)-)-)   (   )
(  (   ((-(-(/(/(/\======,:;:;:;:,======/\)\)\)-)-))   )
    )  '(((-(/(/(/(//////:%%%%%%%:\\\\\\)\)\)\)-)))`  ( (
   ((   '((-(/(/(/('uuuu:WWWWWWWWW:uuuu`)\)\)\)-))`    )
     ))  '((-(/(/(/('|||:wwwwwwwww:|||')\)\)\)-))`    ((
  (   ((   '((((/(/('uuu:WWWWWWWWW:uuu`)\)\))))`     ))
        ))   '':::UUUUUU:wwwwwwwww:UUUUUU:::``     ((   )
          ((      ''`''`'\wuuuuuuu/``````         ))
           ))            `JJJJJJJJJ`           ((
             ((            LLLLLLLLLLL         ))
               ))         ///|||||||\\\       ((
                 ))      (/(/(/(^)\)\)\)       ((
                  ((                           ))
                    ((                       ((
                      ( )( ))( ( ( ) )( ) (()
        '''
    )
    creature5 = Creature(
        species="Pegasus", 
        origin="Greek",  
        description='''
        TBD
        ''', 
        care_instructions="TBD",
        ascii_art= '''
TBD
        '''
    )
    creature6 = Creature(
        species="Unicorn", 
        origin="Ancient mythology, European folklore", 
        description='''
        TBD
        ''', 
        care_instructions="TBD",
        ascii_art= '''
TBD
        '''
    )
    creature7 = Creature(
        species="Sphinx", 
        origin="Greek, Egyptian", 
        description='''
        TBD
        ''', 
        care_instructions="TBD",
        ascii_art= '''
TBD
        '''
    )
    creature8 = Creature(
        species="Cerberus", 
        origin="Greek", 
        description='''
        TBD
        ''', 
        care_instructions="TBD",
        ascii_art= '''
TBD
        '''
    )
    creature9 = Creature(
        species="Kraken", 
        origin="Norse", 
        description='''
        TBD
        ''', 
        care_instructions="TBD",
        ascii_art= '''
TBD
        '''
    )
    creature10 = Creature(
        species="Chimera", 
        origin="Greek", 
        description='''
        TBD
        ''',
        care_instructions="TBD",
        ascii_art= '''
TBD
        '''
    )
#     creature11 = Creature(
#         species="Centaur", 
#         origin="Greek", 
#         description='''
#         TBD
#         ''',
#         care_instructions="TBD",
#         ascii_art= '''
# TBD
#         '''
#     )
#     creature12 = Creature(
#         species="Satyr/Faun", 
#         origin="Greek, Roman", 
#         description='''
#         TBD
#         ''', 
#         care_instructions="TBD",
#         ascii_art= '''
# TBD
#         '''
#     )
#     creature13 = Creature(
#         species="Mermaid/Merman", 
#         origin="Global", 
#         description='''
#         TBD
#         ''', 
#         care_instructions="TBD",
#         ascii_art= '''
# TBD
#         '''
#     )
#     creature14 = Creature(
#         species="Nymph", 
#         origin="Greek", 
#         description='''
#         TBD
#         ''', 
#         care_instructions="TBD",
#         ascii_art= '''
# TBD
#         '''
#     )
#     creature15 = Creature(
#         species="Valkyrie", 
#         origin="Norse", 
#         description='''
#         TBD
#         ''', 
#         care_instructions="TBD",
#         ascii_art= '''
# TBD
#         '''
#     )
#     creature16 = Creature(
#         species="Basilisk", 
#         origin="European Folklore", 
#         description='''
#         TBD
#         ''', 
#         care_instructions="TBD",
#         ascii_art= '''
# TBD
#         '''
#     )
#     creature17 = Creature(
#         species="Leprechaun", 
#         origin="Celtic, Irish", 
#         description='''
#         TBD
#         ''', 
#         care_instructions="TBD",
#         ascii_art= '''
# TBD
#         '''
#     )
#     creature18 = Creature(
#         species="Werewolf", 
#         origin="European Folklore", 
#         description='''
#         TBD
#         ''', 
#         care_instructions="TBD",
#         ascii_art= '''
# TBD
#         '''
#     )
#     creature19 = Creature(
#         species="Minotaur", 
#         origin="Greek", 
#         description='''
#         TBD
#         ''', 
#         care_instructions="TBD",
#         ascii_art= '''
# TBD
#         '''
#     )
#     creature20 = Creature(
#         species="Harpy", 
#         origin="Greek", 
#         description='''
#         TBD
#         ''', 
#         care_instructions="TBD",
#         ascii_art= '''
# TBD
#         '''
#     )
#     creature21 = Creature(
#         species="Gorgon", 
#         origin="Greek", 
#         description='''
#         TBD
#         ''', 
#         care_instructions="TBD",
#         ascii_art= '''
# TBD
#         '''
#     )
#     creature22 = Creature(
#         species="Cyclops", 
#         origin="Greek", 
#         description='''
#         TBD
#         ''', 
#         care_instructions="TBD",
#         ascii_art= '''
# TBD
#         '''
#     )
#     creature23 = Creature(
#         species="Gnome", 
#         origin="European Folklore", 
#         description='''
#         TBD
#         ''', 
#         care_instructions="TBD",
#         ascii_art= '''
# TBD
#         '''
#     )
#     creature24 = Creature(
#         species="Hundun/Chaos-Beast", 
#         origin="Chinese", 
#         description='''
#         TBD
#         ''', 
#         care_instructions="TBD",
#         ascii_art= '''
# TBD
#         '''
#     )
#     creature25 = Creature(
#         species="Qilin/Kirin", 
#         origin="Chinese, Japanese", 
#         description='''
#         TBD
#         ''', 
#         care_instructions="TBD",
#         ascii_art= '''
# TBD
#         '''
#     )


## Creature Interaction
    # creatureInteraction = CreatureInteraction(name="TBD", effect_on_happiness="TBD", effect_on_health="TBD")

    creatureInteraction1 = CreatureInteraction(name="Train", effect_on_happiness="5", effect_on_health="0", effect_on_obedience="+10")
    creatureInteraction2 = CreatureInteraction(name="Feed", effect_on_happiness="+5", effect_on_health="+10", effect_on_obedience="0")
    creatureInteraction3 = CreatureInteraction(name="Praise", effect_on_happiness="+10", effect_on_health="0", effect_on_obedience="0")
    creatureInteraction4 = CreatureInteraction(name="Pet", effect_on_happiness="+10", effect_on_health="0", effect_on_obedience="0")
    creatureInteraction5 = CreatureInteraction(name="Play", effect_on_happiness="+10", effect_on_health="+5", effect_on_obedience="0")
    creatureInteraction6 = CreatureInteraction(name="Groom", effect_on_happiness="+5", effect_on_health="+5", effect_on_obedience="0")
    creatureInteraction7 = CreatureInteraction(name="Vet Visit", effect_on_happiness="-5", effect_on_health="+25", effect_on_obedience="-5")
    creatureInteraction8 = CreatureInteraction(name="Discipline", effect_on_happiness="-5", effect_on_health="-5", effect_on_obedience="+25")


## Question
    # question = Question(content="TBD", question_id=1)

    question1 = Question(content="Which environment do you prefer?")
    question2 = Question(content="What kind of power do you find most appealing?")
    question3 = Question(content="Which of these traits do you value the most in yourself?")
    question4 = Question(content="How do you approach a problem?")
    question5 = Question(content="What's your favorite time of day?")
    question6 = Question(content="How do you handle conflict?")
    question7 = Question(content="What is your preferred way to travel?")
    question8 = Question(content="What kind of role do you prefer in a group?")
    question9 = Question(content="What do you prefer to do in your free time?")
    question10 = Question(content="Which of these elements do you feel most connected to?")    
    # question11 = Question(content="TBD")
    # question12 = Question(content="TBD")
    # question13 = Question(content="TBD")
    # question14 = Question(content="TBD")
    # question15 = Question(content="TBD")
    # question16 = Question(content="TBD")
    # question17 = Question(content="TBD")
    # question18 = Question(content="TBD")
    # question19 = Question(content="TBD")
    # question20 = Question(content="TBD")
    # question21 = Question(content="TBD")
    # question22 = Question(content="TBD")
    # question23 = Question(content="TBD")
    # question24 = Question(content="TBD")
    # question25 = Question(content="TBD")
    # question26 = Question(content="TBD")
    # question27 = Question(content="TBD")
    # question28 = Question(content="TBD")
    # question29 = Question(content="TBD")
    # question30 = Question(content="TBD")
    # question31 = Question(content="TBD")
    # question32 = Question(content="TBD")
    # question33 = Question(content="TBD")
    # question34 = Question(content="TBD")
    # question35 = Question(content="TBD")
    # question36 = Question(content="TBD")
    # question37 = Question(content="TBD")
    # question38 = Question(content="TBD")
    # question39 = Question(content="TBD")
    # question40 = Question(content="TBD")
    # question41 = Question(content="TBD")
    # question42 = Question(content="TBD")
    # question43 = Question(content="TBD")
    # question44 = Question(content="TBD")
    # question45 = Question(content="TBD")
    # question46 = Question(content="TBD")
    # question47 = Question(content="TBD")
    # question48 = Question(content="TBD")
    # question49 = Question(content="TBD")
    # question50 = Question(content="TBD")
    


## User
    # user = User(username="TBD", password="TBD")

    user1 = User(username="Admin", password="Admin")
    user2 = User(username="Matthew", password="Matthew")
    user3 = User(username="Jonah", password="Jonah")
    user4 = User(username="Abby", password="Abby")
    user5 = User(username="David", password="David")



##UserCreature
    # userCreature = UserCreature(user_id="TBD", creature_id="TBD", creature_species="TBD", creature_name="TBD", happiness="TBD", health="TBD", adoption_day="TBD", last_interaction="TBD")

    userCreature1 = UserCreature(
        user_id=2,
        creature_id=1,
        creature_species="Dragon-Western",
        creature_name="Dwight", 
        happiness=50, 
        health=50,
        adoption_day=datetime(
            year=2023,
            month=3,
            day=28
        ),
        last_interaction=datetime(
            year=2023,
            month=3,
            day=28
        )
        )

    userCreature2 = UserCreature(
        user_id=2,
        creature_id=3,
        creature_species="Griffin/Gryphon",
        creature_name="Gregory", 
        happiness=50, 
        health=50,
        adoption_day=datetime(
            year=2023,
            month=3,
            day=28
        ),
        last_interaction=datetime(
            year=2023,
            month=3,
            day=28
        )
        )
    
    userCreature3 = UserCreature(
        user_id=3,
        creature_id=2,
        creature_species="Dragon-Eastern",
        creature_name="Denny", 
        happiness=50, 
        health=50,
        adoption_day=datetime(
            year=2023,
            month=3,
            day=28
        ),
        last_interaction=datetime(
            year=2023,
            month=3,
            day=28
        )
        )

#Answer
    # answer = Answer(content="TBD", question_id=1, creature_id1=1, creature_id2=2, creature_id3=3)
    answer1 = Answer(content="Mountains and caves", question_id=1, creature_id1=1, creature_id2=3, creature_id3=10)
    answer2 = Answer(content="Open skies", question_id=1, creature_id1=2, creature_id2=4, creature_id3=5)
    answer3 = Answer(content="Forests and meadows", question_id=1, creature_id1=6, creature_id2=7, creature_id3=8)
    answer4 = Answer(content="Deep seas and oceans", question_id=1, creature_id1=9, creature_id2=2, creature_id3=5)
    answer5 = Answer(content="Flight", question_id=2, creature_id1=2, creature_id2=4, creature_id3=5)
    answer6 = Answer(content="Strength", question_id=2, creature_id1=1, creature_id2=3, creature_id3=8)
    answer7 = Answer(content="Wisdom", question_id=2, creature_id1=7, creature_id2=6, creature_id3=10)
    answer8 = Answer(content="Adaptability", question_id=2, creature_id1=9, creature_id2=4, creature_id3=1)
    answer9 = Answer(content="Loyalty", question_id=3, creature_id1=1, creature_id2=8, creature_id3=6)
    answer10 = Answer(content="Creativity", question_id=3, creature_id1=4, creature_id2=3, creature_id3=10)
    answer11 = Answer(content="Intelligence", question_id=3, creature_id1=7, creature_id2=2, creature_id3=9)
    answer12 = Answer(content="Courage", question_id=3, creature_id1=5, creature_id2=8, creature_id3=1)
    answer13 = Answer(content="Head-on", question_id=4, creature_id1=3, creature_id2=8, creature_id3=5)
    answer14 = Answer(content="Strategically", question_id=4, creature_id1=7, creature_id2=2, creature_id3=10)
    answer15 = Answer(content="Patiently", question_id=4, creature_id1=6, creature_id2=4, creature_id3=9)
    answer16 = Answer(content="Adapt and change", question_id=4, creature_id1=1, creature_id2=9, creature_id3=4)
    answer17 = Answer(content="Dawn", question_id=5, creature_id1=4, creature_id2=5, creature_id3=2)
    answer18 = Answer(content="Daytime", question_id=5, creature_id1=6, creature_id2=3, creature_id3=7)
    answer19 = Answer(content="Dusk", question_id=5, creature_id1=10, creature_id2=8, creature_id3=1)
    answer20 = Answer(content="Nighttime", question_id=5, creature_id1=9, creature_id2=2, creature_id3=8)
    answer21 = Answer(content="Stand your ground", question_id=6, creature_id1=1, creature_id2=8, creature_id3=3)
    answer22 = Answer(content="Diplomacy", question_id=6, creature_id1=6, creature_id2=7, creature_id3=5)
    answer23 = Answer(content="Adapt and find a solution", question_id=6, creature_id1=4, creature_id2=9, creature_id3=2)
    answer24 = Answer(content="Use cunning", question_id=6, creature_id1=10, creature_id2=9, creature_id3=7)
    answer25 = Answer(content="Flying", question_id=7, creature_id1=5, creature_id2=2, creature_id3=4)
    answer26 = Answer(content="Running", question_id=7, creature_id1=6, creature_id2=8, creature_id3=3)
    answer27 = Answer(content="Swimming", question_id=7, creature_id1=9, creature_id2=10, creature_id3=1)
    answer28 = Answer(content="Teleportation", question_id=7, creature_id1=7, creature_id2=4, creature_id3=2)
    answer29 = Answer(content="Leader", question_id=8, creature_id1=1, creature_id2=3, creature_id3=7)
    answer30 = Answer(content="Strategist", question_id=8, creature_id1=2, creature_id2=10, creature_id3=9)
    answer31 = Answer(content="Healer", question_id=8, creature_id1=6, creature_id2=4, creature_id3=5)
    answer32 = Answer(content="Protector", question_id=8, creature_id1=8, creature_id2=9, creature_id3=1)
    answer33 = Answer(content="Adventure", question_id=9, creature_id1=1, creature_id2=5, creature_id3=3)
    answer34 = Answer(content="Meditate", question_id=9, creature_id1=6, creature_id2=4, creature_id3=2)
    answer35 = Answer(content="Solve puzzles", question_id=9, creature_id1=7, creature_id2=9, creature_id3=10)
    answer36 = Answer(content="Protect loved ones", question_id=9, creature_id1=8, creature_id2=1, creature_id3=5)
    answer37 = Answer(content="Fire", question_id=10, creature_id1=1, creature_id2=4, creature_id3=10)
    answer38 = Answer(content="Water", question_id=10, creature_id1=9, creature_id2=2, creature_id3=8)
    answer39 = Answer(content="Earth", question_id=10, creature_id1=3, creature_id2=6, creature_id3=7)
    answer40 = Answer(content="Air", question_id=10, creature_id1=5, creature_id2=4, creature_id3=2)
    # answer41 = Answer(content="TBD", question_id=11, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer42 = Answer(content="TBD", question_id=11, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer43 = Answer(content="TBD", question_id=11, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer44 = Answer(content="TBD", question_id=11, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer45 = Answer(content="TBD", question_id=12, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer46 = Answer(content="TBD", question_id=12, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer47 = Answer(content="TBD", question_id=12, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer48 = Answer(content="TBD", question_id=12, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer49 = Answer(content="TBD", question_id=13, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer50 = Answer(content="TBD", question_id=13, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer51 = Answer(content="TBD", question_id=13, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer52 = Answer(content="TBD", question_id=13, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer53 = Answer(content="TBD", question_id=14, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer54 = Answer(content="TBD", question_id=14, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer55 = Answer(content="TBD", question_id=14, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer56 = Answer(content="TBD", question_id=14, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer57 = Answer(content="TBD", question_id=15, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer58 = Answer(content="TBD", question_id=15, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer59 = Answer(content="TBD", question_id=15, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer60 = Answer(content="TBD", question_id=15, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer61 = Answer(content="TBD", question_id=16, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer62 = Answer(content="TBD", question_id=16, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer63 = Answer(content="TBD", question_id=16, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer64 = Answer(content="TBD", question_id=16, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer65 = Answer(content="TBD", question_id=17, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer66 = Answer(content="TBD", question_id=17, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer67 = Answer(content="TBD", question_id=17, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer68 = Answer(content="TBD", question_id=17, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer69 = Answer(content="TBD", question_id=18, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer70 = Answer(content="TBD", question_id=18, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer71 = Answer(content="TBD", question_id=18, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer72 = Answer(content="TBD", question_id=18, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer73 = Answer(content="TBD", question_id=19, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer74 = Answer(content="TBD", question_id=19, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer75 = Answer(content="TBD", question_id=19, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer76 = Answer(content="TBD", question_id=19, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer77 = Answer(content="TBD", question_id=20, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer78 = Answer(content="TBD", question_id=20, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer79 = Answer(content="TBD", question_id=20, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer80 = Answer(content="TBD", question_id=20, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer81 = Answer(content="TBD", question_id=21, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer82 = Answer(content="TBD", question_id=21, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer83 = Answer(content="TBD", question_id=21, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer84 = Answer(content="TBD", question_id=21, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer85 = Answer(content="TBD", question_id=22, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer86 = Answer(content="TBD", question_id=22, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer87 = Answer(content="TBD", question_id=22, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer88 = Answer(content="TBD", question_id=22, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer89 = Answer(content="TBD", question_id=23, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer90 = Answer(content="TBD", question_id=23, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer91 = Answer(content="TBD", question_id=23, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer92 = Answer(content="TBD", question_id=23, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer93 = Answer(content="TBD", question_id=24, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer94 = Answer(content="TBD", question_id=24, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer95 = Answer(content="TBD", question_id=24, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer96 = Answer(content="TBD", question_id=24, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer97 = Answer(content="TBD", question_id=25, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer98 = Answer(content="TBD", question_id=25, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer99 = Answer(content="TBD", question_id=25, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer100 = Answer(content="TBD", question_id=25, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer101 = Answer(content="TBD", question_id=26, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer102 = Answer(content="TBD", question_id=26, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer103 = Answer(content="TBD", question_id=26, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer104 = Answer(content="TBD", question_id=26, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer105 = Answer(content="TBD", question_id=27, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer106 = Answer(content="TBD", question_id=27, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer107 = Answer(content="TBD", question_id=27, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer108 = Answer(content="TBD", question_id=27, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer109 = Answer(content="TBD", question_id=28, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer110 = Answer(content="TBD", question_id=28, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer111 = Answer(content="TBD", question_id=28, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer112 = Answer(content="TBD", question_id=28, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer113 = Answer(content="TBD", question_id=29, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer114 = Answer(content="TBD", question_id=29, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer115 = Answer(content="TBD", question_id=29, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer116 = Answer(content="TBD", question_id=29, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer117 = Answer(content="TBD", question_id=30, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer118 = Answer(content="TBD", question_id=30, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer119 = Answer(content="TBD", question_id=30, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer120 = Answer(content="TBD", question_id=30, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer121 = Answer(content="TBD", question_id=31, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer122 = Answer(content="TBD", question_id=31, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer123 = Answer(content="TBD", question_id=31, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer124 = Answer(content="TBD", question_id=31, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer125 = Answer(content="TBD", question_id=32, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer126 = Answer(content="TBD", question_id=32, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer127 = Answer(content="TBD", question_id=32, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer128 = Answer(content="TBD", question_id=32, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer129 = Answer(content="TBD", question_id=33, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer130 = Answer(content="TBD", question_id=33, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer131 = Answer(content="TBD", question_id=33, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer132 = Answer(content="TBD", question_id=33, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer133 = Answer(content="TBD", question_id=34, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer134 = Answer(content="TBD", question_id=34, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer135 = Answer(content="TBD", question_id=34, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer136 = Answer(content="TBD", question_id=34, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer137 = Answer(content="TBD", question_id=35, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer138 = Answer(content="TBD", question_id=35, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer139 = Answer(content="TBD", question_id=35, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer140 = Answer(content="TBD", question_id=35, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer141 = Answer(content="TBD", question_id=36, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer142 = Answer(content="TBD", question_id=36, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer143 = Answer(content="TBD", question_id=36, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer144 = Answer(content="TBD", question_id=36, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer145 = Answer(content="TBD", question_id=37, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer146 = Answer(content="TBD", question_id=37, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer147 = Answer(content="TBD", question_id=37, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer148 = Answer(content="TBD", question_id=37, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer149 = Answer(content="TBD", question_id=38, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer150 = Answer(content="TBD", question_id=38, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer151 = Answer(content="TBD", question_id=38, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer152 = Answer(content="TBD", question_id=38, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer153 = Answer(content="TBD", question_id=39, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer154 = Answer(content="TBD", question_id=39, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer155 = Answer(content="TBD", question_id=39, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer156 = Answer(content="TBD", question_id=39, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer157 = Answer(content="TBD", question_id=40, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer158 = Answer(content="TBD", question_id=40, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer159 = Answer(content="TBD", question_id=40, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer160 = Answer(content="TBD", question_id=40, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer161 = Answer(content="TBD", question_id=41, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer162 = Answer(content="TBD", question_id=41, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer163 = Answer(content="TBD", question_id=41, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer164 = Answer(content="TBD", question_id=41, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer165 = Answer(content="TBD", question_id=42, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer166 = Answer(content="TBD", question_id=42, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer167 = Answer(content="TBD", question_id=42, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer168 = Answer(content="TBD", question_id=42, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer169 = Answer(content="TBD", question_id=43, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer170 = Answer(content="TBD", question_id=43, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer171 = Answer(content="TBD", question_id=43, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer172 = Answer(content="TBD", question_id=43, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer173 = Answer(content="TBD", question_id=44, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer174 = Answer(content="TBD", question_id=44, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer175 = Answer(content="TBD", question_id=44, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer176 = Answer(content="TBD", question_id=44, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer177 = Answer(content="TBD", question_id=45, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer178 = Answer(content="TBD", question_id=45, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer179 = Answer(content="TBD", question_id=45, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer180 = Answer(content="TBD", question_id=45, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer181 = Answer(content="TBD", question_id=46, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer182 = Answer(content="TBD", question_id=46, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer183 = Answer(content="TBD", question_id=46, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer184 = Answer(content="TBD", question_id=46, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer185 = Answer(content="TBD", question_id=47, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer186 = Answer(content="TBD", question_id=47, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer187 = Answer(content="TBD", question_id=47, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer188 = Answer(content="TBD", question_id=47, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer189 = Answer(content="TBD", question_id=48, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer190 = Answer(content="TBD", question_id=48, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer191 = Answer(content="TBD", question_id=48, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer192 = Answer(content="TBD", question_id=48, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer193 = Answer(content="TBD", question_id=49, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer194 = Answer(content="TBD", question_id=49, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer195 = Answer(content="TBD", question_id=49, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer196 = Answer(content="TBD", question_id=49, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer197 = Answer(content="TBD", question_id=50, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer198 = Answer(content="TBD", question_id=50, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer199 = Answer(content="TBD", question_id=50, creature_id1=1, creature_id2=2, creature_id3=3)
    # answer200 = Answer(content="TBD", question_id=50, creature_id1=1, creature_id2=2, creature_id3=3)


    everything = [
        creature1, creature2, creature3, creature4, creature5, 
        creature6, creature7, creature8, creature9, creature10, 
        # creature11, creature12, creature13, creature14, creature15, 
        # creature16, creature17, creature18, creature19, creature20, 
        # creature21, creature22, creature23, creature24, creature25, 
        creatureInteraction1, creatureInteraction2, creatureInteraction3, creatureInteraction4,
        creatureInteraction5, creatureInteraction6, creatureInteraction7, creatureInteraction8,
        question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, 
        # question11, question12, question13, question14, question15, question16, question17, question18, question19, question20, 
        # question21, question22, question23, question24, question25, question26, question27, question28, question29, question30, 
        # question31, question32, question33, question34, question35, question36, question37, question38, question39, question40, 
        # question41, question42, question43, question44, question45, question46, question47, question48, question49, question50, 
        user1, user2, user3, user4, user5, 
        userCreature1, userCreature2, userCreature3, 
        answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9, answer10, 
        answer11, answer12, answer13, answer14, answer15, answer16, answer17, answer18, answer19, answer20, 
        answer21, answer22, answer32, answer24, answer25, answer26, answer27, answer28, answer29, answer30, 
        answer31, answer32, answer33, answer34, answer35, answer36, answer37, answer38, answer39, answer40, 
        # answer41, answer42, answer43, answer44, answer45, answer46, answer47, answer48, answer49, answer50, 
        # answer51, answer52, answer53, answer54, answer55, answer56, answer57, answer58, answer59, answer60, 
        # answer61, answer62, answer63, answer64, answer65, answer66, answer67, answer68, answer69, answer70, 
        # answer71, answer72, answer73, answer74, answer75, answer76, answer77, answer78, answer79, answer80, 
        # answer81, answer82, answer83, answer84, answer85, answer86, answer87, answer88, answer89, answer90, 
        # answer91, answer92, answer93, answer94, answer95, answer96, answer97, answer98, answer99, answer100, 
        # answer101, answer102, answer103, answer104, answer105, answer106, answer107, answer108, answer109, answer110, 
        # answer111, answer112, answer113, answer114, answer115, answer116, answer117, answer118, answer119, answer120, 
        # answer121, answer122, answer123, answer124, answer125, answer126, answer127, answer128, answer129, answer130, 
        # answer131, answer132, answer133, answer134, answer135, answer136, answer137, answer138, answer139, answer140, 
        # answer141, answer142, answer143, answer144, answer145, answer146, answer147, answer148, answer149, answer150, 
        # answer151, answer152, answer153, answer154, answer155, answer156, answer157, answer158, answer159, answer160, 
        # answer161, answer162, answer163, answer164, answer165, answer166, answer167, answer168, answer169, answer170, 
        # answer171, answer172, answer173, answer174, answer175, answer176, answer177, answer178, answer179, answer180, 
        # answer181, answer182, answer183, answer184, answer185, answer186, answer187, answer188, answer189, answer190, 
        # answer191, answer192, answer193, answer194, answer195, answer196, answer197, answer198, answer199, answer200, 
        ]

    session.add_all(everything)
    session.commit()
    