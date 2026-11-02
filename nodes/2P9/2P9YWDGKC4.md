---
tag: 2P9YWDGKC4
kind: concept
name: Hankel transform
msc: [44A20, 33C10, 42B10]
specializes: [YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Hankel_transform
same_as:
  wikidata: Q155208
  wikipedia: Hankel transform
---

## Summary

The Hankel transform of order $\nu$ of a function $f$ on $(0, \infty)$ is $\int_0^\infty f(r)\, J_\nu(kr)\, r\, dr$, where $J_\nu$ is the [[Bessel function of the first kind|CZCMRDWDYW]].
It is the radial part of the [[Fourier transform|DPVM34ADZV]].
The Fourier transform of a radial function in the plane is a Hankel transform of order $0$, and in higher dimensions other orders appear.
With this normalization it is its own inverse.
It is used to solve problems with circular or cylindrical symmetry, such as heat flow and vibrations of a drum.

## Explanations

### L1 human

The Fourier transform writes a function as a sum of plane waves.
For a function that only depends on the distance to a centre, circular waves are better suited, and their profiles are Bessel functions.
The Hankel transform measures how much of each circular wave of frequency $k$ the function contains.
For example, the Gaussian $e^{-r^2/2}$ has the Hankel transform $e^{-k^2/2}$ of order $0$, the same shape again.
