---
tag: JB8QMT8DCH
kind: concept
name: Inverse Fourier transform
msc: [42B10, 42A38]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_inversion_theorem
---

## Summary

The inverse Fourier transform takes a function of frequency and builds a function of position by superposing the waves $e^{2\pi i x \cdot \xi}$ with these amplitudes.
It has the same form as the [[Fourier transform|DPVM34ADZV]], with the opposite sign in the exponent.
The [[Fourier inversion theorem|T4Z8YQZKZV]] says that it undoes the Fourier transform, so a function can be recovered from its frequency content.

## Explanations

### L1 human

The Fourier transform measures how much of each frequency a signal contains.
The inverse Fourier transform goes back: given the amount of each frequency, it adds up all the corresponding waves to rebuild the signal.
The two operations look almost the same, with only a sign changed in the exponent.
For example, the bell curve $e^{-\pi \abs{\xi}^2}$ is sent to the same bell curve $e^{-\pi \abs{x}^2}$.
