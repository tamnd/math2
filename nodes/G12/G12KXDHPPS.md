---
tag: G12KXDHPPS
kind: concept
name: Fourier series
msc: [42A16, 42A20]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_series
same_as:
  wikidata: Q179467
  wikipedia: Fourier series
---

## Summary

The Fourier series of a periodic function writes it as a sum of sines and cosines, or of complex exponentials $e^{inx}$.
Its coefficients are computed by integrals.
It turns problems about periodic functions into problems about sequences of coefficients.
Whether and in which sense the series converges back to the function is a central question of harmonic analysis.
[[Parseval's identity|047RFCNVSK]] and [[Fejér's theorem|TPJZCSXSVN]] give two answers.

## Explanations

### L1 human

A musical sound can be split into a fundamental tone and its overtones.
The Fourier series does the same for any periodic function: it is a sum of pure waves whose frequencies are whole multiples of a base frequency.
Each coefficient says how much of one wave is present.
For example, the sawtooth function equal to $x$ on $(-\pi, \pi)$ is $2(\sin x - \frac{1}{2}\sin 2x + \frac{1}{3} \sin 3x - \cdots)$ at every point strictly between $-\pi$ and $\pi$.
