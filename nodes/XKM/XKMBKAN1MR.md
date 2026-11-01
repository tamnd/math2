---
tag: XKMBKAN1MR
kind: definition
name: Cohomological dimension of a field
msc: [12G10, 12G05]
defines: QZMZXFFJFJ
uses: [EESNTXFWHZ, PGKWBJDTKX, EF4ZWACHD8, 0SN0MAEKYX]
sources:
  - url: https://en.wikipedia.org/wiki/Cohomological_dimension
---

## Definition

Let $K$ be a field with [[absolute Galois group|PGKWBJDTKX]] $G_K$, and let $p$ be a [[prime number|0SN0MAEKYX]].
For a discrete torsion $G_K$-module $M$, let $H^q(K, M)(p)$ be the $p$-primary part of the [[Galois cohomology|EESNTXFWHZ]] group $H^q(K, M)$.
The *$p$-cohomological dimension* $\operatorname{cd}_p(K)$ is the least integer $n \ge 0$ with the following property.
For all $q > n$ and all discrete torsion $G_K$-modules $M$, $H^q(K, M)(p) = 0$.
If there is no such $n$, then $\operatorname{cd}_p(K) = \infty$.
The *cohomological dimension* of $K$ is $\operatorname{cd}(K) = \sup_p \operatorname{cd}_p(K)$.

## Remarks

These are the [[cohomological dimensions|EF4ZWACHD8]] $\operatorname{cd}_p(G_K)$ and $\operatorname{cd}(G_K)$ of the profinite group $G_K$.
It suffices to test one degree and simple modules: $\operatorname{cd}_p(K) \le n$ if and only if $H^{n+1}(K, M) = 0$ for every simple discrete $G_K$-module $M$ with $pM = 0$.
Example: a finite field $\F_q$ has $\operatorname{cd}(\F_q) = 1$, since $G_{\F_q}$ is the profinite completion $\widehat{\Z}$ of $\Z$, whose cohomology with torsion coefficients vanishes above degree $1$, while $H^1(\F_q, \Z/p\Z) = \Hom(\widehat{\Z}, \Z/p\Z) \ne 0$.
Example: $\operatorname{cd}(K) = 0$ if and only if $K$ is separably closed.
Example: $\R$ has $\operatorname{cd}_2(\R) = \infty$, since $G_\R$ has order $2$ and $H^q(\Z/2\Z, \Z/2\Z) \cong \Z/2\Z$ for all $q \ge 0$.
More generally, a field with a nontrivial finite absolute Galois group has infinite cohomological dimension.
If $K$ has characteristic $p > 0$, then $\operatorname{cd}_p(K) \le 1$.
A finite extension of $\Q_p$ has cohomological dimension $2$.
