---
about:
- Y3900T2EY5
kind: statement
msc:
- 32L10
- 32C35
- 32A26
name: Vanishing of Dolbeault cohomology passes to an affine hyperplane section
role: corollary
sources:
- url: https://github.com/jirilebl/scv/blob/78d7d41554695c389552c301398803d4633b9208/scv.tex#L12681
  locator: scv.tex:12681
tag: 7TQ8Z8KHSF
uses:
- Y3900T2EY5
---

## Statement

Let $U \subset \C^n$ be an open set, and let $L \subset \C^n$ be an affine hyperplane.
Fix integers $p \ge 0$ and $q \ge 1$.
Write $H^{(p,q)}$ for the [[Dolbeault cohomology|Y3900T2EY5]] of an open set.
Suppose that $H^{(p,q)}(U) = 0$ and $H^{(p,q+1)}(U) = 0$.
Then $H^{(p,q)}(U \cap L) = 0$.

## Remarks

The set $U \cap L$ is open in $L$, and $L$ is a copy of $\C^{n-1}$.
So the group $H^{(p,q)}(U \cap L)$ is the Dolbeault cohomology of an open subset of $\C^{n-1}$.
The result says that two consecutive vanishing groups on $U$ force the vanishing of the lower group on the slice.
