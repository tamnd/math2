---
tag: VA7MH05Z3B
kind: concept
name: Zeilberger's algorithm
msc: [33F10, 05A19, 68W30]
sources:
  - url: https://en.wikipedia.org/wiki/Wilf%E2%80%93Zeilberger_pair
---

## Summary

Zeilberger's algorithm, also called the method of creative telescoping, takes a definite sum $f(n) = \sum_k F(n, k)$ of a hypergeometric term.
It finds a linear [[recurrence|0FYX44GP92]] in $n$ with polynomial coefficients that $f$ satisfies.
It works by running a parametrised version of [[Gosper's algorithm|NHMJQBS04M]] on a combination of shifts $F(n + j, k)$.
With the recurrence and a few initial values, identities for definite sums can be proved or discovered automatically.
It is a main tool of the "A = B" approach to hypergeometric identities.

## Explanations

### L1 human

Many identities say that a sum over $k$ of binomial-like terms has a simple value depending on $n$.
Zeilberger's algorithm does not guess the value; it finds a recurrence in $n$ that the sum must satisfy.
For $\sum_k \binom{n}{k}$ it finds $f(n + 1) = 2f(n)$, and with $f(0) = 1$ this gives $2^n$.
If the claimed value satisfies the same recurrence and the same initial values, the identity is proved.
