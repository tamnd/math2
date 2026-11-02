---
tag: AAECHE30BD
kind: concept
name: Fourier series on the torus
msc: ["42B05", "42A16"]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_series
---

## Summary

A Fourier series on the torus $\mathbb{T}^n = \R^n / \Z^n$ expands a function that is periodic in each of $n$ variables into waves.
There is one wave $e^{2\pi i k \cdot x}$ for each integer vector $k \in \Z^n$.
For $n = 1$ it is the classical [[Fourier series|G12KXDHPPS]] of a periodic function.
The coefficients form a function on $\Z^n$.
The passage from $f$ to its coefficients is a case of the [[Fourier transform on locally compact abelian groups|VHN5VW5Q92]], for the compact group $\mathbb{T}^n$.
Convergence in several variables depends on how the partial sums are formed, for example over cubes or over balls in $\Z^n$.
See the [[definition|T4JEMK1549]].

## Explanations

### L1 human

Think of a function on a square whose values on opposite edges match, like a wallpaper pattern that tiles the plane.
Such a pattern can be written as a sum of plane waves, each oscillating a whole number of times across the square in each direction.
The wave with frequency vector $k = (k_1, k_2)$ is $e^{2\pi i (k_1 x_1 + k_2 x_2)}$.
For instance, $\cos(2\pi x_1) \cos(2\pi x_2)$ is the sum of the four waves with $k = (\pm 1, \pm 1)$, each with coefficient $\frac14$.
