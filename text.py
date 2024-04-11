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


def topics():
    """
    Gives user a list of topics to select to get future predictions.
    """
    print("\nThere is four different topics to focus on.\n")
    time.sleep(1)
    print("\nYou need to pick only one topic to get a prediction.\n")
    time.sleep(2)
    print("1. Health")
    print("2. Work")
    print("3. Education")
    print("3. Relationship")
    time.sleep(2)
    print("\nType the number you selected and press enter.\n")
