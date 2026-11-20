---
tag: RWST1DAHFM
kind: example
name: A linear map out of R² ⊕ R built from its pieces
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
instance_of: [0S7W6EG32V]
illustrates: [N04WS31KXB]
uses: [02WZB422CE, 0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_sum_of_modules
    locator: Universal property
---

## Example

Let $V_1 = \R^2$ and $V_2 = \R$, with [[external direct sum|02WZB422CE]] $\R^2 \oplus \R$, whose vectors are pairs $((x, y), t)$.
Take the [[linear maps|0RJF668P1T]] $f_1 \colon \R^2 \to \R$, $f_1(x, y) = x + y$, and $f_2 \colon \R \to \R$, $f_2(t) = 2t$.
We check the [[universal property|N04WS31KXB]] step by step.

1. The formula of the property gives $f((x, y), t) = f_1(x, y) + f_2(t) = x + y + 2t$.
2. $f$ is linear, since it is a sum of linear expressions in $x$, $y$ and $t$.
3. On the first summand: $f(\iota_1(x, y)) = f((x, y), 0) = x + y = f_1(x, y)$.
4. On the second summand: $f(\iota_2(t)) = f((0, 0), t) = 2t = f_2(t)$.
5. Uniqueness: if $g$ is linear with the same restrictions, then $g((x, y), t) = g((x, y), 0) + g((0, 0), t) = f_1(x, y) + f_2(t)$. So $g = f$.

In coordinates, $f$ has the $1 \times 3$ matrix $\begin{pmatrix} 1 & 1 & 2 \end{pmatrix}$, the block row of $f_1$ and $f_2$.

## Remarks

The kernel of $f$ is the plane $x + y + 2t = 0$, which is not the sum of the kernels of $f_1$ and $f_2$.
For instance $((1, 1), -1)$ lies in $\ker f$, but its parts $(1, 1)$ and $-1$ lie in neither kernel.

## Explanations

### L1 human

A map on the pairs is built by applying one map to each part and adding the results.

### L2 human

The value at $((1, 2), 3)$ is $f_1(1, 2) + f_2(3) = 3 + 6 = 9$.
The matrix $\begin{pmatrix} 1 & 1 & 2 \end{pmatrix}$ applied to $(1, 2, 3)$ gives $1 + 2 + 6 = 9$ as well.
