---
tag: 2DDZXF5EBY
kind: concept
name: Mathieu function
msc: ["33E10", 34B30]
sources:
  - url: https://en.wikipedia.org/wiki/Mathieu_function
same_as:
  wikidata: Q1908689
  wikipedia: Mathieu function
---

## Summary

Mathieu functions are solutions of Mathieu's equation $y'' + (a - 2q \cos 2x) y = 0$.
For each $q$, only special values of $a$, the characteristic values, admit solutions of period $\pi$ or $2\pi$.
These periodic solutions $\operatorname{ce}_r(x, q)$ and $\operatorname{se}_r(x, q)$ are the Mathieu functions in the narrow sense.
They arise when the [[Helmholtz equation|MNXKTXJ35G]] is separated in elliptic coordinates, for instance for vibrations of an elliptic drum.
Mathieu's equation is the basic example of a [[Hill differential equation|YE7H8DGDPY]], studied by [[Floquet theory|BJVZXPB297]].

## Explanations

### L1 human

Mathieu's equation describes an oscillator whose stiffness is shaken periodically in time.
For $q = 0$ the shaking is off, and the equation $y'' + a y = 0$ has the periodic solutions $\cos rx$ and $\sin rx$ when $a = r^2$.
For $q \ne 0$ periodic solutions still exist, but only when $a$ is tuned to special values $a_r(q)$ or $b_r(q)$ that move with $q$.
The periodic solutions are deformed cosines $\operatorname{ce}_r$ and deformed sines $\operatorname{se}_r$.
For other values of $a$ the solutions are either bounded but not periodic, or they grow exponentially, which is the phenomenon of parametric resonance.
