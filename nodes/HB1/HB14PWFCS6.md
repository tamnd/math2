---
tag: HB14PWFCS6
kind: definition
name: Envelope
msc: [53A04, 34A09, 34A26]
defines: 827KR3MVVY
uses: [06JMR2XWXW, 05AXG3QRKR, 01R1HW3Y42]
sources:
  - url: https://en.wikipedia.org/wiki/Envelope_(mathematics)
---

## Definition

Let $J \subseteq \R$ be an open interval, let $U \subseteq \R^2$ be open, and let $F : U \times J \to \R$ be continuously differentiable.
For $c \in J$, let $C_c = \set{(x, y) \in U : F(x, y, c) = 0}$, a one-parameter family of curves.
An *envelope* of the family is a [[regular curve|06JMR2XWXW]] $\gamma : J \to U$ such that for each $c \in J$:

1. $\gamma(c)$ lies on $C_c$, that is, $F(\gamma(c), c) = 0$;
2. the gradient $\nabla_{x,y} F(\gamma(c), c)$ is nonzero;
3. $\gamma$ is tangent to $C_c$ at $\gamma(c)$, that is, $\nabla_{x,y} F(\gamma(c), c) \cdot \gamma'(c) = 0$.

## Remarks

Differentiating $F(\gamma(c), c) = 0$ and using clause 3 gives $\partial F / \partial c\, (\gamma(c), c) = 0$, where $\partial F/\partial c$ is the [[partial derivative|05AXG3QRKR]] in $c$.
So the points of an envelope satisfy the two equations $F = 0$ and $\partial F / \partial c = 0$.
Eliminating $c$ gives the discriminant set, which contains the envelope but may also contain singular points of the curves.
Example: $F(x, y, c) = x \cos c + y \sin c - 1$, the lines at distance $1$ from the origin.
Then $\gamma(c) = (\cos c, \sin c)$ satisfies $F = \cos^2 c + \sin^2 c - 1 = 0$, and $\gamma'(c) = (-\sin c, \cos c)$ is orthogonal to $\nabla F = (\cos c, \sin c)$; so the unit circle is the envelope.
Non-example: the concentric circles $x^2 + y^2 - c^2 = 0$, $c > 0$, have no envelope, since $\partial F / \partial c = -2c \ne 0$ and clause 3 can never hold together with clause 1.
For a regular curve $\beta$, the family of its [[tangent lines|01R1HW3Y42]], with parameter $c$ the parameter of $\beta$, has $\beta$ itself as an envelope.
