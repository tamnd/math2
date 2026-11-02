---
tag: 3CVERVJRV9
kind: definition
name: Equilibrium of a difference equation
msc: [39A05, 37C25]
defines: D62PEKHRV5
uses: [W46BP9W06H, 07TZV87Y0T]
sources:
  - url: https://en.wikipedia.org/wiki/Fixed_point_(mathematics)
---

## Definition

Let $X$ be a set and let $k \ge 1$.
Let $F \colon X^k \to X$ be a function, and consider the autonomous [[recurrence|07TZV87Y0T]]
$$x_{n+1} = F(x_n, x_{n-1}, \dots, x_{n-k+1}) \qquad (n \ge k - 1).$$
A point $x^* \in X$ is an *equilibrium* (or *equilibrium point*) of this difference equation if $F(x^*, x^*, \dots, x^*) = x^*$.
For $k = 1$, this says that $x^*$ is a [[fixed point|W46BP9W06H]] of $F$.

## Remarks

The point $x^*$ is an equilibrium if and only if the constant sequence $x_n = x^*$ is a solution.
Example: for the logistic recurrence $x_{n+1} = r x_n (1 - x_n)$ on $\R$ with $r \ne 0$, the equation $r x (1 - x) = x$ gives the equilibria $0$ and $1 - 1/r$.
For $r = 2$, check: $2 \cdot \tfrac12 \cdot \tfrac12 = \tfrac12$.
Non-example: $x_{n+1} = x_n + 1$ on $\R$ has no equilibrium, since $x + 1 \ne x$ for every $x$.
For a non-autonomous equation $x_{n+1} = F(n, x_n)$, an equilibrium is a point $x^*$ with $F(n, x^*) = x^*$ for all $n$.
Other names are fixed point, steady state and stationary solution.
