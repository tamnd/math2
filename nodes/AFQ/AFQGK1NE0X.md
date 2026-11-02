---
tag: AFQGK1NE0X
kind: definition
name: Dirichlet energy
msc: [31B05, 35A15, 49J10]
defines: YG3W8CBB3E
uses: [02BH3MCBQB, M4CEZ5K9HP]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_energy
---

## Definition

Let $n \ge 1$ and let $\Omega \subseteq \R^n$ be an [[open set|02BH3MCBQB]].
Let $u \colon \Omega \to \R$ be continuously differentiable, or more generally weakly differentiable with locally integrable gradient $\nabla u$.
The *Dirichlet energy* of $u$ is
$$E[u] = \frac{1}{2} \int_\Omega \abs{\nabla u(x)}^2 \, dx \in [0, \infty].$$

## Remarks

Example: on the unit square $(0, 1)^2$, $u(x, y) = x^2$ has $\nabla u = (2x, 0)$, so $E[u] = \frac12 \int_0^1 4x^2 \, dx = \frac23$.
Non-example of finiteness: on the interval $(0, 1)$, $u(x) = x^{1/4}$ is continuously differentiable, but $E[u] = \frac12 \int_0^1 \frac{1}{16} x^{-3/2} \, dx = \infty$.
The functions in $L^2(\Omega)$ with finite energy form the [[Sobolev space|M4CEZ5K9HP]] $H^1(\Omega) = W^{1,2}(\Omega)$.
Some authors omit the factor $\frac12$; the minimizers are the same.
$E[u] = 0$ for a function on a connected open set if and only if $u$ is constant.
The energy is invariant under conformal maps in dimension $2$.
