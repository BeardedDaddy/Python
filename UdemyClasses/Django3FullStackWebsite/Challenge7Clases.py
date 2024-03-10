class Car:
    def __init__(self, make, model, year): # These are variable of the init function for the class.  # noqa
        self.make = make  # This is a method of the class.
        self.model = model  # This is a method of the class.
        self.year = year  # This is a method of the class.
    
    def age(self): # This is a method of the class. It is a function that is part of the class. It takes in a parameter called self. The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class like age.  # noqa
        return 2020 - self.year

Car1 = Car("Toyota", "Corolla", 2015) # To call this function you assign the class to a variable.  # noqa
print(Car1.age())  # To print this function you print the variable also adding the method of the class.  # noqa
