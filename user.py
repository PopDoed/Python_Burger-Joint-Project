class User:  # User superclass
    """
    Allows for the creation of a User account object to store their information.
    Has get name, id, and tax method for calculating and printing bill.
    *Not to be used as an object, only a superclass for the below subclasses.
    """

    def __init__(self, name, ID):           # User instance variables
        self._ID = ID
        self._name = name
        self._tax = None

    def getName(self):              # Returns name of user
        return self._name

    def getID(self):                # Returns ID of user
        return self._ID

    def getTax(self):               # Returns user's tax value (to be overwitten)
        return None


class Student(User):  # Student Class
    def __init__(self, name, ID):
        super().__init__(name, ID)
        self._tax = 0

    def getTax(self):  # Overwritten method for student tax
        return self._tax


class Teacher(User):  # Teacher Class
    def __init__(self, name, ID):
        super().__init__(name, ID)
        self._tax = 0.09

    def getTax(self):  # Overwritten method for teacher tax
        return self._tax