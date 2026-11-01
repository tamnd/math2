---
tag: YS09Z1YNEK
kind: concept
name: Gaussian binomial coefficient
msc: [05A30, 11B65, 05A10]
specializes: [GFSDMJHHVA]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_binomial_coefficient
same_as:
  wikidata: Q5527834
  wikipedia: Gaussian binomial coefficient
---

## Summary

The Gaussian binomial coefficient $\binom{n}{k}_q$ is the [[q-analog|GFSDMJHHVA]] of the [[binomial coefficient|0GBZM0MT0F]] $\binom{n}{k}$, see the [[definition|TZ6Y9XXQJW]].
It is a polynomial in $q$ with nonnegative integer coefficients, and it equals $\binom{n}{k}$ at $q = 1$.
When $q$ is a prime power, it counts the $k$-dimensional subspaces of the [[vector space|000AYPA9AJ]] $\F_q^n$.
Its coefficients count the [[integer partitions|0JV30XN73Z]] whose [[Young diagram|096AHMB3P4]] fits in a $k \times (n - k)$ box.

## Explanations

### L1 human

The ordinary binomial coefficient counts subsets of a set.
The Gaussian binomial coefficient counts subspaces of a vector space over a finite field with $q$ elements.
For example, $\binom{4}{2}_q = 1 + q + 2q^2 + q^3 + q^4$.
At $q = 1$ it gives $6$, the number of $2$-element subsets of a $4$-element set.
At $q = 2$ it gives $35$, the number of planes through the origin in $\F_2^4$.
