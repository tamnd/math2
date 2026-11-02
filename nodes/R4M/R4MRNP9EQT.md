---
tag: R4MRNP9EQT
kind: concept
name: Gelfand–Levitan theory
msc: [34A55, 34L25, 34B24]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_scattering_transform
---

## Summary

Gelfand–Levitan theory reconstructs the potential $q$ of a [[Sturm–Liouville|7WV6B2502K]] operator $-y'' + q y$ from its spectral measure.
The key step is a linear integral equation, the Gelfand–Levitan equation, whose kernel is built from the spectral data.
Its solution $K(x, t)$ is a transformation kernel that turns cosines into the solutions of the perturbed equation, and $q(x) = 2 \frac{d}{dx} K(x, x)$.
Israel Gelfand and Boris Levitan introduced it, and the related Marchenko equation is a basic tool of the inverse scattering transform.

## Explanations

### L1 human

Suppose you know the notes a string can play, together with some extra information, and you want to find the varying stiffness of the string.
Gelfand–Levitan theory gives a recipe for this inverse problem.
It compares the given spectral data with those of a plain string, writes the difference as a kernel, and solves one linear integral equation.
The answer $q$ then appears from the diagonal values of the solution.
When the spectral data are those of the plain string, the kernel is zero and the recipe returns $q = 0$.
