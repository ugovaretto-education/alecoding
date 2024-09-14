# Containers.

# Associative containers are collections of elements accessed through an index
# which does not need to be number withing a specific range but could be any
# object type from which a numerical index can be computed through a hash
# function  like e.g. a string.
# Built-in associative containers, where values are accessed through keys,
# include a standard dictionary and a dictionary that returns a default
# value if the key is not in the dictionary.


# Set is also a built-in containers and contains a collection of elements
# of the same type, making it efficient to quickly check if an element
# is part of the set or not, avoiding iterating sequentially on the elements.

# Dictionary

string_to_int = dict()
string_to_int["one"] = 1
string_to_int["two"] = 2

# OR
string_to_int = {}
string_to_int["one"] = 1
string_to_int["two"] = 2

print(string_to_int["two"])

# Trying to access an element not in the dictionary
# generates a 'KeyError' exception.

# Iterate over keys and values
for key, value in string_to_int.items():
    print(f"key = {key}, value = {value}")


# Set

numbers = set()
numbers.add(1)
numbers.add(100)
numbers.add(1000)
numbers.add(10000)

# use 'in' to check if element in set
assert 100 in numbers

# iterate like on ranges
for n in numbers:
    print(n)

# Standard set operations such as union, difference and intersection
# are supported.
