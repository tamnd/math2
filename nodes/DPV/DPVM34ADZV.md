---
tag: DPVM34ADZV
kind: concept
name: Fourier transform
msc: [42B10, 42A38, 35A22]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_transform
same_as:
  wikidata: Q6520159
  wikipedia: Fourier transform
---

## Summary

The Fourier transform writes a function on $\R^n$ as a superposition of plane waves $e^{2\pi i x \cdot \xi}$ and records the amplitude of each frequency $\xi$.
It turns derivatives into multiplication by polynomials in $\xi$, and convolution into ordinary multiplication.
So it changes linear partial differential equations with constant coefficients into algebraic or ordinary differential equations.
It extends to $L^2$ functions and to [[tempered distributions|AES2T5JPFP]].
See the [[definition|6V59T5KJBX]].

## Explanations

### L1 human

A sound is a mix of pure tones of different pitches.
The Fourier transform takes the sound as a function of time and tells how much of each pitch it contains.
On the frequency side, taking a derivative just multiplies each pitch by a factor proportional to its frequency.
This is why the transform solves equations such as the heat equation so easily.
The bell curve $e^{-\pi x^2}$ is special: its transform is the same bell curve.
