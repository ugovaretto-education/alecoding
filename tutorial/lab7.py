# Iterators

# An iterator is an object that contains an enumerable (countable)
# number of elements.
# You use the 'next' function to return the next object.

atuple = ("one", "two", "three")
an_iterator = iter(atuple)
print(next(an_iterator))
print(next(an_iterator))
print(next(an_iterator))

# The following statemnt fails with a raised 'StopIteration" exception
# because there are no more elements to return.

# print(next(an_iterator))


# When using a 'for' loop to iterate:
for element in atuple:
    print(element)

# The code gets automatically translated to the following:

# Loop until a 'StopIteration' exception is thrown.
# Reset the iterator by creating a new one
an_iterator = iter(atuple)
while True:
    try:
        # Retrieve next element.
        element = next(an_iterator)
        print(element)
    except StopIteration:
        # StopIteration is raised when non more elements are available.
        # Exit loop.
        break

# The 'range" function generates an iterator over a sequence of numbers:
for i in range(10):  # generate 10 numbers 0 to 9
    print(i)

# It is possible to specify start element and step.
# Generate 10 numbers starting at 5 with a step of 10.
for i in range(5, 100, 10):  # generate 10 numbers 0 to 9
    print(i)


# Custom iterators
# The iterator protocol requires all iterators to implement the
# __iter__ and  __next__ methods.
class MyPow2Range:
    def __init__(self, num_elements: int):
        self.num_elements = num_elements

    def __iter__(self):
        self.count = 0
        self.value = 1
        return self

    def __next__(self):
        if self.count < self.num_elements:
            x = self.value
            self.count += 1
            self.value *= 2
            return x
        else:
            raise StopIteration


def my_pow2_range(count: int) -> MyPow2Range:
    return iter(MyPow2Range(count))


# Iterate from 2^0 to 2^9, the first ten power of two numbers.
for i in my_pow2_range(10):
    print(i)
