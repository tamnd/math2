---
tag: SJ2BVG9F4W
kind: definition
name: Elliptic curve
msc: [14H52, 11G05, 11G07]
defines: 427N6S6QQW
uses: [04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_curve
---

## Definition

Let $K$ be a [[field|04C5ZBG1WT]].
An *elliptic curve over $K$* is a pair $(E, O)$ with two properties.
$E$ is a smooth projective curve over $K$ of genus $1$, and $O \in E(K)$ is a point of $E$ defined over $K$.

Equivalently, it is a curve in the projective plane given by a Weierstrass equation with $a_1, \ldots, a_6 \in K$:
$$y^2 + a_1 xy + a_3 y = x^3 + a_2 x^2 + a_4 x + a_6.$$
Its discriminant $\Delta$ must be nonzero, and $O = [0 : 1 : 0]$ is the point at infinity.
If the characteristic of $K$ is not $2$ or $3$, every elliptic curve has an equation $y^2 = x^3 + ax + b$ with $a, b \in K$, and the condition $\Delta \ne 0$ becomes $4a^3 + 27b^2 \ne 0$.

## Remarks

Example: $E \colon y^2 = x^3 - x$ over $\Q$.
Here $a = -1$, $b = 0$, and $4a^3 + 27b^2 = -4 \ne 0$, so the cubic $x^3 - x = x(x-1)(x+1)$ has three distinct roots and $E$ is smooth.

Non-example: $y^2 = x^3 + x^2$ has $\Delta = 0$.
Its projective closure has a node at $(0, 0)$, where both partial derivatives of $y^2 - x^3 - x^2$ vanish, so the smoothness condition fails.

The condition $4a^3 + 27b^2 \ne 0$ says that $x^3 + ax + b$ has no repeated root in an algebraic closure of $K$.
For $y^2 = x^3 + ax + b$ one has $\Delta = -16(4a^3 + 27b^2)$.
The set $E(K)$ of points over $K$, including $O$, is an abelian group with identity $O$ under the chord-and-tangent group law.
