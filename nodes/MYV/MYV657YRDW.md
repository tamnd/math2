---
tag: MYV657YRDW
kind: concept
name: Spectral method
msc: [65N35, 65M70]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_method
same_as:
  wikidata: Q2308831
  wikipedia: Spectral method
---

## Summary

A spectral method approximates the solution of a differential equation by a finite sum of smooth global functions, such as trigonometric functions or [[Chebyshev polynomials|M6EAR1JHPP]].
The coefficients are fixed by a [[Galerkin|Y5B0PEBKE8]] condition, a tau condition or collocation at chosen points.
For smooth solutions the error decreases faster than any power of the number of terms, often exponentially.
So they are the method of choice for smooth problems on simple domains.
Examples are turbulence in periodic boxes and weather models on the sphere.
See the [[definition|QFJEFGR171]].

## Explanations

### L1 human

A finite element method builds the solution from many small local pieces.
A spectral method instead uses a few waves that each stretch over the whole domain, as in a [[Fourier series|G12KXDHPPS]].
Derivatives of waves are easy: differentiating $e^{ikx}$ just multiplies it by $ik$.
For a smooth solution, the wave amplitudes drop very fast, so a few dozen waves can give many correct digits.
