---
tag: R38W9GFMQX
kind: example
name: Coiflet
msc: [42C40, 65T60]
instance_of: [4PZ35C0GV3]
uses: [1GHQMBR7DE, YH4BERB952, 7QERXM0C52]
sources:
  - url: https://en.wikipedia.org/wiki/Coiflet
same_as:
  wikidata: Q3487000
  wikipedia: Coiflet
---

## Example

Coiflets are a family of compactly supported orthonormal wavelets constructed by Ingrid Daubechies and named after Ronald Coifman.
For an even integer $L \ge 2$, the coiflet of order $L$ is a real orthonormal wavelet $\psi$ with [[scaling function|YH4BERB952]] $\varphi$ such that:

1. $\psi$ has $L$ [[vanishing moments|7QERXM0C52]]: $\int_{\R} x^l \psi(x) \, dx = 0$ for $l = 0, 1, \dots, L-1$.
2. $\int_{\R} \varphi(x) \, dx = 1$ and $\int_{\R} x^l \varphi(x) \, dx = 0$ for $l = 1, \dots, L-1$.

The low-pass filter of the coiflet of order $L$ has $3L$ coefficients, so $\varphi$ and $\psi$ are supported on intervals of length $3L - 1$.
For $L = 2$ the filter has $6$ coefficients.

## Remarks

The vanishing moments of the scaling function are the distinctive feature.
For a smooth function $f$, they make the scaling coefficient $\ip{f}{\varphi_{j,k}}$ close to $2^{-j/2} f(2^{-j} k)$, where $\varphi_{j,k}(x) = 2^{j/2}\varphi(2^j x - k)$, with an error that is small to high order in $2^{-j}$.
So samples of $f$ can be used directly as starting coefficients of the discrete wavelet transform.
To get these extra conditions, coiflets need longer filters than the [[Daubechies wavelets|90V8S5CXE6]] with the same number of vanishing moments of $\psi$.
Coiflets are also closer to symmetric than Daubechies wavelets.

## Explanations

### L1 human

Most wavelets only ask that the wavelet itself have zero average against low-degree polynomials.
Coiflets also ask this of the scaling function, apart from its total mass.
As a result, the scaling function acts almost like a point sample of the signal.
This makes them convenient when the input data are just samples of a smooth function.
