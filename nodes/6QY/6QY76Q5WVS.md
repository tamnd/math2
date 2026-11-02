---
tag: 6QY76Q5WVS
kind: statement
role: theorem
name: Mahler's compactness theorem
msc: [11H06, "22E40"]
uses: [WN9V7WSJKF, 0R6EWFKRCF, 0BR3FY5Q8M]
about: [WN9V7WSJKF]
sources:
  - url: https://en.wikipedia.org/wiki/Mahler's_compactness_theorem
same_as:
  wikidata: Q6734194
  wikipedia: Mahler's compactness theorem
---

## Statement

Let $n \ge 1$, and let $\mathcal{L}_n$ be the set of [[lattices|WN9V7WSJKF]] in $\R^n$.
Identify $\mathcal{L}_n$ with the [[quotient space|0BR3FY5Q8M]] $\mathrm{GL}_n(\R)/\mathrm{GL}_n(\Z)$, by sending $g$ to the lattice $g\Z^n$, and give it the quotient topology.
Let $A \subseteq \mathcal{L}_n$.
Then $A$ has [[compact|0R6EWFKRCF]] closure in $\mathcal{L}_n$ if and only if there are constants $C > 0$ and $\varepsilon > 0$ such that for every $\Lambda \in A$:

1. the covolume of $\Lambda$ is at most $C$;
2. every nonzero vector $v \in \Lambda$ has $\norm{v} \ge \varepsilon$.

## Remarks

The proof uses reduction theory.
Under the two bounds, each lattice of $A$ has a reduced basis whose vectors have length bounded above and below, with angles bounded away from $0$.
Such bases form a compact set of matrices, whose image in $\mathcal{L}_n$ contains $A$.
The converse holds because covolume and the length of a shortest nonzero vector are continuous on $\mathcal{L}_n$.

Example: the lattices $\Lambda_t = \Z (t, 0) \oplus \Z (0, 1/t)$ in $\R^2$ have covolume $1$.
Their shortest nonzero vector has length $t$ for $0 < t \le 1$.
As $t \to 0$ condition 2 fails, and indeed $\Lambda_t$ leaves every compact subset of $\mathcal{L}_2$.

Both conditions are needed.
The lattices $t\Z^2$ with $t \to \infty$ satisfy condition 2 but not condition 1, and they also leave every compact set.

## Explanations

### L1 human

A lattice in the plane is a regular grid of points.
The theorem says when a family of grids stays within a bounded region of the space of all grids.
The grids must not have too large a cell, and they must not have two points too close together.
A grid that degenerates, by squashing in one direction, always produces short vectors.

### L2 human

For unimodular lattices, condition 1 is automatic, so a set of unimodular lattices is relatively compact exactly when the lattices avoid a fixed ball around $0$.
This gives the basic criterion for divergence in the homogeneous space $\mathrm{SL}_n(\R)/\mathrm{SL}_n(\Z)$.
It is used in homogeneous dynamics, for example in the non-divergence results of Margulis and Dani for unipotent flows, and in Diophantine approximation through Dani's correspondence.
