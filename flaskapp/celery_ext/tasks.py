from flaskapp import celery
from flaskapp.models import User
from time import sleep

@celery.task()
def make_coffee(name='Unknown'):
    user = User.get(1)
    coffee = '''A special coffee for you {}, it was made by {}, enjoy it!!!
                                      (
                                    )     (
                             ___...(-------)-....___
                         .-""       )    (          ""-.
                   .-'``'|-._             )         _.-|
                  /  .--.|   `""---...........---""`   |
                 /  /    |                             |
                 |  |    |                             |
                  \  \   |                             |
                   `\ `\ |                             |
                     `\ `|                             |
                     _/ /\                             /
                    (__/  \                           /
                 _..---""` \                         /`""---.._
              .-'           \                       /          '-.
             :               `-.__             __.-'              :
             :                  ) ""---...---"" (                 :
              '._               `"--...___...--"`              _.'
                \""--..__                              __..--""/
                 '._     """----.....______.....----"""     _.'
                    `""--..,,_____            _____,,..--""`
                                  `"""----"""`
    '''.format(name, user.name)
    print(coffee)


@celery.task()
def make_capuccino(name='Unknown'):
    user = User.get(1)
    sleep(15)
    coffee = """A special capuccino for you {}, it was made by {}, sorry for the delay!!!
                                   ) ( 
                                  (    ) 
                                     (
                                 ,o(__Oo,
                                O,_()_(_)o, 
                               ( _),(o_),_)
                              _|`--------(_)
                             (C|          |__
                           /` `\          /  `\`
                           \    `========`    /
                            `'---------------'                                
    """.format(name, user.name)
    print(coffee)

