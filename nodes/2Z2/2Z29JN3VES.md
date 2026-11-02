---
tag: 2Z29JN3VES
kind: concept
name: Convolution
msc: ["43A15", "22D15", "44A35"]
sources:
  - url: https://en.wikipedia.org/wiki/Convolution
same_as:
  wikidata: Q210857
  wikipedia: Convolution
---

## Summary

Convolution combines two functions $f$ and $h$ on a group into a new function $f * h$ by averaging translates of one function, weighted by the other.
On $\R^n$ it is $(f * h)(x) = \int f(y) h(x - y) \, dy$, and on a [[locally compact group|AHV05ZBCYW]] the integral is taken against a [[Haar measure|VY0HXD3GC4]].
It turns $L^1$ of the group into an algebra, it describes sums of independent random variables, and the Fourier transform turns it into pointwise multiplication.

## Explanations

### L1 human

To convolve a signal with a short bump, replace the value at each point by a weighted average of nearby values, with weights given by the bump.
The result is a smoothed version of the signal.
For sequences on the integers, convolving $(1, 1)$ with $(1, 2, 1)$ gives $(1, 3, 3, 1)$, exactly the coefficients of $(1 + x)(1 + 2x + x^2)$.
So convolution is the multiplication of polynomials and power series, written in terms of their coefficients.
