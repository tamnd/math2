---
about:
  - 7WV6B2502K
kind: statement
msc:
  - 34B24
  - 34B05
name: Orthogonality of eigenfunctions of the equation x'' + lambda x = 0 with standard boundary conditions
role: theorem
sources:
  - url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ch-fourier-and-pde.tex#L340
    locator: ch-fourier-and-pde.tex:340
tag: X8JB2RKK95
uses:
  - TM8VQJWGHZ
  - 3FW4J270FV
  - 0BQAA2BK3Q
  - 0Y2X7P2WB7
---

## Statement

Consider the equation $x'' + \lambda x = 0$ on an interval $[a, b]$ as a [[boundary value problem|TM8VQJWGHZ]] with one of three kinds of boundary conditions.
The first kind is $x(a) = 0$ and $x(b) = 0$.
The second kind is $x'(a) = 0$ and $x'(b) = 0$.
The third kind is [[periodic boundary conditions|3FW4J270FV]]: $x(a) = x(b)$ and $x'(a) = x'(b)$.

A nonzero solution for a given $\lambda$ is an eigenfunction, and $\lambda$ is then an [[eigenvalue|0BQAA2BK3Q]].

Fix one of the three kinds of conditions.
Let $x_1$ and $x_2$ be eigenfunctions for eigenvalues $\lambda_1 \ne \lambda_2$.
Then $x_1$ and $x_2$ are [[orthogonal|0Y2X7P2WB7]] in the sense of the integral inner product:
$$\int_a^b x_1(t)\, x_2(t)\, dt = 0.$$

## Remarks

The usual proof integrates by parts twice.
It gives $(\lambda_1 - \lambda_2) \int_a^b x_1 x_2\, dt = x_1' x_2 - x_1 x_2' \big|_a^b$, which vanishes under each of the three kinds of conditions.
