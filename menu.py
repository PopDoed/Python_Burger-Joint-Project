class Menu_Item:
    """
    Class for Menu Items
    Allows for the creation of item objects to be added to the order
    Item object has dicts for the price and item name associated with each itemID
    Also takes an itemQuantity argument with a default value of for multiple orders of the same item.
    """
    def __init__(self, itemID, itemQuant = 1):
        self._itemNameDict = {1 : "De Anza Burger",
                              2 : "Bacon Cheese Burger",
                              3 : "Mushroom Swiss Burger",
                              4 : "Western Burger",
                              5 : "Don Cali Burger"
                              }
        self._itemPriceDict = {1 : 5.25,
                               2 : 5.75,
                               3 : 5.95, 
                               4 : 5.95,
                               5 : 5.95
                               }
        self._id = itemID
        self._quantity = itemQuant
    
    def getItemID(self):
        return self._id
    
    def getName(self):
        return self._itemNameDict[self._id]
    
    def getPrice(self):
        return self._itemPriceDict[self._id]
    
    def getQuantity(self):
        return self._quantity     