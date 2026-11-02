---
tag: 5BW26GPS2A
kind: concept
name: FBI transform
msc: [35A27, 44A15, 35S30]
specializes: [YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier%E2%80%93Bros%E2%80%93Iagolnitzer_transform
same_as:
  wikidata: Q5424638
  wikipedia: Fourier–Bros–Iagolnitzer transform
---

## Summary

The FBI transform, named after Fourier, Bros and Iagolnitzer, is a phase-space transform.
It looks at a function near a point $x$ at frequency $\xi$ through a Gaussian window of width about $\abs{\xi}^{-1/2}$.
It is a tool of microlocal analysis.
Smoothness and real analyticity of a function near a point, in given directions, can be read off from the decay of its FBI transform.
In particular, it characterizes the analytic [[wave front set|3T5Q9WVQX8]] through exponential decay.
It is a close relative of the [[Bargmann transform|QPH28QH036]] and of the short-time Fourier transform with a Gaussian window.

## Explanations

### L1 human

To see whether a function is smooth near a point, one can zoom in there and look at its high-frequency content.
The FBI transform does this with a Gaussian magnifying glass placed at $x$ and tuned to frequency $\xi$.
The higher the frequency, the narrower the glass.
If the result dies off very fast as the frequency grows, the function is real analytic near $x$ in that direction of frequency.
