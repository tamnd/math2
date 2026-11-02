---
tag: 4F812GHFZK
kind: concept
name: Resonance
msc: [34C15, 34A30]
sources:
  - url: https://en.wikipedia.org/wiki/Resonance
same_as:
  wikidata: Q172858
  wikipedia: Resonance
---

## Summary

Resonance is the strong response of a linear system when it is forced at one of its own natural frequencies.
For a linear equation with constant coefficients and forcing $e^{\lambda t}$, it happens when $\lambda$ is a root of the characteristic polynomial.
Then the response is not a multiple of $e^{\lambda t}$ but picks up a power of $t$, and an undamped oscillator has unbounded solutions.
It explains the collapse of structures under periodic loads and the tuning of circuits and instruments.
See the [[definition|NTB5JQGPGC]] and the worked [[forced oscillator|0X4NT20S3G]].

## Explanations

### L1 human

A child on a swing goes higher and higher when pushed in time with the swing.
The pushes add up because they match the swing's own rhythm.
For the undamped oscillator $x'' + x = \cos t$, the forcing has the natural frequency $1$.
A solution is $x(t) = \frac{1}{2} t \sin t$, whose swings grow without bound.
With forcing $\cos(2t)$ instead, every solution stays bounded.
