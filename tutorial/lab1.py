# variables

int_var: int = 1
str_var: str = "hello"
decimal_var: float = -12.12345

print(f"{int_var} {str_var} {decimal_var}")


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
