from inspect import getmodule, stack


def child2_fun():
    frame = stack()[1]
    module = getmodule(frame[0]).__name__
    print(f"Child 2 fun, called from {module}")
    return "Child 2 invoked"
