---
tag: XK7YECSHR9
kind: example
name: The subgroup 2Z of Z has no complement
msc: ["15A03", "13C05"]
topics: [QHKTJ89V6S]
audience: ug2
not_instance_of:
  - target: 0M83V17KHX
    note: Z is a module over the ring Z, which is not a field, and no submodule W of Z satisfies 2Z + W = Z and 2Z ∩ W = 0
illustrates: [0P9T8WHNMH]
uses: [04C3BAHV03, 0V33SPH7RR]
sources:
  - url: https://en.wikipedia.org/wiki/Complemented_subspace
    locator: Algebraic direct sum
---

## Example

Consider $\Z$ as a module over the ring $\Z$, and its submodule $2\Z$ of even integers.
We check that no submodule $W$ of $\Z$ satisfies $\Z = 2\Z \oplus W$, so $2\Z$ has no [[complement|04C3BAHV03]].

1. The submodules of $\Z$ are its subgroups, because multiplying by an integer is repeated addition.
   Every subgroup of $\Z$ is $n\Z$ for some integer $n \ge 0$.
   So $W = n\Z$ for some $n \ge 0$.
2. If $n = 0$, then $W = \{0\}$, and $2\Z + W = 2\Z$.
   This is not $\Z$, since $1$ is odd.
3. If $n \ge 1$, then the number $2n$ is even and is a multiple of $n$, so it lies in $2\Z$ and in $n\Z$.
   Since $2n \ne 0$, the [[intersection|0V33SPH7RR]] $2\Z \cap W$ is not $\{0\}$.
4. In both cases one of the two conditions fails, so $W$ is not a complement of $2\Z$.

So the [[existence of complements|0P9T8WHNMH]] fails when the field of scalars is replaced by the ring $\Z$.

## Remarks

The proof of existence over a field breaks at one step.
There we take a vector $v$ outside $U + W$ and show that $F v$ meets $U$ only in $0$, by dividing by a nonzero scalar.
Here the vector $1$ lies outside $2\Z$, but $\Z \cdot 1 = \Z$ meets $2\Z$ in all of $2\Z$, because $2 \cdot 1 \in 2\Z$ and $2$ has no inverse in $\Z$.

A second reason uses the quotient.
Over a field, every complement of $U$ is isomorphic to the quotient by $U$.
Here the quotient $\Z / 2\Z$ has two elements, while every nonzero submodule $n\Z$ of $\Z$ is infinite, so no submodule of $\Z$ is isomorphic to $\Z / 2\Z$.

The same argument shows that no proper nonzero subgroup $k\Z$ with $k \ge 2$ has a complement in $\Z$, since $kn$ lies in both $k\Z$ and $n\Z$.
Over the field $\mathbb{Q}$ the picture changes completely: $\mathbb{Q}$ is a one-dimensional vector space over itself, and its only subspaces $\{0\}$ and $\mathbb{Q}$ are complements of each other.

## Explanations

### L1 human

Over the integers we cannot divide by $2$.
Every collection of the form "all multiples of $n$", with $n \ge 1$, contains the even number $2n$.
So it always overlaps the even numbers in more than $0$, and no such collection can complete the even numbers to all integers without overlap.

### L2 human

Over a field, a complement of $U$ is a copy of the quotient by $U$ inside the space.
Here the quotient $\Z / 2\Z$ is a group with two elements, and $\Z$ has no subgroup with two elements, since every nonzero subgroup $n\Z$ is infinite.
So the theorem on complements and quotients already rules out a complement before we test any candidate.
The lesson is that the existence of complements is a special feature of vector spaces, and it fails for modules over most rings.
