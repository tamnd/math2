---
tag: HKPHRSN3ER
kind: definition
name: Legendre transformation
msc: [26A51, 44A15, 52A41]
defines: ZQYMWVT1TT
uses: [0TK8Y3J5RW, 0A61B60B5R, 011EJQWWJS, 0BTMQ04556]
sources:
  - url: https://en.wikipedia.org/wiki/Legendre_transformation
---

## Definition

Let $I$ be an open [[interval|0TK8Y3J5RW]] of $\R$, and let $f \colon I \to \R$ be a [[differentiable function|0A61B60B5R]] whose derivative $f'$ is [[strictly increasing|011EJQWWJS]] on $I$.
Let $J = f'(I)$; it is an interval, and $f' \colon I \to J$ is a bijection with inverse $g \colon J \to I$.
The *Legendre transform* of $f$ is the function $f^* \colon J \to \R$ given by
$$f^*(p) = p \, g(p) - f(g(p)).$$
The map $f \mapsto f^*$ is the *Legendre transformation*.

## Remarks

For $p \in J$ one has $f^*(p) = \sup_{x \in I} \big(p x - f(x)\big)$, and the [[supremum|0BTMQ04556]] is attained at $x = g(p)$.
Indeed $x \mapsto p x - f(x)$ has derivative $p - f'(x)$, which is positive for $x < g(p)$ and negative for $x > g(p)$.
The function $f^*$ is differentiable with $(f^*)' = g = (f')^{-1}$, and $(f^*)^* = f$.
The supremum formula, taken over all $x$, defines the convex conjugate of any function, which extends this definition.

Example: $f(x) = e^x$ on $\R$.
Here $f'(x) = e^x$ is strictly increasing, $J = (0, \infty)$ and $g(p) = \ln p$.
So $f^*(p) = p \ln p - p$ for $p > 0$.

Non-example: $f(x) = x^3$ on $\R$.
Its derivative $3x^2$ is not strictly increasing, since $3 \cdot (-1)^2 = 3 \cdot 1^2$, so the definition does not apply.
