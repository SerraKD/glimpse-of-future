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

> In the beginning, I created a one big nested loop the get all user inputs. Even though it functioned, it became too complex and difficult to read, so I separated it into three different functions age, nickname, and relationship.
> Later on, Because all three functions were getting and returning user data, I created a Class for User and added the functions as methods into the class.

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

# Testing

## Manual Testing

## Validator Testing

## Fixed Bugs

## Remaining Bugs

# Deployment

# Deployment to Heroku

# Libraries

## os

## time

## colorama

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
- https://pypi.org/project/colorama/
- https://pypi.org/project/emoji/
- https://www.geeksforgeeks.org/python-program-to-print-emojis/
- https://unicode.org/emoji/charts/full-emoji-list.html
- https://www.geeksforgeeks.org/python-time-module/
- https://www.geeksforgeeks.org/python-check-if-given-string-is-numeric-or-not/?ref=header_search
- https://stackoverflow.com/questions/74662334/using-user-input-function-in-classes
- https://www.tutorialspoint.com/how-do-i-call-a-variable-from-another-function-in-python#:~:text=To%20summarize%2C%20when%20it%20comes,requirements%20of%20the%20specific%20scenario.
- https://www.geeksforgeeks.org/python-string-lower/?ref=header_search

# Acknowledgements
