---
tag: ~1b1da4fe
kind: definition
name: Linear map
msc: [15A04]
defines: ~2402e937
uses: [~dddb6485]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Definition and first consequences
---

## Definition

Let $F$ be a field and let $V$ and $W$ be [[vector spaces|~d0f609e9]] over $F$.
A map $T \colon V \to W$ is *linear* when, for all $u, v \in V$ and $a \in F$,
$$T(u + v) = T(u) + T(v), \qquad T(av) = a\, T(v).$$
A linear map is also called a *linear transformation*.

## Remarks

A linear map sends $0$ to $0$ and linear combinations to linear combinations: $T(\sum a_i v_i) = \sum a_i T(v_i)$.
For an $m \times n$ matrix $A$, the map $F^n \to F^m$, $x \mapsto Ax$, is linear.
Rotations of $\R^2$ about the origin are linear; translations by a nonzero vector are not linear.
Each linear map between finite-dimensional spaces has a [[matrix|~64faa62e]] in a choice of bases.

## Explanations

### L1 human

A linear map respects the two operations of a vector space.
The image of a sum is the sum of the images, and the image of a scaled vector is the scaled image.
In the plane, linear maps send lines through the origin to lines through the origin, or to the origin, and keep parallel lines parallel.
