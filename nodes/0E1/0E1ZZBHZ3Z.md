---
tag: 0E1ZZBHZ3Z
kind: definition
name: Riccati equation
msc: [34A34]
defines: 0VT2QK6X6Q
uses: [0P97V20RW7, 0Z3YKRQZ48, 0ZB84QCDKR]
sources:
  - url: https://en.wikipedia.org/wiki/Riccati_equation
    locator: lead section
---

## Definition

Let $I$ be an open interval and let $q_0, q_1, q_2 : I \to \mathbb{R}$ be continuous functions, with $q_0$ and $q_2$ not identically zero.
A Riccati equation is an [[ordinary differential equation|0P97V20RW7]] of the form
$$y' = q_0(x) + q_1(x)\, y + q_2(x)\, y^2.$$

## Remarks

If $q_2 = 0$, the equation is [[linear|0Z3YKRQZ48]]. If $q_0 = 0$, it is a [[Bernoulli equation|0ZB84QCDKR]] with $n = 2$.
If $y_1$ is one solution, then the substitution $y = y_1 + 1/v$ gives a linear first-order equation for $v$.
If $q_2$ has no zero and is differentiable, the substitution $y = -u' / (q_2 u)$ gives the second-order linear equation $u'' - \left(q_1 + q_2'/q_2\right) u' + q_0 q_2\, u = 0$.
Example: $y' = 1 + y^2$ has the solutions $y = \tan(x + C)$.

## Explanations

### L1 human

A Riccati equation is the next case after a linear equation: the right side is a quadratic polynomial in $y$.
In general, there is no formula for its solutions.
But if you know one solution, you can find all the others.
