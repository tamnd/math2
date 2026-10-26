---
tag: 0TH9CPW3VS
kind: statement
role: proposition
name: Reduction of a higher-order equation to a first-order system
msc: [34A99]
uses: [0P97V20RW7, 04SW7WECS8, 075VBY4K4X]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinary_differential_equation
    locator: Reduction to a first-order system
---

## Statement

Let $n \ge 1$, let $U$ be a subset of $\mathbb{R} \times \mathbb{R}^n$, and let $f : U \to \mathbb{R}$ be a function.
Consider the equation $y^{(n)} = f\left(x, y, y', \dots, y^{(n-1)}\right)$ and the first-order system for $z = (z_1, \dots, z_n)$:
$$z_1' = z_2, \quad z_2' = z_3, \quad \dots, \quad z_{n-1}' = z_n, \quad z_n' = f(x, z_1, \dots, z_n).$$
Let $I$ be an open interval.
If $y$ is a [[solution|04SW7WECS8]] of the equation on $I$, then $z = \left(y, y', \dots, y^{(n-1)}\right)$ is a solution of the system on $I$.
Conversely, let $z$ be a solution of the system on $I$. Then $y = z_1$ is a solution of the equation on $I$, and $z_k = y^{(k-1)}$ for $k = 1, \dots, n$.

## Remarks

The initial conditions $y^{(k)}(x_0) = c_k$ for $k = 0, \dots, n-1$ become the one condition $z(x_0) = (c_0, \dots, c_{n-1})$. So results on first-order [[initial value problems|075VBY4K4X]] apply to equations of each order.
For $y'' = -y$, the system is $z_1' = z_2$, $z_2' = -z_1$.
The same method changes a system of equations of order $n$ into a larger first-order system.

## Explanations

### L1 human

The trick is to give new names to the derivatives of $y$.
Each new unknown is the derivative of the one before it, and the last one is given by the equation.
So we only need a theory of first-order systems.
