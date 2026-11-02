---
tag: 34VJ4T7ZSB
kind: concept
name: Fourier–Bessel series
msc: [42C10, 33C10]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier%E2%80%93Bessel_series
same_as:
  wikidata: Q5475809
  wikipedia: Fourier–Bessel series
---

## Summary

A Fourier–Bessel series expands a function on an interval $[0, b]$ in the functions $J_\nu(j_{\nu,k} x / b)$.
Here $J_\nu$ is the Bessel function of the first kind and $j_{\nu,k}$ are its positive zeros.
These functions are orthogonal for the weight $x$, so the series is a [[generalized Fourier series|SNJC87TBHD]].
They are the eigenfunctions of a singular [[Sturm–Liouville problem|7WV6B2502K]] coming from [[Bessel's equation|EAV97QH9DF]].
Fourier–Bessel series solve problems with circular or cylindrical symmetry, such as the vibrations of a circular drum or heat flow in a cylinder.

## Explanations

### L1 human

A vibrating string has sine waves as its basic shapes, and any shape of the string is a sum of them.
A circular drum skin has different basic shapes: in the radial direction they are Bessel functions, scaled so that they vanish at the rim.
A Fourier–Bessel series writes a radial profile on the drum as a sum of these basic shapes.
For example, the constant profile $1$ on $[0, 1)$ is $\sum_k \frac{2}{j_k J_1(j_k)} J_0(j_k x)$, where $j_k$ are the zeros of $J_0$.
