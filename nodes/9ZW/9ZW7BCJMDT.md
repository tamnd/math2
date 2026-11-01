---
tag: 9ZW7BCJMDT
kind: statement
role: theorem
name: Combinatorial Nullstellensatz
msc: ["05E40", 11B75, 13F20]
uses: [04C5ZBG1WT, 07GNX8GCYP, 0P4JRMSWNH]
about: [07GNX8GCYP]
sources:
  - url: https://en.wikipedia.org/wiki/Restricted_sumset
---

## Statement

Let $F$ be a [[field|04C5ZBG1WT]] and let $f \in F[x_1, \dots, x_n]$ be a [[polynomial in $n$ variables|07GNX8GCYP]].
Let $S_1, \dots, S_n$ be nonempty finite subsets of $F$ and let $g_i(x_i) = \prod_{s \in S_i} (x_i - s)$.

1. If $f(s_1, \dots, s_n) = 0$ for all $(s_1, \dots, s_n) \in S_1 \times \dots \times S_n$, then there are polynomials $h_1, \dots, h_n \in F[x_1, \dots, x_n]$ with $\deg h_i \le \deg f - \deg g_i$ and $f = \sum_{i=1}^n h_i g_i$.
2. Let $t_1, \dots, t_n \ge 0$ be integers with $\abs{S_i} > t_i$ for each $i$. Suppose that the [[degree|0P4JRMSWNH]] of $f$ is $t_1 + \dots + t_n$ and that the coefficient of $x_1^{t_1} \cdots x_n^{t_n}$ in $f$ is nonzero. Then there is $(s_1, \dots, s_n) \in S_1 \times \dots \times S_n$ with $f(s_1, \dots, s_n) \ne 0$.

## Remarks

The result and its name are due to Alon.
For part 1, reduce $f$ by replacing each power $x_i^{e}$ with $e \ge \abs{S_i}$ using $g_i(x_i) = 0$; the remainder has degree less than $\abs{S_i}$ in each $x_i$ and still vanishes on $S_1 \times \dots \times S_n$.
A polynomial of that kind which vanishes on the whole grid is zero.
This follows by induction on $n$, since a nonzero polynomial in one variable of degree $d$ has at most $d$ roots.
Part 2 follows from part 1.
If $f$ vanished on the grid, then $f = \sum_i h_i g_i$ with the stated degree bounds.
Every monomial of top degree in $h_i g_i$ has $x_i$-degree at least $\abs{S_i} > t_i$, so $x_1^{t_1} \cdots x_n^{t_n}$ could not appear in $f$.

The size condition is needed: for $n = 1$, $f = x_1(x_1 - 1)$, $t_1 = 2$ and $S_1 = \set{0, 1}$, we have $\abs{S_1} = t_1$ and $f$ vanishes on $S_1$.

Example: the [[Cauchy–Davenport theorem|F7K7XFACSG]] follows from part 2.
For a prime $p$ and nonempty $A, B \subseteq \Z/p\Z$ with $\abs{A} + \abs{B} - 1 \le p$, suppose the [[sumset|XNBN31HQWB]] $A + B$ lies in a set $C$ of size $\abs{A} + \abs{B} - 2$.
Apply part 2 to $f(x, y) = \prod_{c \in C} (x + y - c)$ with $t_1 = \abs{A} - 1$ and $t_2 = \abs{B} - 1$: the coefficient of $x^{t_1} y^{t_2}$ is $\binom{t_1 + t_2}{t_1}$, which is nonzero modulo $p$, yet $f$ vanishes on $A \times B$, a contradiction.

## Explanations

### L1 human

A polynomial that is not too big cannot vanish on a large grid of points.
The theorem makes "not too big" precise: look at one top-degree term and compare its exponents with the sizes of the sets along each axis.
If each set is larger than the matching exponent, the polynomial is nonzero somewhere on the grid.

### L2 human

The method is to encode a combinatorial property as the vanishing of a polynomial on a grid, then exhibit a nonzero top coefficient.
It gives short proofs of results in additive number theory, such as Cauchy–Davenport, and of results on graph colouring and on hyperplane coverings of the cube.
It is a sharp version, for grids, of the fact that a nonzero polynomial cannot vanish everywhere on $F^n$ when $F$ is infinite.
