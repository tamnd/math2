---
tag: B1TEQ98JZD
kind: concept
name: Tate algebra
msc: [32P05, 14G22, 12J25]
sources:
  - url: https://en.wikipedia.org/wiki/Restricted_power_series
---

## Summary

The Tate algebra in $n$ variables over a complete non-archimedean field $K$ is the algebra of power series whose coefficients tend to $0$.
These are exactly the power series that converge on the closed unit polydisc over an algebraic closure of $K$.
With the Gauss norm it is a [[Banach algebra|9KYWN94QDN]], and it is a [[Noetherian|0670T59HGE]] unique factorization domain.
Its quotients, the affinoid algebras, are the local building blocks of [[rigid analytic spaces|YAH6MZVG7K]], as polynomial rings are for algebraic varieties.

## Explanations

### L1 human

Over the [[$p$-adic numbers|BT6T702C28]], a series $\sum a_k$ converges exactly when its terms tend to $0$.
So a power series $\sum a_k x^k$ converges at every $x$ with $\abs{x} \le 1$ exactly when $\abs{a_k} \to 0$.
The Tate algebra collects these power series, in one or several variables.
For example $\sum_k p^k x^k$ belongs to it, while $\sum_k x^k$ does not, since it diverges at $x = 1$.
It plays the role that the ring of holomorphic functions on a closed polydisc plays in complex analysis.
