---
tag: ~d4a0af0b
kind: statement
role: theorem
name: The medians meet at the centroid
msc: [51M04]
uses: [~b5525f68, ~66b2a048]
sources:
  - url: https://en.wikipedia.org/wiki/Centroid
    locator: Of a triangle
  - url: https://en.wikipedia.org/wiki/Median_(geometry)
    locator: Relation to center of mass
---

## Statement

Let $ABC$ be a triangle in the Euclidean space $\mathbb{R}^n$, and let $G = \frac{1}{3}(A + B + C)$ be its [[centroid|~66b2a048]].
Then $G$ lies on each of the three [[medians|~b5525f68]] of $ABC$.
More precisely, let $M_A$ be the midpoint of $B$ and $C$. Then $G = A + \frac{2}{3}(M_A - A)$, and the same holds for the vertices $B$ and $C$.

## Remarks

The formula shows that $G$ divides each median in the ratio $2 : 1$, counted from the vertex.
The proof is one line: $A + \frac{2}{3}\left(\frac{B + C}{2} - A\right) = \frac{1}{3}(A + B + C)$.
The statement is true in each affine space over a field in which $2$ and $3$ are invertible. Mathlib states it for each simplex.

## Explanations

### L1 human

Draw the three medians of a paper triangle. They always cross at one point. This point is two thirds of the way from each vertex to the middle of the opposite side.
