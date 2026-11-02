---
tag: QYY4NMDY5H
kind: concept
name: Wiener–Hopf equation
msc: ["45E10", 47B35]
specializes: [EY75YD988Z]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener%E2%80%93Hopf_method
---

## Summary

A Wiener–Hopf equation is a [[convolution integral equation|EY75YD988Z]] on the half-line.
The kernel depends only on $x - t$, but the unknown lives on $[0, \infty)$ and the integral runs over $[0, \infty)$.
The cut at $0$ breaks the translation symmetry, so the [[Fourier transform|DPVM34ADZV]] alone does not solve it.
It is solved by the [[Wiener–Hopf method|H4NXEY6QTZ]].
This method factors the symbol of the equation into pieces that extend holomorphically to the two half-planes.
Such equations model radiative transfer in a half-space, diffraction by a half-plane, and optimal causal filtering.

## Explanations

### L1 human

Imagine a medium that fills half of space, such as a star's atmosphere seen as a slab of infinite depth.
Each layer interacts with the others through a rule that depends only on their distance, but there are no layers beyond the surface.
The equation for the state of the layers is then a convolution, cut off at the surface.
A small example: the function $\varphi(x) = 1 + x$ satisfies $\varphi(x) = \int_0^\infty \frac{1}{2} e^{-\abs{x - t}} \varphi(t)\, dt$ for all $x \ge 0$.
