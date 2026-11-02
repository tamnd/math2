---
tag: ZZD7X71HVN
kind: definition
name: Lane–Emden equation
msc: [35J61, 85A15]
defines: ANRZZMH2Q0
uses: [0NT64JV96A, 0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Lane%E2%80%93Emden_equation
---

## Definition

Let $n \ge 0$ be a real number, called the polytropic index.
The *Lane–Emden equation* of index $n$ is the [[ordinary differential equation|0NT64JV96A]]
$$\frac{1}{\xi^2} \frac{d}{d\xi} \left( \xi^2 \frac{d\theta}{d\xi} \right) + \theta^n = 0$$
for a function $\theta$ of $\xi > 0$, with the initial conditions $\theta(0) = 1$ and $\theta'(0) = 0$.
When $n$ is not an integer, the equation is considered on the interval where $\theta \ge 0$.

## Remarks

For a radial function $u(x) = \theta(\abs{x})$ on $\R^3$, the first term is the [[Laplacian|0E0B6RA8K0]] $\Delta u$, so the equation is $\Delta u + u^n = 0$.
Example: for $n = 0$, $\theta(\xi) = 1 - \xi^2/6$ is the solution.
Indeed, $\xi^2 \theta' = -\xi^3/3$, whose derivative divided by $\xi^2$ is $-1$, and $\theta^0 = 1$.
Non-example: for $n = 1$, the constant $\theta = 1$ is not a solution, since the left side equals $1$.
Closed-form solutions are known for $n = 0$, $n = 1$, where $\theta = \sin \xi / \xi$, and $n = 5$, where $\theta = (1 + \xi^2/3)^{-1/2}$.
In PDE the name Lane–Emden equation, or Lane–Emden–Fowler equation, is also used for $-\Delta u = \abs{u}^{p-1} u$ on a domain of $\R^N$ with $p > 1$.
