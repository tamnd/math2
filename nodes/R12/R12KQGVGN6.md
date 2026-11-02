---
tag: R12KQGVGN6
kind: concept
name: Perron–Wiener–Brelot solution
msc: [31B20, 31C05, 31A25]
specializes: [AEZ7PPCNQS]
sources:
  - url: https://en.wikipedia.org/wiki/Perron_method
---

## Summary

The Perron–Wiener–Brelot solution is the generalized solution of the [[Dirichlet problem|8D56GQ4AG8]] given by the [[Perron method|AEZ7PPCNQS]] with both upper and lower classes.
The upper solution is the infimum of [[superharmonic functions|X4V2S56YQQ]] lying above the boundary data.
The lower solution is the supremum of [[subharmonic functions|Z1MHMGFNFW]] lying below it.
When the two agree and are harmonic, the boundary function is called resolutive, and the common value is the PWB solution.
Wiener showed that every continuous boundary function is resolutive, and Brelot characterized resolutive functions as those integrable for harmonic measure.

## Explanations

### L1 human

Squeeze the unknown solution between functions that are too large at the boundary and functions that are too small.
If the best upper bound and the best lower bound meet, the meeting point is the solution.
For continuous boundary data on a bounded open set they always meet, even when the solution does not take the boundary values at every point.
For the punctured disc with data $0$ on the circle and $1$ at the centre, the PWB solution is $0$.
