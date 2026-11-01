---
tag: 44KMEHYN1R
kind: counterexample
name: Sorgenfrey plane
msc: [54G20, 54D15, 54B10]
uses: [Y4T3GVK8GV, 0GBG8B49AA, 0NSR9V8TED, 0Z2P41SVDP, 0ZCK8DQYN1, SW0SN1NEJE]
sources:
  - url: https://en.wikipedia.org/wiki/Sorgenfrey_plane
---

## Counterexample

The Sorgenfrey plane is the product $\R_\ell \times \R_\ell$ of two copies of the [[Sorgenfrey line|Y4T3GVK8GV]] with the [[product topology|0GBG8B49AA]].
Each factor is normal, but the Sorgenfrey plane is not [[normal|0NSR9V8TED]].

## Remarks

The basic open sets are the half-open rectangles $[a, b) \times [c, d)$.
The anti-diagonal $D = \set{(x, -x) : x \in \R}$ is [[closed|0ZCK8DQYN1]], since it is closed in the coarser Euclidean topology.
It is discrete: the rectangle $[x, x + 1) \times [-x, -x + 1)$ meets $D$ only in $(x, -x)$.
The plane is [[separable|0Z2P41SVDP]], because $\Q \times \Q$ is dense.
By Jones' lemma, a separable normal space has no closed discrete subset $D$ with $2^{\abs{D}} > 2^{\aleph_0}$.
Here $\abs{D} = 2^{\aleph_0}$, so the plane is not normal.
Concretely, the points of $D$ with rational first coordinate and those with irrational first coordinate form two disjoint closed sets that no disjoint open sets separate.
The plane also shows that a product of two [[Lindelöf|SW0SN1NEJE]] spaces need not be Lindelöf.

## Explanations

### L1 human

The Sorgenfrey line is a well-behaved space.
Multiplying it by itself gives a plane in which two disjoint closed sets cannot be pulled apart by open sets.
So normality is a property that does not survive products.
The trouble sits on the line $y = -x$, where the half-open rectangles touch the line in only one point each.
