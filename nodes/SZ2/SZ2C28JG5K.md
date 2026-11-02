---
tag: SZ2C28JG5K
kind: definition
name: Caloric function
msc: ["35K05", "31C45"]
defines: PFJP8T03C4
uses: [VP2HN86VAG, 0E0B6RA8K0, KD404MF042]
sources:
  - url: https://en.wikipedia.org/wiki/Heat_equation
---

## Definition

Let $n \ge 1$ and let $\Omega$ be an open subset of $\R^n \times \R$, with points written $(x, t)$, $x \in \R^n$, $t \in \R$.
A *caloric function* on $\Omega$ is a function $u \colon \Omega \to \R$ such that:

1. $u$ is twice continuously differentiable in $x$ and once continuously differentiable in $t$ on $\Omega$.
2. $u$ satisfies the [[heat equation|VP2HN86VAG]]
$$\frac{\partial u}{\partial t}(x, t) = \Delta_x u(x, t) \quad \text{for all } (x, t) \in \Omega,$$
where $\Delta_x = \sum_{i=1}^n \partial^2 / \partial x_i^2$ is the [[Laplacian|0E0B6RA8K0]] in the space variables.

## Remarks

Example: on $\R \times \R$, the function $u(x, t) = x^2 + 2t$ is caloric, since $\partial_t u = 2$ and $\partial_x^2 u = 2$.
On $\R^n \times (0, \infty)$, the [[heat kernel|KD404MF042]] $\Phi(x, t) = (4 \pi t)^{-n/2} e^{-\abs{x}^2 / (4t)}$ is caloric.

Non-example: $u(x, t) = x^2 + t$ on $\R \times \R$ is smooth but not caloric, because $\partial_t u = 1$ while $\partial_x^2 u = 2$.

Some authors write the heat equation as $\partial_t u = k \Delta u$ with a constant $k > 0$; a change of the time scale reduces this to $k = 1$.
A function with $\partial_t u \le \Delta u$ is called subcaloric, and one with $\partial_t u \ge \Delta u$ is called supercaloric.
Caloric functions are also called temperatures.
