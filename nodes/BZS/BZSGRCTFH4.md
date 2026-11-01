---
tag: BZSGRCTFH4
kind: statement
role: theorem
name: Rado's theorem
msc: [05D10, 11B75]
uses: [G5TWXV565S, 0VD9ZSWWJG]
about: [G5TWXV565S]
sources:
  - url: https://en.wikipedia.org/wiki/Rado%27s_theorem_(Ramsey_theory)
same_as:
  wikidata: Q3527146
  wikipedia: Rado's theorem (Ramsey theory)
---

## Statement

Let $A$ be an $m \times n$ [[matrix|0VD9ZSWWJG]] with rational entries, with columns $c_1, \dots, c_n \in \Q^m$.
The system $Ax = 0$ is called partition regular if the following holds for every finite colouring of the positive integers.
There is a solution $x = (x_1, \dots, x_n)$ in positive integers whose entries all have the same colour.
The matrix $A$ satisfies the columns condition if the index set $\set{1, \dots, n}$ has a partition into nonempty sets $I_1, \dots, I_k$ with these properties, where $s_j = \sum_{i \in I_j} c_i$:

1. $s_1 = 0$.
2. For each $j$ with $2 \le j \le k$, the vector $s_j$ is a linear combination with rational coefficients of the columns $c_i$ with $i \in I_1 \cup \dots \cup I_{j-1}$.

Then the system $Ax = 0$ is partition regular if and only if $A$ satisfies the columns condition.

## Remarks

For a single equation $a_1 x_1 + \dots + a_n x_n = 0$ with nonzero integer coefficients, the columns condition says that some nonempty set of the coefficients $a_i$ has sum $0$.
So $x + y - z = 0$ is partition regular, because $1 + (-1) = 0$; this is [[Schur's theorem|V6XJQXZ7E8]].
The equation $x + y - 3z = 0$ is not partition regular, because no nonempty subset of $\set{1, 1, -3}$ sums to $0$.
The system $x_i - x_0 - i y = 0$ for $1 \le i \le k - 1$, in the unknowns $x_0, \dots, x_{k-1}, y$, satisfies the columns condition with $I_1 = \set{x_0, \dots, x_{k-1}}$ and $I_2 = \set{y}$.
Its monochromatic solutions are arithmetic progressions $x_0, x_0 + y, \dots, x_0 + (k-1)y$ with $y \ge 1$, so [[van der Waerden's theorem|V96FRZ2ME1]] is a special case.
The proof of sufficiency builds the monochromatic solution from many uses of van der Waerden's theorem.
The proof of necessity colours each integer by its last nonzero digit in base $p$, for a suitable prime $p$.

## Explanations

### L1 human

Colour every positive integer with one of finitely many colours.
Some systems of linear equations always have a solution inside a single colour, whatever the colouring is.
Rado's theorem tells exactly which systems have this property, with a simple test on the columns of the matrix.
For one equation the test is easy: some of the coefficients must add up to zero.

### L2 human

Rado's theorem is a central result of [[Ramsey theory|G5TWXV565S]] on the integers.
It contains Schur's theorem and van der Waerden's theorem as special cases.
The columns condition is checked by linear algebra over $\Q$, so partition regularity is decidable.
