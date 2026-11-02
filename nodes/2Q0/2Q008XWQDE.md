---
tag: 2Q008XWQDE
kind: statement
role: theorem
name: Jordan–Brouwer separation theorem
msc: [55M05, 57N35]
uses: [0XPR1E85W0, T62369RFH6, 0QT00PB5G2, 0V032VWTHD, 05D5EGMFYV]
about: [T62369RFH6, 0V032VWTHD]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_curve_theorem
---

## Statement

Let $n \ge 1$ and let $X \subseteq \R^{n+1}$ be a subset [[homeomorphic|0QT00PB5G2]] to the [[$n$-sphere|T62369RFH6]] $S^n$.
Then the complement $\R^{n+1} \setminus X$ has exactly two [[connected components|0V032VWTHD]], one bounded and one unbounded, and $X$ is the [[boundary|05D5EGMFYV]] of each of them.

## Remarks

The proof uses [[Alexander duality|KK05CSTM15]] in $S^{n+1} = \R^{n+1} \cup \set{\infty}$.
It gives $\tilde{H}_0(S^{n+1} \setminus X; \Z) \cong \tilde{H}^n(X; \Z) \cong \Z$, with Čech cohomology on the right.
So $S^{n+1} \setminus X$ has two path components, which are open, hence also its connected components.
Removing the point $\infty$ from the component that contains it does not disconnect it, since $n + 1 \ge 2$.
For $n = 1$ the theorem is the Jordan curve theorem in the plane.

Example: the unit sphere $S^n$ itself separates $\R^{n+1}$ into the open unit ball and the set $\set{x : \norm{x} > 1}$.

For $n \ge 2$ the theorem says nothing about the shape of the components.
For the Alexander horned sphere in $\R^3$, the unbounded component is not simply connected, unlike the outside of a round sphere.
The Schoenflies theorem, which says that the bounded component is an open disc, holds for $n = 1$ but needs extra hypotheses, such as local flatness, for $n \ge 2$.
The case $n = 0$ is excluded: two points on the line $\R$ leave three components.

## Explanations

### L1 human

A closed surface in space without self-intersections, however crumpled, has an inside and an outside.
To get from the inside to the outside you must cross the surface, and every point of the surface touches both sides.

### L2 human

The theorem is one of the first applications of homology to geometry.
It is used to prove [[invariance of domain|6X2D0JDFQW]], and through it the topological invariance of dimension.
The contrast with the Schoenflies problem shows that homology can detect the number of components but not their homeomorphism type.
