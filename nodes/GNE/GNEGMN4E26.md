---
tag: GNEGMN4E26
kind: definition
name: Group law on an elliptic curve
msc: [14H52, 11G05]
defines: P7V1BQJPSS
uses: [427N6S6QQW, 082GHNPJ53, 04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_curve
    locator: The group law
---

## Definition

Let $K$ be a [[field|04C5ZBG1WT]] of characteristic not $2$ or $3$, and let $E \colon y^2 = x^3 + ax + b$ be an [[elliptic curve|427N6S6QQW]] over $K$, with $a, b \in K$ and $4a^3 + 27b^2 \ne 0$.
Let $E(K)$ be the set of solutions $(x, y) \in K^2$ together with the point at infinity $O$.
The *group law* on $E(K)$ is the operation $+$ defined as follows, for $P = (x_1, y_1)$ and $Q = (x_2, y_2)$ in $E(K)$:

1. $O + P = P + O = P$ for every $P \in E(K)$.
2. If $x_1 = x_2$ and $y_1 = -y_2$, then $P + Q = O$.
3. Otherwise, let $\lambda = \frac{y_2 - y_1}{x_2 - x_1}$ if $x_1 \ne x_2$, and $\lambda = \frac{3x_1^2 + a}{2y_1}$ if $P = Q$.
Then $P + Q = (x_3, y_3)$ with $x_3 = \lambda^2 - x_1 - x_2$ and $y_3 = \lambda(x_1 - x_3) - y_1$.

With this operation, $E(K)$ is an [[abelian group|082GHNPJ53]] with identity $O$, and the inverse of $(x, y)$ is $(x, -y)$.

## Remarks

Geometrically, $P + Q + R = O$ exactly when $P$, $Q$, $R$ are the three intersection points, counted with multiplicity, of $E$ with a line in the projective plane.
The number $\lambda$ is the slope of the line through $P$ and $Q$, or of the tangent at $P$ when $P = Q$.

Example: on $y^2 = x^3 + 1$ over $\Q$, take $P = Q = (2, 3)$.
Then $\lambda = \frac{3 \cdot 4 + 0}{6} = 2$, $x_3 = 4 - 2 - 2 = 0$ and $y_3 = 2(2 - 0) - 3 = 1$, so $2P = (0, 1)$, and indeed $1^2 = 0^3 + 1$.

Non-example: the operation $P * Q$ that sends $P, Q$ to the third intersection point of their line with $E$, without the reflection, is not a group law.
A neutral element $e$ for $*$ would have to lie on the tangent line at every point of $E$.
But only finitely many tangent lines of a smooth cubic pass through a given point.

Associativity is the hard part of the proof that $E(K)$ is a group; it follows from the theorem of Riemann–Roch or from a direct computation with the formulas.
For a general Weierstrass equation the formulas change, but the geometric rule stays the same.
