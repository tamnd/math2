---
tag: 2W7R5JHF0C
kind: concept
name: Completion of a normed space
msc: [46B99, "54E50"]
specializes: [06RW4RKWH7]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_metric_space
---

## Summary

The completion of a normed space $X$ is a [[Banach space|06GZ956657]] that contains a copy of $X$ as a dense subspace, with the same norm.
It exists and is unique up to isometric isomorphism.
It lets one prove results for Banach spaces and apply them to incomplete spaces.
Many important spaces, such as $L^p$ spaces and Sobolev spaces, can be built as completions of spaces of nice functions.

## Explanations

### L1 human

A normed space may have holes: Cauchy sequences that do not converge to anything inside it.
The completion fills these holes and changes nothing else, much as the real numbers fill the gaps in the rationals.
For example, finitely supported sequences with the norm $\left(\sum_k \abs{x_k}^2\right)^{1/2}$ do not form a complete space.
Their completion is the space $\ell^2$ of all square-summable sequences.
