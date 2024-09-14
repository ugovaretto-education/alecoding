from typing import Generator

# Generators

# Generators are similar to ierators in that at each invocation
# they return an element but are implemented as regular functions
# using 'yield' instead of return.


def counter(max_count: int) -> Generator:
    counter = 0
    while counter <= max_count:
        yield counter  # return value and save current state
        counter += 1  # at the next invocation the code resumes from here
    return -1  # WARNING: 'return' in a Generator is equivalent to
    #            raising StopIteration


for i in counter(10):
    print(i)


# Tuple comprehension as generators.
# Using a comprehension iside a tuple is equivalent to
# writing a generator.
generator = (x for x in range(10))
for i in generator:
    print(i)


# OUt of scope for this tutorial but it is possible to
# use 'yield from' to extract values from another generator and
# creeate a transparent connection between a subgenerator and the
# code calling a generator.
# It is also possible to send code to a generator by receiving
# data through '(yield)' invocation.
