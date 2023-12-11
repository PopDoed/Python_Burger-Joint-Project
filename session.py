# Modules
from user import *
from order import *
from data import *
from display import *
from webAPI import *

class Session:
    """
    Session class allows for multiple orders in one user session
    Also allows for grouping of the processes and objects in a session into one session process
    Makes code more easily expandable
    """
    
    sessionID = 0 # All time number of sessions created

    def __init__(self):
        self._orderNum = 0                                  # Keeps track of the orders within a session

    def getOrderNum(self):                                    # Returns current order number
        return self._orderNum

    def __getUserInfo__(self):                                          # Internal method for gathering user info
        while True:                                                     # Loops until break
            try:
                name = str(input("Please enter your last name: \n"))
                ID = int(input("Please enter your student ID: ( ID < 100 for student, ID >= 100 for teacher)\n"))   # gets name and ID
                
                if name.isalpha() and ID > 0:
                    break                                           # Exits loop if correct inputs are given
                else:
                    raise ValueError                               # This way the program will catch an error for either input with one exception
            except ValueError:
                print("Invalid Input.")
        userInfList = [name, ID]                            # Creates a temporary string of user info to be passed

        if userInfList[1] < 100:                                        # Identifies user as teacher or student
            user = Student(userInfList[0], userInfList[1])
        elif userInfList[1] >= 100:
            user = Teacher(userInfList[0], userInfList[1])
        return user                                                             # Returns user object

    def __orderAsk__(self):                                                # Internal method for asking user if theyd like to make an order
        while True:
            try:
                print()
                if self._orderNum == 0:                                 # Checks if this is the first order of the section
                    print("Would you like to make an order?")
                else:
                    print("Would you like to make another order?")
                y_n = input("'y' = yes, 'n' = no\n")

                if y_n == "y" or "n":                                       # Exits loop if correct input is given
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid input.\n")              # Invalid input catcher
        if y_n == "y":
            self._orderNum += 1                                     # order number incrementer
            return True
        if y_n == "n":
            return False

    def __displayAsk__(self, order, user, session):                         # Internal method for asking user if theyd like to display bill graphically
        while True:
            try:
                print()
                print("Would you like to display your bill in a GUI window?") 
                y_n = input("'y' = yes, 'n' = no\n")

                if y_n == "y" or "n":
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid input.\n")                         # Invalid input catcher

        if y_n == "y":
            display = BillDisplay(order, user, session)                 # Creates bill display object
            display.root.mainloop()                                        # Keeps display on screen until closed
        if y_n == "n":
            return

    def mainLoop(self, session):                                # Main program Loop
        user = session.__getUserInfo__()                    # Gets user info and creates teacher or student object

        ordering = session.__orderAsk__()                    # Asks if the user would like to make an order

        while ordering:                                             # Ordering Loop
            print("Order Number: ", self._orderNum)
            order = Order(session)                                  # Creates an order object
            order.getOrder()                                        # Receives user order
            order.computeBill(user)                                 # Computes necessary bill values

            order.printBill(user)                                   # Prints bill in terminal

            order.writeBillFile(user)                               # Creates a bill text file

            data = Data(session)                                    # Creates a data storing object for the order
            data.dataMaker(order, user)                 # Creates a formatted string with user and order data
            data.dataSaver()                               # Adds user and order data to database

            session.__displayAsk__(order, user, session)        # Asks to display bill visually

            api = webAPI(order, user, session)          # Creates an api object for an order object to easily interact with.
            y_n = api.askToPost()                           # Asks user if they would like to send their data
            api.postData(y_n)                                               # Sends data

            ordering = session.__orderAsk__()                   # Asks user if theyd like to order again

        print("Thanks for coming!")                                         # Goodbye message
