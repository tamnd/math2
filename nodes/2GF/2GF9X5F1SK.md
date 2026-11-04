---
tag: 2GF9X5F1SK
kind: proof
name: Proof of Abel's identity
msc: [34A30]
proves: 0VGWKX2JHB
uses: [0N5NF1RGBP, 0EQZSAB9EC, 0V9A43H7WV, 0M0TKFRX2A, 0NC2A3HWGT, 0RXX2PT1MQ, 0EX9GFJ0B3, 003QDZ4T16, 0E8HNVBCSP]
sources:
  - url: https://en.wikipedia.org/wiki/Abel%27s_identity
    locator: Proof
---

## Proof

We show that $W$ solves $W' = -p W$ and then solve this linear equation.

1. As solutions of the [[homogeneous equation|0EQZSAB9EC]], $y_1$ and $y_2$ are twice differentiable on $I$. So $y_1, y_2, y_1', y_2'$ are differentiable.
2. By the [[product rule|0V9A43H7WV]] and [[linearity of differentiation|0M0TKFRX2A]], the [[Wronskian|0N5NF1RGBP]] $W = y_1 y_2' - y_1' y_2$ is differentiable on $I$, with $W' = y_1' y_2' + y_1 y_2'' - y_1'' y_2 - y_1' y_2' = y_1 y_2'' - y_1'' y_2$.
3. The equation gives $y_k'' = -p\, y_k' - q\, y_k$ for $k = 1, 2$. Substituting, $W' = y_1 \left(-p y_2' - q y_2\right) - \left(-p y_1' - q y_1\right) y_2$.
4. The terms with $q$ cancel, and $W' = -p\left(y_1 y_2' - y_1' y_2\right) = -p W$ on $I$.
5. Let $P(x) = \int_{x_0}^{x} p(t)\, dt$. Since $p$ is continuous, [[$P$ is differentiable with $P' = p$|0NC2A3HWGT]]. Also $P(x_0) = 0$.
6. Let $G = W e^{P}$. By the product rule, the [[chain rule|0RXX2PT1MQ]] and [[the derivative of the exponential|0EX9GFJ0B3]], $G' = W' e^{P} + W p\, e^{P} = (-p W + p W) e^{P} = 0$.
7. So [[$G$ is constant|003QDZ4T16]] on $I$, and $G(x) = G(x_0) = W(x_0) e^{0} = W(x_0)$ for each $x \in I$.
8. By the [[exponential of a sum|0E8HNVBCSP]], $e^{P(x)} e^{-P(x)} = e^{0} = 1$. Multiplying $W(x) e^{P(x)} = W(x_0)$ by $e^{-P(x)}$ gives $W(x) = W(x_0) \exp\left(-\int_{x_0}^{x} p(t)\, dt\right)$.

## Idea

Differentiating $W$ leaves only second derivatives. The equation expresses them through first derivatives and the function, and the result is $-p W$. A linear first-order equation $W' = -p W$ has exponential solutions, fixed by the value at $x_0$.
