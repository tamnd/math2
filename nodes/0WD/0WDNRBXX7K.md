---
tag: 0WDNRBXX7K
kind: definition
name: Cauchy–Euler equation
aliases: [euler-cauchy-equation, equidimensional-equation]
msc: [34A30]
defines: 03F7N3915D
uses: [0PB7K8M7FG, 0A6PGTTP2A]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%E2%80%93Euler_equation
    locator: The equation
inventory: [DMS1GK7ATX]
---

## Definition

Let $n \ge 1$ and let $a_0, \dots, a_n$ be real numbers with $a_n \ne 0$.
The Cauchy–Euler equation with these coefficients is the [[linear differential equation|0PB7K8M7FG]]
$$a_n x^n y^{(n)} + a_{n-1} x^{n-1} y^{(n-1)} + \dots + a_1 x\, y' + a_0\, y = 0$$
for an unknown function $y$ on the interval $x > 0$.

## Remarks

The substitution $x = e^{t}$, $u(t) = y(e^t)$ changes it into a [[linear equation with constant coefficients|0A6PGTTP2A]] for $u$.
For $n = 2$, the trial solution $y = x^m$ gives the indicial equation $a_2 m (m - 1) + a_1 m + a_0 = 0$.
For order $2$: a double root $m$ gives the solutions $x^m$ and $x^m \ln x$. Roots $\alpha \pm i \beta$ with $\beta \ne 0$ give $x^\alpha \cos(\beta \ln x)$ and $x^\alpha \sin(\beta \ln x)$.
Example: $x^2 y'' - 2 y = 0$ gives $m(m-1) - 2 = 0$, so $m = 2$ or $m = -1$, and the solutions are $c_1 x^2 + c_2 x^{-1}$.

## Explanations

### L1 human

In this equation, each derivative $y^{(k)}$ is multiplied by $x^k$.
So powers $x^m$ behave like exponentials do for constant coefficients: the equation becomes a polynomial equation in $m$.
