# Modules
from menu import *
from user import *

class Order:
    """
    order class allows for grouping of order related data 
    contains ordering related proccesses and main functions of the program
    """
    def __init__(self, session):
        self._total = 0.0                               # Total price of order
        self._tax = 0.0                                 # Tax to be applied
        self._itemCount = 0                             # Number of individual items in order
        self._itemList = []                             # Container for menu item objects in the order
        self._orderNum = session.getOrderNum()          # Assigns order number

    def __showMenu__(self):                             # Internal method for showing the menu
        print("=======MENU=======")
        print("1. De Anza Burger $5.25")
        print("2. Bacon Cheese $5.75")
        print("3. Mushroom Swiss $5.95")
        print("4. Western Burger $5.95")
        print("5. Don Cali Burger $5.95")
        print("6. Exit\n")

    def __addItem__(self, itemID, itemQuant):           # Internal method for adding a menu item object to the itemlist container
        item = Menu_Item(itemID, itemQuant)
        self._itemList.append(item)

    def getItemList(self):                              # returns itemlist container 
        return self._itemList 

    def getTotal(self):                                 # returns total price
        return self._total

    def getItemCount(self):                             # returns item count
        return self._itemCount

    def getOrder(self):                                                                 # Ordering Proccess function
        self.__showMenu__()                                                                 # Shows the menu
        while True:                                                                         # Loops until break
            try:
                itemID = int(input("Enter the item number of the burger you want (1-5), or 6 to exit:\n")) # Collects itemID of menu item and converts to integer
                if itemID == 6:                                                                 # Checks for exit
                    print()
                    break
                elif itemID < 1 or itemID > 6:                                          # Checks if input is within range of IDs
                    print("Invalid choice. Please select a valid option (1-5), or 6 to exit.")
                    continue
                itemQuant = int(input(f"How many of option {itemID} do you want?\n"))           # Asks for item quantity and stores it in itemQuant variable
                print()
                self.__addItem__(itemID, itemQuant)                                            # Adds menu item object 
            except ValueError:
                print("Invalid input.")

    def computeBill(self, user):                                                # Bill computing Function
        if len(self._itemList) > 0:                                             # Checks if items are in the list
            for item in self._itemList:                                         # iterates through list
                self._itemCount += item.getQuantity()                           # increments itemCount by the quantity of items in the menu item object 
                self._total += item.getPrice() * item.getQuantity()             # Calculates the pre tax total 
            self._total += self._total * user.getTax()                          # Calculates post tax total 

    def printBill(self, user):                                                  # Bill printing function
        print("=======Receipt=======")                                          # Prints necessary bill information
        print("Customer Name:", user.getName())
        print("Customer ID:", str(user.getID()), "\n")

        if len(self._itemList) > 0:                                             # Iterates through itemList
            for item in self._itemList:                                         
                print(                                                          # Prints the name, quantity, and price of each menu item object
                    item.getName(),
                    " x",
                    str(item.getQuantity()),
                    " | ",
                    "$" + str(item.getPrice() * item.getQuantity()),
                )
            print()
            print("Tax Percentage:", str(int(user.getTax() * 100)) + "%")       # Prints the users applied tax percentage
            print("Total + Tax: ", "$" + str(round(self._total)))               # Prints the users total
        else:
            print("You ordered nothing!")

    def writeBillFile(self, user):                                              # The same as the print bill function except writes the data into a text file rather than printing it.
        billfile = open("bill.txt", "w")
        billfile.write("=======Receipt=======\n")
        billfile.write("Customer Name: " + user.getName() + "\n")
        billfile.write("Customer ID: " + str(user.getID()) + "\n" + "\n")

        if len(self._itemList) > 0:
            for item in self._itemList:
                billfile.write(
                    item.getName()
                    + " x"
                    + str(item.getQuantity())
                    + " | "
                    + "$"
                    + str(item.getPrice() * item.getQuantity())
                    + "\n"
                )
            billfile.write("\n")
            billfile.write(
                "Tax Percentage: " + str(int(user.getTax() * 100)) + "%" + "\n"
            )
            billfile.write("Total + Tax: " + "$" + str(round(self._total)) + "\n")
        else:
            billfile.write("You ordered nothing!")

        billfile.close()
