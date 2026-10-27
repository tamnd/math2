---
tag: 0XYAFCN0PT
kind: statement
role: theorem
name: Second fundamental theorem of calculus
msc: [26A42]
uses: [0BARQY52N5, 0HBY48G8G1, 0N1JQXZXHC]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus
    locator: Second part
inventory: [S67NDX266Q]
---

## Statement

Let $a < b$, and let $F \colon [a, b] \to \mathbb{R}$ be continuous on $[a, b]$ and differentiable on $(a, b)$.
Assume that $F'$ extends to a [[Riemann integrable|0N1JQXZXHC]] function $f$ on $[a, b]$.
Then
$$\int_a^b f(x) \, dx = F(b) - F(a).$$

## Remarks

For a partition $P$, the [[mean value theorem|0BARQY52N5]] gives tags $t_i$ with $F(x_i) - F(x_{i-1}) = f(t_i)(x_i - x_{i-1})$. So $F(b) - F(a)$ is a [[Riemann sum|0HBY48G8G1]] of $f$ for each partition.
One writes $F(b) - F(a) = \big[ F(x) \big]_a^b$.
The hypothesis that $f$ is integrable is needed. Some differentiable functions have derivatives that are not Riemann integrable.
Mathlib states it as `intervalIntegral.integral_eq_sub_of_hasDeriv_right_of_le`.

## Explanations

### L1 human

To integrate $f$, find a function $F$ with derivative $f$.
The integral is the change of $F$ from $a$ to $b$.
