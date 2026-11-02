---
tag: 56YF8W9NXP
kind: statement
role: theorem
name: h-cobordism theorem
msc: [57R80, 57R65]
uses: [F45VQ47GPV, T8BVGPPSZP, XZG6MTSWCN, S1XK3HXHFX, 0KZZ70ZHXP]
about: [T8BVGPPSZP]
sources:
  - url: https://en.wikipedia.org/wiki/H-cobordism
---

## Statement

Let $n \ge 5$.
Let $W$ be a compact smooth $(n+1)$-manifold whose boundary is a disjoint union $\partial W = M_0 \sqcup M_1$ of two closed $n$-manifolds.
Assume that $W$ is an *h-cobordism*: both inclusions $M_0 \hookrightarrow W$ and $M_1 \hookrightarrow W$ are [[homotopy equivalences|XZG6MTSWCN]].
Assume also that $M_0$ is connected and [[simply connected|S1XK3HXHFX]].
Then $W$ is [[diffeomorphic|0KZZ70ZHXP]] to $M_0 \times [0, 1]$ by a diffeomorphism that is the identity on $M_0$.
In particular $M_0$ and $M_1$ are diffeomorphic.

## Remarks

The theorem is due to Smale.
Idea of the proof: a Morse function on $W$ gives a [[handle decomposition|9V11N8VVTP]] of $W$ on $M_0$.
The homotopy equivalence condition makes the handle chain complex acyclic, and handles are traded and cancelled in pairs until none remain.
Cancelling a pair needs the Whitney trick to remove extra intersection points of spheres in a level set.
The Whitney trick needs simple connectivity and level sets of dimension at least $5$.
A cobordism with no handles is a product.

The theorem at work: let $\Sigma$ be a smooth closed $m$-manifold homotopy equivalent to $S^m$ with $m \ge 6$.
Removing two disjoint open balls from $\Sigma$ gives an h-cobordism between two copies of $S^{m-1}$, which is therefore a product.
It follows that $\Sigma$ is homeomorphic to $S^m$, the [[generalized Poincaré conjecture|8KDV43WZ3Z]] in these dimensions.

Both extra hypotheses are needed.
Without simple connectivity there are h-cobordisms that are not products; the obstruction is the Whitehead torsion, see the [[s-cobordism theorem|E1E5ABP89W]].
For $n = 4$ the smooth statement fails: Donaldson found smooth $5$-dimensional h-cobordisms between simply connected $4$-manifolds that are not products.

## Explanations

### L1 human

Two manifolds are h-cobordant when they form the two ends of a bigger manifold that each end fills up, up to homotopy.
The theorem says that in high dimensions, when there are no loops to worry about, such a bigger manifold is just a cylinder.
So the two ends are the same manifold.
In this way the theorem proves the Poincaré conjecture in dimensions at least six.

### L2 human

The h-cobordism theorem converts a homotopy-theoretic condition into a diffeomorphism.
It is the base of the classification of high-dimensional manifolds through [[surgery theory|MHHN8386TG]]: surgery produces cobordisms, and the theorem shows that suitable cobordisms are products.
Its proof is the model application of Morse theory and handle cancellation.
The [[s-cobordism theorem|E1E5ABP89W]] extends it to manifolds with a nontrivial fundamental group.
In dimension $4$ the topological version holds by Freedman's work, but the smooth version fails.
