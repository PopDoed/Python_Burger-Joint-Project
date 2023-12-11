# Daniel Morgan

# Object-Oriented burger joint ordering system.
"""
Everything is formatted in a way that the program could be easily expanded and that data from any piece of the program could be easily manipulated and stored!
    For example:
        One possible expansion would be to store user and session data.
        Then you could have an account system and the user wouldnt have to re-enter their name and ID everytime a session is created
"""

# Modules
from user import *
from order import *
from data import *
from display import *
from webAPI import *
from session import *


def sessionStart():  # Main program loop starting function (Either makes a new session or does nothing)
    print("Welcome to Burger Hut!")
    while True:
        print("Would you like to start a user session?")
        y_n = input("'y' = yes, 'n' = no\n")
        try:
            if y_n == "y" or "n":
                break
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid input.\n")

    if y_n == "y":
        Session().sessionID += 1  # incrememnts session number
        return Session()  # Returns a session object reference to be put into a variable
    else:
        return None  # Creates no session if user doesnt want one.


if __name__ == "__main__":
    session = sessionStart()  # Session creating function

    if (
        session != None
    ):  # if a session exists start the main program loop, if no session was created, program terminates.
        session.mainLoop(session)
    else:
        print("Thanks for coming!")  # Goodbye message
