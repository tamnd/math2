---
tag: VJCJYXGTDY
kind: concept
name: Zeta function regularization
msc: ["11M41", "58J52", "40G99"]
sources:
  - url: https://en.wikipedia.org/wiki/Zeta_function_regularization
same_as:
  wikidata: Q1048264
  wikipedia: Zeta function regularization
---

## Summary

Zeta function regularization assigns finite values to divergent sums $\sum \lambda_n$ and divergent products $\prod \lambda_n$ of positive numbers.
One forms the zeta function $\zeta_\lambda(s) = \sum \lambda_n^{-s}$, which converges for large $\operatorname{Re} s$, and continues it by [[analytic continuation|0M3YQJ81NB]].
The regularized sum is $\zeta_\lambda(-1)$, and the regularized product is $e^{-\zeta_\lambda'(0)}$.
For $\lambda_n = n$ the [[Riemann zeta function|1XWBY4N0VT]] gives the regularized value $-\frac{1}{12}$ of $1 + 2 + 3 + \cdots$.
The method is used for determinants of Laplacians and in quantum field theory.

## Explanations

### L1 human

The sum $1 + 2 + 3 + \cdots$ diverges, but the sum $1^{-s} + 2^{-s} + 3^{-s} + \cdots$ converges when $s > 1$ and defines a function of $s$.
That function has a unique analytic continuation to all complex $s \ne 1$.
Plugging $s = -1$ into the extension formally gives back $1 + 2 + 3 + \cdots$, and the value obtained is $-\frac{1}{12}$.
Zeta regularization does the same for any sequence of positive numbers that grows fast enough.
