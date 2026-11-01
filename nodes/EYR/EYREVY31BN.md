---
tag: EYREVY31BN
kind: concept
name: Eisenstein series
msc: [11F11]
specializes: [GWKN5VG78A]
sources:
  - url: https://en.wikipedia.org/wiki/Eisenstein_series
same_as:
  wikidata: Q1313257
  wikipedia: Eisenstein series
---

## Summary

The Eisenstein series $G_k$ of even weight $k \ge 4$ is the sum of $(m\tau + n)^{-k}$ over all pairs of integers $(m, n) \neq (0, 0)$.
It is the simplest [[modular form|GWKN5VG78A]] of weight $k$ for the [[modular group|VEKV1EM77B]] that is not a [[cusp form|A50Y012RBP]].
Its $q$-expansion involves the [[Riemann zeta function|1XWBY4N0VT]] and the divisor sums $\sigma_{k-1}(n)$.
The series $E_4$ and $E_6$ generate the ring of all modular forms for $\mathrm{SL}_2(\Z)$.

## Explanations

### L1 human

Take the lattice of points $m\tau + n$ in the complex plane and add up the $k$-th powers of their reciprocals.
Changing the basis of the lattice by a matrix of $\mathrm{SL}_2(\Z)$ only reorders the sum, and this gives the modular symmetry.
The result has a neat expansion: $E_4 = 1 + 240 \sum_{n \ge 1} \sigma_3(n) q^n$, where $\sigma_3(n)$ is the sum of the cubes of the divisors of $n$.
Comparing such expansions proves surprising identities between divisor sums.
