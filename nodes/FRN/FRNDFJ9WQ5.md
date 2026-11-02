---
tag: FRNDFJ9WQ5
kind: concept
name: Riesz transform
msc: [42B20, 44A15]
specializes: [HTMCEARGDD]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz_transform
same_as:
  wikidata: Q7333169
  wikipedia: Riesz transform
---

## Summary

The Riesz transforms $R_1, \ldots, R_n$ are the $n$ [[singular integral operators|HTMCEARGDD]] on $\R^n$ with Fourier multipliers $-i\xi_j/\abs{\xi}$.
They are the higher-dimensional analogue of the [[Hilbert transform|NSCEBXM7ZM]], which is the case $n = 1$.
They express second derivatives through the Laplacian, by $\partial_j\partial_k = -R_j R_k \Delta$, so their $L^p$ bounds give $L^p$ estimates for elliptic equations.
They are bounded on $L^p(\R^n)$ for $1 < p < \infty$ and commute with translations and dilations.

## Explanations

### L1 human

The Hilbert transform on the line keeps the size of each frequency and turns its phase by a quarter turn.
In several variables there is one such operator for each coordinate direction.
The $j$-th Riesz transform weights the frequency $\xi$ by the $j$-th component of its direction $\xi/\abs{\xi}$, and turns the phase by a quarter turn.
Together they turn a function into a vector field, much as the gradient does, but without changing the size of frequencies.
For example, the sum $R_1^2 + \cdots + R_n^2$ is minus the identity, because the squared components of a unit vector add up to $1$.
