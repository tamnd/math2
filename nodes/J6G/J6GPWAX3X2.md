---
tag: J6GPWAX3X2
kind: concept
name: Approximately additive function
msc: [39B82, 39B52]
sources:
  - url: https://en.wikipedia.org/wiki/Hyers%E2%80%93Ulam%E2%80%93Rassias_stability
---

## Summary

An approximately additive function is a map $f$ from an abelian group to a normed space.
The norm of its defect $f(x + y) - f(x) - f(y)$ is at most a fixed $\delta$.
It is an [[additive function|KF719SZD5T]] up to a uniform error.
[[Hyers' theorem|VFRJ0P2P15]] says that an approximately additive map from a normed space to a Banach space lies within $\delta$ of a unique additive map.
Such maps are also called $\delta$-additive maps.

## Explanations

### L1 human

An additive function turns sums into sums exactly.
An approximately additive function does so with an error that never exceeds a fixed amount.
The floor function is an example: $\floor{x + y} - \floor{x} - \floor{y}$ is always $0$ or $1$.
It stays within distance $1$ of the additive function $x \mapsto x$.
