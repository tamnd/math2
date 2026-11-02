---
tag: WBCN9A847H
kind: concept
name: Orlicz space
msc: ["46E30"]
sources:
  - url: https://en.wikipedia.org/wiki/Orlicz_space
same_as:
  wikidata: Q3058185
  wikipedia: Orlicz space
---

## Summary

Fix a convex growth function $\Phi$.
The Orlicz space $L^\Phi(\mu)$ consists of the measurable functions $f$ for which $\Phi(\abs{f})$ is integrable after scaling $f$.
The choice $\Phi(t) = t^p$ gives the [[Lp space|SASP14MA1Z]] $L^p$, so Orlicz spaces generalise the $L^p$ scale.
They are Banach spaces with the Luxemburg norm.
They describe integrability conditions that lie between the $L^p$ spaces, such as $L \log L$, which appears in the theory of maximal functions and singular integrals.

## Explanations

### L1 human

The space $L^p$ asks that $\abs{f}^p$ have finite integral.
An Orlicz space replaces the power $t^p$ by another convex function $\Phi(t)$.
With $\Phi(t) = e^t - 1$ one asks for exponential integrability, which is stronger than every $L^p$ condition on a finite measure space.
With $\Phi(t) = t \log(1 + t)$ one asks, on a finite measure space, for a little more than integrability, but less than any $L^p$ with $p > 1$.
