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
    print("\nWelcome to the Glimpse of the Future \U0001F52E\n")
    time.sleep(2)
    print("With me, you can glance at your future\n")
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


def game_start():
    """
    Asks user if they want to start the game
    """
    print("\nAre you ready? \U0001F9D9\n")
    time.sleep(2)
    print('\nIf so, please type in "yes" and press enter.\n')
