---
tag: RMXW3D9XZ3
kind: statement
role: theorem
name: Analyticity of the bilateral Laplace transform of a law
msc: [44A10, "60E10"]
uses: [059TJN0NZ1, 6J2AGD0BYY, HYA7QQ1E38, 0NAHXR1FRH]
about: [6J2AGD0BYY, 0WQVXP7PDB]
sources:
  - url: https://en.wikipedia.org/wiki/Two-sided_Laplace_transform
---

## Statement

Let $\mu$ be a [[probability measure|059TJN0NZ1]] on $\R$.
Let $I$ be the set of real $\sigma$ with $\int_{\R} e^{-\sigma x} \, d\mu(x) < \infty$.
Then:

1. $I$ is an interval that contains $0$.
2. For every $s \in \C$ with $\operatorname{Re} s \in I$, the integral $\mathcal{B}\mu(s) = \int_{\R} e^{-sx} \, d\mu(x)$ converges absolutely.
3. On the open strip $S = \set{s \in \C : \operatorname{Re} s \in \operatorname{int} I}$, the function $\mathcal{B}\mu$ is [[holomorphic|0NAHXR1FRH]], and for every $n \ge 0$ and $s \in S$,
$$(\mathcal{B}\mu)^{(n)}(s) = \int_{\R} (-x)^n e^{-sx} \, d\mu(x),$$
where this integral converges absolutely.

Here $\operatorname{int} I$ is the interior of $I$, and $\mathcal{B}\mu$ is the [[two-sided Laplace transform|6J2AGD0BYY]] of $\mu$.

## Remarks

Part 1 holds because $\sigma \mapsto e^{-\sigma x}$ is convex, so $e^{-\sigma x} \le e^{-a x} + e^{-b x}$ for $a \le \sigma \le b$; and $0 \in I$ because $\mu$ has total mass $1$.
Part 2 holds because $\abs{e^{-sx}} = e^{-x \operatorname{Re} s}$.
For part 3, fix $a < \operatorname{Re} s < b$ in $I$; then $\abs{x}^n e^{-x \operatorname{Re} s} \le C_n (e^{-a x} + e^{-b x})$ for a constant $C_n$, so [[differentiation under the integral sign|0AR06W1E1B]] is allowed by dominated convergence.
On the real axis this says that the [[moment-generating function|0WQVXP7PDB]] $M(t) = \mathcal{B}\mu(-t)$ is real analytic on the interior of its domain, with $M^{(n)}(t) = \int x^n e^{tx} \, d\mu(x)$.
Example: for the exponential law with rate $\lambda$, $I = (-\lambda, \infty)$ and $\mathcal{B}\mu(s) = \lambda/(\lambda + s)$, which is holomorphic for $\operatorname{Re} s > -\lambda$ and has a pole at $s = -\lambda$.
The open strip is needed in part 3: the derivative formula uses room on both sides of $\operatorname{Re} s$, and at an end point of $I$ the integral $\int \abs{x} e^{-x \operatorname{Re} s} \, d\mu(x)$ may diverge.
If $I = \set{0}$, as for the Cauchy law, the strip is empty and the statement says nothing.

## Explanations

### L1 human

Averaging $e^{-sX}$ over a random quantity $X$ gives a function of $s$.
This theorem says that, wherever the average is finite with a little room to spare, the function is as smooth as possible.
It is given locally by a convergent power series.
Its derivatives are found by differentiating inside the average.

### L2 human

This is the reason why a moment-generating function that is finite near $0$ produces all the moments, as its derivatives at $0$.
It is also the starting point of large deviation theory, where the convex function $\log M$ and its derivatives are used.
The domain of finiteness is the [[strip of convergence|HYA7QQ1E38]] of the bilateral transform.
The same proof gives analyticity of the two-sided Laplace transform of any measure on its open strip.
On the imaginary axis the transform is the characteristic function, which is always defined but need not be analytic.
