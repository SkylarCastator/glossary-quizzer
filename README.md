# Glossary Quizzer

## Introduction

One of the hardest things I struggle with because of my dyslexia is remembering words and using them in the correct context. This is known as rapid naming deficit.


"Rapid Naming Deficit: This type of dyslexia is associated with  difficulties in quickly naming or retrieving familiar objects, colors,  or letters. People with rapid naming deficit may have slower word  retrieval and face challenges in reading fluently."


 I have been doing a lot of studying recently and one thing I really wanted to maintain as I work through a bunch of new information is to keep communication about these subjects at the front of my mind. 

There are several ways to practice this, either memory palaces, flash cards ect. What I wanted to do was to make a simple application to help me maintain these list of items and a way to test myself against what I know and what I don't know. 


## Installing the Project

First visit the GitHub page to be able to copy the project.

https://github.com/SkylarCastator/glossary-quizzer 


This project runs in python so make sure you have python installed and pip installed on your machine. This application currently only runs on Mac and Linux. (Windows coming soon)
Install the requirements file by using your terminal.

Run the command:

pip3 install -r requirements.txt

Once that is completed that is all you should need to do. Launch the application by running:

python3 main.py



## Main Menu

Launching the application you will find yourself seeing this menu:

You can start a quiz. These are quiz's that are saved with the project initially. The project currently contains:

    Computer Graphics

    Artificial Intelligence

    Computer Science

I will add more saved quiz's in the future, or you can add your own. The option above showing "Load Quiz", asks the user to enter a URL of Wikipedia glossary page.

Example: https://en.wikipedia.org/wiki/Glossary_of_aerospace_engineering

The application is designed to be able to read these types of pages and then create a quiz data file from the content on the page. Once the data file is created, it can now be found in the "Start Quiz" menu.



## The Quiz

When you launch a quiz the interface will first show you the quiz name and the number of vocab words for the quiz. Currently the quiz contains all of the vocab words from the Wikipedia page. In future releases, you will be able to thin them down to smaller bites.
The Quiz will then start to prompt the user using a definition. The user will select between multiple options and find out if they have the correct answer or not. 


After each question the user is asked if they want to continue or quit. Press continue to keep going with the quizzing, if you quit, the quiz is saved and you can come back and pick it up where you left off. It also contains all of the users correct and incorrect answers to be reviewed at a later date. You can resume a quiz using the main menu option "Resume Quiz". If you wish to restart the quiz, just use the start quiz option and start over from scratch.

Once you have completed the quiz, you will get the final results shown to you including the path of the JSON file listing all the answers you got correct or incorrect.




## Conclusion

Hopefully others will find this application as useful as I do. I made it quite quickly to help improve my studying and simplify the process for creating the question/ answer interface that comes with writing flash cards. There are several things to still fix and improve so feel free to add comments and create a PR in the GitHub repository:

https://github.com/SkylarCastator/glossary-quizzer

Finally, remember pure memorization can't replace using the information in a instrumental way. This is only one part of the learning process and is not a substitute for  experimentation and self learning.

