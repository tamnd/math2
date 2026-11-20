---
tag: BBQGT4RJKX
kind: example
name: Quotients along the chain z-axis, yz-plane, R³
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
instance_of: [0BR3FY5Q8M]
illustrates: [07RB3EMBWW, GCHY414Y11]
uses: [0SVR29SV1V, 0XSJ25Z9M4]
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem C (modules)
---

## Example

Let $V = \R^3$, let $U = \{(0, y, z)\}$ be the $yz$-plane, and let $W = \{(0, 0, z)\}$ be the $z$-axis, so $W \subseteq U$.
We check the [[third isomorphism theorem|07RB3EMBWW]] and the [[correspondence theorem|GCHY414Y11]].

1. The map $(x, y, z) + W \mapsto (x, y)$ is an [[isomorphism|0XSJ25Z9M4]] $V / W \cong \R^2$, since two vectors have the same coset modulo $W$ exactly when they have the same $x$ and $y$.
2. Under this isomorphism, $U / W = \{(0, y, z) + W\}$ becomes the line $L = \{(0, y)\}$ in $\R^2$.
3. So $(V / W)/(U / W) \cong \R^2 / L$, and $\R^2 / L \cong \R$ through $(x, y) + L \mapsto x$.
4. On the other side, $V / U \cong \R$ through $(x, y, z) + U \mapsto x$.
5. The map of the theorem sends $\big((x, y, z) + W\big) + U/W$ to $(x, y, z) + U$, and both have label $x$. So it is an isomorphism.

For the [[correspondence theorem|GCHY414Y11]], the subspaces of $V / W \cong \R^2$ are matched with the subspaces of $\R^3$ that contain the $z$-axis.

6. The zero subspace of $\R^2$ corresponds to $W$.
7. A line $\R(a, b)$ in $\R^2$ corresponds to the plane spanned by $(a, b, 0)$ and $(0, 0, 1)$, which contains the $z$-axis.
8. The whole $\R^2$ corresponds to $\R^3$.
9. The line $L$ of step 2 corresponds to $U$, as it should.

## Remarks

The dimensions agree: $\dim\big((V / W)/(U / W)\big) = 2 - 1 = 1$ and $\dim(V / U) = 3 - 2 = 1$.
A plane of $\R^3$ that does not contain the $z$-axis, such as the $xy$-plane, does not appear in the correspondence.
Its image in $V / W$ is all of $\R^2$, which corresponds to $\R^3$ instead.

## Explanations

### L1 human

Squashing the $z$-axis flattens space to a plane.
Squashing next the image of the $yz$-plane, a line in that plane, leaves a line.
Squashing the $yz$-plane at once gives the same line.

### L2 human

The correspondence matches the planes through the $z$-axis with the lines through the origin in the quotient plane.
Each such plane is a union of vertical lines, and each vertical line becomes a point of the quotient.
