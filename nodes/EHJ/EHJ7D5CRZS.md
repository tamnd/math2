---
tag: EHJ7D5CRZS
kind: concept
name: Slowly varying function
msc: [26A12, "40E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Slowly_varying_function
same_as:
  wikidata: Q4287804
  wikipedia: Slowly varying function
---

## Summary

A slowly varying function is a positive function $L$ on $(0, \infty)$ such that $L(ax)/L(x) \to 1$ as $x \to \infty$ for every $a > 0$.
Such functions grow or decay more slowly than any positive power of $x$, like the logarithm.
They appear as correction factors in [[Karamata's Tauberian theorem|DBEGF38V9H]], in probability theory and in the study of asymptotic behaviour.

## Explanations

### L1 human

A slowly varying function hardly notices if you double or triple its argument, once the argument is large.
The logarithm is the standard example: $\log(2x) = \log x + \log 2$, and the extra $\log 2$ is tiny compared with $\log x$ for large $x$.
So $\log(2x) / \log x$ gets closer and closer to $1$.
A power such as $x^2$ is not slowly varying, because doubling $x$ multiplies $x^2$ by $4$.
