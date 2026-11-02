---
tag: VX1R6FN6PS
kind: concept
name: Interpolation space
msc: [46B70]
sources:
  - url: https://en.wikipedia.org/wiki/Interpolation_space
same_as:
  wikidata: Q3058180
  wikipedia: Interpolation space
---

## Summary

Let $X_0$ and $X_1$ be two Banach spaces that sit in a common space.
An interpolation space for them is a Banach space between them with this property.
Every linear map bounded on both $X_0$ and $X_1$ is bounded on it too.
The model case is the Riesz–Thorin theorem.
It says that the [[Lp spaces|SASP14MA1Z]] with $p$ between $p_0$ and $p_1$ are interpolation spaces for $L^{p_0}$ and $L^{p_1}$.
The real method of Lions and Peetre and the complex method of Calderón build interpolation spaces in general.
Interpolation gives bounds for operators such as the Fourier transform and singular integrals, and it defines fractional Sobolev spaces.

## Explanations

### L1 human

Suppose you know that an operation is well behaved for two extreme ways of measuring size.
Interpolation lets you conclude that it is also well behaved for the measures of size in between.
For example, the Fourier transform is bounded from $L^1$ to $L^\infty$ and from $L^2$ to $L^2$.
Interpolation then gives the Hausdorff–Young inequality: it is bounded from $L^p$ to $L^q$ for $1 \le p \le 2$ and $1/p + 1/q = 1$.
