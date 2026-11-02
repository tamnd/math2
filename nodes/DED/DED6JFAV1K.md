---
tag: DED6JFAV1K
kind: concept
name: Complete statistic
msc: [62B05]
specializes: [0Q5CG2NEQ8]
sources:
  - url: https://en.wikipedia.org/wiki/Completeness_(statistics)
same_as:
  wikidata: Q2532735
  wikipedia: Completeness (statistics)
---

## Summary

A [[statistic|0Q5CG2NEQ8]] is complete when no non-trivial function of it has expectation zero under every parameter value.
Completeness means that the family of laws of the statistic is rich enough to separate functions of it.
It is the key hypothesis of the [[Lehmann–Scheffé theorem|QQZPWDWS29]] and of [[Basu's theorem|6GATRFMJYY]].
By Lehmann–Scheffé, an unbiased estimator that is a function of a complete [[sufficient statistic|WP4TGXJQJG]] is the unique best one.

## Explanations

### L1 human

Suppose a function of the statistic averages to zero whatever the parameter is.
For a complete statistic, this can only happen if the function is zero.
So two unbiased estimators that are both functions of a complete statistic must agree.
For example, the number of heads in $n$ tosses of a coin with any chance $p$ is complete, because a polynomial in $p$ that vanishes for all $p$ is zero.
