---
kind: statement
name: Vanishing of Dolbeault cohomology descends to a hyperplane section
tag: ~a5b0b1ad
role: corollary
msc:
  - 32L10
  - 32C35
about:
  - Y3900T2EY5
uses:
  - Y3900T2EY5
  - 0PYW26VNT6
sources:
  - url: https://github.com/jirilebl/scv/blob/78d7d41554695c389552c301398803d4633b9208/scv.tex#L12709
    locator: scv.tex:12709
---

## Statement

Let $U \subset \C^n$ be an open set. Assume that the [[Dolbeault cohomology|Y3900T2EY5]] group $H^{(0,q)}(U)$ is zero for every $q$ with $1 \leq q \leq n-1$.

Let $L \subset \C^n$ be an affine hyperplane, that is, an [[affine subspace|0PYW26VNT6]] of complex dimension $n-1$.

Then $H^{(0,q)}(U \cap L) = 0$ for every $q$ with $1 \leq q \leq n-2$.

## Remarks

The set $U \cap L$ is open in $L$, and $L$ is a copy of $\C^{n-1}$. So the conclusion covers all degrees $q$ from $1$ up to the top relevant degree $n-2$ for $U \cap L$. The vanishing range drops by one when we pass to the hyperplane.
