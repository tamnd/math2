---
tag: SVABG134WE
kind: concept
name: Trigonometric interpolation
msc: [42A15, 65T40]
sources:
  - url: https://en.wikipedia.org/wiki/Trigonometric_interpolation
same_as:
  wikidata: Q464356
  wikipedia: Trigonometric interpolation
---

## Summary

Trigonometric interpolation fits a [[trigonometric polynomial|J3NJQ5FZJ5]] through prescribed values at given points of a period.
With $2n + 1$ distinct nodes in one period there is exactly one interpolating trigonometric polynomial of degree at most $n$.
It is the periodic counterpart of [[Lagrange interpolation|237KR6FRCK]] by ordinary polynomials.
For equally spaced nodes its coefficients are given by the [[discrete Fourier transform|TST0GH66A5]].
This makes it fast to compute and central in numerical analysis and signal processing.

## Explanations

### L1 human

Suppose you measure a periodic quantity, like temperature over a day, at a few moments.
Trigonometric interpolation finds a sum of a few waves that passes exactly through all the measurements.
For example, through the values $1, 0, 0$ at the angles $0, 2\pi/3, 4\pi/3$ passes the curve $\frac{1}{3} + \frac{2}{3} \cos x$.
With equally spaced measurements, the waves are found by the discrete Fourier transform.
