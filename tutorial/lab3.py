# list

list_1 = [1, 3, 4]

list_2 = ["first", "second", "third"]


# when passing a list to a function, the list is not copied:
# the reference (memory location) to the list is passed instead;
# and therefore modifying the list inside the function modifies the
# original list that was passed to the function

def print_first_element(alist: list) -> None:
    print(alist[0])


def print_last_element(alist: list) -> None:
    print(alist[len(alist) - 1])


def print_element_at_index(alist: list, index: int) -> None:
    print(alist[index])


def append_element(alist: list[int], element: int) -> list[int]:
    new_list = alist.copy()  # make a copy of the list
    new_list.append(element)
    return new_list


def append_element_inplace(alist: list[int], element: int) -> None:
    alist.append(element)


def remove_element_at_index(alist: list, index: int) -> list[int]:
    new_list = alist.copy()
    new_list.pop(index)
    return new_list


def remove_element_at_index_inplace(alist: list, index: int) -> None:
    alist.pop(index)

# when passing int or float a copy of the value passed to the function is made
# and therefore changing the value inside the body of the function does not
# change the original value

# str types are immutable and cannot be changed in any way


def main() -> None:
    pass


if __name__ == "__main__":
    main()
