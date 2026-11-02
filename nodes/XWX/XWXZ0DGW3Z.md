---
tag: XWXZ0DGW3Z
kind: concept
name: Numerical range
msc: [47A12]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_range
same_as:
  wikidata: Q1579053
  wikipedia: Numerical range
---

## Summary

The numerical range of an operator $T$ on a complex Hilbert space is the set of values $\ip{Tx}{x}$ for unit vectors $x$.
It is a convex subset of the complex plane whose closure contains the spectrum.
It gives easy bounds for the spectrum and for the norm, and it characterises self-adjoint operators as those with real numerical range.

## Explanations

### L1 human

For a unit vector $x$, the number $\ip{Tx}{x}$ measures how much $Tx$ points back in the direction of $x$.
In quantum mechanics it is the expected value of the observable $T$ in the state $x$.
Collecting these numbers over all unit vectors gives the numerical range.
For a real symmetric $2 \times 2$ matrix with eigenvalues $1$ and $3$, the numerical range is the interval $[1, 3]$.
