"""
Imports:
os imported for clearing the terminal
https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python
time imported to add time delays for print statements
https://realpython.com/python-sleep/
"""
import os
import time
import colorama
import emoji
import text

text.welcome()


def game_start():
    """
    After the welcome message, asks user if they want to play the game.
    Checks the user answer if entered in correct method.
    If answer is yes, moves on to picking a topic to get future predictions.
    If user answers no, takes user back to welcome message.
    """
    text.game_start()

    while True:
        answer = input(": ")
        if answer == "yes":
            """#create function to continue with picking topic"""
        elif answer == "no":
            """#create function to ask again if they are sure"""
        else:
            """#take back to welcome"""


print(game_start())
