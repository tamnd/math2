---
tag: 2WSV04QETW
kind: concept
name: Prony's method
msc: [65D10, 41A30, 65F20]
sources:
  - url: https://en.wikipedia.org/wiki/Prony%27s_method
same_as:
  wikidata: Q7249979
  wikipedia: Prony's method
---

## Summary

Prony's method recovers a sum of exponentials $f(k) = \sum_{j=1}^{n} c_j z_j^k$ from equally spaced samples.
It uses the fact that such samples satisfy a [[linear recurrence|0NDVHBVBXB]] whose characteristic polynomial has the roots $z_j$.
One solves a [[Hankel|PQ1D8FQB3E]] linear system for the recurrence, finds the roots, and then solves a linear system for the amplitudes $c_j$.
The method underlies many techniques of signal processing and spectral estimation.
It is close to rational approximation, since the generating function $\sum_k f(k) w^k$ of such samples is rational.

## Explanations

### L1 human

A signal made of a few decaying or oscillating exponentials has a hidden regularity: each sample is a fixed combination of the previous few.
Prony's method first finds that combination from the data.
The roots of the associated polynomial reveal the rates and frequencies, and the remaining sizes come from a small linear system.
For example, the samples $2, 3, 5, 9$ of $2^k + 1$ satisfy $f(k+2) = 3 f(k+1) - 2 f(k)$, whose polynomial $z^2 - 3z + 2$ has roots $1$ and $2$.
