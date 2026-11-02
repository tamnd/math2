---
tag: 8YYJBVP68F
kind: statement
role: theorem
name: Loop theorem
msc: [57K30]
uses: [R20TB2KEQQ, 7DS6B2BFK8, S1XK3HXHFX, 0CB0DX5BVV, FH5WSPD79F]
about: [R20TB2KEQQ]
sources:
  - url: https://en.wikipedia.org/wiki/Loop_theorem
same_as:
  wikidata: Q3822213
  wikipedia: Loop theorem
---

## Statement

Let $M$ be a [[3-manifold|R20TB2KEQQ]] with boundary $\partial M$, and let $F \subseteq \partial M$ be a connected surface.
Let $N$ be a [[normal subgroup|0CB0DX5BVV]] of the [[fundamental group|S1XK3HXHFX]] $\pi_1(F)$.
Assume that the kernel of the map $\pi_1(F) \to \pi_1(M)$ induced by inclusion is not contained in $N$.
Then there is an embedding $g \colon (D^2, \partial D^2) \to (M, F)$ of the closed disk such that the loop $g|_{\partial D^2}$ represents an element of $\pi_1(F)$ that is not in $N$.

## Remarks

The version with $N$ is due to Stallings; Papakyriakopoulos proved the case $N = \set{1}$ in 1957.
The proof uses the same tower of double coverings as the proof of [[Dehn's lemma|FH5WSPD79F]].
Take $N = \set{1}$, and suppose some loop that is essential in $F$ becomes null-homotopic in $M$.
Then some embedded essential loop in $F$ bounds an embedded disk in $M$.
For example, if $M$ is a solid torus $D^2 \times S^1$ and $F$ is its boundary torus, the meridian disk $D^2 \times \set{1}$ is such a disk.

## Explanations

### L1 human

If a loop on the boundary of a $3$-dimensional space can be shrunk inside the space but not on the boundary, then there is an embedded disk that shows it.
The disk has its edge on the boundary and does not cross itself.
So an algebraic fact about loops produces a concrete geometric object.

### L2 human

The loop theorem is the reason why "compressible" can be tested with fundamental groups.
A two-sided surface in a $3$-manifold is incompressible exactly when its fundamental group injects into that of the manifold.
Together with Dehn's lemma and the sphere theorem, it is a basic step in the theory of Haken manifolds.
