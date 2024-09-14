# List comprehension.

alist = [3 * x for x in range(10)]
print(alist)

# With conditions.
# Same as above but restrict to numbers divisible by 4.
alist = [3 * x for x in range(30) if x % 4 == 0]
print(alist)

# Nesting


def flatten(matrix: list[list]) -> list:
    # '(row) for row in matrix' returns all rows
    # 'for element in row' returns all element in each row
    return [element for row in matrix for element in row]


matrix = [[11, 12, 13],
          [21, 33, 23]]

assert flatten(matrix) == [11, 12, 13, 21, 22, 23]
