from flaskapp import celery
from flaskapp.models import User


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
