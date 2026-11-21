---
tag: 3GD87G9ARX
kind: example
name: The 2-types of dense linear orders
msc: ["03C07", "06A05"]
topics: [Z772KEC9BY]
audience: grad
instance_of: [VDY4PG5WHN, A0VNTN725W]
uses: [VDY4PG5WHN, A0VNTN725W, 9V71Q3SD1G, 2W4S2H4VYA, 7FDDXV3JK7, 1513J40TKA]
sources:
  - url: https://en.wikipedia.org/wiki/Type_(model_theory)
    locator: Stone spaces
  - book: isbn:9780387987606
    locator: Chapter 4
---

## Example

Let $T$ be the theory of [[dense linear orders|2W4S2H4VYA]] without endpoints, in the language $\set{<}$.
We show that the [[Stone space|VDY4PG5WHN]] $S_2(\emptyset)$ of $T$ has exactly three points, and each one is isolated.

1. The atomic formulas in $x_1, x_2$ are $x_i = x_j$ and $x_i < x_j$ for $i, j \in \set{1, 2}$.
2. In a linear order exactly one of $x_1 < x_2$, $x_1 = x_2$ and $x_2 < x_1$ holds, and this choice decides every atomic formula.
3. The theory $T$ has [[quantifier elimination|7FDDXV3JK7]], so every formula $\varphi(x_1, x_2)$ is equivalent modulo $T$ to a Boolean combination of atomic formulas.
4. So a complete $2$-type is fixed by its choice in step 2, and there are at most three types.
5. In $(\Q, <)$ the pairs $(0, 1)$, $(0, 0)$ and $(1, 0)$ realize the three choices, so there are exactly three types.
6. The formula $x_1 < x_2$ lies in exactly one type, so $[x_1 < x_2]$ is a single point; the same holds for the two other formulas.

So $S_2(\emptyset)$ is a discrete space with three points, and each type is an [[isolated type|A0VNTN725W]].

## Remarks

The same argument shows that a complete $n$-type of $T$ is the same as an ordering of $x_1, \dots, x_n$ in which ties are allowed.
So $S_n(\emptyset)$ is finite for each $n$, with $1$, $3$, $13$ and $75$ points for $n = 1, 2, 3, 4$.
This matches the [[Ryll-Nardzewski theorem|1513J40TKA]], since $T$ is $\aleph_0$-categorical.
With parameters the space grows: $S_1(\Q)$ computed in $(\R, <)$ has $2^{\aleph_0}$ points.

## Explanations

### L1 human

Two points of a dense order with no ends can be related in only three ways: the first is smaller, they are equal, or the first is larger.
Nothing else about the pair can be said with the order alone.
So there are exactly three kinds of pairs.

### L2 human

We count the $3$-types.

1. An ordering with ties of three variables puts them into $k$ blocks in order, for $k = 1, 2, 3$.
2. There is $1$ ordering with one block, $6$ orderings with two blocks ($3$ ways to split, times $2$ orders), and $6$ with three blocks.
3. So there are $1 + 6 + 6 = 13$ complete $3$-types.

The typical use is to see that a theory with quantifier elimination in a finite relational language has finitely many $n$-types.
The trap is to forget the ties: the type $x_1 = x_2$ is a type of pairs as well.
