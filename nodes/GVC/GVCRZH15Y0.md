---
tag: GVCRZH15Y0
kind: concept
name: Analytic signal
msc: [94A12, 44A15, 42A50]
sources:
  - url: https://en.wikipedia.org/wiki/Analytic_signal
same_as:
  wikidata: Q485394
  wikipedia: Analytic signal
---

## Summary

The analytic signal of a real function $f$ is the complex function $f + i\, Hf$, where $H$ is the [[Hilbert transform|NSCEBXM7ZM]].
Its Fourier transform vanishes at negative frequencies and is twice that of $f$ at positive frequencies.
It is the boundary value of a [[holomorphic function|0NAHXR1FRH]] on the upper half-plane, which explains the name.
In signal processing it defines the instantaneous amplitude and phase of a real signal.

## Explanations

### L1 human

A real signal, such as a sound wave, contains each frequency twice, once with a positive and once with a negative sign, and the two halves carry the same information.
The analytic signal throws away the negative frequencies and doubles the positive ones.
The result is a complex signal that turns around the origin of the plane.
Its distance from the origin is the envelope of the signal and its angle is the phase.
For example, the analytic signal of $\cos t$ is $e^{it} = \cos t + i \sin t$.
