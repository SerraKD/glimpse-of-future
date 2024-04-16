# Glimpse of the Future

The Glimpse of the Future is a Python based text game, deployed with a mock terminal provided by Code Institute, using Heroku.

The main inspirations for this game are Fortune Tellers and Magic 8 ball.

There are four different topics users can select to get predictions: Health, Work, Education, and Relationship. The game requires the user's age and relationship status to provide relevant future predictions. Depending on the collected data, a prediction is displayed and users are given a chance to select another topic. If the user chooses not to continue playing, the game asks for the user's nickname and farewell the user with the input provided.

[Visit the deployed version](https://glimpse-of-future-18938565c6a2.herokuapp.com/)

![Image of welcome screen]()

## Table Of Contents

- [Glimpse of the Future](#glimpse-of-the-future)
- [Planning](#planning)
  - [Flow Chart](#flow-chart)
  - [User Experience (UX)](#user-experience-ux)
- [How To Play](#how-to-play)
- [Features](#features)

  - [Existing Features](#existing-features)

    - [Welcome Screen](#welcome-screen)
    - [Select Topic Screen](#select-topic-screen)
    - [User Input](#user-input)
      - [Age](#age)
      - [Nickname](#nickname)
      - [Relatonship Status](#relatonship-status)
    - [Future Predictions](#future-predictions)

      - [Health Predictions](#health-predictions)
      - [Work Predictions](#work-predictions)
      - [Education Predictions](#education-predictions)
      - [Relationship Predictions](#relationship-predictions)

    - [Game End](#game-end)

  - [Future Enhancements](#future-enhancements)

- [Data Model](#data-model)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Validator Testing](#validator-testing)
  - [Fixed Bugs](#fixed-bugs)
  - [Remaining Bugs](#remaining-bugs)
- [Deployment](#deployment)
- [Deployment to Heroku](#deployment-to-heroku)
- [Libraries](#libraries)
  - [os](#os)
  - [time](#time)
  - [colorama](#colorama)
- [Emoji](#emoji)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

# Planning

## Flow Chart

In the planning stage, I used [LucidChart](https://www.lucidchart.com/pages/) to create main logic flow of the game. The final version of the application has a few differences, such as when the game asks for user input or how the game reacts to those inputs. I mentioned it in more detail in the [User Input](#user-input) section.

![Image of Flow Chart]()

## User Experience (UX)

### Site Goals

- Give clear instructions about how to play the game.
- Get and validate the input appropriately.
- Create curiosity with the intro to get users' attention.
- Play the game smoothly and effortlessly.
- Provide future predictions that feel particular to the user.

### Target Audiences

- Individuals who have interest in fortune tellers.
- Individuals who are at the age to have an interest in provided topics.

### User Stories

As a user, i want to;

- Have a clear understanding of how to play the game.
- Get direct instructions for the inputs.
- Get predictions that are suitable for my personal details.
- Have a smooth experience.

# How To Play

1. After the welcome text, to start playing, type yes and enter after the "Are you ready?" question.
2. Four different topics for predictions will be provided, pick one topic and enter the number you selected.
3. Depending on the selected topic, game will ask for inputs like age and relationship status. Correctly enter the answer as shown as in examples and press enter.
4. After the prediction text, the game will proceed with the " Would you like to know more?" question. If the answer is yes, repeat the second and third steps.
5. If the answer is no, the game will ask an input for a nickname, and proceed to the goodbye text.

# Features

## Existing Features

### Welcome Screen

Welcome text greets the user, explains the game, and gives clear instructions for how to play.

![Image of welcome screen]()

" Please wait for a prompt to input a message. " is specially added to the welcome text to inform users at the beginning of the game.

After welcoming, the game asks the user if they are ready. If the user answers yes, the game proceeds to the Select topic screen.

![Image of are you ready text]()

If the user answers no, the game gives user a second chance. If the answer is again no, the game proceeds to say goodbye.

Any invalid input returns an error message and asks to try again.

![Image of goodbye text]()

### Select Topic Screen

Provides list of available topics to get future predictions.

![Image of topics text]()

The first three topics require users to input their age, fourth topic requires both age and relationship status.

After selecting and entering the topic number, the game proceeds to get the user input.

### User Input

Depending on the selected topic, the game asks user input for age and relationship status.

Any invalid input returns an error message and asks to try again.

![Image of invalid input text]()

> In the flow chart, all user inputs are asked right after the welcome text. While writing the code I changed that into asking the input whenever it was needed because it logically made more sense and seemed more suitable to the game.

#### Age

Age input is requested for all topics.

![Image of age input text]()

#### Nickname

The game requests for a nickname after getting the prediction and saying no to Would you like to know more question.
The reason for this is to give the user a feeling more of a personal and life-like experience.

![Image of nickname input text]()

#### Relatonship Status

The game requests for relationship input only if the user selects the Relationship topic to provide an accurate prediction.

![Image of age and relationship input text]()

### Future Predictions

Every topic has multiple predictions and displays a text depending on the collected user data.

#### Health Predictions

Has three different texts:

1. For age <= 25
2. For age between 25 and 45
3. For age between 45 and 100

![Image of health1 text]()

> Any age that is not described as above range falls into the not-for-you category, inform users that this topic is not suitable for them.

![Image of not-for-you text]()

#### Work Predictions

Has three different texts:

1. For age <= 18
2. For age between 18 and 24
3. For age between 24 and 100

![Image of work2 text]()

> Any age that is not described as above range falls into the not-for-you category, inform users that this topic is not suitable for them.

![Image not-for-you text]()

#### Education Predictions

Has three different texts:

1. For age < 18
2. For age between 18 and 24
3. For age between 24 and 100

![Image of education1 text]()

> Any age that is not described as above range falls into the not-for-you category, inform users that this topic is not suitable for them.

![Image not-for-you text]()

#### Relationship Predictions

Has eight different texts:

1. For age between 15 and 19, single
2. For age between 15 and 19, dating
3. For age between 19 and 45, single
4. For age between 19 and 45, dating
5. For age between 19 and 45, married
6. For age between 45 and 100, single
7. For age between 45 and 100, dating
8. For age between 45 and 100, married

![Image of relationship2 text]()

> Any age that is not described as above range falls into the not-for-you category, inform users that this topic is not suitable for them.

![Image not-for-you text]()

### Game End

After the user says no to the "Would you like to learn more" question, the game proceeds to get the user's nickname and a goodbye text.

![Image game end text]()

## Future Enhancements

In the future, I would like to use the User class to save user data to the system and allow users to have accounts.

I would like to get additional user data like gender, and interests, and create enhanced future predictions to give more detailed and personalized future predictions.

# Data Model

> In the beginning, I created a one big nested loop the get all user inputs. Even though it functioned, it became too complex and difficult to read, so I separated it into three different functions age, nickname, and relationship.
> Later on, Because all three functions were getting and returning user data, I created a Class for User and added the functions as methods into the class.

# Testing

## Manual Testing

## Validator Testing

## Fixed Bugs

> 1. " Make get age functions return value integer to avoid repetition" [main d7117d8]

- Otherwise i had to repeat in select topic function loops.

> 2. " Fix the typo in topics function in text.py" [main 3daa1a5]

- I called relationship topic number 3. Would confuse the user when selecting a topic. I fixed the text as 4.

> 3. " Fix the function call for age in select topic, use returned value instead" [main a7eb663]

- I was calling the user_age() function in the if and all the elif blocks in select_topic. So function was being called again for each check. I called the function once and stored the return value. (Credits John from Tutor Assistance)

> 4. " Fix the age range for relationships in select topic function" [main bfaa4cc]

- There was a gap in if-elif loops for age, making it miss a couple of age ranges. I fixed the error by rearranging the range.

> 5. " Fix the code for get relationship functions user input validation by adding list" [main d4a2c7c]

- The get relationship function was validating user input by checking if the entered answer is alphabetical. By adding a list of accepted answers in the if loop I ensured that only the correct answer will make the game proceed.

> 6. " Fix the code for game start function, rearrange the calling of the select topic and game start functions" [main c48881b]

- Because of the calling of the select topic function, even if the user says no to continue playing game was proceeding with giving the user options to select a topic. By moving the game start function under the select topic function I managed to prevent unwanted loops. I also added another while true to to nested loop to make sure the function behaves as expected.

> 7. " Add style bright to texts in text.py" [main 96cfb72]

- There was a bug in Heroku causing the colorama text colors to seem darker than the terminal in Gitpod. I added a bright style to ensure that the text is easily readable.

> 8. " Refactor all if else statements with Pylint in run.py" [main 4663398]

- Because all if-else statemens had breaks, I removed unnecessary elif and else statements for cleaner code.

> 9. " Fix the code for game start function, make input validation work correctly" [main ae5d6bc]

- After adding changes to if-else statements with Pylint, I found a new bug in the game start functions input validation. When a user enters incorrect answer, it creates an infinite loop. By removing the secondary while statement, adding the else statement, and correcting the indentation I fixed the error.

## Remaining Bugs

- Users can input a message before the prompt.

Unfortunately, I couldn't work on this bug but I added an exclusive text to the welcome screen to inform the user to wait for a prompt.

![Image of wait for a prompt to input text]()

# Deployment

I used [Gitpod](https://gitpod.io/) to develop this website.

I deployed the website in early stages of develepment on [GitHub](https://github.com/) with following steps;

1. Log in to Github and go to projects' repository.
2. Find the Settings on the top of the repository and click.
3. On the left side of the screen, find Pages and select.
4. Under the Branch section, click on the dropdown that says none, and pick "Main" and click on save button.
5. The page is now deployed.

# Deployment to Heroku

# Libraries

## os

- os used to clear text in terminal.

- https://docs.python.org/3/library/os.html

## time

- Time is used to add delays to texts.

- https://www.geeksforgeeks.org/sleep-in-python/?ref=lbp

## colorama

- Colorama Fore and Style is used to add different colors to text in terminal.

- https://pypi.org/project/colorama/

# Emoji

- Emojis are used to make texts more interesting and give users a fun experience.

- Importing emoji was not necessary because I used Unicodes.

- Unicodes taken from : https://unicode.org/emoji/charts/full-emoji-list.html

- https://pypi.org/project/emoji/

# Credits

- All content is written by me.
- https://childmind.org/article/how-to-help-kids-have-good-romantic-relationships/ Used as a reference to create appropriate relationship advice for teens.
- [LucidChart](https://www.lucidchart.com/pages/) used to create game flow chart.
- [Grammarly](https://app.grammarly.com/) Used to check the grammar of all text content.
- [Tiny PNG](https://tinypng.com/) used for file compression.
- [CI Python Linter](https://pep8ci.herokuapp.com/) used for validator testing.
- The Heroku mock terminal is provided by [Code Institute](https://codeinstitute.net/global/).
- Clear terminal function is taken from https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python

  > Below documents and sites were used as study and reference material.

- https://www.geeksforgeeks.org/print-colors-python-terminal/
- https://www.geeksforgeeks.org/python-program-to-print-emojis/
- https://www.geeksforgeeks.org/python-check-if-given-string-is-numeric-or-not/?ref=header_search
- https://stackoverflow.com/questions/74662334/using-user-input-function-in-classes
- https://www.tutorialspoint.com/how-do-i-call-a-variable-from-another-function-in-python#:~:text=To%20summarize%2C%20when%20it%20comes,requirements%20of%20the%20specific%20scenario.
- https://www.geeksforgeeks.org/python-string-lower/?ref=header_search

# Acknowledgements

- I am deeply grateful to my Mentor Rory Patrick Sheridan, for his invaluable guidance, support, and great tips.
- Special thanks to John from Tutor Assistance for his help and great explanation.
