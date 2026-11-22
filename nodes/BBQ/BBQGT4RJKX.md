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

Let $V = \R^3$, let $U = \{(0, y, z)\}$ be the $yz$-plane, and let $W = \{(0, 0, z)\}$ be the $z$-axis, so that $W \subseteq U \subseteq V$.
We check the [[third isomorphism theorem|07RB3EMBWW]] and the [[correspondence theorem|GCHY414Y11]] for this chain.

1. The map $(x, y, z) + W \mapsto (x, y)$ is an [[isomorphism|0XSJ25Z9M4]] $V / W \cong \R^2$.
   Two vectors have the same coset modulo $W$ exactly when they differ by some $(0, 0, t)$, that is, when they have the same $x$ and the same $y$.
2. Under this isomorphism, $U / W = \{(0, y, z) + W\}$ becomes the line $L = \{(0, y)\}$ of $\R^2$.
3. So $(V / W) / (U / W) \cong \R^2 / L$.
   Two points of $\R^2$ differ by a vector of $L$ exactly when they have the same first entry, so $\R^2 / L \cong \R$ through $(x, y) + L \mapsto x$.
4. On the other side, two vectors of $\R^3$ differ by a vector of $U$ exactly when they have the same $x$, so $V / U \cong \R$ through $(x, y, z) + U \mapsto x$.
5. The map of the theorem sends $\big((x, y, z) + W\big) + U / W$ to $(x, y, z) + U$, and both have the label $x$.
   In these coordinates it is the identity map of $\R$, so it is an isomorphism.

The correspondence theorem matches the subspaces of $V / W \cong \R^2$ with the subspaces of $\R^3$ that contain the $z$-axis.
We list the matching by dimension.

6. The zero subspace of $\R^2$ corresponds to $W$ itself.
7. A line $\R(a, b)$ of $\R^2$, with $(a, b) \ne (0, 0)$, corresponds to the plane spanned by $(a, b, 0)$ and $(0, 0, 1)$.
   This plane contains the $z$-axis, and its image in $\R^2$ is the line $\R(a, b)$.
8. The whole plane $\R^2$ corresponds to $\R^3$.
9. The line $L$ of step 2, which is $\R(0, 1)$, corresponds to the plane spanned by $(0, 1, 0)$ and $(0, 0, 1)$, which is $U$, as it should.

## Remarks

The dimensions agree with the [[dimension of a quotient space|0SXDQ6TN00]]: $\dim \big((V / W) / (U / W)\big) = 2 - 1 = 1$ and $\dim (V / U) = 3 - 2 = 1$.

A plane of $\R^3$ that does not contain the $z$-axis, such as the $xy$-plane, has no place of its own in the correspondence.
Its image in $V / W$ is all of $\R^2$, because $(x, y, 0) + W$ already hits every pair $(x, y)$.
That image corresponds to $\R^3$, which is the sum of the $xy$-plane and the $z$-axis.

If we replace $U$ by the plane spanned by $(1, 1, 0)$ and $(0, 0, 1)$, the same steps work with the line $\R(1, 1)$ in place of $L$.
Then both $\R^2 / \R(1, 1)$ and $V / U$ are measured by $x - y$ in place of $x$.

## Explanations

### L1 human

Squashing the $z$-axis to a point flattens space onto a plane, the $xy$-plane seen from above.
The $yz$-plane, seen from above, is now just the $y$-axis of that flat picture.
Squashing that line as well leaves only the $x$-coordinate.
Squashing the $yz$-plane at once, without the first step, also leaves only the $x$-coordinate, and that is the third isomorphism theorem.

### L2 human

The correspondence matches the planes through the $z$-axis with the lines through the origin of the quotient plane $V / W$.
Each plane through the $z$-axis is a union of vertical lines, and each vertical line becomes a single point of the quotient.
So a vertical plane turns into a line of points, and different vertical planes turn into different lines.
The trap is to try to match every plane of $\R^3$ in this way; only the planes that contain the $z$-axis are unions of whole vertical lines.
