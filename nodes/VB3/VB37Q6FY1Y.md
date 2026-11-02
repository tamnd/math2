---
tag: VB37Q6FY1Y
kind: concept
name: Trigonometric integrals
msc: ["33E20", "33B10"]
sources:
  - url: https://en.wikipedia.org/wiki/Trigonometric_integral
same_as:
  wikidata: Q1094282
  wikipedia: Trigonometric integral
---

## Summary

The trigonometric integrals are the sine integral $\operatorname{Si}(x) = \int_0^x \frac{\sin t}{t}\, dt$ and the cosine integral $\operatorname{Ci}(x) = -\int_x^\infty \frac{\cos t}{t}\, dt$, with their hyperbolic versions $\operatorname{Shi}$ and $\operatorname{Chi}$.
They are antiderivatives of $\frac{\sin x}{x}$ and $\frac{\cos x}{x}$, which have no elementary antiderivatives.
The sine integral tends to $\frac{\pi}{2}$, the value of the [[Dirichlet integral|0GZNSHMG4Q]], and its overshoot describes the Gibbs phenomenon of Fourier series.
They are closely related to the [[exponential integral|EV6ZDQ0NDY]].

## Explanations

### L1 human

The [[sinc function|P1T98BECWR]] $\frac{\sin t}{t}$ has a tall hump at $0$ and smaller and smaller ripples.
The sine integral adds up its area from $0$ to $x$.
It first rises above $\frac{\pi}{2}$, then swings below, and settles at $\frac{\pi}{2}$ with smaller and smaller swings.
Its first peak, at $x = \pi$, is its largest value, about $1.852$, roughly $18\%$ above the limit.
