---
tag: 0MCDDSCB9Z
kind: statement
role: theorem
name: Orthogonal projection is the closest point
msc: [46C05, 65F20]
uses: [0Q8HZTJC7G, 0KG4D8AP6G]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_projection_theorem
    locator: Finite dimensional case
---

## Statement

Let $V$ be an inner product space over $\R$ or $\C$, let $W$ be a finite-dimensional subspace of $V$, and let $v \in V$.
Let $P_W$ be the [[orthogonal projection|0B8KZRT28M]] onto $W$.
Then, for all $w \in W$,
$$\norm{v - P_W(v)} \le \norm{v - w},$$
with equality only for $w = P_W(v)$.

## Remarks

The proof: $v - w = (v - P_W(v)) + (P_W(v) - w)$ is a sum of orthogonal vectors, so the Pythagorean theorem applies.
The number $\norm{v - P_W(v)}$ is the distance from $v$ to $W$.
The Hilbert projection theorem gives the same result for closed convex sets in Hilbert spaces.
This is the basis of the method of [[least squares|0BYTQ4X1HC]].

## Explanations

### L1 human

The nearest point of a subspace to a given vector is the foot of the perpendicular.
Every other point of the subspace is farther away, by the Pythagorean theorem.
This turns problems of best approximation into problems of projection.
