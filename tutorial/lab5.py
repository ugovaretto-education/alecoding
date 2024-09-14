# OOP

class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def print(self):
        print(self.first_name, self.last_name)

# Use the Person class to create an object, and then
# execute the printname method:


x = Person("John", "Doe")
x.print()


class Student(Person):
    def __init__(self, first_name: str, last_name: str, graduation_year: int):
        super().__init__(first_name, last_name)
        self.graduation_year = graduation_year

    def print(self):
        super.print()
        print(self.graduation_year)


def print_personal_data(p: Person):
    p.print()


s = Student("Jane", "Doe", 2022)
print_personal_data(s)
# iterators, exceptions and generators

# Exceptions are signals emitted by prefixing
# the signal name with the 'raise' statement
# and can be caught by wrapping code into
# a try catch block where the code inside the
# catch section is executed only if the code
# in the try section emits an exception

# raise exeption


def throw_exception():
    print("throw_exception() raising exception of type EnvironmentError")
    raise EnvironmentError


def try_catch():
    try:
        print("Calling function 'throw_exception'...")
        throw_exception()
        print("We never get here!!")  # this line is never reached
        # because the function throw_exception
        # raises an exception and therefore
        # the code jumps to the 'except' statement
    except EnvironmentError:
        print("Exception of type 'EnvironmentError caught")
    except Exception:
        print("Some other exception caught")


# Iterate over random access array (i.e. something that is indexable)
# exposing it as a sequence
class RandomAccessIterator:
    def __init__(self, array):
        # pointer to random access array
        self._array_ref = array
        # start index
        self._index = 0
        # record size
        self._length = len(array)

    # return reference to instance being created
    # when clent code invokes 'iter(object)' this
    # method is invoked
    def __iter__(self):
        return self

    # invoked by client code to retrieve next element
    # in sequence.
    def __next__(self):
        if self._index < self._length:
            item = self._array_ref[self._index]
            self._index += 1
            return item
        else:
            # attempt to access an element beyond the end
            # of the array
            raise StopIteration


# iterate using 'for' which will automatically invoke '__iter__'
# and '__next__'
def for_iteration():
    alist = [10, 9, 8, 7]
    it = iter(RandomAccessIterator(alist))
    # 'for' calls 'iter' on 'it1' and then at each
    # iteration invokes the 'next' method to retrieve
    # the next element
    print("Iterating over list using 'for'")
    for element in it:
        print(element)


# iterate using 'while' and explicitly construct the iterator and
# invoke '__next__' to iterate over random access sequence
def while_next_iteration():
    alist = [10, 9, 8, 7]
    it = RandomAccessIterator(alist).__iter__()
    print()
    print("Iterating over list using 'while' and '__next__'")
    try:
        while True:
            element = it.__next__()
            print(element)
    except StopIteration:
        print("Iteration completed")


# once the iteration is completed the iteration
# object cannot be used anymore

# Generators
# Generators are functions that act as iterators
# using the 'yield' keyword to stop and return a value
# each time their are invoked. The state is frozen at each 'yield'
# invocation and the next time the function is called execution restart
# from where it stopped.

def left_shift_str(string: str):
    for i in range(0, len(string)):
        # concatenate last part of string after index
        # with first part of string achieving a left shift
        # operation
        yield string[i:] + string[:i]


def iterate_with_generator():
    s = "1234567"
    # generate a sequence-like object
    # behind the scenes this is turned into an object
    # that has an __iter__ and __next__ method as a regular
    # iterator
    sequence = left_shift_str(s)
    for i in sequence:
        print(i)
