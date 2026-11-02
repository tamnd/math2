---
tag: 7Y56QCZSZJ
kind: concept
name: Error function
msc: ["33B20", "60E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Error_function
same_as:
  wikidata: Q579262
  wikipedia: Error function
---

## Summary

The error function is $\operatorname{erf} x = \frac{2}{\sqrt{\pi}} \int_0^x e^{-t^2}\, dt$.
It is the integral of the Gaussian bell curve, scaled so that $\operatorname{erf} x \to 1$ as $x \to \infty$.
It gives the [[cumulative distribution function|0H8H7ZTHW2]] of the [[normal distribution|05AQE0QR0D]], and it appears in solutions of the [[heat equation|VP2HN86VAG]].
It has no expression in terms of elementary functions.

## Explanations

### L1 human

The bell curve $e^{-t^2}$ is the shape of the normal distribution.
The error function measures the area under this curve between $0$ and $x$, scaled so that the total area on the positive side is $1$.
It starts at $0$, rises quickly, and levels off near $1$ after $x \approx 2$.
For example, $\operatorname{erf}(1/\sqrt{2}) \approx 0.683$: a normal random value lies within one standard deviation of the mean with probability about $68\%$.
