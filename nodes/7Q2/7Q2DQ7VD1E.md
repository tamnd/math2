---
tag: 7Q2DQ7VD1E
kind: proof
name: Proof of the divergence theorem on a rectangle in the plane
msc: ["26B20"]
proves: 0GZ3D8F921
uses: [02NSMQVQWK, 0R0T1VWH5X, 0NKBMFC18R, 0NHGY0N0JB, 0TCBZMEYGN, 05AXG3QRKR]
sources:
  - url: https://en.wikipedia.org/wiki/Green%27s_theorem
    locator: Proof when D is a simple region
---

## Proof

We use Fubini's theorem and the fundamental theorem of calculus on each term.

1. Since $F = (P, Q)$ is of [[class $C^1$|0TCBZMEYGN]] on an open set containing $R$, the [[partial derivatives|05AXG3QRKR]] $P_x = \partial P / \partial x$ and $Q_y = \partial Q / \partial y$ are continuous on $R$.
2. By linearity of the [[double integral|0NKBMFC18R]], $\iint_R (P_x + Q_y) \, dA = \iint_R P_x \, dA + \iint_R Q_y \, dA$. This is the integral of the [[divergence|02NSMQVQWK]] of $F$.
3. By [[Fubini's theorem|0R0T1VWH5X]] for the continuous function $P_x$, $\iint_R P_x \, dA = \int_c^d \left( \int_a^b P_x(x, y) \, dx \right) dy$.
4. Fix $y \in [c, d]$. The function $x \mapsto P(x, y)$ is continuous on $[a, b]$, and its derivative on $(a, b)$ is the continuous function $x \mapsto P_x(x, y)$.
5. By the [[fundamental theorem of calculus|0NHGY0N0JB]], $\int_a^b P_x(x, y) \, dx = P(b, y) - P(a, y)$. So $\iint_R P_x \, dA = \int_c^d \big( P(b, y) - P(a, y) \big) \, dy$.
6. By Fubini's theorem in the other order, $\iint_R Q_y \, dA = \int_a^b \left( \int_c^d Q_y(x, y) \, dy \right) dx$.
7. For fixed $x \in [a, b]$, the fundamental theorem of calculus gives $\int_c^d Q_y(x, y) \, dy = Q(x, d) - Q(x, c)$. So $\iint_R Q_y \, dA = \int_a^b \big( Q(x, d) - Q(x, c) \big) \, dx$.
8. Adding steps 5 and 7 with step 2 gives the stated formula.

## Idea

On a rectangle, each part of the divergence can be integrated first in its own variable. The fundamental theorem of calculus turns that inner integral into a difference of boundary values. So the integral of $P_x$ only sees the right and left sides, and the integral of $Q_y$ only sees the top and bottom sides.
