---
tag: FR6NT0GB24
kind: definition
name: Leontief production function
msc: [91B38, 91B66]
defines: KTTZ1J9SPZ
sources:
  - url: https://en.wikipedia.org/wiki/Leontief_production_function
---

## Definition

Let $n \ge 1$ be a number of inputs and let $a_1, \dots, a_n > 0$ be constants, where $a_i$ is the amount of input $i$ needed per unit of output.
The *Leontief production function* with these coefficients is the function $f \colon \R^n_+ \to \R_+$ given by
$$f(x_1, \dots, x_n) = \min \left( \frac{x_1}{a_1}, \frac{x_2}{a_2}, \dots, \frac{x_n}{a_n} \right).$$

## Remarks

Example: with $a_1 = 1$ and $a_2 = 2$, the function $f(x_1, x_2) = \min(x_1, x_2 / 2)$ gives $f(10, 14) = \min(10, 7) = 7$.
At $(10, 14)$ the input $x_1$ is in excess: $f(9, 14) = 7$ as well.

Non-example: $f(x_1, x_2) = x_1 + x_2 / 2$ uses the same coefficients but a sum instead of a minimum; the inputs are perfect substitutes there, not perfect complements.

The function has constant returns to scale: $f(t x) = t f(x)$ for $t \ge 0$.
It is continuous and concave but not differentiable on the ray $x_1 / a_1 = \cdots = x_n / a_n$.
With two inputs its elasticity of substitution is $0$, and it is the limit $\rho \to -\infty$ of the [[constant elasticity of substitution|MYBPAD9TGZ]] family.
