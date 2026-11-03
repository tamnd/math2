---
tag: F1Y5PYXKPS
kind: concept
name: Describing function
msc: [93C10, 93C80]
sources:
  - url: https://en.wikipedia.org/wiki/Describing_function
same_as:
  wikidata: Q1925419
  wikipedia: Describing function
---

## Summary

Feed a sinusoid into a nonlinear element and keep only the first harmonic of the output.
The describing function is the complex gain from the input to this harmonic, as a function of the input amplitude.
It replaces the nonlinearity by an amplitude-dependent linear gain, ignoring the higher harmonics of the output.
Its main use is to predict limit cycles in feedback loops that contain one nonlinear element.
The prediction uses an approximate balance condition on the [[Nyquist plot|Z7SPHAWMDX]] of the linear part.
The method is approximate: it works well when the linear part of the loop filters out the higher harmonics.

## Explanations

### L1 human

Feed a sine wave into a nonlinear device, such as an on-off switch, and the output is periodic but not a sine wave.
Keep only the sine-wave part of the output, its first [[Fourier|G12KXDHPPS]] component, and compare it with the input.
The ratio is the describing function, and unlike for a linear device it depends on how large the input is.
For a switch that outputs $+M$ or $-M$ according to the sign of the input, the ratio is $4M/(\pi A)$ for input amplitude $A$: large inputs see a small gain.
