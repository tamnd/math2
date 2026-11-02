---
tag: PK3RGWY032
kind: concept
name: Hausdorff summation
msc: ["40G05", "40C05"]
specializes: [M6311DWJ1E]
sources:
  - url: https://en.wikipedia.org/wiki/Divergent_series
---

## Summary

Hausdorff summation is a family of [[matrix summability methods|M6311DWJ1E]], one for each sequence $(\mu_n)$ of numbers.
The matrix is built from $(\mu_n)$ and its iterated differences with binomial weights.
The family contains the [[Cesàro|N8ZGG7EW6J]] methods and the [[Euler|81Q4ERP594]] methods as special cases.
Hausdorff characterized the regular methods of the family by a moment condition on $(\mu_n)$, which links summability with the Hausdorff moment problem.

## Explanations

### L1 human

Many classical summation methods turn a sequence into weighted averages with binomial coefficients in the weights.
Hausdorff noticed that they all come from one recipe fed with a sequence $(\mu_n)$.
Feeding $\mu_n = \frac{1}{n+1}$ into the recipe gives the plain running averages of Cesàro.
Feeding $\mu_n = 2^{-n}$ gives Euler's averages with the weights of Pascal's triangle.
