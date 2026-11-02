---
tag: 84MVNJCYR4
kind: concept
name: p-adic gamma function
msc: ["11S80", "33B15"]
sources:
  - url: https://en.wikipedia.org/wiki/P-adic_gamma_function
same_as:
  wikidata: Q7116917
  wikipedia: P-adic gamma function
---

## Summary

The $p$-adic gamma function $\Gamma_p$ of Morita is a continuous function on the [[p-adic integers|V6TJAFZ4MD]] that plays the role of the [[gamma function|0H5SYBSED9]].
It interpolates a modified [[factorial|0XWG0JGDFW]] in which the factors divisible by $p$ are left out.
It satisfies a functional equation like $\Gamma(x+1) = x\,\Gamma(x)$, and it appears in the Gross–Koblitz formula for Gauss sums.

## Explanations

### L1 human

The ordinary factorial $n!$ cannot be extended continuously in the $p$-adic sense, because $n!$ becomes divisible by high powers of $p$ and so $p$-adically small.
The fix is to skip the factors that are multiples of $p$.
The resulting products, with a sign, change only a little when $n$ changes by a high power of $p$.
So they extend to a continuous function on all $p$-adic integers.
For example, for $p = 3$ the value at $5$ is $-(1 \cdot 2 \cdot 4) = -8$, since the factor $3$ is skipped.
