---
tag: QWXTB8VVXN
kind: statement
role: theorem
name: Frankel conjecture
msc: [32Q10, 53C55]
uses: [X60JG9AEQJ, JSGWAN2RJV]
about: [X60JG9AEQJ]
sources:
  - url: https://en.wikipedia.org/wiki/Frankel_conjecture
same_as:
  wikidata: Q104862566
  wikipedia: Frankel conjecture
---

## Statement

Let $X$ be a compact [[Kähler manifold|X60JG9AEQJ]] of complex dimension $n$, with Kähler metric $g$ and curvature tensor $R$.
Suppose that $g$ has positive holomorphic bisectional curvature: $R(u, \bar u, v, \bar v) > 0$ for every point $p \in X$ and all nonzero $u, v \in T^{1,0}_p X$.
Then $X$ is biholomorphic to complex projective space $\mathbb{CP}^n$.

## Remarks

Frankel stated the conjecture in 1961 for compact Kähler manifolds of positive sectional curvature; the version above uses the weaker hypothesis of positive bisectional curvature.
It was proved in 1979 by Mori, as a consequence of his proof of the Hartshorne conjecture that a smooth projective variety with ample tangent bundle is a projective space.
Independently, Siu and Yau gave a differential-geometric proof in 1980, using energy-minimizing harmonic maps from $\mathbb{CP}^1$ to produce rational curves.

Example: the Fubini–Study metric on [[complex projective space|7GJ4STCNNM]] has constant positive holomorphic sectional curvature and positive bisectional curvature, so $\mathbb{CP}^n$ satisfies the hypothesis.

Positive Ricci curvature is not enough.
The product $\mathbb{CP}^1 \times \mathbb{CP}^1$ with the product of Fubini–Study metrics has positive Ricci curvature, but its bisectional curvature vanishes for $u$ tangent to the first factor and $v$ to the second.
It is not biholomorphic to $\mathbb{CP}^2$, since its second Betti number is $2$, while that of $\mathbb{CP}^2$ is $1$.

## Explanations

### L1 human

Positive curvature makes a space round, like a sphere.
The Frankel conjecture, now a theorem, says that in Kähler geometry a strong form of positive curvature leaves only one possibility: the space is complex projective space.
It is a complex analogue of the sphere theorems of Riemannian geometry.

### L2 human

Holomorphic bisectional curvature compares two complex directions at a point; it is weaker than sectional curvature and stronger than Ricci curvature.
Mori's proof works in algebraic geometry: positivity makes the tangent bundle ample, and then one finds and bends rational curves to recognize $\mathbb{CP}^n$.
Mori's method of bending rational curves became a basis of the minimal model program.
The theorem was later extended by Mok to compact Kähler manifolds of nonnegative bisectional curvature, which are built from projective spaces, Hermitian symmetric spaces and flat tori.
