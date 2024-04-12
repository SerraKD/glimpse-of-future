"""
time imported to add time delays for print statements
https://realpython.com/python-sleep/
https://www.geeksforgeeks.org/print-colors-python-terminal/
"""
import time
from colorama import Fore, Back, Style
import emoji


def welcome():
    """
    Welcomes user to the game and gives details about the game.
    """
    time.sleep(1)
    print(Fore.MAGENTA + "\nWelcome to the Glimpse of the Future \U0001F52E\n")
    time.sleep(2)
    print(Fore.BLUE + "With me, you can glance at your future\n")
    time.sleep(1)
    print("and see what's to come!\n")
    time.sleep(2)
    print("\nYou don't need to do much.\n")
    time.sleep(1)
    print("I will do most of the work for you.\n")
    time.sleep(2)
    print("\nAll I need is basic details as: \n")
    time.sleep(1)
    print("your nickname, age, and relationship status.\n")
    time.sleep(3)
    print("\nThere will be four different topics to focus on.\n")
    time.sleep(1)
    print("Health, work, education, and relationship.\n")
    time.sleep(2)
    print("\nYou need to pick one topic to get a chance\n")
    time.sleep(1)
    print("to sneak a peek at your future.\n")
    time.sleep(2)
    print("\nDon't worry if you are hungry for more, \U0001F60C\n")
    time.sleep(1)
    print("You can pick another topic after the first sneak peek.\n")
    time.sleep(2)
    print("\nBut we can get to all that later.\n")
    time.sleep(3)
    print(Style.RESET_ALL)


def game_start():
    """
    Asks user if they want to start the game
    """
    print(Fore.GREEN + "\nAre you ready? \U0001F9D9\n")
    time.sleep(1)
    print('\nIf so, please type in "yes" and press enter.\n')
    print(Style.RESET_ALL)


def user_answer_no():
    """
    Asks user if they are sure to not start the game
    """
    print(Fore.RED + "\nHmm... I knew that you would say no. \U0001F9D9\n")
    time.sleep(2)
    print('\nI will give you one more chance..\n')
    time.sleep(2)
    print(Style.RESET_ALL)


def user_answer_final():
    """
    If user insist on not playing game, prints text to say bye
    """
    print(Fore.RED + "\nI understand.\n")
    time.sleep(2)
    print("\nSome humans can't handle the great fear of the unknown.\n")
    time.sleep(2)
    print("\nIf you change your mind, you know where to find me.\U0001F609\n")
    time.sleep(3)
    print(Style.RESET_ALL)


def incorrect_input():
    """
    Lets user know that answer given is in incorrect format.
    """
    print(Fore.RED + '\n"That is incorrect. Please try again."\n')
    print(Style.RESET_ALL)


def topics():
    """
    Gives user a list of topics to select to get future predictions.
    """
    print("\nThere is four different topics to focus on.\n")
    time.sleep(1)
    print("\nYou need to pick only one topic to get a prediction.\n")
    time.sleep(2)
    print("1. Health \U0001F3E5")
    print("2. Work \U0001F4BC")
    print("3. Education \U0001F4DA")
    print("3. Relationship \U0001F496")
    time.sleep(2)
    print("\nType the number you selected and press enter.\n")


def know_more():
    """
    After the first prediction, ask user if they want to know more.
    """
    print(Fore.YELLOW + "\nWould you like to know more?\U0001F4AD\n")
    time.sleep(1)
    print('If so, please type in "yes" and press enter.\n')


def game_end():
    """
    Displays end game text
    """
    print(Fore.MAGENTA + "\nIt was a pleasure meeting you.\n")
    print("\nAnd thank you for letting me take a peek into your future.\n")
    time.sleep(2)
    print("\nBut others need me now, \U0001F9D9\n")
    time.sleep(1)
    print("so I must go.\n")
    time.sleep(2)
    print("We will meet again.\n")
    print("\n \U0001F441 \n")
    time.sleep(3)
    print(Style.RESET_ALL)


"""
#Topics
"""


def health_1():
    """
    Health future prediction text for age <=25
    """
    time.sleep(1)
    print(Fore.GREEN + "\nYou are young, wild, and free. \U0001F57A\n")
    time.sleep(2)
    print("But you will not stay that way forever!\n")
    time.sleep(2)
    print("\nCall me bitter if you will, but I must say,\n")
    time.sleep(1)
    print("it would be best if you took better care of yourself.\n")
    time.sleep(2)
    print("I don't foresee concerns regarding your health in the future.\n")
    time.sleep(2)
    print("\nJust remember my advice and\n")
    time.sleep(3)
    print("take care of your physical and mental well-being.\n")
    time.sleep(1)


def health_2():
    """
    Health future prediction text for age <=45
    """
    time.sleep(1)
    print(Fore.GREEN + "\nHmm.. A curious choice for you. \U0001F914\n")
    time.sleep(2)
    print("I see that you worry about your health sometimes.\n")
    time.sleep(1)
    print("\nWell, you shouldn't.\n")
    time.sleep(1)
    print("Instead, do what you need to do to take care of yourself.\n")
    time.sleep(2)
    print("I see a few minor health problems that may arise in the future.\n")
    time.sleep(2)
    print("But there is no need to panic, everyone has minor issues.\n")
    time.sleep(3)
    print("Focus on the good and you will be okay.\n")
    time.sleep(1)


def health_3():
    """
    Health future prediction text for age =>46
    """
    time.sleep(1)
    print(Fore.GREEN + "\nWhat is that sound?!\n")
    time.sleep(2)
    print("Oh, it's your bones cracking. \U0001F468\n")
    time.sleep(1)
    print("\nI am just kidding of course.\n")
    time.sleep(1)
    print("You are in great shape, keep up the good work!\n")
    time.sleep(2)
    print("Things may not be easy in the future,\n")
    time.sleep(2)
    print("But that's just life, right?\n")
    time.sleep(3)
    print("I foresee good health and lots of happiness for you.\n")
    time.sleep(1)
