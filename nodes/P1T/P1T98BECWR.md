---
tag: P1T98BECWR
kind: concept
name: Sinc function
msc: ["33B10", "94A12"]
sources:
  - url: https://en.wikipedia.org/wiki/Sinc_function
same_as:
  wikidata: Q855949
  wikipedia: Sinc function
---

## Summary

The sinc function is $\operatorname{sinc} x = \frac{\sin x}{x}$, with the value $1$ at $x = 0$.
Signal processing often uses the normalised version $\frac{\sin \pi x}{\pi x}$, whose zeros are the non-zero integers.
The normalised sinc function is the [[Fourier transform|DPVM34ADZV]] of the indicator function of an interval, and it is the interpolation kernel in the sampling theorem.
Its integral over $(0, \infty)$ is the [[Dirichlet integral|0GZNSHMG4Q]], equal to $\frac{\pi}{2}$.

## Explanations

### L1 human

The sine wave $\sin x$ goes up and down forever with the same height.
Dividing by $x$ makes the waves smaller and smaller far from the origin.
Near $0$ both $\sin x$ and $x$ are small, and their quotient is close to $1$.
So the graph has a tall central hump of height $1$ and decaying ripples on both sides, crossing zero at $\pm\pi, \pm 2\pi, \ldots$.
