---
tag: 9A4ZZ6ASN0
kind: concept
name: Pseudoconvexity at a boundary point
aliases: [levi-pseudoconvex-at-a-point, strongly-pseudoconvex-at-a-point, weakly-pseudoconvex-point]
msc: [32T05]
uses: [80MTNXWW80, PETEQQCS0B, Z7RVXBA2KB]
sources:
  - url: https://github.com/jirilebl/scv/blob/78d7d41554695c389552c301398803d4633b9208/scv.tex#L5699
    locator: scv.tex:5699
---

## Summary

Let $U \subset \C^n$ be open with smooth boundary, and let $p \in \partial U$.
Choose a defining function $r$ of $\partial U$ near $p$ with $r < 0$ on $U$.
For a vector $X_p = \sum_k a_k \, \partial/\partial z_k |_p$ in the holomorphic tangent space of $\partial U$ at $p$, the [[Levi form|80MTNXWW80]] is the Hermitian quadratic form $\sum_{k,\ell} \bar a_k a_\ell \, \partial^2 r / \partial \bar z_k \partial z_\ell (p)$.

The set $U$ is pseudoconvex at $p$ when this form is nonnegative for every such $X_p$, that is, when the Levi form is positive semidefinite at $p$.
It is strongly pseudoconvex at $p$ when the form is strictly positive for every nonzero $X_p$, that is, when the Levi form is positive definite.
It is weakly pseudoconvex at $p$ when it is pseudoconvex but not strongly pseudoconvex there.

A domain is pseudoconvex when it is pseudoconvex at every boundary point, which gives a [[Levi pseudoconvex domain|PETEQQCS0B]].
A bounded domain is strongly pseudoconvex when it is strongly pseudoconvex at every boundary point, which gives a [[strongly pseudoconvex domain|Z7RVXBA2KB]].
For unbounded domains the usage in the literature varies.
