---
tag: FMVVV8VKHG
kind: definition
name: Cohomological dimension of a group
msc: [20J05, 20J06]
defines: EF4ZWACHD8
uses: [G5S1M9, HK2AA1YSQ2, 0KTW26C80J, 0KVGH0J5B3, PEMNN32A43]
sources:
  - url: https://en.wikipedia.org/wiki/Cohomological_dimension
---

## Definition

Let $G$ be a [[group|G5S1M9]].
The *cohomological dimension* $\mathrm{cd}(G)$ is the smallest integer $n \ge 0$ such that $H^k(G, M) = 0$ for every $G$-module $M$ and every $k > n$.
Here $H^k(G, M)$ is the cohomology group.
If there is no such integer, then $\mathrm{cd}(G) = \infty$.

## Remarks

Equivalently, $\mathrm{cd}(G)$ is the smallest $n$ such that $\Z$, with trivial action, has a [[projective resolution|HK2AA1YSQ2]] of length $n$ over the group ring $\Z[G]$.
For a subgroup $H$ of $G$, $\mathrm{cd}(H) \le \mathrm{cd}(G)$.
The only group with $\mathrm{cd}(G) = 0$ is the trivial group.

Example: $\mathrm{cd}(\Z) = 1$.
The resolution $0 \to \Z[t, t^{-1}] \xrightarrow{\ t - 1\ } \Z[t, t^{-1}] \to \Z \to 0$ has length $1$, and $H^1(\Z, \Z) \cong \Z$ is not zero.
More generally, $\mathrm{cd}(\Z^n) = n$, and a nontrivial [[free group|0KTW26C80J]] has cohomological dimension $1$.

Non-example: a nontrivial finite [[cyclic group|0KVGH0J5B3]] $C_m$ has $H^{2k}(C_m, \Z) \cong \Z/m\Z \ne 0$ for every $k \ge 1$, so no integer $n$ works and $\mathrm{cd}(C_m) = \infty$.
Since a group containing $C_m$ has dimension at least that of $C_m$, every group of finite cohomological dimension is [[torsion-free|PEMNN32A43]].
