---
tag: S6KGGNFKDF
kind: definition
name: Relaxation of a variational problem
msc: [49J45]
defines: DPS8QZBVB0
uses: [1EQM0DJ4NC, RN4G8SGP6P, 0CQHFPGJ45]
sources:
  - url: https://en.wikipedia.org/wiki/Relaxation_(approximation)
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]] and let $J \colon X \to (-\infty, +\infty]$ be a [[functional|1EQM0DJ4NC]].
The *relaxed functional*, or lower semicontinuous envelope, of $J$ is
$$\bar J(u) = \sup \set{ G(u) : G \colon X \to [-\infty, +\infty] \text{ is lower semicontinuous and } G \le J }.$$
The *relaxed problem* of the problem $\inf_X J$ is the problem $\inf_X \bar J$.

## Remarks

The function $\bar J$ is itself [[lower semicontinuous|RN4G8SGP6P]], and $\bar J \le J$.
If $X$ is a metric space, then $\bar J(u) = \inf \set{ \liminf_k J(u_k) : u_k \to u }$.
In the calculus of variations one uses the sequential form of this formula for weak convergence in a Sobolev space.

The relaxed problem has the same infimum: $\inf_X \bar J = \inf_X J$.
If $X$ is a metric space, every limit of a subsequence of a minimising sequence of $J$ is a minimiser of $\bar J$.

Example: on $X = \R$, let $J(u) = u^2$ for $u \ne 0$ and $J(0) = 1$.
Then $\bar J(u) = u^2$ for all $u$, which attains the common infimum $0$ at $u = 0$, while $J$ does not attain it.

Example: let $J(u) = \int_0^1 \big( (u'^2 - 1)^2 + u^2 \big) \, dx$ on $W^{1,4}_0(0, 1)$ with weak convergence.
Its relaxation is $\bar J(u) = \int_0^1 \big( f^{**}(u') + u^2 \big) \, dx$, where $f^{**}(\xi) = \big(\max(\xi^2 - 1, 0)\big)^2$ is the convex envelope of $f(\xi) = (\xi^2 - 1)^2$.
The function $u = 0$ minimises $\bar J$, with $\bar J(0) = 0 = \inf J$, although $J$ has no minimiser.

Non-example: for maps $u \colon \Omega \to \R^m$ with $m, n \ge 2$, replacing the integrand by its convex envelope does not give $\bar J$ in general.
For $2 \times 2$ matrices, $\det$ is weakly continuous on $W^{1,p}$ for $p > 2$, so it needs no relaxation, but its convex envelope is $-\infty$.
The correct integrand is the quasiconvex envelope, under growth conditions.
