---
tag: NSCEBXM7ZM
kind: concept
name: Hilbert transform
msc: [44A15, 42A50, 30H10]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_transform
same_as:
  wikidata: Q685437
  wikipedia: Hilbert transform
---

## Summary

The Hilbert transform is the linear operator on functions of a real variable given by convolution with $\frac{1}{\pi x}$ in the [[principal value|0SYR10HD4R]] sense.
Let $u + iv$ be holomorphic on the upper half-plane and decay at infinity.
Then the transform sends the boundary values of $u$ to those of $v$, so it is the operator of [[harmonic conjugation|050F2FMTKF]] on the line.
On the Fourier side it multiplies by $-i \sgn(\xi)$.
It is the model example of a singular integral operator, and it appears in signal processing and in the [[Kramers–Kronig relations|GFS95PZ5YK]].

## Explanations

### L1 human

The Hilbert transform shifts the phase of each frequency component of a signal by a quarter turn.
It sends $\cos$ to $\sin$ and $\sin$ to $-\cos$.
If $u + iv$ is holomorphic in the upper half-plane and decays at infinity, then on the real line $v$ is the Hilbert transform of $u$.
For example, $\frac{i}{x + i} = \frac{1}{1 + x^2} + i \frac{x}{1 + x^2}$, so the transform of $\frac{1}{1 + x^2}$ is $\frac{x}{1 + x^2}$.
