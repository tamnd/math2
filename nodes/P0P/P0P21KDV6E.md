---
tag: P0P21KDV6E
kind: concept
name: Absolutely continuous measure
msc: [28A10, 28A15]
sources:
  - url: https://en.wikipedia.org/wiki/Absolute_continuity
---

## Summary

A measure $\nu$ is absolutely continuous with respect to a measure $\mu$, written $\nu \ll \mu$, when every $\mu$-null set is also $\nu$-null.
By the [[Radon–Nikodym theorem|1ZSZS5G1Q4]], for σ-finite measures this holds exactly when $\nu$ has a density with respect to $\mu$.
It is the measure-theoretic counterpart of the [[absolute continuity|ZT6F4C2YHK]] of functions.
A nondecreasing function on a closed bounded interval is absolutely continuous exactly when its Lebesgue–Stieltjes measure is absolutely continuous with respect to Lebesgue measure.
In probability, random variables with a density are those whose law is absolutely continuous with respect to Lebesgue measure.

## Explanations

### L1 human

Absolute continuity of $\nu$ with respect to $\mu$ means that $\nu$ never sees anything that $\mu$ ignores.
If a set is negligible for $\mu$, it is negligible for $\nu$ too.
The normal distribution is absolutely continuous with respect to Lebesgue measure on $\R$, since it is given by a density.
A point mass at $0$ is not: the single point $\set{0}$ has length $0$ but carries mass $1$.
