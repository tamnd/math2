---
tag: C07WNRSW52
kind: concept
name: Sine and cosine transforms
msc: ["42A38", "44A15"]
sources:
  - url: https://en.wikipedia.org/wiki/Sine_and_cosine_transforms
same_as:
  wikidata: Q1328722
  wikipedia: Sine and cosine transforms
---

## Summary

The sine and cosine transforms are the real forms of the [[Fourier transform|DPVM34ADZV]] for functions on the half-line $[0, \infty)$.
The cosine transform integrates $f$ against $\cos(2\pi x \xi)$, and the sine transform integrates it against $\sin(2\pi x \xi)$.
They are the Fourier transforms of the even and of the odd extension of $f$, up to constant factors.
They are used to solve boundary value problems on a half-line, where the boundary condition picks the even or the odd extension.
See the [[definition|Q4HR7AF2R9]].

## Explanations

### L1 human

A signal that starts at time $0$ can be mirrored to negative times in two ways: as an even copy or as an odd copy.
The mirrored signal has a Fourier transform made only of cosines in the even case and only of sines in the odd case.
So one real transform suffices instead of a complex one.
For $f(x) = e^{-x}$ on $[0, \infty)$, the cosine transform is $1/(1 + 4\pi^2 \xi^2)$.
These transforms are the continuous analogues of the [[sine and cosine series|Y6EPBG6S8G]] of a function on an interval.
