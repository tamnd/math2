---
tag: E06PG40SVD
kind: concept
name: Spherical transform
msc: ["43A90", "43A32", "22E30"]
sources:
  - url: https://en.wikipedia.org/wiki/Zonal_spherical_function
---

## Summary

The spherical transform of a [[Gelfand pair|W38ZDXDVYC]] $(G, K)$ integrates a bi-$K$-invariant function against the bounded [[spherical functions|BKZNC76RC8]].
It is the Gelfand transform of the commutative convolution algebra $L^1(K \backslash G / K)$, so it turns convolution into pointwise multiplication.
For $G = \R^n$ with $K$ trivial it is the ordinary [[Fourier transform|DPVM34ADZV]], and for $G = \R^n \rtimes \mathrm{SO}(n)$ with $K = \mathrm{SO}(n)$ it is the Fourier transform of radial functions.
For semisimple Lie groups its inversion and Plancherel formula are governed by the [[Harish-Chandra c-function|4X2N0BN3M0]].

## Explanations

### L1 human

Take a space with a lot of symmetry, such as the sphere or the hyperbolic plane.
On it, the functions that depend only on the distance from a base point are the simplest ones.
The spherical functions are the special functions of this kind that behave like waves.
The spherical transform measures how much of each wave a given radial function contains.
On the line, the waves are the exponentials $e^{i \xi x}$ and the transform is the Fourier transform.
