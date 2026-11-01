---
tag: FVFFKNKEDF
kind: concept
name: Entourage
msc: ["54E15"]
specializes: [05AVARPXA2]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_space
---

## Summary

An entourage of a [[uniform space|A54T86KS63]] is one of the sets of pairs of points that make up its uniform structure.
Each entourage stands for one degree of closeness: the pairs in it are the pairs of points that are close to that degree.
Entourages replace the numbers $\varepsilon$ of metric spaces in the definitions of uniform continuity, Cauchy filters and completeness.

## Explanations

### L1 human

In a metric space, the pairs $(x, y)$ with distance less than $\varepsilon$ form a set of pairs, a relation on the space.
Such sets, and all larger ones, are the entourages of the metric.
For $\R$ and $\varepsilon = 1$, the entourage is the open band $\set{(x, y) : \abs{x - y} < 1}$ around the diagonal of the plane.
Smaller entourages are thinner bands, and so they say "closer".
