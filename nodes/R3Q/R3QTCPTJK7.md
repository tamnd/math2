---
tag: R3QTCPTJK7
kind: concept
name: Power series in several variables
msc: [32A05]
specializes: [0MZB06ST2B]
sources:
  - url: https://en.wikipedia.org/wiki/Power_series
---

## Summary

A power series in several variables is an infinite sum $\sum_\alpha c_\alpha (z - a)^\alpha$ of monomials in $z_1 - a_1, \dots, z_n - a_n$, indexed by [[multi-indices|0PJXBR6QA3]] $\alpha$.
It extends the one-variable [[power series|0MZB06ST2B]].
A function on an open set of $\C^n$ is [[holomorphic|507C34W0ZT]] exactly when it is locally the sum of a convergent power series.
The domain of convergence of such a series is the interior of the set where it converges.
Unlike in one variable, it is not always a polydisc; it is a [[logarithmically convex|EHWH6EF4QY]] complete [[Reinhardt domain|WA0SE56FVH]].

## Explanations

### L1 human

A polynomial in $z_1$ and $z_2$ is a finite sum of terms $c \, z_1^j z_2^k$.
A power series allows infinitely many such terms.
For example, $\sum_{j, k \ge 0} z_1^j z_2^k$ is the product of two geometric series, and it equals $\frac{1}{(1 - z_1)(1 - z_2)}$ when $\abs{z_1} < 1$ and $\abs{z_2} < 1$.
The terms have no natural order, so one asks the sum of their absolute values to be finite.
