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


def get_nickname():
    """
    Gets user input for nickname in correct form
    and returns user information
    """

    print(Fore.YELLOW + "\nPlease enter a nickname only using letters.\n")
    print("E.g. simba\n")
    while True:
        nickname = input(":")
        if nickname.isalpha():
            break
        else:
            text.incorrect_input()
    return nickname


def get_age():
    """
    Gets user input for age in correct form
    and returns user information
    """

    print(Fore.YELLOW + "\nPlease enter your age in numbers.\n")
    print("E.g. 21\n")
    while True:
        age = input(":")
        if age.isdigit():
            break
        else:
            text.incorrect_input()
    return age


def user_age():
    """
    Gets the returned value of get age to pass it to
    select topic function
    """
    age_input = get_age()
    return age_input


def get_relationship():
    """
    Gets user input for relationship status in correct form
    and returns user information
    """

    print(Fore.YELLOW + "\nPlease enter your relationship status.\n")
    print("E.g. single, dating, married \n")
    while True:
        relationship = input(":")
        if relationship.isalpha():
            break
        else:
            text.incorrect_input()
    return relationship


def user_relationship():
    """
    Gets the returned value of get relationship to pass it to
    select topic function
    """
    relationship_input = get_relationship()
    return relationship_input


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
            break
        elif answer == "no":
            # ask user if they are sure saying no
            text.user_answer_no()
            text.game_start()
            answer = input(" ").lower()
            if answer == "yes":
                clear_terminal()
                break
            elif answer == "no":
                text.user_answer_final()
                clear_terminal()
                break
            else:
                text.incorrect_input()
        else:
            text.incorrect_input()


game_start()


def get_more_topics():
    """
    Asks user if they want to know more. If answer is yes brings
    them back to select topic. If they answer no, moves on to
    thank you for playing.
    """
    text.know_more()
    while True:
        answer = input(" ").lower()
        if answer == "yes":
            clear_terminal()
            select_topic()
            break
        elif answer == "no":
            # add thank you for playing func
            clear_terminal()
            text.game_end()
            break
        else:
            text.incorrect_input()


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
            clear_terminal()
            while True:
                if int(user_age()) <= 25:
                    text.health_1()
                    get_more_topics()
                    break
                elif int(user_age()) in range(25, 45):
                    text.health_2()
                    get_more_topics()
                    break
                elif int(user_age()) in range(45, 100):
                    text.health_3()
                    get_more_topics()
                    break
                else:
                    pass
            break
        elif topic == "2":
            # add the work prediction
            clear_terminal()
            break
        elif topic == "3":
            # add the Education prediction
            clear_terminal()
            break
        elif topic == "4":
            # add the relationship prediction
            clear_terminal()
            break
        else:
            text.incorrect_input()


select_topic()
