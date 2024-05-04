import mroot as mr
import mroot.child2 as mrc2


def child1_fun():
    print("Child 1 fun")


def child1_invoke_child2():
    print(f"Child 1 -> {mrc2.child2_fun()}")


def child1_invoke_root():
    print(f"Child 1 -> {mr.root_fun()}")
