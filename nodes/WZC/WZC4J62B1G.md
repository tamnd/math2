---
tag: WZC4J62B1G
kind: concept
name: Cauchy filter
msc: ["54E15", 54A20]
specializes: [15PF73BKY6]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_space
---

## Summary

A Cauchy filter on a [[uniform space|A54T86KS63]] is a [[filter|15PF73BKY6]] that contains arbitrarily small sets, where "small" is measured by the [[entourages|FVFFKNKEDF]].
It is the uniform version of a [[Cauchy sequence|0PWX18FM4G]].
A uniform space is complete when every Cauchy filter converges, and this gives completeness without a metric.

## Explanations

### L1 human

A Cauchy sequence is a sequence whose terms eventually all lie very close together.
A filter is a family of "large" sets.
A Cauchy filter has, for each degree of closeness, a member whose points are all that close to each other.
In $\R$, the filter of all sets that contain an interval $(-\varepsilon, \varepsilon)$ for some $\varepsilon > 0$ is a Cauchy filter.
In the rational numbers, the filter of neighbourhoods of $\sqrt{2}$ traced on $\Q$ is a Cauchy filter that does not converge in $\Q$.
