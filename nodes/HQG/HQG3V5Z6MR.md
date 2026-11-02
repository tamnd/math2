---
tag: HQG3V5Z6MR
kind: statement
role: lemma
name: Sperner's lemma
msc: ["05E45", 55M20]
uses: [V8GZ0W1ZZ5, 0FQSDC2EQ2]
about: [V8GZ0W1ZZ5]
sources:
  - url: https://en.wikipedia.org/wiki/Sperner's_lemma
same_as:
  wikidata: Q733336
  wikipedia: Sperner's lemma
---

## Statement

Let $n \ge 1$ and let $\Delta$ be an $n$-simplex in $\R^n$ with vertices $v_0, \ldots, v_n$.
Let $T$ be a triangulation of $\Delta$ by a finite [[simplicial complex|V8GZ0W1ZZ5]].
Let $\lambda$ be a colouring of the vertices of $T$ by $\set{0, 1, \ldots, n}$.
Assume the following for every set $S \subseteq \set{0, \ldots, n}$.
Each vertex of $T$ in the face $\operatorname{conv}\set{v_i : i \in S}$ of $\Delta$ has a colour in $S$, where $\operatorname{conv}$ is the [[convex hull|0FQSDC2EQ2]].
Then the number of $n$-simplices of $T$ whose vertices carry all $n + 1$ colours is odd; in particular there is at least one.

## Remarks

The proof is by induction on $n$ with a parity count.
Call an $(n-1)$-face of $T$ a door if its vertices carry exactly the colours $0, \ldots, n-1$.
Count pairs (an $n$-simplex of $T$, a door in it).
A fully coloured simplex has one door, and any other simplex has zero or two.
An interior door lies in two simplices, while a boundary door lies in one.
All boundary doors lie in the face $\operatorname{conv}\set{v_0, \ldots, v_{n-1}}$, where their number is odd by induction; so the number of fully coloured simplices is odd.

Example: for $n = 1$, subdivide a segment from $v_0$ to $v_1$ and colour $v_0$ with $0$, $v_1$ with $1$, and the inner points freely.
The colour changes an odd number of times along the segment, so an odd number of small segments have both colours.

The boundary condition is needed: if every vertex of $T$ gets the colour $0$, there is no fully coloured simplex.

## Explanations

### L1 human

Cut a triangle into small triangles and colour every corner red, green or blue.
Colour the three big corners with the three colours, and colour each point on a big side with one of the two colours at the ends of that side.
Then some small triangle has all three colours, and in fact the number of such triangles is odd.

### L2 human

Sperner's lemma is a discrete form of the [[Brouwer fixed-point theorem|N7AAJ2MW5T]]: applying it to finer and finer triangulations and passing to a limit gives a fixed point.
Its constructive proof by following doors gives algorithms for approximate fixed points and for economic equilibria.
It is also used for fair division problems, such as envy-free cake cutting.
