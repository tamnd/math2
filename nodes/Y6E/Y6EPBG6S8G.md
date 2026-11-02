---
tag: Y6EPBG6S8G
kind: concept
name: Sine and cosine series
msc: [42A16, 42A20]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_series
---

## Summary

The Fourier sine series and the Fourier cosine series expand a function given on the interval $[0, \pi]$ in the functions $\sin nx$ alone or $\cos nx$ alone.
They are the [[Fourier series|G12KXDHPPS]] of the odd and of the even $2\pi$-periodic extension of the function.
They appear when separation of variables is applied to the heat or wave equation on an interval.
Dirichlet boundary conditions lead to sine series, and Neumann conditions to cosine series.

## Explanations

### L1 human

A function given only on $[0, \pi]$ can be extended to $[-\pi, \pi]$ in two natural ways: as an odd function or as an even function.
The odd extension has a Fourier series with only sines, and the even extension one with only cosines.
For example, the constant $1$ on $(0, \pi)$ has the cosine series $1$ and the sine series $\frac{4}{\pi}\left(\sin x + \frac{\sin 3x}{3} + \frac{\sin 5x}{5} + \cdots\right)$.
The sine series vanishes at $0$ and $\pi$, which suits a vibrating string fixed at both ends.
