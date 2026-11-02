---
tag: N0B51FAA9S
kind: concept
name: Haar system
msc: [42C10, 42C40]
sources:
  - url: https://en.wikipedia.org/wiki/Haar_wavelet
---

## Summary

The Haar system is an orthonormal basis of $L^2([0, 1])$.
It consists of the constant function $1$ and the rescaled, shifted copies of one step function.
This step function is $1$ on the left half and $-1$ on the right half of $[0, 1)$.
Alfréd Haar introduced it in 1910, as an orthonormal system in which every continuous function has a uniformly convergent expansion.
It is the simplest example of a [[wavelet|4PZ35C0GV3]] basis, and it is a [[Schauder basis|528G11SDWR]] of $L^p([0, 1])$ for $1 \le p < \infty$.

## Explanations

### L1 human

Start with the average of a function over $[0, 1]$.
Then record how the average over the left half differs from the average over the right half.
Then do the same inside each half, inside each quarter, and so on.
Each step uses one function that is $+1$ on one half of a dyadic interval and $-1$ on the other half, scaled to have length $1$ in $L^2$.
These numbers rebuild the function step by step, with finer and finer detail.
