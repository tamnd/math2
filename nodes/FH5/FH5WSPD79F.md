---
tag: FH5WSPD79F
kind: statement
role: theorem
name: Dehn's lemma
msc: [57K30, 57N35]
uses: [R20TB2KEQQ, QYEAZTYGPT, AQVHM3FP0D]
about: [R20TB2KEQQ]
sources:
  - url: https://en.wikipedia.org/wiki/Dehn%27s_lemma
same_as:
  wikidata: Q3229337
  wikipedia: Dehn's lemma
---

## Statement

Let $M$ be a [[3-manifold|R20TB2KEQQ]] and let $D$ be the closed $2$-disk.
Let $f \colon D \to M$ be a piecewise linear map.
Its singular set is the closure of the set of points $x \in D$ such that $f^{-1}(f(x))$ contains a point other than $x$.
If the singular set of $f$ does not meet $\partial D$, then there is a piecewise linear embedding $g \colon D \to M$ with $g = f$ on $\partial D$.

## Remarks

Dehn published a proof in 1910, and Kneser found a gap in it.
Papakyriakopoulos gave a proof in 1957 with his tower construction.
One lifts $f$ through a tower of double coverings of regular neighborhoods of its image, until the singularities can be removed at the top.
Then one pushes the embedded disk back down the tower.
A key application is to knots: a tame [[knot|QYEAZTYGPT]] $K$ in $S^3$ is trivial if and only if its [[knot group|AQVHM3FP0D]] is infinite cyclic.
If the knot group is $\Z$, the longitude of $K$ is null-homotopic in the complement, and Dehn's lemma turns a singular disk bounded by it into an embedded disk.

## Explanations

### L1 human

Suppose a loop in a $3$-dimensional space bounds a disk that may cross itself, but only away from its edge.
Dehn's lemma says that the loop then also bounds a disk that does not cross itself at all.
It turns information about homotopy into information about embedded surfaces.

### L2 human

Dehn's lemma, the loop theorem and the sphere theorem form the classical toolkit of $3$-manifold topology.
They all say that a map that is nontrivial up to homotopy can be replaced by an embedding.
They are used to show that an incompressible surface is the same as a two-sided surface whose inclusion is injective on fundamental groups.
