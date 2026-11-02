---
tag: WYCJN9GDW4
kind: definition
name: Brill–Noether theory
msc: [14H51, 14C20]
defines: 82ZR6BCJXV
uses: [XJM2MT4S3Y, 6W8TDV9VVN, 3Z9DCWYXQZ, 7JCF2TE3V5, GHRPE8CXJ9]
sources:
  - url: https://en.wikipedia.org/wiki/Brill%E2%80%93Noether_theory
---

## Definition

Let $X$ be a smooth projective [[algebraic curve|XJM2MT4S3Y]] of [[genus|6W8TDV9VVN]] $g$ over an algebraically closed field.
For an integer $d$, let $\operatorname{Pic}^d(X)$ be the set of isomorphism classes of [[line bundles|7JCF2TE3V5]] of degree $d$ on $X$.
It is a subset of the [[Picard group|3Z9DCWYXQZ]] of $X$.
For integers $r \ge 0$ and $d$:

1. The *Brill–Noether locus* is $W^r_d(X) = \set{L \in \operatorname{Pic}^d(X) : h^0(X, L) \ge r + 1}$, the set of line bundles of degree $d$ whose complete [[linear system|GHRPE8CXJ9]] has dimension at least $r$.
2. The *Brill–Noether number* is $\rho(g, r, d) = g - (r + 1)(g - d + r)$.

*Brill–Noether theory* is the study of the loci $W^r_d(X)$, in particular of when they are nonempty and of their dimension.

## Remarks

The locus $W^r_d(X)$ is a closed subvariety of $\operatorname{Pic}^d(X)$, which is a copy of the Jacobian, of dimension $g$.
The number $\rho$ is the expected dimension of $W^r_d(X)$: it is $g$ minus the number of conditions $(r + 1)(g - d + r)$ that the existence of $r + 1$ sections imposes, as predicted by Riemann–Roch.
Existence theorem (Kempf, Kleiman–Laksov): if $\rho \ge 0$, then $W^r_d(X)$ is nonempty for every curve $X$.
Griffiths–Harris theorem: for a general curve $X$ of genus $g$, $W^r_d(X)$ is empty if $\rho < 0$, and it has dimension $\rho$ if $0 \le \rho \le g$.
Example: for $g = 3$, $r = 1$, $d = 2$, one gets $\rho = 3 - 2 \cdot 2 = -1$, so a general curve of genus $3$ has no pencil of degree $2$ and is not hyperelliptic.
Example: for $r = 0$ and $0 \le d \le g$, one gets $\rho = d$, and $W^0_d(X)$ is the image of the $d$-fold symmetric product of $X$, of dimension $d$.
