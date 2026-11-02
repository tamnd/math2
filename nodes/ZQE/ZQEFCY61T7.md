---
tag: ZQEFCY61T7
kind: concept
name: Fourier multiplier
msc: ["42B15", "42A45"]
sources:
  - url: https://en.wikipedia.org/wiki/Multiplier_(Fourier_analysis)
same_as:
  wikidata: Q6935014
  wikipedia: Multiplier (Fourier analysis)
---

## Summary

A Fourier multiplier is an operator that acts on a function by multiplying its [[Fourier transform|DPVM34ADZV]] by a fixed function $m$, called the symbol.
Differential operators with constant coefficients, the [[Hilbert transform|NSCEBXM7ZM]], the heat semigroup and frequency filters are all of this form.
Every symbol in $L^\infty$ gives a bounded operator on $L^2$, and the bounded operators on $L^2(\R^n)$ that commute with translations are exactly these.
Which symbols give bounded operators on $L^p$ for $p \ne 2$ is a central and hard question of harmonic analysis, studied through [[$L^p$ multipliers|RAGR38Q40B]].
See the [[definition|SD89TZ1PHR]].

## Explanations

### L1 human

An equalizer on a music player raises or lowers each frequency by its own factor.
A Fourier multiplier does exactly that to a function.
It splits the function into frequencies, multiplies the amount of frequency $\xi$ by a number $m(\xi)$, and puts the pieces back together.
For example, $m(\xi) = 1$ for $\abs{\xi} \le 1$ and $0$ otherwise is an ideal low-pass filter that keeps only the low frequencies.
