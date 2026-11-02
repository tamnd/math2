---
tag: SC8HT9T2GA
kind: definition
name: Periodic boundary conditions
msc: [34B05, 34B24]
defines: 3FW4J270FV
uses: [TM8VQJWGHZ, 0QQRP17Z7S]
sources:
  - url: https://en.wikipedia.org/wiki/Periodic_boundary_conditions
---

## Definition

Let $a < b$ be real numbers and consider a [[linear differential equation|0QQRP17Z7S]] of order $2$ on $[a, b]$.
A function $y \in C^1([a, b])$ satisfies the periodic boundary conditions on $[a, b]$ if
$$y(a) = y(b) \quad \text{and} \quad y'(a) = y'(b).$$
For an equation of order $n$, the periodic boundary conditions are $y^{(k)}(a) = y^{(k)}(b)$ for $k = 0, 1, \ldots, n - 1$.

## Remarks

Example: on $[0, 2\pi]$, the function $y(x) = \sin x$ satisfies $y(0) = 0 = y(2\pi)$ and $y'(0) = 1 = y'(2\pi)$.
So it satisfies the periodic boundary conditions, and it solves $y'' + y = 0$.
Non-example: on $[0, \pi]$, the same function has $y(0) = y(\pi) = 0$ but $y'(0) = 1 \ne -1 = y'(\pi)$, so the second condition fails.
The eigenvalue problem $-y'' = \lambda y$ with periodic boundary conditions on $[0, 2\pi]$ has the eigenvalues $\lambda = k^2$ for $k = 0, 1, 2, \ldots$.
The eigenvalue $0$ has the eigenfunction $1$, and each $k^2$ with $k \ge 1$ has the two independent eigenfunctions $\cos kx$ and $\sin kx$.
Unlike separated conditions, periodic conditions couple the two endpoints, so eigenvalues of multiplicity $2$ can occur.
If the coefficients of the equation are $(b - a)$-periodic, a solution with these conditions extends to a $(b - a)$-periodic solution on $\R$.

## Explanations

### L1 human

Periodic boundary conditions say that the start and the end of the interval look the same to the solution.
The value and the slope must match at both ends.
Then copies of the solution glue together into a smooth repeating function on the whole line.
