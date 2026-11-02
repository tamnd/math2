---
tag: EVPZ7ZG1HB
kind: concept
name: Ring of convergent power series
msc: [32B05, 13J07, 32A05]
specializes: [3E8ZG3NJYZ]
sources:
  - url: https://en.wikipedia.org/wiki/Function_of_several_complex_variables
---

## Summary

The ring of convergent power series $\C\{z_1, \dots, z_n\}$ consists of the formal power series in $n$ variables that converge on some neighbourhood of the origin.
It is a subring of the ring of [[multivariate formal power series|3E8ZG3NJYZ]] $\C[\![z_1, \dots, z_n]\!]$.
It is isomorphic to the ring of [[germs of holomorphic functions|7PJ8KVZZCQ]] at $0 \in \C^n$, and it is the basic algebraic object of local analytic geometry.
It is a Noetherian local unique factorization domain, as is its formal completion.

## Explanations

### L1 human

A power series in several variables is an infinite sum of monomials $z_1^{k_1} \cdots z_n^{k_n}$ with coefficients.
Some such series converge near the origin, such as $\sum_{k} (z_1 z_2)^k$, and some converge only at the origin, such as $\sum_k k!\, z_1^k$.
The convergent ones can be added and multiplied, and they form a ring.
This ring encodes all holomorphic functions near the origin, through their Taylor series.
