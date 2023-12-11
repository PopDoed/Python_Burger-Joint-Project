# Libraries
from sqlite3 import *

# Modules
from user import *
from order import *


class Data:
    """
    Allows for easy grouping and manipulation of order related data through user Interface
    Takes order data and transfers it into a database
    """
    def __init__(self, session):                        # Connects to the database and then
        self._conn = connect("orders.db")
        self._cursor = self._conn.cursor()

        self._orderNum = session.getOrderNum()
        self._dataString = ""                   # Empty data string for data values to be concatenated into

        try:                                         # Creates the data table if one does not already exist
            self._cursor.execute(
                """
                                CREATE TABLE orders
                                (name text, id real, itemcount real, total real)
                                """
            )
        except OperationalError:                   # if table exists already program moves on
            pass

    def dataMaker(self, order, user):       # Formats data for insertion into database
        valueList = [                  # List of recorded data values
            str(user.getName()),            
            str(user.getID()),
            str(order.getItemCount()),
            str(order.getTotal()),
        ]

        for value in valueList:  # Iterates through list of formatted data values concatenating them to the empty string
            self._dataString += value     
            self._dataString += ", "


    def dataSaver(self):
        commandString = "INSERT INTO orders VALUES (?, ?, ?, ?)"  # Placeholder format
        values = tuple(self._dataString.split(", ")[:-1])               # Convert the string to a tuple

        self._cursor.execute(commandString, values)  # Executes command string with inserted tuple of values
        self._conn.commit()  # Commits changes
        self._conn.close()

