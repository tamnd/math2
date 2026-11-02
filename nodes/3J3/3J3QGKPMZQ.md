---
tag: 3J3QGKPMZQ
kind: concept
name: Polygamma function
msc: ["33B15"]
sources:
  - url: https://en.wikipedia.org/wiki/Polygamma_function
same_as:
  wikidata: Q857956
  wikipedia: Polygamma function
---

## Summary

The polygamma function of order $m$ is the $m$-th derivative of the [[digamma function|HWRRXB0YXS]], so the $(m+1)$-th derivative of $\log \Gamma$.
For $m \ge 1$ it is a series of inverse powers, closely tied to the [[Hurwitz zeta function|G4SW7HJG88]].
Its values at $1$ are, up to sign and a factorial, values $\zeta(m+1)$ of the [[Riemann zeta function|1XWBY4N0VT]].
The case $m = 1$ is the [[trigamma function|5VGVPENA0F]].

## Explanations

### L1 human

Start from the logarithm of the gamma function and differentiate it again and again.
The first derivative is the digamma function, the second is the trigamma function, and the later ones are the polygamma functions.
From order one on, each of them is a simple sum such as $\sum_{k \ge 0} \frac{1}{(z+k)^2}$.
For example, the trigamma function at $1$ is $1 + \frac14 + \frac19 + \cdots = \frac{\pi^2}{6}$.
