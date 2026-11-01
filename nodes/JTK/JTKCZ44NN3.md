---
tag: JTKCZ44NN3
kind: concept
name: Riemann–Liouville integral
msc: [26A33]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann%E2%80%93Liouville_integral
same_as:
  wikidata: Q4162532
  wikipedia: Riemann–Liouville integral
---

## Summary

The Riemann–Liouville integral of order $\alpha > 0$ is the integral operator $I_a^\alpha f(x) = \frac{1}{\Gamma(\alpha)} \int_a^x (x - t)^{\alpha - 1} f(t) \, dt$.
For a whole number $\alpha = n$ it is the $n$-fold repeated integral, by [[Cauchy's formula for repeated integration|EYXG11V76E]].
It is the basic operator of [[fractional calculus|T73XK15SA2]], and fractional derivatives are defined from it.

## Explanations

### L1 human

Integrating $n$ times from $a$ is the same as one integral with the weight $(x - t)^{n-1} / (n - 1)!$.
Replace $n$ by any positive real $\alpha$ and the factorial by the [[gamma function|0H5SYBSED9]], and the formula still makes sense.
This gives integrals of order $1/2$, $3/2$, and so on.
For example, with $a = 0$, the integral of order $\alpha$ of $1$ is $x^\alpha / \Gamma(\alpha + 1)$.
