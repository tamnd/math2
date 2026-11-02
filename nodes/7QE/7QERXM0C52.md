---
tag: 7QERXM0C52
kind: concept
name: Vanishing moments of a wavelet
msc: [42C40, 65T60]
sources:
  - url: https://en.wikipedia.org/wiki/Daubechies_wavelet
---

## Summary

A [[wavelet|4PZ35C0GV3]] $\psi$ has $p$ vanishing moments if it is orthogonal to all polynomials of degree less than $p$, that is, $\int x^k \psi(x) \, dx = 0$ for $k = 0, \dots, p - 1$.
Then the wavelet coefficients of a function that is smooth near a point are very small at fine scales near that point.
This is why wavelets with many vanishing moments compress smooth signals well.
The [[Daubechies wavelets|90V8S5CXE6]] have the shortest support among orthonormal wavelets with a given number of vanishing moments.

## Explanations

### L1 human

A wavelet with vanishing moments cannot see polynomials of low degree: its inner product with them is zero.
A smooth function looks like a polynomial on a small interval, by Taylor's formula.
So a narrow wavelet with many vanishing moments sees almost nothing of a smooth function, and its coefficient is close to zero.
Large coefficients appear only near jumps and other rough spots, which is what makes compression possible.
