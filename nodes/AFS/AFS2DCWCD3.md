---
tag: AFS2DCWCD3
kind: concept
name: Bochner–Riesz means
msc: [42B08, 42B15]
sources:
  - url: https://en.wikipedia.org/wiki/Bochner%E2%80%93Riesz_mean
same_as:
  wikidata: Q4936247
  wikipedia: Bochner–Riesz mean
---

## Summary

The Bochner–Riesz means of a function $f$ on $\R^n$ are the operators $S^\delta_R f$ that multiply the [[Fourier transform|DPVM34ADZV]] of $f$ by $(1 - \abs{\xi}^2/R^2)_+^\delta$.
They are a smoothed version of the spherical partial sums of the Fourier integral, with smoothing order $\delta \ge 0$.
The central question is for which $\delta$ and $p$ they are bounded on $L^p(\R^n)$, which decides whether $S^\delta_R f \to f$ in $L^p$ as $R \to \infty$.
This question is tied to the restriction and Kakeya problems.

## Explanations

### L1 human

To rebuild a function from its frequencies, one may add up all frequencies of size less than $R$ and let $R$ grow.
A sharp cut at $\abs{\xi} = R$ behaves badly in higher dimensions, so one fades the frequencies out gently near the edge of the ball instead.
The exponent $\delta$ says how gentle the fade is: $\delta = 0$ is the sharp cut, and larger $\delta$ gives a smoother fade.
In one dimension with $\delta = 1$ and the factor $1 - \abs{\xi}/R$ instead, one gets the familiar Fejér means; the Bochner–Riesz means are the round analogue in $\R^n$.
