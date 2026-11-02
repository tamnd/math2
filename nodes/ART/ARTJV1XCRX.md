---
tag: ARTJV1XCRX
kind: concept
name: Resolvent kernel
msc: [45B05, 45P05]
specializes: [GSMBXT7FPK]
sources:
  - url: https://en.wikipedia.org/wiki/Liouville%E2%80%93Neumann_series
---

## Summary

The resolvent kernel $R(x, s; \lambda)$ of a [[kernel|GSMBXT7FPK]] $K$ gives the solution of the [[integral equation of the second kind|8KJCN49V64]] $\varphi = f + \lambda K \varphi$.
The solution is $\varphi(x) = f(x) + \lambda \int_a^b R(x, s; \lambda) f(s) \, ds$.
For small $\abs{\lambda}$ it is the sum $\sum_{n \ge 1} \lambda^{n-1} K_n$ of the [[iterated kernels|9QNBFERMHD]].
It thus inverts the operator $I - \lambda K$ once and for all, for every right side $f$.
For a continuous kernel it extends to a meromorphic function of $\lambda$, whose poles are characteristic values of $K$.

## Explanations

### L1 human

Solving the equation for each new right side separately is wasteful.
The resolvent kernel is a single formula that turns any right side directly into the solution.
It plays the role of the inverse matrix in linear algebra.
For example, for $K(x, s) = x s$ on $[0, 1]$ the resolvent kernel is $R(x, s; \lambda) = 3 x s / (3 - \lambda)$.
