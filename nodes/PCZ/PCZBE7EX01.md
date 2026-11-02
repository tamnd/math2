---
tag: PCZBE7EX01
kind: statement
role: theorem
name: Poisson integral formula
msc: [31B10, 31B20, 31A10]
uses: [0DEB0JMN0W, TCYSWCTYYM, 0YE5868HZB, 0X3WGX95FE, 0WQE3G7B88]
about: [TCYSWCTYYM, 8D56GQ4AG8]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson_kernel
---

## Statement

Let $n \ge 2$ and $R > 0$, let $B = \set{x \in \R^n : \abs{x} < R}$ be the [[open ball|0YE5868HZB]], and let $S = \partial B$ be its boundary sphere with surface measure $dS$.
Let $\sigma_{n-1}$ be the [[surface area|0WQE3G7B88]] of the unit sphere in $\R^n$, and for $x \in B$ and $y \in S$ put
$$P(x, y) = \frac{R^2 - \abs{x}^2}{\sigma_{n-1} R \, \abs{x - y}^n}.$$

1. If $u$ is [[continuous|0X3WGX95FE]] on $\overline{B}$ and [[harmonic|0DEB0JMN0W]] on $B$, then $u(x) = \int_S P(x, y) \, u(y) \, dS(y)$ for every $x \in B$.
2. If $g$ is continuous on $S$, then $u(x) = \int_S P(x, y) \, g(y) \, dS(y)$ is harmonic on $B$, and $u(x) \to g(y_0)$ as $x \to y_0$ for every $y_0 \in S$.

## Remarks

Proof idea: $P(\cdot, y)$ is harmonic in $B$, positive, and has integral $1$ over $S$.
It is minus the outward normal derivative, in the second variable, of the Green's function of the ball.
Part 1 follows from Green's representation formula on smaller balls and a limit.
Part 2 holds because $P(x, \cdot)$ concentrates near $y_0$ as $x \to y_0$, so the integral is an approximate identity.
For $n = 2$ and $R = 1$ the formula is $u(re^{i\theta}) = \frac{1}{2\pi}\int_0^{2\pi} \frac{1 - r^2}{1 - 2r\cos(\theta - t) + r^2} \, u(e^{it}) \, dt$, the classical [[Poisson kernel|TCYSWCTYYM]] of the disc.
At $x = 0$ the formula gives the mean value property: $u(0)$ is the average of $u$ over $S$.
Together, parts 1 and 2 solve the [[Dirichlet problem|8D56GQ4AG8]] on a ball, with a unique solution.

## Explanations

### L1 human

If you know a harmonic function on the surface of a ball, you know it inside.
The value at an inside point is a weighted average of the boundary values.
Boundary points close to the inside point get large weights, and far points get small ones.

### L2 human

The Poisson formula is the main tool for local results on harmonic functions.
From it one gets [[Harnack's inequality|YNH832D50W]], gradient estimates, the real analyticity of harmonic functions, and the fact that uniform limits of harmonic functions are harmonic.
It also yields the converse of the mean value property.
It is the basic step in Perron's method, where a function is replaced by its Poisson integral on a small ball.
