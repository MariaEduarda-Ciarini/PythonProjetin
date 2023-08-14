class Customer:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print("Calling @property name()")
        return self.__name.title()

    @name.setter
    def name(self, name):
        print("Calling setter name()")
        self.__name = name