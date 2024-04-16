"""
Imports
"""
import os
from colorama import Fore
import text


def clear_terminal():
    """
    os.system terminal cleaning fuction, clears text in terminal.
    referance:
    https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python
    """
    os.system('cls' if os.name == 'nt' else 'clear')


class User():
    """
    Creates an instance of user
    """
    name = " "
    age = 0
    relationship = " "

    def get_nickname(self):
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
            text.incorrect_input()
        self.name = nickname
        return self.name

    def get_age(self):
        """
        Gets user input for age in correct form
        and returns user information
        """
        print(Fore.YELLOW + "\nPlease enter your age in numbers.\n")
        print("E.g. 21\n")
        while True:
            userage = input(":")
            if userage.isdigit():
                break
            text.incorrect_input()
        self.age = userage
        return self.age

    def get_relationship(self):
        """
        Gets user input for relationship status in correct form
        and returns user information
        """
        print(Fore.YELLOW + "\nPlease enter your relationship status.\n")
        print("E.g. single, dating, married \n")
        while True:
            userrel = input(":")
            if userrel in ["single", "dating", "married"]:
                break
            text.incorrect_input()
        self.relationship = userrel
        return self.relationship


def user_nickname():
    """
    Gets the returned value of get nickname to pass it to
    end game function
    """
    User.get_nickname(User)
    return User.name


def user_age():
    """
    Gets the returned value of get age to pass it to
    select topic function
    """
    User.get_age(User)
    return int(User.age)


def user_rel():
    """
    Gets the returned value of get relationship to pass it to
    select topic function
    """
    User.get_relationship(User)
    return User.relationship


def health_predictions():
    """
    Depending on the collected user data a health prediction will be displayed.
    """
    clear_terminal()
    User.age = user_age()
    while True:
        if User.age <= 25:
            text.health_1()
            get_more_topics()
            break
        if User.age in range(25, 45):
            text.health_2()
            get_more_topics()
            break
        if User.age in range(45, 100):
            text.health_3()
            get_more_topics()
            break
        text.not_for_you()
        get_more_topics()
        break


def work_predictions():
    """
    Depending on the collected user data a work prediction will be displayed.
    """
    clear_terminal()
    User.age = user_age()
    while True:
        if User.age <= 18:
            text.work_1()
            get_more_topics()
            break
        if User.age in range(18, 24):
            text.work_2()
            get_more_topics()
            break
        if User.age in range(24, 100):
            text.work_3()
            get_more_topics()
            break
        text.not_for_you()
        get_more_topics()
        break


def education_predictions():
    """
    Depending on the collected user data an education
    prediction will be displayed.
    """
    clear_terminal()
    User.age = user_age()
    while True:
        if User.age < 18:
            text.education_1()
            get_more_topics()
            break
        if User.age in range(18, 24):
            text.education_2()
            get_more_topics()
            break
        if User.age in range(24, 100):
            text.education_3()
            get_more_topics()
            break
        text.not_for_you()
        get_more_topics()
        break


def relationship_predictions():
    """
    Depending on the collected user data a relationship
    prediction will be displayed.
    """
    clear_terminal()
    User.relationship = user_rel()
    User.age = user_age()
    while True:
        if User.age in range(15, 19) and User.relationship == "single":
            text.relationship_1()
            get_more_topics()
            break
        if User.age in range(15, 19) and User.relationship == "dating":
            text.relationship_2()
            get_more_topics()
            break
        if User.age in range(19, 45) and User.relationship == "single":
            text.relationship_3()
            get_more_topics()
            break
        if User.age in range(19, 45) and User.relationship == "dating":
            text.relationship_4()
            get_more_topics()
            break
        if User.age in range(19, 45) and User.relationship == "married":
            text.relationship_5()
            get_more_topics()
            break
        if User.age in range(45, 100) and User.relationship == "single":
            text.relationship_6()
            get_more_topics()
            break
        if User.age in range(45, 100) and User.relationship == "dating":
            text.relationship_7()
            get_more_topics()
            break
        if User.age in range(45, 100) and User.relationship == "married":
            text.relationship_8()
            get_more_topics()
            break
        text.not_for_you()
        get_more_topics()
        break


def select_topic():
    """
    Allows user to select a topic from 4 topics provided
    to get future predictions.
    """
    clear_terminal()

    text.topics()
    while True:
        topic = input(" ")
        if topic == "1":
            health_predictions()
            break
        if topic == "2":
            work_predictions()
            break
        if topic == "3":
            education_predictions()
            break
        if topic == "4":
            relationship_predictions()
            break
        text.incorrect_input()


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
        if answer == "no":
            User.name = user_nickname()
            clear_terminal()
            print(f'{User.name},')
            text.game_end()
            break
        text.incorrect_input()


def game_start():
    """
    After the welcome message, asks user if they want to play the game.
    Checks the user answer if entered in correct method. If answer is yes,
    moves on to selecting a topic. If user answers no, asks user if they
    are sure. Again if answer is no, finish game.
    """
    text.game_start()
    while True:
        answer = input(" ").lower()
        if answer == "yes":
            clear_terminal()
            select_topic()
            break
        if answer == "no":
            text.user_answer_no()
            text.game_start()
            answer = input(" ").lower()
            if answer == "yes":
                clear_terminal()
                select_topic()
                break
            if answer == "no":
                text.user_answer_final()
                clear_terminal()
                break
            text.incorrect_input()
        else:
            text.incorrect_input()


if __name__ == "__main__":
    text.welcome()
    game_start()
