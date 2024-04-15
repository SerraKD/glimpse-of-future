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
    print("4. Relationship \U0001F496")
    time.sleep(2)
    print("\nType the number you selected and press enter.\n")


def know_more():
    """
    After the first prediction, ask user if they want to know more.
    """
    print(Fore.YELLOW + "\nWould you like to know more?\U0001F4AD\n")
    time.sleep(1)
    print('If so, please type in "yes" and press enter.\n')


def not_for_you():
    """
    Informs user that selected topic is not suitable for their age
    """
    print(Fore.YELLOW + "\nThis topic is not suitable for you.\n")
    time.sleep(1)
    print("\nTry to pick another one.\U0001F917\n")
    time.sleep(2)


def game_end():
    """
    Displays end game text
    """
    print(Fore.MAGENTA + "\nIt was a pleasure meeting you.\n")
    time.sleep(1)
    print("\nAnd thank you for letting me take a peek into your future.\n")
    time.sleep(2)
    print("\nBut others need me now, \U0001F9D9\n")
    time.sleep(1)
    print("so I must go.\n")
    time.sleep(1)
    print("We will meet again.\n")
    print("\n \U0001F441 \n")
    time.sleep(3)
    print(Style.RESET_ALL)


# Prediction texts


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


def work_1():
    """
    Work future prediction text for age <=18
    """
    time.sleep(1)
    print(Fore.GREEN + "\nYou have a whole future ahead of you. \U000023F3\n")
    time.sleep(2)
    print("And, a lot of decisions are to be made.\n")
    time.sleep(2)
    print("\nBefore picking your profession, discover yourself.\n")
    time.sleep(1)
    print("Learn your strengths and weaknesses.\n")
    time.sleep(2)
    print("Remember that everyone is unique,\n")
    time.sleep(2)
    print("and decide what you will do with your future based on yourself,\n")
    time.sleep(1)
    print("not others.\n")
    time.sleep(2)


def work_2():
    """
    Work future prediction text for age in range(18, 24)
    """
    time.sleep(1)
    print(Fore.GREEN + "\nDon't worry. \U0001F60C\n")
    time.sleep(2)
    print("This is a difficult time for everyone.\n")
    time.sleep(2)
    print("\nIt's okay if you are not a hundred percent sure\n")
    time.sleep(1)
    print("about the path you have taken.\n")
    time.sleep(2)
    print("Work hard to get the results you want,\n")
    time.sleep(1)
    print("and if you are not pleased with the outcome,\n")
    time.sleep(1)
    print("Remember that change is a part of the life.\n")
    time.sleep(2)


def work_3():
    """
    Work future prediction text for age in range(24, 100)
    """
    time.sleep(1)
    print(Fore.GREEN + "\nI see lots of worries and as-ifs. \U0001F9D0\n")
    time.sleep(2)
    print("I know you are not hearing this enough,\n")
    time.sleep(2)
    print("so let me tell you that you are doing great.\n")
    time.sleep(1)
    print("\nGive yourself some slack, and appreciate your achievements.\n")
    time.sleep(2)
    print("You will get the desired results\n")
    time.sleep(1)
    print("when you continue with the hard work.\n")
    time.sleep(2)


def education_1():
    """
    Education future prediction text for age <=18
    """
    time.sleep(1)
    print(Fore.GREEN + "\nWorry less about the achievements \U0001F939\n")
    time.sleep(2)
    print("and try to focus on what needs to be done.\n")
    time.sleep(2)
    print("\nPlease don't compare yourself to others,\n")
    time.sleep(1)
    print("only get inspired by them.\n")
    time.sleep(2)
    print("Your grades do not determine your value,\n")
    time.sleep(1)
    print("your actions do.\n")
    time.sleep(2)
    print("Do your best, and you will fulfill your dreams.\n")
    time.sleep(2)


def education_2():
    """
    Education future prediction text for age in range(18, 24)
    """
    time.sleep(1)
    print(Fore.GREEN + "\nBig changes are ahead of you! \U0001F3C3\n")
    time.sleep(2)
    print("It's okay if you are anxious about what's to come.\n")
    time.sleep(2)
    print("\nYou are not alone in this journey!\n")
    time.sleep(2)
    print("I see great friendships will be made.\n")
    time.sleep(1)
    print("And you will learn a lot about yourself.\n")
    time.sleep(1)
    print("Things might get difficult, but you will persevere.\n")
    time.sleep(2)


def education_3():
    """
    Education future prediction text for age in range(24, 100)
    """
    time.sleep(1)
    print(Fore.GREEN + "\nLearning doesn't stop at a particular age.\n")
    time.sleep(2)
    print("And you are no exception to that fact! \U0001F481\n")
    time.sleep(2)
    print("\nThis is the best time to finally take a step and\n")
    time.sleep(1)
    print("study that subject you always wanted.\n")
    time.sleep(2)
    print("You might be surprised how great it will turn out\n")
    time.sleep(2)


def relationship_1():
    """
    Relationship future prediction text for age in range(15, 19) and single
    #https://childmind.org/article/how-to-help-kids-have-good-romantic-relationships/
    """
    time.sleep(1)
    print(Fore.GREEN + "\nYou should love yourself first, \U0001FAC0\n")
    time.sleep(2)
    print("and be your own person.\n")
    time.sleep(2)
    print("\nThere will be someone who loves you just the way you are.\n")
    time.sleep(1)
    print("That is the kind of person you want to be with.\n")
    time.sleep(2)
    print("Your friends are as important as your date,\n")
    time.sleep(1)
    print("don't take them for granted.\n")
    time.sleep(2)


def relationship_2():
    """
    Relationship future prediction text for age in range(15, 19) and dating
    #https://childmind.org/article/how-to-help-kids-have-good-romantic-relationships/
    """
    time.sleep(1)
    print(Fore.GREEN + "\nI see that you and your partner\n")
    time.sleep(1)
    print("love each other very much. \U0001F525\n")
    time.sleep(2)
    print("\nBeing your own person is an important\n")
    time.sleep(1)
    print("part of a happy relationship.\n")
    time.sleep(2)
    print("So as not to hide from problems.\n")
    time.sleep(1)
    print("I foresee little arguments here and there.\n")
    time.sleep(2)
    print("Talk to each other about your feelings and needs.\n")
    time.sleep(2)


def relationship_3():
    """
    Relationship future prediction text for age range(19, 45) and single
    """
    time.sleep(1)
    print(Fore.GREEN + "\nI foresee love is on the corner \U0001F496\n")
    time.sleep(2)
    print("You are just not paying attention.\n")
    time.sleep(2)
    print("\nThere is a person who is deeply interested in you,\n")
    time.sleep(1)
    print("although it may not look like that sometimes.\n")
    time.sleep(2)
    print("Give it time and have patience.\n")
    time.sleep(2)


def relationship_4():
    """
    Relationship future prediction text for age range(19, 45) and dating
    """
    time.sleep(1)
    print(Fore.GREEN + "\nI see that you and your partner\n")
    time.sleep(2)
    print("love each other very much. \U0001F525\n")
    time.sleep(2)
    print("\nDon't let small arguments become a bigger issue.\n")
    time.sleep(2)
    print("Learn how to talk to each other effectively and,\n")
    time.sleep(2)
    print("try to be understanding of your partner's feelings and needs.\n")
    time.sleep(2)
    print("I foresee a great future for both of you.\n")
    time.sleep(2)


def relationship_5():
    """
    Relationship future prediction text for age range(19, 45) and married
    """
    time.sleep(1)
    print(Fore.GREEN + "\nI think you will agree with me, when I say,\n")
    time.sleep(2)
    print("marriage is not always easy. \U0001F9D0\n")
    time.sleep(2)
    print("\nJust like other good things in life,\n")
    time.sleep(1)
    print("you need to put in the work. \n")
    time.sleep(2)
    print("Arguments and disagreements are part of being human,\n")
    time.sleep(1)
    print("And you will have your fair share of them.\n")
    time.sleep(2)
    print("Communicate, pay attention, and understand each other.\n")
    time.sleep(2)


def relationship_6():
    """
    Relationship future prediction text for age range(45, 100) and single
    """
    time.sleep(1)
    print(Fore.GREEN + "\nHmm.. A curious choice for you. \U0001F914\n")
    time.sleep(2)
    print("I see that you worry about dating.\n")
    time.sleep(2)
    print("\nTake this time in your life to get to know your new self,\n")
    time.sleep(1)
    print("do things you always wanted to do, and explore.\n")
    time.sleep(2)
    print("Love will knock on your door when you least expect it.\n")
    time.sleep(2)


def relationship_7():
    """
    Relationship future prediction text for age range(45, 100) and dating
    """
    time.sleep(1)
    print(Fore.GREEN + "\nI see you two are great together.\U0001F970\n")
    time.sleep(2)
    print("You know that relationships are hard work,\n")
    time.sleep(2)
    print("and to get results you have to put in an effort.\n")
    time.sleep(1)
    print("I foresee a minor disagreement between you and your partner,\n")
    time.sleep(2)
    print("to sort it out try to be understanding of their point of view.\n")
    time.sleep(2)


def relationship_8():
    """
    Relationship future prediction text for age range(45, 100) and married
    """
    time.sleep(1)
    print(Fore.GREEN + "\nI think you will agree with me, when I say,\n")
    time.sleep(1)
    print("that marriage is not always easy. \U0001F9D0\n")
    time.sleep(1)
    print("But you have already overcome many roadblocks.\n")
    time.sleep(2)
    print("After some time, people often forget\n")
    time.sleep(1)
    print("how important the positive feedback is.\n")
    time.sleep(2)
    print("Try to remind your partner that\n")
    time.sleep(1)
    print("their companionship is very much appreciated.\n")
    time.sleep(2)
