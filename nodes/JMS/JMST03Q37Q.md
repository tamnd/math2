---
tag: JMST03Q37Q
kind: definition
name: Jacobi equation
msc: [49K05]
defines: FSD6S7DR8D
uses: [JRQZ803Q5Y, 4C3BANJ8AH, PS0VV149ET, 0NT64JV96A]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi_field
---

## Definition

Let $a < b$ and let $L \colon [a, b] \times \R \times \R \to \R$, written $L(x, y, p)$, be of class $C^3$.
Let $J(y) = \int_a^b L(x, y, y') \, dx$ be the [[integral functional|JRQZ803Q5Y]] of $L$.
Let $y_0 \in C^2([a, b])$ be a solution of the [[Euler–Lagrange equation|PS0VV149ET]] of $J$.
Put $P(x) = L_{pp}(x, y_0(x), y_0'(x))$ and $Q(x) = L_{yy}(x, y_0(x), y_0'(x)) - \frac{d}{dx} L_{yp}(x, y_0(x), y_0'(x))$.
The *Jacobi equation* of $J$ along $y_0$ is the linear [[ordinary differential equation|0NT64JV96A]]
$$-\frac{d}{dx}\big( P(x) \, h'(x) \big) + Q(x) \, h(x) = 0$$
for an unknown function $h$ on $[a, b]$.

## Remarks

For $h \in C^1([a, b])$ with $h(a) = h(b) = 0$, the [[second variation|4C3BANJ8AH]] of $J$ at $y_0$ equals $\int_a^b (P h'^2 + Q h^2) \, dx$.
The Jacobi equation is the Euler–Lagrange equation of this quadratic functional.
It is also the linearisation of the Euler–Lagrange equation of $J$ at $y_0$.
If $y(x, c)$ is a smooth family of extremals with $y(x, 0) = y_0(x)$, then $h = \partial y / \partial c$ at $c = 0$ solves it.

Example: for $L = p^2 - y^2$ and $y_0 = 0$, one has $P = 2$ and $Q = -2$.
The Jacobi equation is $h'' + h = 0$; the function $h = \sin x$ satisfies it, since $h'' = -\sin x = -h$.

Non-example: for the same $L$, the function $h = x$ does not solve it, since $-2h'' - 2h = -2x \ne 0$ for $x \ne 0$.
It does solve the Jacobi equation $h'' = 0$ of $L = p^2$, whose extremals are straight lines.

When $P > 0$ on $[a, b]$, the equation has a unique solution for given $h(a)$ and $h'(a)$.
For curves $y \colon [a, b] \to \R^n$ the same construction gives a linear system with matrices $P$ and $Q$.
