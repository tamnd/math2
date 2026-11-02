---
tag: D75XZC18PP
kind: statement
role: theorem
name: Beck's theorem
msc: [52C10, 52C30]
uses: [0XW7V9ZZ05, 0MP9BCF6DP, 0AFNNTRTJE, NQBWFSC1E0]
about: [0AFNNTRTJE]
sources:
  - url: https://en.wikipedia.org/wiki/Beck%27s_theorem_(geometry)
same_as:
  wikidata: Q3527011
  wikipedia: Beck's theorem (geometry)
---

## Statement

There are constants $c_1 > 0$ and $c_2 > 0$ with the following property.
Let $P$ be a finite set of $n$ points in the [[Euclidean plane|0XW7V9ZZ05]].
Say that a [[line|0MP9BCF6DP]] is *determined* by $P$ if it contains at least two points of $P$.
Then at least one of the following holds.

1. Some line contains at least $c_1 n$ points of $P$.
2. $P$ determines at least $c_2 n^2$ distinct lines.

## Remarks

The proof counts pairs of points of $P$ according to the number of points on the line through them.
The [[Szemerédi–Trotter theorem|NQBWFSC1E0]] bounds the number of lines containing between $k$ and $2k$ points of $P$ by $O(n^2/k^3 + n/k)$.
Sum this bound over dyadic ranges of $k$.
Unless some line is very rich, a constant fraction of the $\binom{n}{2}$ pairs then lie on lines with few points.
Those lines are then of order $n^2$ in number.
Example: if $P$ consists of $n - 1$ [[collinear|0AFNNTRTJE]] points and one point off their line, clause 1 holds, while $P$ determines only $n$ lines.
If $P$ is the set of vertices of a regular $n$-gon, no line contains more than $2$ points, so clause 2 must hold; indeed all $\binom{n}{2}$ lines are distinct.

## Explanations

### L1 human

Take $n$ points in the plane.
Either many of them lie on one line, or the points determine a huge number of lines, about as many as there are pairs of points.
There is no middle ground where the points are spread out but determine few lines.

### L2 human

József Beck proved the theorem in 1983, and it is a standard application of the Szemerédi–Trotter incidence bound.
A consequence is a weak form of Dirac's conjecture: some point of $P$ lies on at least $c n$ of the lines determined by $P$, unless most points are collinear.
It belongs to the circle of results around the [[Sylvester–Gallai theorem|T3GGJN70P2]] and the orchard-planting problem, which count lines with few points.
