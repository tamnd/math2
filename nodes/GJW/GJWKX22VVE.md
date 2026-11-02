---
tag: GJWKX22VVE
kind: problem
name: Riemann problem
msc: [35L65, 35L67, 35L45]
uses: [8RA7AMWSAF, 1A01A3EJRX]
about: [8RA7AMWSAF]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_problem
same_as:
  wikidata: Q2152221
  wikipedia: Riemann problem
history:
  posed_by: "Bernhard Riemann"
  first_stated: "1860"
---

## Problem

Let $F \colon \R^m \to \R^m$ be a $C^1$ function and consider the system of [[conservation laws|8RA7AMWSAF]] $u_t + F(u)_x = 0$ in one space dimension.
Let $u_l, u_r \in \R^m$ be two constant states.
Find an [[entropy solution|1A01A3EJRX]] $u \colon \R \times (0, \infty) \to \R^m$ with the initial values
$$u(x, 0) = \begin{cases} u_l & \text{if } x < 0, \\ u_r & \text{if } x > 0. \end{cases}$$

## Remarks

The equation and the data are unchanged by the scaling $(x, t) \mapsto (\lambda x, \lambda t)$ for $\lambda > 0$, so one looks for self-similar solutions $u(x, t) = v(x / t)$.

Scalar case with convex flux.
Let $m = 1$ and let $F$ be smooth and uniformly convex, and let $G$ be the inverse function of $F'$.
If $u_l > u_r$, the entropy solution is the [[shock wave|JSDMGGTG7G]] equal to $u_l$ for $x < \sigma t$ and to $u_r$ for $x > \sigma t$, where $\sigma = \dfrac{F(u_l) - F(u_r)}{u_l - u_r}$.
If $u_l < u_r$, the entropy solution is the [[rarefaction wave|MFN4Q5SH8H]] equal to $u_l$ for $x < F'(u_l) t$, to $G(x/t)$ for $F'(u_l) t \le x \le F'(u_r) t$, and to $u_r$ for $x > F'(u_r) t$.

Systems.
Consider a strictly hyperbolic system whose characteristic fields are each genuinely nonlinear or linearly degenerate.
Lax showed that its Riemann problem has a unique solution made of at most $m$ elementary waves when $\abs{u_l - u_r}$ is small.
These waves are shocks, rarefaction waves and contact discontinuities, one for each characteristic family, separated by constant states.
For large data, or for more general systems, solutions may fail to exist or to be unique in this class.
For the Euler equations of gas dynamics, the problem posed by Riemann, the solution is known explicitly up to solving one scalar equation, and it may contain a vacuum.

Solutions of Riemann problems are the building blocks of [[Godunov's scheme|43HZJ7DRT0]] and of the [[Glimm scheme|Y70AC2X30T]].

## Explanations

### L1 human

Put a wall in a tube, with gas at one pressure on the left and another pressure on the right, and remove the wall at time zero.
The Riemann problem asks what happens next.
Waves leave the place of the wall: some are sharp jumps, others are smooth fans that spread out.
Because the start has no length scale, the picture at time $2$ is the picture at time $1$ stretched by a factor $2$.
