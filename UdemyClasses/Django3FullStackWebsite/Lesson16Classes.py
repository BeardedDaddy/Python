class Dog():
    """This is an class called Dog. It has a method called bark.
    """
    # dogInfo = "Hey dogs are cool."  # This is a class attribute. It is an attribute that is shared by all instances of the class.  # noqa
    def __init__(self, name="", age=0, furcolor=""): # What are inside the parameters are called attributes. This is a method of the class. It is a function that is part of the class. It is called a constructor. It is called when an instance of the class is created. It is used to initialize the attributes of the class.  # noqa
        self.name = name
        self.age = age
        self.furcolor = furcolor

        # This is a method of the class. It is a function that is part of the class. It is called a constructor. It is called when an instance of the class is created. It is used to initialize the attributes of the class.  # noqa

    def bark(self, str): # This is a method of the class. It is a function that is part of the class. It takes in a parameter called str. The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.  # noqa
        """This is a function that prints WOOF! to the console.
        """
        print("WOOF!" + str) # This is a print statement that prints WOOF! to the console. It also prints the string that is passed in as an argument to the method. # noqa

mydog = Dog("Fido", 13, "Brown")  # Here we are creating an instance of the Dog class and assigning it to the variable mydog. Which simply means to assign the class to the variable.  This instance is only used if you do not create an instance variable like on line 5. You would than create an init function that will have the parameters called attributes.   # noqa

mydog.bark(" Hey I'm talking to you.")  # Here we are calling the bark method of the mydog instance of the Dog class. Which simply means to call the method of the class. We are also passing in a string as an argument to the bark method.  # noqa 

# mydog.name = "Fido"  # Here we are creating an attribute called name and assigning it the value of Fido to the mydog instance of the Dog class. Which simply means to create an attribute of the class.  # noqa

# mydog.age = 3  # Here we are creating an attribute called age and assigning it the value of 3 to the mydog instance of the Dog class. Which simply means to create an attribute of the class.  # noqa

# print(mydog.name)  # Here we are printing the name attribute of the mydog instance of the Dog class. Which simply means to print the attribute of the class.  # noqa

print(mydog.age)  # Here we are printing the age attribute of the mydog instance of the Dog class. Which simply means to print the attribute of the class.  # noqa

# Dog.dogInfo = "Hey there."
# print(Dog.dogInfo)  # Here we are printing the dogInfo attribute of the Dog class. Which simply means to print the attribute of the class.  # noqa
