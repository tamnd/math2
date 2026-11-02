---
tag: 4WX0HAK9X9
kind: definition
name: Graded poset
msc: [06A07]
defines: 1C7TKGTB2F
uses: [0QV2JS9RJ3, 4HHDPZ4BDY]
sources:
  - url: https://en.wikipedia.org/wiki/Graded_poset
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]].
For $x, y \in P$, say that $y$ covers $x$ when $x < y$ and no $z \in P$ satisfies $x < z < y$; this is the [[covering relation|4HHDPZ4BDY]].
A *rank function* on $P$ is a map $\rho \colon P \to \Z$ such that:

1. if $x < y$, then $\rho(x) < \rho(y)$;
2. if $y$ covers $x$, then $\rho(y) = \rho(x) + 1$.

A *graded poset* is a partially ordered set together with a rank function.

## Remarks

Example: the power set of a finite set, ordered by inclusion, is graded by $\rho(A) = \abs{A}$.
A subset $B$ covers $A$ exactly when $B = A \cup \set{b}$ with $b \notin A$, so the rank goes up by one.
Example: the positive divisors of an integer $n \ge 1$, ordered by divisibility, are graded by the number of prime factors counted with multiplicity.
Non-example: the [[pentagon lattice|DHC8TZXGYS]] with elements $0 < a < b < 1$ and $0 < c < 1$ has no rank function.
The covers $0, a, b, 1$ would give $\rho(1) = \rho(0) + 3$, while the covers $0, c, 1$ would give $\rho(1) = \rho(0) + 2$.
Some authors also require $\rho$ to take values in $\N$, or require all maximal chains to have the same length; the conventions should be checked in each source.
