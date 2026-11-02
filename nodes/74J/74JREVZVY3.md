---
tag: 74JREVZVY3
kind: definition
name: Eulerian poset
msc: [06A07, 52B05]
defines: N1Q0BJAEFX
uses: [1C7TKGTB2F, B0QT3SM5DT, 2Y75S8NG5B]
sources:
  - url: https://en.wikipedia.org/wiki/Eulerian_poset
---

## Definition

Let $P$ be a finite [[graded poset|1C7TKGTB2F]] with rank function $\rho$.
Assume that $P$ is [[bounded|B0QT3SM5DT]], with a least element $\hat 0$ and a greatest element $\hat 1$.
For $x \le y$ in $P$, let $[x, y] = \set{z \in P : x \le z \le y}$.
The poset $P$ is *Eulerian* when for all $x < y$ in $P$, the interval $[x, y]$ has as many elements of even rank as of odd rank.

## Remarks

Equivalently, the [[Möbius function|2Y75S8NG5B]] of $P$ is $\mu(x, y) = (-1)^{\rho(y) - \rho(x)}$ for all $x \le y$.

Example: the lattice of subsets of a finite set $S$, with $\rho(A) = \abs{A}$.
Check: for $A \subsetneq B$ with $\abs{B \setminus A} = k \ge 1$, the interval $[A, B]$ has $\sum_{j \text{ even}} \binom{k}{j} = 2^{k-1}$ elements of each parity of rank.

Non-example: the chain $0 < 1 < 2$ with $\rho(i) = i$ is graded and bounded, but the interval $[0, 2]$ has two elements of even rank and one of odd rank.

Every interval of an Eulerian poset is again Eulerian.
The face lattice of a convex polytope is Eulerian.
