---
tag: 3RQJAWJ9BD
kind: definition
name: Saddle point of a function on a product
msc: [90C47, 49J35]
defines: 7MFNVVJHTE
uses: [0R3H5PANRQ, 0QF1MZ9FRG]
sources:
  - url: https://en.wikipedia.org/wiki/Saddle_point
---

## Definition

Let $X$ and $Y$ be sets, let $A \subseteq X$ and $B \subseteq Y$, and let $f \colon X \times Y \to [-\infty, +\infty]$.
A pair $(a, b) \in A \times B$ is a *saddle point of $f$ on $A \times B$* if
$$f(a, y) \le f(a, b) \le f(x, b) \quad \text{for all } x \in A \text{ and } y \in B.$$

## Remarks

Equivalently, $a$ minimizes $f(\cdot, b)$ on $A$ and $b$ maximizes $f(a, \cdot)$ on $B$.
If $(a, b)$ is a saddle point, then
$$\inf_{x \in A} \sup_{y \in B} f(x, y) = f(a, b) = \sup_{y \in B} \inf_{x \in A} f(x, y),$$
with the [[infimum|0QF1MZ9FRG]] and [[supremum|0R3H5PANRQ]] attained at $a$ and $b$.
Conversely, if both sides are equal and the outer infimum and supremum are attained at $a$ and $b$, then $(a, b)$ is a saddle point.
Here $f$ is minimized in the first variable; some authors use the opposite order.

Example: $f(x, y) = x^2 - y^2$ on $\R \times \R$ and $(a, b) = (0, 0)$.
Then $f(0, y) = -y^2 \le 0 = f(0, 0) \le x^2 = f(x, 0)$ for all $x, y$.

Non-example: $f(x, y) = xy$ on $[0, 1] \times [0, 1]$ and $(a, b) = (1, 1)$.
The right inequality fails, since $f(0, 1) = 0 < 1 = f(1, 1)$.
The pair $(0, 1)$ is a saddle point: $f(0, y) = 0 \le 0 \le x = f(x, 1)$.
