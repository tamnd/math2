---
tag: SNC7NR587P
kind: definition
name: Laplace's equation
msc: [35J05]
defines: S8RG6N1PRT
uses: [0E0B6RA8K0, 09EGC6F8PT, 0VW90BBSJ4]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace%27s_equation
---

## Definition

Let $n \ge 1$ and let $U \subseteq \R^n$ be open.
*Laplace's equation* on $U$ is the equation
$$\Delta u = \frac{\partial^2 u}{\partial x_1^2} + \cdots + \frac{\partial^2 u}{\partial x_n^2} = 0 \quad \text{in } U$$
for an unknown function $u \colon U \to \R$, where $\Delta$ is the [[Laplacian|0E0B6RA8K0]].
A classical solution is a function $u$ that is twice continuously differentiable on $U$ and satisfies the equation at every point of $U$.

## Remarks

The classical solutions are exactly the harmonic functions on $U$.
Every classical solution is in fact infinitely differentiable, and even real analytic.
The inhomogeneous equation $\Delta u = f$ is Poisson's equation.
Some authors write the Laplacian as $\nabla^2$ or $\nabla \cdot \nabla$, and in physics the equation is often written $\nabla^2 \phi = 0$.

Example: on $\R^3 \setminus \set{0}$, the function $u(x) = 1 / \abs{x}$ is a solution.
With $r = \abs{x}$, one has $\partial_i u = -x_i / r^3$ and $\partial_i^2 u = -1/r^3 + 3 x_i^2 / r^5$, and the sum over $i = 1, 2, 3$ is $-3/r^3 + 3 r^2 / r^5 = 0$.

Non-example: on $\R^2$, the function $u(x, y) = x^2 + y^2$ is not a solution, since $\Delta u = 2 + 2 = 4 \ne 0$.
