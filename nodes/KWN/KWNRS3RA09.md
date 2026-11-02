---
tag: KWNRS3RA09
kind: statement
role: theorem
name: Thom transversality theorem
msc: [57R35, 58A20, 57R45]
uses: [F45VQ47GPV, VKFW27WXEZ, A2PDZ8GA9C, GRH8MCVN3N]
about: [A2PDZ8GA9C]
sources:
  - url: https://en.wikipedia.org/wiki/Transversality_theorem
---

## Statement

Let $X$ and $Y$ be [[smooth manifolds|F45VQ47GPV]], let $k \ge 0$, and let $J^k(X, Y)$ be the [[jet bundle|HC3VBBCJQP]] of $k$-jets of smooth maps from $X$ to $Y$.
For a smooth map $f \colon X \to Y$, let $j^k f \colon X \to J^k(X, Y)$ be its $k$-jet extension, which sends $x$ to the $k$-jet of $f$ at $x$.
Let $W$ be an [[embedded submanifold|VKFW27WXEZ]] of $J^k(X, Y)$.
Give $C^\infty(X, Y)$ the Whitney $C^\infty$ topology.
Then the set of maps $f \in C^\infty(X, Y)$ such that $j^k f$ is [[transverse|A2PDZ8GA9C]] to $W$ is a [[residual set|GRH8MCVN3N]] in $C^\infty(X, Y)$, and in particular it is dense.

## Remarks

For $k = 0$ one has $J^0(X, Y) = X \times Y$, and with $W = X \times Z$ the theorem says that maps transverse to a submanifold $Z \subseteq Y$ are generic.
The space $C^\infty(X, Y)$ with the Whitney topology is a Baire space, so a residual set is dense.
The proof reduces to the parametric transversality theorem.
If a smooth family $F \colon X \times S \to Y$ is transverse to $Z$, then $F(\cdot, s)$ is transverse to $Z$ for almost every $s$.
This follows from Sard's theorem applied to the projection $F^{-1}(Z) \to S$.
Locally one adds polynomial terms of degree at most $k$ to $f$, which moves $j^k f$ in all directions of the fibre.
Example: let $k = 1$ and let $W$ be the set of $1$-jets whose linear part has rank $r$.
The theorem shows that for a generic $f$ the set of points where $df$ has rank $r$ is a submanifold of the expected codimension.
This is how Whitney's results on generic singularities are obtained.

## Explanations

### L1 human

A typical smooth map is in general position with respect to any fixed condition on its derivatives.
Whatever submanifold one fixes in the space of jets, most maps meet it cleanly, and one can always reach such a map by an arbitrarily small change.
So in proofs one may assume that the maps one works with are transverse to whatever one likes.

### L2 human

The theorem is the source of most genericity statements in differential topology and singularity theory.
With $k = 0$ it gives transversality of maps to submanifolds, which is used to define intersection numbers and the Pontryagin–Thom construction.
With $k = 1$ it shows that generic maps have only mild singularities, for instance that Morse functions are dense and that generic maps $M^n \to \R^{2n}$ are immersions.
With higher $k$ it is the starting point of the classification of stable singularities.
