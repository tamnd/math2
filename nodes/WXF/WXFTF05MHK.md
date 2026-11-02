---
tag: WXFTF05MHK
kind: statement
role: theorem
name: Poisson integral for the half-space
msc: [31B10, 31B20, 31A10]
uses: [0DEB0JMN0W, TCYSWCTYYM, 0X3WGX95FE, 0WQE3G7B88]
about: [TCYSWCTYYM, 8D56GQ4AG8]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson_kernel
---

## Statement

Let $n \ge 2$, write points of $\R^n$ as $x = (x', x_n)$ with $x' \in \R^{n-1}$, and let $H = \set{x \in \R^n : x_n > 0}$ be the upper half-space.
Let $\sigma_{n-1}$ be the [[surface area|0WQE3G7B88]] of the unit sphere in $\R^n$, and for $x \in H$ and $y \in \R^{n-1}$ put
$$P(x, y) = \frac{2 x_n}{\sigma_{n-1} \left( \abs{x' - y}^2 + x_n^2 \right)^{n/2}}.$$
Let $g \colon \R^{n-1} \to \R$ be bounded and [[continuous|0X3WGX95FE]], and define
$$u(x) = \int_{\R^{n-1}} P(x, y) \, g(y) \, dy, \qquad x \in H.$$
Then $u$ is bounded and [[harmonic|0DEB0JMN0W]] on $H$, and $u(x) \to g(y_0)$ as $x \to (y_0, 0)$ with $x \in H$, for every $y_0 \in \R^{n-1}$.

## Remarks

Proof idea: for fixed $y$, $P(\cdot, y)$ is harmonic in $H$.
It is, up to a constant factor, the normal derivative at the boundary of the Green's function of $H$ built by reflection.
The kernel is positive and $\int_{\R^{n-1}} P(x, y) \, dy = 1$, so $\abs{u} \le \sup \abs{g}$.
As $x_n \to 0$ the kernel concentrates at $x'$, which gives the boundary values.
For $n = 2$ the kernel is $\frac{1}{\pi} \frac{x_2}{(x_1 - y)^2 + x_2^2}$, the Poisson kernel of the upper half-plane.
Boundedness matters for uniqueness: $u(x) = x_n$ is harmonic on $H$ with boundary values $0$, but it is not the Poisson integral of $0$.

## Explanations

### L1 human

This formula fills in a harmonic function on a half-space from its values on the flat boundary.
The value at a point is a weighted average of the boundary values, with weights concentrated below the point.
The closer the point is to the boundary, the sharper the concentration.

### L2 human

The half-space formula is the model for boundary behaviour of harmonic functions, nontangential limits and Hardy spaces.
In $\R^2$ it is the link between harmonic functions on the upper half-plane and the Hilbert transform.
The family $P(\cdot, y)$ for $x_n = t$ fixed is the Poisson semigroup, an approximate identity used throughout harmonic analysis.
