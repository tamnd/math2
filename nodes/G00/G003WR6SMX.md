---
tag: G003WR6SMX
kind: statement
role: theorem
name: Cellular approximation theorem
msc: [57Q05, 55Q05]
uses: [5W95QFHXPR, F2F143KQ2M, ADDS6HE5SV]
about: [5W95QFHXPR]
sources:
  - url: https://en.wikipedia.org/wiki/Cellular_approximation_theorem
same_as:
  wikidata: Q5058350
  wikipedia: Cellular approximation theorem
---

## Statement

Let $X$ and $Y$ be [[CW complexes|5W95QFHXPR]] with $n$-skeleta $X^n$ and $Y^n$.
A map $g \colon X \to Y$ is *cellular* if $g(X^n) \subseteq Y^n$ for all $n \ge 0$.
Let $f \colon X \to Y$ be a continuous map, and let $A \subseteq X$ be a subcomplex such that $f$ restricted to $A$ is cellular.
Then $f$ is [[homotopic|F2F143KQ2M]] [[relative to|ADDS6HE5SV]] $A$ to a cellular map.

## Remarks

The proof proceeds cell by cell, by induction on the dimension.
The key lemma concerns a map from a closed $k$-disk into a space obtained by attaching an $n$-cell with $n > k$.
Such a map can be deformed so that it misses a point of the open cell, and then pushed off the cell by radial projection.
Taking $A = \emptyset$ shows that every map is homotopic to a cellular map.

Example: give $S^n$ the CW structure with one $0$-cell and one $n$-cell, and let $k < n$.
Every map $S^k \to S^n$ is homotopic to a cellular map, which sends $S^k = (S^k)^k$ into the $k$-skeleton of $S^n$, a single point.
So $\pi_k(S^n) = 0$ for $k < n$.

The theorem also shows that the inclusion $X^n \to X$ induces an isomorphism on $\pi_k$ for $k < n$ and a surjection for $k = n$.

## Explanations

### L1 human

A continuous map can be very wild, for example a curve can fill a whole square.
The theorem says that between CW complexes one can always straighten a map, up to homotopy, so that it sends low-dimensional cells into low-dimensional parts of the target.
This is why a loop in a sphere of dimension $2$ or more can always be shrunk to a point.

### L2 human

Cellular approximation reduces many homotopy questions to combinatorics of cells.
It gives the vanishing of $\pi_k(S^n)$ for $k < n$.
It shows that the fundamental group of a CW complex depends only on its $2$-skeleton.
It also makes the maps induced on cellular chain complexes well defined.
Its simplicial ancestor is the simplicial approximation theorem.
