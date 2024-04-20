# Generate Pythsgorean triples.
def generate_triples(num_tuples: int, N: int) -> list[tuple[int, int, int]]:
    triples: list[tuple[int, int, int]] = []
    for a in range(1, N):
        for b in range(a, N):
            c = a
            while c * c < a * a + b * b:
                c += 1
            if c * c == a * a + b * b:
                triples.append((a, b, c))
                if len(triples) >= num_tuples:
                    return triples
    return []


# Print commma separated list of triples, one per line.
def print_triples(triples: list[tuple[int, int, int]]) -> None:
    for t in triples:
        print(f"{t[0]},{t[1]},{t[2]}")


# Convert triple list to dict with key equal to the hypotenuse and value equsl to the other two sides
# of a right triangle.
def triples_dict(triples: list[tuple[int, int, int]]) -> dict[int, tuple[int, int]]:
    d = dict()
    for t in triples:
        d[t[2]] = (t[0], t[1])
    return d


# Read triples from file as list of comma separated triples.
def read_triples(file_name: str) -> dict[int, tuple[int, int]]:
    d = dict()
    with open(file_name) as f:
        for line in f:
            t = tuple(map(lambda x: int(str.strip(x)), str.split(line, ",")))
            d[t[2]] = (t[0], t[1])
    return d


# Given a number returns the triple with the hypotenuse length closest to the passed number.
def closest_triple(
    triples: dict[int, tuple[int, int]], min_dist: int
) -> tuple[int, int, int]:
    hyps = list(triples.keys())  # extract hypotenuse lenghts
    dist = map(
        lambda i: abs(i - min_dist), hyps
    )  # compute distance between each hypotenuse length and passed values
    # find the index of the item with minimum distance
    index = min(enumerate(dist), key=lambda x: x[1])[0]
    # return closest triple matching hypotenuse length
    c = hyps[index]
    return (triples[c][0], triples[c][1], c)
