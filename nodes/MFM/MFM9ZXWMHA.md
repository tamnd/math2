---
tag: MFM9ZXWMHA
kind: concept
name: Regular variation
msc: [26A12, "40E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Slowly_varying_function
---

## Summary

A positive function $f$ on $(0, \infty)$ is regularly varying if $f(ax)/f(x)$ has a positive finite limit as $x \to \infty$ for every $a > 0$.
The limit is then always a power $a^\rho$, and $f(x) = x^\rho L(x)$ with $L$ a [[slowly varying function|EHJ7D5CRZS]].
So regularly varying functions behave like powers up to a slowly varying factor.
They are the natural comparison functions in [[Karamata's Tauberian theorem|DBEGF38V9H]].

## Explanations

### L1 human

A regularly varying function scales almost like a power of $x$ when $x$ is large.
If $f(x) = x^2 \log x$, then doubling $x$ multiplies $f$ by about $4$, and the error in this "about" goes away as $x$ grows.
The number $\rho$ in $a^\rho$ is the index; here it is $2$.
The exponential function is not regularly varying, because doubling $x$ squares $e^x$, which is far more than any fixed factor.
