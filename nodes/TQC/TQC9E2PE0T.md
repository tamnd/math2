---
tag: TQC9E2PE0T
kind: example
name: Orthogonal Lie algebra
msc: [17B20, "22E60"]
instance_of: [5JJYBJ6A8K]
uses: [G8FEGYDSNE, 0PBY4E9GQF, 0TKYAEJ8N7]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_group
---

## Example

Let $k$ be a field and $n \ge 1$.
The *orthogonal Lie algebra* is
$$\mathfrak{so}_n(k) = \set{X \in \mathfrak{gl}_n(k) : X^T = -X},$$
the space of [[skew-symmetric matrices|0PBY4E9GQF]], with the bracket $[X, Y] = XY - YX$ of the [[general linear Lie algebra|G8FEGYDSNE]].

Check that it is closed under brackets: if $X^T = -X$ and $Y^T = -Y$, then
$$[X, Y]^T = Y^T X^T - X^T Y^T = YX - XY = -[X, Y].$$
For $\operatorname{char} k \ne 2$, a skew-symmetric matrix has zero diagonal, and $\dim \mathfrak{so}_n(k) = n(n-1)/2$.

For $n = 3$ and $k = \R$, let $L_1, L_2, L_3$ be the matrices of the maps $v \mapsto e_i \times v$, where $e_1, e_2, e_3$ is the standard basis.
They form a basis of $\mathfrak{so}_3(\R)$ with $[L_1, L_2] = L_3$, $[L_2, L_3] = L_1$, $[L_3, L_1] = L_2$.
So $\mathfrak{so}_3(\R)$ is isomorphic to $\R^3$ with the cross product.

## Remarks

For $k = \R$, $\mathfrak{so}_n(\R)$ is the Lie algebra of the [[orthogonal group|0TKYAEJ8N7]] $O(n)$ and of its identity component $SO(n)$.
Differentiating $A(t)^T A(t) = I$ at $t = 0$ with $A(0) = I$ gives $X^T + X = 0$ for $X = A'(0)$.
More generally, for a symmetric bilinear form with matrix $S$, the condition is $X^T S + S X = 0$.

## Explanations

### L1 human

Rotations of space form the orthogonal group.
Their infinitesimal versions, the angular velocities, are the skew-symmetric matrices.
In three dimensions an angular velocity is a vector $\omega$, acting by $v \mapsto \omega \times v$.
The bracket of two such matrices then corresponds to the cross product of the vectors.
