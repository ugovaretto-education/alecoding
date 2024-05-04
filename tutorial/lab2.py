# functions

def double(v: float) -> float:
    return v + v


def call_double(v: float) -> None:
    print(f"doubling {v}: {double(v)}")


if __name__ == "__main__":
    call_double()
