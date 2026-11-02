---
tag: GEK0NP5WQM
kind: concept
name: n-term approximation
msc: [41A46, 41A65]
specializes: [YS1GRQRVY7]
sources:
  - url: https://en.wikipedia.org/wiki/Sparse_approximation
---

## Summary

$n$-term approximation approximates a function or vector by a linear combination of at most $n$ elements.
These elements are chosen freely from a fixed family, called a dictionary, such as a basis.
The best error with $n$ terms, $\sigma_n(f)$, measures how well $f$ can be compressed with respect to that dictionary.
The set of $n$-term combinations is not a linear space, so this is a basic model of [[nonlinear approximation|YS1GRQRVY7]].
It underlies wavelet compression, [[sparse approximation|WC8P971XGW]] and greedy algorithms such as [[matching pursuit|8KJ9P9KQ5H]].

## Explanations

### L1 human

In ordinary approximation one fixes in advance which basis functions to use, for example the first $n$ Fourier modes.
In $n$-term approximation one may pick any $n$ basis functions, and the choice depends on the target.
A signal with a few sharp features is well described by a few well-placed [[wavelets|4PZ35C0GV3]], even if they are not the first ones.
For an [[orthonormal basis|0S9GGTR0EX]] of a [[Hilbert space|HM2HHE3J51]] the best choice is simple: keep the $n$ coefficients of largest absolute value.
For example, $f = 3e_1 + e_2 + 2e_3$ in $\R^3$ has best $1$-term approximation $3e_1$, with error $\sqrt{1^2 + 2^2} = \sqrt{5}$.
