# Library
import tkinter as tk

class BillDisplay:
    """
    Display class allows the use of a seperate public interface from the order class. 
    This gives further visual organization and distinction from other methods of showing the bill that dont use the tkinter module
    The functionality of the class is encapsulated entirely within the __init__() function. since working with tkinter in this way was easier for me to figure out and manage.
    """
    def __init__(self, order, user, session): 
        self._orderNum = session.getOrderNum() # Assigns order number for the bill object to be related to

        self.order = order                          # creates an instance variable reference to the order object for simplification purposes
        self.user = user                            # creates an instance variable reference to the user object for simplification purposes

        self.root = tk.Tk()                             # Creates the tk window object
        self.root.title("Burger Hut Bill")                  # Titles the window

        self.label = tk.Label(self.root, text="=======Receipt=======")                  # Creates first text box
        self.label.pack()                                                               # Puts wigit into a block before adding to window

        self.customer_name_label = tk.Label(self.root, text="Customer Name: " + user.getName())     # Customer name widget
        self.customer_name_label.pack()

        self.customer_id_label = tk.Label(self.root, text="Customer ID: " + str(user.getID()))      # Customer ID widget
        self.customer_id_label.pack()

        if len(self.order.getItemList()) > 0:                               # If there are items in the item list container, iterate through it 
            for item in self.order.getItemList():                   
                item_label = tk.Label(
                    self.root,
                    text=f"{item.getName()} x{item.getQuantity()} | ${item.getPrice() * item.getQuantity()}",   # Creates widgets with each menu item, it's quantity, and it's price
                )
                item_label.pack()

            tax_label = tk.Label(self.root, text=f"Tax Percentage: {int(user.getTax() * 100)}%")  # Creates widget displaying tax percent
            tax_label.pack()

            total_label = tk.Label(self.root, text=f"Total + Tax: ${round(self.order.getTotal())}") # Creates widget displaying total
            total_label.pack()
        else:
            empty_order_label = tk.Label(self.root, text="You ordered nothing!")       # If there are no items in the itemlist container, you ordered nothing.
            empty_order_label.pack()

        self.root.mainloop()                # Main display loop keeps window on screen until closed.
