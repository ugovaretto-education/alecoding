from inspect import getmodule, stack


def root_fun():
    frame = stack()[1]
    module = getmodule(frame[0]).__name__
    print(f"Root function, called from {module}")
    return "Root invoked"
