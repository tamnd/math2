---
tag: X8MCVW56QP
kind: statement
role: theorem
name: Balancing domain decomposition
msc: [65N55, 65F08, 65F10]
uses: [R997ZAD141, 6HWFBXYPZP, KE98SW3SBD, AB3S6MHJ8X, 98GZ9DVHTA, B4TTNHSTRX]
about: [AN054RHT1K, KE98SW3SBD]
sources:
  - url: https://en.wikipedia.org/wiki/Balancing_domain_decomposition_method
same_as:
  wikidata: Q4850008
  wikipedia: Balancing domain decomposition method
---

## Statement

Let $\Omega \subset \R^d$, $d \in \set{2, 3}$, be a polygonal or polyhedral domain.
Divide it into $N$ non-overlapping subdomains $\Omega_i$ of diameter about $H$, triangulated by a quasi-uniform mesh of size $h$.
Let $\rho > 0$ be constant on each $\Omega_i$.
Consider the [[finite element|98GZ9DVHTA]] discretization of $-\nabla \cdot (\rho \nabla u) = f$ by continuous piecewise linear functions, with homogeneous Dirichlet conditions on part of $\partial \Omega$.
Let $S = \sum_i R_i^T S_i R_i$ be the interface [[Schur complement|6HWFBXYPZP]], where $R_i$ restricts interface values to $\partial \Omega_i$ and $S_i$ is the local Schur complement of $\Omega_i$.
Let $D_i$ be diagonal weight matrices with $\sum_i R_i^T D_i R_i = I$.
Let $Z_i$ have columns spanning the null space of $S_i$ (the constants for a floating subdomain), and let $R_0^T$ have the columns $R_i^T D_i Z_i$.
With $Q_0 = R_0^T (R_0 S R_0^T)^{-1} R_0$, the *balancing domain decomposition* preconditioner is
$$M^{-1} = Q_0 + (I - Q_0 S) \Bigl( \sum_{i=1}^{N} R_i^T D_i S_i^{\dagger} D_i R_i \Bigr) (I - S Q_0),$$
where $S_i^\dagger$ is a generalized inverse of $S_i$.
Choose the weights $D_i$ from the values of $\rho$ as in the standard theory.
Then the [[condition number|AB3S6MHJ8X]] of $M^{-1} S$ satisfies
$$\kappa(M^{-1} S) \le C \Bigl( 1 + \log \frac{H}{h} \Bigr)^2,$$
with $C$ independent of $h$, $H$, $N$ and the values of $\rho$.

## Remarks

The local operator $\sum_i R_i^T D_i S_i^\dagger D_i R_i$ is the Neumann–Neumann preconditioner: each $S_i^\dagger$ solves a Neumann problem on $\Omega_i$.
A Neumann problem on a subdomain that does not touch the Dirichlet boundary is solvable only if its right-hand side is orthogonal to the constants.
The coarse correction $Q_0$ "balances" the residual so that these compatibility conditions hold, and at the same time it passes global information between all subdomains.
The proof bounds the energy of the weighted average of local functions by trace and discrete harmonic extension estimates, which bring in the factor $(1 + \log(H/h))^2$.

The bound depends on $H/h$ only, so refining the mesh and adding subdomains in proportion keeps the number of [[conjugate gradient|AFXZGQB4EN]] iterations nearly constant.
The method was introduced by Jan Mandel in 1993.

## Explanations

### L1 human

Balancing domain decomposition is a way to precondition the interface problem of the [[Schur complement method|R997ZAD141]].
Each piece of the domain solves a local problem with free (Neumann) edges, and the results are averaged on the interfaces.
A small global problem fixes the parts that the local solves cannot see.
The theorem says the number of iterations grows only like a squared logarithm of the number of mesh cells per subdomain.

### L2 human

The plain Neumann–Neumann method has no coarse space and scales poorly with the number of subdomains.
BDD adds a coarse space, and the later BDDC method uses a different coarse space built from primal constraints.
Its condition number bound is of the same polylogarithmic type as that of FETI methods, and in fact the two families are closely related.
It is one of the [[domain decomposition methods|AN054RHT1K]] that are robust with respect to large jumps of the coefficient across subdomains.
