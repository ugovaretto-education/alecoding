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
