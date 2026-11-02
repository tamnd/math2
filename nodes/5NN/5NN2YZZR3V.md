---
tag: 5NN2YZZR3V
kind: concept
name: Fourier coefficient
msc: [42A16]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_series
---

## Summary

The $n$-th Fourier coefficient $\hat f(n)$ of a $2\pi$-periodic integrable function $f$ measures how much of the wave $e^{inx}$ is present in $f$.
It is the average of $f(x) e^{-inx}$ over one period, and it is the inner product of $f$ with the [[Fourier monomial|TZYSW0975T]] $e_n$.
The sequence $(\hat f(n))_{n \in \Z}$ determines $f$ up to a null set, and the [[Fourier series|G12KXDHPPS]] of $f$ is $\sum_n \hat f(n) e^{inx}$.
The size of the coefficients for large $\abs{n}$ reflects the smoothness of $f$.

## Explanations

### L1 human

To find how much of the frequency $n$ is in a signal, multiply the signal by the wave $e^{-inx}$ and average over one period.
The other frequencies average out to zero, and only the part with frequency $n$ survives.
For example, for $f(x) = 3 + 5 \cos 2x$ the coefficient $\hat f(0)$ is $3$, the coefficients $\hat f(2)$ and $\hat f(-2)$ are $\frac{5}{2}$, and all the others are $0$.
