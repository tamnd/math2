---
tag: P50N7QXQSF
kind: definition
name: Approximation algorithm
msc: [68W25, 90C27, 68Q25]
defines: 4WEVBDQ8SR
uses: [9DMSG5HAQX, GVT2NKN37K, 0AHKWBQSWV, 0MJ04A50QW]
sources:
  - url: https://en.wikipedia.org/wiki/Approximation_algorithm
---

## Definition

Consider a minimization problem in which each instance $I$ has a nonempty finite set of feasible solutions.
Each feasible solution $S$ has a cost $c(S) > 0$, and $\mathrm{OPT}(I)$ is the least cost of a feasible solution of $I$.
Let $\rho \ge 1$ be a real number.
A *$\rho$-approximation algorithm* for the problem is an [[algorithm|9DMSG5HAQX]] $A$ with these properties:

1. $A$ runs in time polynomial in the size of $I$, as for problems in [[P|GVT2NKN37K]].
2. For every instance $I$, $A$ outputs a feasible solution $A(I)$.
3. For every instance $I$, $c(A(I)) \le \rho \cdot \mathrm{OPT}(I)$.

For a maximization problem, clause 3 becomes $c(A(I)) \ge \mathrm{OPT}(I) / \rho$.
The number $\rho$ is called the *approximation ratio* of $A$.

## Remarks

Example: for minimum [[vertex cover|0AHKWBQSWV]] in a graph, take a maximal [[matching|0MJ04A50QW]] $M$ greedily and output both ends of each edge of $M$.
The output covers every edge, since an uncovered edge could be added to $M$.
Every vertex cover contains an end of each edge of $M$, and these ends are distinct, so $\mathrm{OPT} \ge \abs{M}$, while the output has $2 \abs{M}$ vertices.
So this is a $2$-approximation algorithm.

Non-example: an exact algorithm that tries all subsets of vertices satisfies clauses 2 and 3 with $\rho = 1$, but it fails clause 1, since it takes exponential time.

A *polynomial-time approximation scheme* is a family of $(1 + \varepsilon)$-approximation algorithms, one for each $\varepsilon > 0$.
