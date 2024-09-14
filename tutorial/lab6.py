# Named arguments

def fun(arg1: int, arg2: str):
    print(f"arg1: {arg1} arg2: {arg2}")


fun(arg1=10, arg2="a string")

# Argument list


def args_fun(*args):
    for i in args:
        print(i)


args_fun(1, 2, "three")

# Keyword arguments


def kwargs_fun(*args, **kwargs):
    print()
    print("Arguments")
    for i in args:
        print(i)
    print()
    print("Named Arguments")
    for k, v in kwargs.items():
        print(f"name: {k}, value: {v}")

kwargs_fun("arg 1", "arg 2", arg_3=10, arg_4="four")
