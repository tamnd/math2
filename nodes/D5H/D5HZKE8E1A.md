---
tag: D5HZKE8E1A
kind: concept
name: Oscillatory integral
msc: [42B20, 41A60]
sources:
  - url: https://en.wikipedia.org/wiki/Oscillatory_integral
---

## Summary

An oscillatory integral is an integral of the form $\int e^{i\lambda\phi(x)} \psi(x) \, dx$.
Here $\phi$ is a real phase function, $\psi$ is an amplitude and $\lambda$ is a large real parameter.
The main question is how fast it decays as $\lambda \to \infty$, which depends on the critical points of $\phi$.
Fourier transforms of measures on curved surfaces, Bessel functions and solutions of dispersive equations are all oscillatory integrals.
Their estimates are basic tools in harmonic analysis, number theory and PDE.

## Explanations

### L1 human

When $\lambda$ is large, the factor $e^{i\lambda\phi(x)}$ spins around the unit circle very fast as $x$ moves.
Its positive and negative parts nearly cancel, so the integral is small.
The cancellation is weakest where $\phi$ is flat, at points where its derivative vanishes, and these points decide the size of the integral.
For example, $\int_{-\infty}^{\infty} e^{i\lambda x^2} e^{-x^2} \, dx = \sqrt{\pi/(1 - i\lambda)}$, which is of size $\lambda^{-1/2}$ for large $\lambda$, because the phase $x^2$ is flat at $x = 0$.
