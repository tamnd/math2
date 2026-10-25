"""Check the certificate of the subgroups of S4, for the computation node ~4ba583eb.

The certificate is /work/certificate. It has one line for each subgroup of S4: the order, and then the elements. An element is the string of the images of 1, 2, 3 and 4. The checker does not use GAP. It finds the subgroups of S4 again with its own search, and it accepts the certificate only when these things are true:

- Each line is a set of elements of S4 with the size that the line gives.
- The lines are the subgroups that the search finds, each one time.
- The order of each subgroup divides 24.

The search starts with the trivial subgroup. For each subgroup H that it has and each element g of S4, it adds the subgroup that H and g generate. Each subgroup has a finite set of generators, so the search finds each subgroup.

The checker exits with the code 0 when it accepts the certificate, and with the code 1 when it does not.
"""

import itertools
import sys

N = 4
ORDER = 24
ELEMENTS = ["".join(map(str, p)) for p in itertools.permutations(range(1, N + 1))]
IDENTITY = "".join(map(str, range(1, N + 1)))


def compose(p, q):
    """The element that maps i to p(q(i))."""
    return "".join(p[int(q[i]) - 1] for i in range(N))


def generate(gens):
    """The subgroup that the elements gens generate, as a frozenset."""
    group = {IDENTITY}
    todo = [IDENTITY]
    while todo:
        x = todo.pop()
        for g in gens:
            y = compose(g, x)
            if y not in group:
                group.add(y)
                todo.append(y)
    return frozenset(group)


def subgroups():
    """Each subgroup of S4, by the search of the module docstring."""
    found = {generate([])}
    todo = list(found)
    while todo:
        h = todo.pop()
        for g in ELEMENTS:
            k = generate(list(h) + [g])
            if k not in found:
                found.add(k)
                todo.append(k)
    return found


def read(path):
    """The subgroups of the certificate, as a list of frozensets."""
    rows = []
    with open(path, encoding="ascii") as f:
        for number, line in enumerate(f, 1):
            fields = line.split()
            if not fields or not fields[0].isdigit():
                raise ValueError(f"line {number} does not start with an order")
            order, elements = int(fields[0]), fields[1:]
            if any(e not in ELEMENTS for e in elements):
                raise ValueError(f"line {number} has a string that is not an element of S{N}")
            if len(set(elements)) != len(elements) or len(elements) != order:
                raise ValueError(f"line {number} gives the order {order}, and it has {len(set(elements))} different elements")
            rows.append(frozenset(elements))
    return rows


def main():
    try:
        rows = read("/work/certificate")
    except (OSError, ValueError) as e:
        print(f"the certificate is not valid: {e}")
        return 1
    want = subgroups()
    if len(set(rows)) != len(rows):
        print("the certificate has a subgroup two times")
        return 1
    if set(rows) != want:
        print(f"the certificate has {len(rows)} subgroups, and the search finds {len(want)} different ones")
        return 1
    bad = sorted({len(h) for h in rows if ORDER % len(h) != 0})
    if bad:
        print(f"these orders do not divide {ORDER}: {bad}")
        return 1
    orders = sorted({len(h) for h in rows})
    print(f"accepted: {len(rows)} subgroups of S{N}")
    for k in orders:
        print(f"order {k}: {sum(1 for h in rows if len(h) == k)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
