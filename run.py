"""
Imports:
os imported for clearing the terminal
https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python
time imported to add time delays for print statements
https://realpython.com/python-sleep/
"""
import os
import time
from colorama import Fore, Back, Style
import emoji
import text

text.welcome()


def clear_terminal():
    """
    os.system terminal cleaning fuction, clears text in terminal.
    referance:
    https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_user_info():
    """
    Gets user input in correct form and collects user information
    like nickname, age and relationship status
    that is needed to proceed the game.
    """
    print(Fore.YELLOW + "\nPlease enter a nickname only using letters.\n")
    while True:
        nickname = input(":")
        if nickname.isalpha():
            break
        else:
            print(Fore.RED + '\n"That is not correct. Please try again."\n')

    print(Fore.YELLOW + "\nPlease enter your age in numbers.\n")
    while True:
        age = input(":")
        if age.isdigit():
            break
        else:
            print(Fore.RED + '\n"That is not correct. Please try again."\n')

    print(Fore.YELLOW + "\nPlease enter your relationship status.\n")
    while True:
        relationship = input(":")
        if relationship.isalpha():
            break
        else:
            print(Fore.RED + '\n"That is not correct. Please try again."\n')


def game_start():
    """
    After the welcome message, asks user if they want to play the game.
    Checks the user answer if entered in correct method.
    If answer is yes, moves on to getting user information.
    If user answers no, takes user back to welcome message.
    """
    text.game_start()

    while True:
        answer = input(" ").lower()
        if answer == "yes":
            # clear terminal, get user info
            clear_terminal()
            get_user_info()
            break
        elif answer == "no":
            # ask user if they are sure saying no
            text.user_answer_no()
            text.game_start()
            answer = input(" ").lower()
            if answer == "yes":
                clear_terminal()
                get_user_info()
                break
            elif answer == "no":
                text.user_answer_final()
                clear_terminal()
                break
            else:
                print(Fore.RED + '\n"That is incorrect. Please try again."\n')
        else:
            print(Fore.RED + '\n"That is incorrect. Please try again."\n')
            # take back to welcome
            text.welcome()


game_start()


def select_topic():
    """
    Allows user to select a topic from 4 topics provided
    to get future predictions. Depending on the collected
    user data a prediction will be displayed.
    """
    clear_terminal()
    text.topics()
    while True:
        topic = input(" ")
        if topic == "1":
            # add the health prediction
            break
        elif topic == "2":
            # add the work prediction
            break
        elif topic == "3":
            # add the Education prediction
            break
        elif topic == "4":
            # add the relationship prediction
            break
        else:
            print(Fore.RED + '\n"That is incorrect. Please try again."\n')
