---
tag: 6J2AGD0BYY
kind: concept
name: Two-sided Laplace transform
msc: [44A10]
sources:
  - url: https://en.wikipedia.org/wiki/Two-sided_Laplace_transform
same_as:
  wikidata: Q1785576
  wikipedia: Two-sided Laplace transform
---

## Summary

The two-sided, or bilateral, Laplace transform of a function $f$ on the whole real line is $\int_{-\infty}^{\infty} f(t) e^{-s t} \, dt$.
It treats past and future times alike, unlike the one-sided [[Laplace transform|0V49JEZW06]], which only sees $t \ge 0$.
It converges in a vertical strip of the complex plane, and on the imaginary axis it becomes the [[Fourier transform|DPVM34ADZV]].
In probability it gives the moment generating function, with $s$ replaced by $-s$.

## Explanations

### L1 human

The ordinary Laplace transform starts the clock at time $0$; the two-sided transform looks at all times, negative and positive.
Because of this, it needs $f$ to be small at both ends, and it usually exists only for $s$ in a band between two vertical lines.
For example, $e^{-\abs{t}}$ has two-sided transform $2/(1 - s^2)$ for $-1 < \operatorname{Re} s < 1$.
