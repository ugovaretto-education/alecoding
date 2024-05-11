# class

# a class is a type, an object is an instance of a class
# a class is like a blueprint defining the structure of an object

# objects pack both functions (called methods when stored inside an object)
# and data
# data and functions stored inside an object are accessible by adding a '.'
# character to the instance name and specifying the data or function to call

# within a member function (method) the data and functions in the same instance
# can be accessing through the 'self' identifier which refers to the current
# instance of the class.

# to initialise the data in the object you define an __init__() method
# accepting a 'self' variable referring to the current object being constructed
# the __init__ method is called a constructor because it construct the object

# methods that start and end with '__' are suppused to be hidden from client
# code and used only internally by the class or object

# when a method receives a 'self' parameter it works on the current instance
# of the class

# methods that do not access 'self' are equivalent to regular functions and
# are called class methods

class AClass:
    def __init__(self):
        self.data: int = 2


an_object_of_type_AClass = AClass()

print(an_object_of_type_AClass.data)


class AnotherClass:
    def __init__(self):
        self.data: int = 2

    def print_data_member(self):
        print(self.data)


an_object_of_type_AnotherClass = AnotherClass()

an_object_of_type_AnotherClass.print_data_member()
