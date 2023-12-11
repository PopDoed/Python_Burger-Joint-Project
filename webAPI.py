# Libraries
import requests

# Modules
from order import *
from user import *

class webAPI: 
    """
    webAPI class allows for easy interaction between objects and the api through user defined methods.
    """
    
    def __init__(self, order, user, session):
        self._url = "https://www.w3schools.com/python/demopage.php"   # API URL
        
        self._orderNum = session.getOrderNum()          # Keeps track of the order the data is related to 
        
        self._orderData = {                                             # Dict of Data
            "Order Number" : self._orderNum, 
            "CustomerID" : user.getID(), 
            "Customer Name": user.getName(),
            "Item Count" : order.getItemCount(),
            "Total" : order.getTotal(),
        }


    def askToPost(self):                            # Asks user if theyd like to send in their data
        while True:
            try:
                print("Would you like to send your data to the provided url? : https://www.w3schools.com/python/demopage.php")
                y_n = input("'y' = yes, 'n' = no\n")

                if y_n == "y" or "n":
                    break
                else:
                    raise ValueError
            except ValueError:                                      # Catches invalid inputs
                print("Please enter a valid input.\n")    
        return y_n                                                     # Passes choice
           
                
    def postData(self, y_n):                                        # Takes choice and posts data, does nothing if choice is no
        if y_n == "y" :
            try:
                response = requests.post(self._url, json = self._orderData)    # Attempts to send data 
                response.raise_for_status()
                print("Order successfully submitted to the web API.")
            except requests.exceptions.RequestException as e:                   # Error message if data is unable to be sent for whatever reason.
                print(f"Error submitting order to the web API: {e}")
        else:
            return
            