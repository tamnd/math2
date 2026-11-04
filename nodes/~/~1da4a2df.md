---
tag: ~1da4a2df
kind: concept
name: Order of vanishing of a holomorphic function at a point
aliases: [order-of-vanishing, vanishing-order]
msc: [32A10]
uses: [0NAHXR1FRH, 2C3PAQ7H50]
sources:
  - url: https://github.com/jirilebl/scv/blob/78d7d41554695c389552c301398803d4633b9208/scv.tex#L14339
    locator: scv.tex:14339
---

## Summary

Let $p \in \mathbb{C}^n$ and let $f$ be a [[holomorphic function|0NAHXR1FRH]] on a neighborhood of $p$.
Expand $f$ near $p$ as a sum $\sum_{k \ge 0} f_k$, where $f_k$ is the [[homogeneous polynomial|2C3PAQ7H50]] of degree $k$ in the variables $z - p$ that collects the terms of total degree $k$ of the Taylor series of $f$ at $p$.

The order of vanishing of $f$ at $p$, written $\operatorname{ord}_p f$, is the least $k \ge 0$ such that $f_k$ is not the zero polynomial.
So it is the degree of the lowest nonzero homogeneous part of the series.

If $f$ is identically zero near $p$, every $f_k$ is zero, and the order is set to be $\infty$.
The order is $0$ exactly when $f(p) \ne 0$.
