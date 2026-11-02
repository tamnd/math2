---
tag: EZXPY4A19C
kind: concept
name: Abel summation
msc: ["40G10"]
specializes: [8X25Q4XYMN]
sources:
  - url: https://en.wikipedia.org/wiki/Abelian_and_Tauberian_theorems
---

## Summary

Abel summation is the [[summability method|8X25Q4XYMN]] that assigns to a series $\sum a_n$ the limit of the [[power series|0VP56B4EMX]] $\sum a_n x^n$ as $x \to 1$ from below.
By [[Abel's theorem|0S4EMDQS2F]], it gives the usual sum to every convergent series.
It sums every series that [[Cesàro summation|N8ZGG7EW6J]] sums, to the same value, and more.
Its partial converses, such as [[Tauber's theorem|8SK3GQ4S0M]] and [[Littlewood's Tauberian theorem|Z35TD4ZZRD]], started the theory of Tauberian theorems.

## Explanations

### L1 human

Damp the $n$-th term of the series by the factor $x^n$, with $x$ slightly below $1$.
The damped series often converges even when the original does not.
Then let $x$ grow to $1$ and see whether the damped sums approach a limit.
For $1 - 1 + 1 - \cdots$, the damped sum is $1 - x + x^2 - \cdots = \frac{1}{1+x}$, which tends to $1/2$.
