---
tag: 6X2D0JDFQW
kind: statement
role: theorem
name: Invariance of domain
msc: [55M10, 54C05]
uses: [0XPR1E85W0, 02BH3MCBQB, 0VGFHTM75Y, 09NWETVTNY, 0QT00PB5G2]
about: [02BH3MCBQB, 0QT00PB5G2]
sources:
  - url: https://en.wikipedia.org/wiki/Invariance_of_domain
same_as:
  wikidata: Q3527201
  wikipedia: Invariance of domain
---

## Statement

Let $n \ge 1$, let $U$ be an [[open subset|02BH3MCBQB]] of [[$\R^n$|0XPR1E85W0]], and let $f \colon U \to \R^n$ be a [[continuous|0VGFHTM75Y]] [[injective|09NWETVTNY]] map.
Then $f(U)$ is open in $\R^n$, and $f$ is a [[homeomorphism|0QT00PB5G2]] from $U$ onto $f(U)$.

## Remarks

For $n = 1$ the claim follows from the intermediate value theorem, since $f$ is then strictly monotone on each interval in $U$; so let $n \ge 2$.
It suffices to show that, for every closed ball $B \subseteq U$, the image $f(B \setminus \partial B)$ of its interior is open.
The image $f(\partial B)$ is homeomorphic to the sphere $S^{n-1}$, so by the [[Jordan–Brouwer separation theorem|2Q008XWQDE]] its complement has two components, a bounded one and an unbounded one.
A homology argument shows that $f(B \setminus \partial B)$ is connected and disjoint from $f(\partial B)$ and that $\R^n \setminus f(B)$ is connected, which forces $f(B \setminus \partial B)$ to be the bounded component, an open set.
The second claim follows from the first, since $f$ then maps open subsets of $U$ to open sets.

Example: it implies invariance of dimension, that is, $\R^m$ and $\R^n$ are not homeomorphic if $m < n$.
Indeed, a homeomorphism $\R^n \to \R^m \subset \R^n$ would have an open image inside the hyperplane $\R^m \times \set{0}$.
But this hyperplane has empty interior in $\R^n$.

Both hypotheses are needed.
Without injectivity, $f(x) = x^2$ on $\R$ has image $[0, \infty)$, which is not open.
The target must have the same dimension: the map $x \mapsto (x, 0)$ from $\R$ to $\R^2$ is continuous and injective, but its image is not open in $\R^2$.

## Explanations

### L1 human

A continuous one-to-one map from an open piece of $n$-dimensional space into $n$-dimensional space cannot squash anything flat or tear it open.
Its image is again an open piece, and the map can be undone continuously.

### L2 human

The theorem shows that the dimension of a topological manifold is well defined.
It also shows that a continuous bijection between manifolds of the same dimension without boundary is a homeomorphism.
It is false in infinite dimensions: on a Hilbert space, the shift operator is a continuous injective linear map whose image is not open.
It is usually proved with homology, through the Jordan–Brouwer separation theorem, or with the Brouwer fixed point theorem.
