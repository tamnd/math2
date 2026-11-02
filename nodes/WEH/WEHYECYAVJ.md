---
tag: WEHYECYAVJ
kind: concept
name: Hartley transform
msc: [44A15, 42A38, 94A12]
specializes: [YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Hartley_transform
same_as:
  wikidata: Q1567607
  wikipedia: Hartley transform
---

## Summary

The Hartley transform is an integral transform like the [[Fourier transform|DPVM34ADZV]], but with the real kernel $\cos(\omega t) + \sin(\omega t)$ in place of $e^{-i\omega t}$.
It sends real functions to real functions, and with the symmetric normalization it is its own inverse.
For a real function it carries the same information as the Fourier transform.
For a real function $f$, the even part of the Hartley transform of $f$ is the real part of the Fourier transform of $f$.
Its odd part is minus the imaginary part of the Fourier transform of $f$.
Its discrete version is used as a real-arithmetic alternative to the discrete Fourier transform.

## Explanations

### L1 human

The Fourier transform describes a real signal by complex numbers.
The Hartley transform packs the same information into real numbers, by adding the cosine and the sine parts instead of keeping them apart.
Applying it twice gives back the signal.
For example, the Gaussian $e^{-t^2/2}$ is even, so its sine part vanishes and its Hartley transform is again $e^{-\omega^2/2}$.
