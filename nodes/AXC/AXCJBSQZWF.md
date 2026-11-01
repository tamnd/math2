---
tag: AXCJBSQZWF
kind: concept
name: Modulus of continuity
msc: [26A16, 26A15]
sources:
  - url: https://en.wikipedia.org/wiki/Modulus_of_continuity
same_as:
  wikidata: Q1144872
  wikipedia: Modulus of continuity
---

## Summary

A modulus of continuity of a function $f$ is a function $\omega$ that bounds how much $f$ can change: $\abs{f(x) - f(y)} \le \omega(\abs{x - y})$.
The best such bound is the function $\delta \mapsto \sup \set{\abs{f(x) - f(y)} : \abs{x - y} \le \delta}$.
A function is [[uniformly continuous|0Q4DR37DVE]] exactly when this bound tends to $0$ with $\delta$.
Moduli of continuity measure the quality of continuity, and [[Lipschitz|0QNVQ4VD9T]] and [[Hölder|0WZTM0EFR6]] conditions are moduli of special forms.

## Explanations

### L1 human

Continuity says that small changes of the input give small changes of the output.
A modulus of continuity says how small, in numbers.
If two inputs are at distance $\delta$, the outputs differ by at most $\omega(\delta)$.
For $f(x) = 3x$ one can take $\omega(\delta) = 3\delta$, and for $f(x) = \sqrt x$ on $[0, \infty)$ one can take $\omega(\delta) = \sqrt \delta$.
