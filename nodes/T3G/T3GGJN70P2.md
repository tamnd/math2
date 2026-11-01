---
tag: T3GGJN70P2
kind: statement
role: theorem
name: Sylvester–Gallai theorem
msc: [52C10, 52C30, 51A20]
uses: [0XW7V9ZZ05]
about: [0XW7V9ZZ05]
sources:
  - url: https://en.wikipedia.org/wiki/Sylvester%E2%80%93Gallai_theorem
same_as:
  wikidata: Q748233
  wikipedia: Sylvester–Gallai theorem
---

## Statement

Let $S$ be a finite set of points in the [[Euclidean plane|0XW7V9ZZ05]].
Suppose that the points of $S$ do not all lie on one line.
Then there is a line that contains exactly two points of $S$.

## Remarks

A line that contains exactly two points of $S$ is called an ordinary line.
Kelly's proof considers all pairs of a point $p \in S$ and a line $\ell$ through two points of $S$ with $p \notin \ell$.
It takes a pair with the least distance from $p$ to $\ell$.
Suppose $\ell$ contained three points of $S$.
Then two of them would lie on the same side of the foot of the perpendicular from $p$, or one of them at the foot.
This gives a pair with a smaller positive distance, a contradiction; so $\ell$ is ordinary.
The hypothesis that $S$ is finite is needed: the integer lattice $\Z^2$ has no ordinary line.
The theorem also fails over the complex numbers.
The nine inflection points of a smooth complex cubic curve form a configuration in which every line through two of them contains a third.
For example, the four vertices of a square have ordinary lines: each side contains exactly two of the vertices.
Green and Tao proved that for all sufficiently large $n$, a set of $n$ points not all on a line has at least $n/2$ ordinary lines.

## Explanations

### L1 human

Scatter finitely many points in the plane, not all on one straight line.
Then you can always find a line passing through exactly two of the points.
This is easy to believe but hard to prove without a clever idea.

### L2 human

The Sylvester–Gallai theorem is a starting point of combinatorial incidence geometry, like the [[Szemerédi–Trotter theorem|NQBWFSC1E0]].
A corollary is that $n$ points not all on a line determine at least $n$ distinct lines.
Its failure over $\C$ and over finite fields shows that it depends on the order structure of the real numbers.
