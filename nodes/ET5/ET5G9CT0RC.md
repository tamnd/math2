---
tag: ET5G9CT0RC
kind: definition
name: Polytope
msc: [52B11, 52B05]
defines: QP7GEKDTYX
uses: [300K6CB1KH]
sources:
  - url: https://en.wikipedia.org/wiki/Polytope
---

## Definition

Let $n \ge 1$.
A *polytope* in $\R^n$ is a set $P = P_1 \cup \cdots \cup P_k$ that is the union of finitely many [[convex polytopes|300K6CB1KH]] $P_1, \ldots, P_k$ in $\R^n$.

## Remarks

Example: the L-shaped region $[0, 2] \times [0, 1] \cup [0, 1] \times [0, 2]$ is the union of two rectangles, which are convex polytopes, so it is a polytope.
It is not convex: it contains $(2, 1)$ and $(1, 2)$, but not their midpoint $(3/2, 3/2)$.
Non-example: the closed unit disc in $\R^2$ is not a polytope.
The boundary of a finite union of convex polygons lies in finitely many lines.
Each line meets the unit circle in at most two points, so this boundary cannot contain the whole circle.
Conventions differ between authors.
In convex geometry and in polyhedral combinatorics "polytope" usually means convex polytope, and some authors require a polytope to be a union of simplices that meet in common faces.
