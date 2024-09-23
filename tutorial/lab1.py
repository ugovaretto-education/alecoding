# variables

int_var: int = 1
str_var: str = "hello"
decimal_var: float = -12.12345

# When using f-strings, i.e. strings pre-fixed with an 'f' character
# it is possible to perform string interpolation by specifying the
# variable name within '{}' braces in the string.
print(f"{int_var} {str_var} {decimal_var}")


def foo(an_argument: int):
    print(an_argument)


foo(10)


def move_forward():
    print("Move Forward")


move_forward()

# list
# A list is a collection of elements of the same type
alist = [1, 4, 5]
first_element = alist[0]

# tuple
# A tuple is a collection of elements of any type.
atuple = (1, "one", False)
first_element = atuple[0]


# class


class AClass:

    def __init__(self, number: int) -> None:
        self.int_data_member = number

    def method(self):
        print("I am an instance of AClass, "
              "containing a integer number of value "
              f"{self.int_data_member}")


a: AClass = AClass(10)

print(f"AClass data member: {a.int_data_member}")

print(f"2 is of type {type(2)}, -3.56 is of type {type(-3.56)}, "
      f"'hello' is of type {type('hello')}")

# Errors
# Python raises an exception signal whenever an error is encountered.


def generate_exception():
    raise Exception("This is an Error!")

# If exceptions are not handled the program terminates printing the
# error message contained in the eception instance thrown.
# Excptions are handled by surrounding the code that can raise an eception
# with a 'try' 'catch' block.
# The 'catch' block reaceives and instance of the exception beint thrown and
# it is possible to specify which type of exception we want to handle in each
# 'except' block.


def handle_exception():
    try:
        generate_exception()
    except Exception as exception_instance:
        print(exception_instance)
    except MemoryError as merror:
        print(merror)
    # ...


handle_exception()

# Built-in exceptions:
# https://www.w3schools.com/python/python_ref_exceptions.asp


# References and values

# Built-in types such as numbers are always copied when assigned to other
# variables.

x = 4
y = x

# x and y contain a copy of the number '4', changing y does not change x
y = 10
assert x == 4

# Classes and lists are not copied when assigned to other variables and
# variables simply store a reference to the instance, and therefore
# changing the content of the object instance will change the content
# of all the variables referencing the same instance.

list1 = [1, 2, 3, 4]
list2 = list1  # points to the same list as list1
list2[-1] = 1111  # change element value
# the changes is visible to list1 as well
assert list1[-1] == 1111
