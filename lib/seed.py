from sqlalchemy import *
from sqlalchemy.orm import *
from classes.answer import Answer
from classes.creature import Creature
from classes.creatureInteraction import CreatureInteraction
from classes.question import Question
from classes.userCreature import UserCreature
from classes.user import User
from classes.base import Base

engine = create_engine('sqlite:///dnd.db')
Answer.__table__.drop(engine)
Creature.__table__.drop(engine)
CreatureInteraction.__table__.drop(engine)
Question.__table__.drop(engine)
User.__table__.drop(engine)
UserCreature.__table__.drop(engine)
Base.metadata.create_all(engine)
with Session(engine) as session:

    # enter in the following order!:

    # creature = Creature(name="TBD", origin="TBD", description="TBD", care_instructions="TBD", ascii_art=''' TBD ''')
    # creatureInteraction = CreatureInteraction(name="TBD", effect_on_happiness="TBD", effect_on_health="TBD")
    # question = Question(content="TBD")
    # user = User(username="TBD", password="TBD")
    # userCreature = UserCreature(creature_id="TBD", creature_name="TBD", happiness="TBD", health="TBD", last_interaction="TBD")
    # answer = Answer(content="TBD", question_id=1, creature_id1=1, creature_id2=2, creature_id3=3)


## Creature
    # creature = Creature(type="TBD", origin="TBD", description="TBD", care_instructions="TBD",ascii_art=''' TBD ''')

    creature1 = Creature(
        type="Dragon-Western", 
        origin="European", 
        description="In European mythology, dragons are legendary creatures typically portrayed as large, fire-breathing reptilian beasts with wings, sharp claws, and scaly skin. They are often depicted as fierce and dangerous creatures that hoard treasure and demand tribute from nearby villages or towns. In some stories, they are seen as agents of evil and chaos, wreaking havoc and destruction wherever they go. However, in other tales, dragons can also be wise and powerful beings that possess magical abilities and knowledge. In some European mythologies, dragons are also associated with royalty and are depicted as protectors of kingdoms and important treasures. They have been a popular theme in European literature and art for centuries and continue to be an iconic symbol of fantasy and adventure.", 
        care_instructions="TBD"
        ascii_art= '''
                 ___====-_  _-====___
           _--^^^#####//      \\#####^^^--_
        _-^##########// (    ) \\##########^-_
       -############//  |\^^/|  \\############-
     _/############//   (@::@)   \\############\_
    /#############((     \\//     ))#############\
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
        type="Dragon-Eastern", 
        origin="Chinese, Japanese, Korean", 
        description="Dragons in Chinese, Japanese, and Korean mythology are revered as powerful, benevolent creatures associated with water, rain, and good fortune. They are typically depicted as long, serpentine creatures with four legs, long whiskers, and a mane of hair or fur running down their backs. Unlike the European dragon, these dragons are often portrayed without wings, and they are said to be able to fly using their magical abilities. They are seen as symbols of strength, good fortune, and divine power, and their images can be found on many cultural artifacts and decorations. Dragons in these mythologies are regarded with great respect and are believed to bring luck and prosperity to those who revere them.", 
        care_instructions="TBD"
        ascii_art= '''
                           _,,,.._       ,_
                        .gMMMMMMMMMp,_    `\
                     .dMMP'       ``^YMb..dP
                    dMMP'
                    MMM:
                    YMMb.
                     YMMMb.
                      `YMM/|Mb.  ,__
                   _,,-~`--..-~-'_,/`--,,,____
               `\,_,/',_.-~_..-~/' ,/---~~~"""`\
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
        type="Griffin/Gryphon", 
        origin="Greek, European", 
        description="A Griffin, also known as a Gryphon, is a legendary creature from Greek and European mythology that has the body of a lion and the head and wings of an eagle. These creatures are often portrayed as fierce and powerful, with sharp talons and keen eyesight. In mythology, they are known to be guardians of treasures and powerful protectors, and their images can be found in art and architecture throughout history. The Griffin represents the combination of the strength and courage of the lion with the grace and wisdom of the eagle, making it a symbol of power and intelligence in many cultures.", 
        care_instructions="TBD"
        ascii_art= '''
                          _)\.-.
         .-.__,___,_.-=-. )\`  a`\_
     .-.__\__,__,__.-=-. `/  \     `\
     {~,-~-,-~.-~,-,;;;;\ |   '--;`)/
      \-,~_-~_-,~-,(_(_(;\/   ,;/
       ",-.~_,-~,-~,)_)_)'.  ;;(
         `~-,_-~,-~(_(_(_(_\  `;\
   ,          `"~~--,)_)_)_)\_   \
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
        type="Phoenix", 
        origin="Greek, Egyptian, Chinese, Japanese", 
        description="The Phoenix is a mythical bird that appears in Greek, Egyptian, Chinese, and Japanese mythology. It is often depicted as a bird with bright and colorful feathers that are said to be reborn from the ashes of its own funeral pyre. In Greek mythology, the Phoenix is a symbol of resurrection and rebirth, while in Egyptian mythology it is associated with the sun and the cycle of life and death. In Chinese and Japanese mythology, the Phoenix is associated with prosperity, good fortune, and feminine grace. Overall, the Phoenix is a symbol of hope, renewal, and transformation, and its mythical qualities have made it a popular symbol in art and literature throughout history.", 
        care_instructions="TBD"
        ascii_art= '''
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
          ((      '''''''\uuuuuuuu/``````         ))
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
        type="Pegasus", 
        origin="Greek",  
        description="TBD", 
        care_instructions="TBD"
        ascii_art= '''
TBD
        '''
    )

    creature6 = Creature(
        type="Unicorn", 
        origin="Ancient mythology, European folklore", 
        description="TBD", 
        care_instructions="TBD"
        ascii_art= '''
TBD
        '''
    )

    creature7 = Creature(
        type="Sphinx", 
        origin="Greek, Egyptian", 
        description="TBD", 
        care_instructions="TBD"
        ascii_art= '''
TBD
        '''
    )

    creature8 = Creature(
        type="Cerberus", 
        origin="Greek", 
        description="TBD", 
        care_instructions="TBD"
        ascii_art= '''
TBD
        '''
    )

    creature9 = Creature(
        type="Kraken", 
        origin="Norse", 
        description="TBD", 
        care_instructions="TBD"
        ascii_art= '''
TBD
        '''
    )

    creature10 = Creature(
        type="Chimera", 
        origin="Greek", 
        description="TBD", 
        care_instructions="TBD"
        ascii_art= '''
TBD
        '''
    )

    creature11 = Creature(
        type="Centaur", 
        origin="Greek", 
        description="TBD", 
        care_instructions="TBD"
        ascii_art= '''
TBD
        '''
    )

    creature12 = Creature(
        type="Satyr/Faun", 
        origin="Greek, Roman", 
        description="TBD", 
        care_instructions="TBD"
        ascii_art= '''
TBD
        '''
    )

    creature13 = Creature(
        type="Mermaid/Merman", 
        origin="Global", 
        description="TBD", 
        care_instructions="TBD"
        ascii_art= '''
TBD
        '''
    )

    creature14 = Creature(
        type="Nymph", 
        origin="Greek", 
        description="TBD", 
        care_instructions="TBD"
        ascii_art= '''
TBD
        '''
    )

    creature15 = Creature(
        type="Valkyrie", 
        origin="Norse", 
        description="TBD", 
        care_instructions="TBD"
        ascii_art= '''
TBD
        '''
    )

    creature16 = Creature(
        type="Basilisk", 
        origin="European Folklore", 
        description="TBD", 
        care_instructions="TBD"
        ascii_art= '''
TBD
        '''
    )

    creature17 = Creature(
        type="Leprechaun", 
        origin="Celtic, Irish", 
        description="TBD", 
        care_instructions="TBD"
        ascii_art= '''
TBD
        '''
    )

    creature18 = Creature(
        type="Werewolf", 
        origin="European Folklore", 
        description="TBD", 
        care_instructions="TBD"
        ascii_art= '''
TBD
        '''
    )

    creature19 = Creature(
        type="Minotaur", 
        origin="Greek", 
        description="TBD", 
        care_instructions="TBD"
        ascii_art= '''
TBD
        '''
    )

    creature20 = Creature(
        type="Harpy", 
        origin="Greek", 
        description="TBD", 
        care_instructions="TBD"
        ascii_art= '''
TBD
        '''
    )

    creature21 = Creature(
        type="Gorgon", 
        origin="Greek", 
        description="TBD", 
        care_instructions="TBD"
        ascii_art= '''
TBD
        '''
    )

    creature22 = Creature(
        type="Cyclops", 
        origin="Greek", 
        description="TBD", 
        care_instructions="TBD"
        ascii_art= '''
TBD
        '''
    )

    creature23 = Creature(
        type="Gnome", 
        origin="TBD", 
        description="TBD", 
        care_instructions="TBD"
        ascii_art= '''
TBD
        '''
    )

    creature24 = Creature(
        type="TBD", 
        origin="TBD", 
        description="TBD", 
        care_instructions="TBD"
        ascii_art= '''
TBD
        '''
    )

    creature25 = Creature(
        type="TBD", 
        origin="TBD", 
        description="TBD", 
        care_instructions="TBD"
        ascii_art= '''
TBD
        '''
    )


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

    question1 = Question(content="TBD")
    question2 = Question(content="TBD")
    question3 = Question(content="TBD")
    question4 = Question(content="TBD")
    question5 = Question(content="TBD")
    question6 = Question(content="TBD")
    question7 = Question(content="TBD")
    question8 = Question(content="TBD")
    question9 = Question(content="TBD")
    question10 = Question(content="TBD")    
    question11 = Question(content="TBD")
    question12 = Question(content="TBD")
    question13 = Question(content="TBD")
    question14 = Question(content="TBD")
    question15 = Question(content="TBD")
    question16 = Question(content="TBD")
    question17 = Question(content="TBD")
    question18 = Question(content="TBD")
    question19 = Question(content="TBD")
    question20 = Question(content="TBD")    
    question21 = Question(content="TBD")
    question22 = Question(content="TBD")
    question23 = Question(content="TBD")
    question24 = Question(content="TBD")
    question25 = Question(content="TBD")
    question26 = Question(content="TBD")
    question27 = Question(content="TBD")
    question28 = Question(content="TBD")
    question29 = Question(content="TBD")
    question30 = Question(content="TBD")
    question31 = Question(content="TBD")
    question32 = Question(content="TBD")
    question33 = Question(content="TBD")
    question34 = Question(content="TBD")
    question35 = Question(content="TBD")
    question36 = Question(content="TBD")
    question37 = Question(content="TBD")
    question38 = Question(content="TBD")
    question39 = Question(content="TBD")
    question40 = Question(content="TBD")
    question41 = Question(content="TBD")
    question42 = Question(content="TBD")
    question43 = Question(content="TBD")
    question44 = Question(content="TBD")
    question45 = Question(content="TBD")
    question46 = Question(content="TBD")
    question47 = Question(content="TBD")
    question48 = Question(content="TBD")
    question49 = Question(content="TBD")
    question50 = Question(content="TBD")
    


## User
    # user = User(username="TBD", password="TBD")


##UserCreature
    # userCreature = UserCreature(creature_id="TBD", creature_name="TBD", happiness="TBD", health="TBD", last_interaction="TBD")


#Answer
    # answer = Answer(content="TBD", question_id=1, creature_id1=1, creature_id2=2, creature_id3=3)


    everything = [
        creature1, creature2, creature3, creature4, creature5, 
        creature6, creature7, creature8, creature9, creature10, 
        creature11, creature12, creature13, creature14, creature15, 
        creature16, creature17, creature18, creature19, creature20, 
        creature21, creature22, creature23, creature24, creature25, 
        creatureInteraction1, creatureInteraction2, creatureInteraction3, creatureInteraction4,
        creatureInteraction5, creatureInteraction6, creatureInteraction7, creatureInteraction8,
        question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, 
        question11, question12, question13, question14, question15, question16, question17, question18, question19, question20, 
        question21, question22, question23, question24, question25, question26, question27, question28, question29, question30, 
        question31, question32, question33, question34, question35, question36, question37, question38, question39, question40, 
        question41, question42, question43, question44, question45, question46, question47, question48, question49, question50, 
        ]

    session.add_all(everything)
    session.commit()
    