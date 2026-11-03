---
tag: FDTVQ96WAH
kind: concept
name: Generalized binomial coefficient
msc: [05A10]
uses: [0SJNCJCCQG, 0WFCGVMRRC]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_genfunction_gen-bin-thm.ptx#L31
    locator: source/s_genfunction_gen-bin-thm.ptx:31
---

## Summary

The generalized binomial coefficient extends the [[binomial coefficient|0GBZM0MT0F]] so that the upper entry may be any real number $p$. The lower entry $k$ stays a nonnegative integer.

The value $\binom{p}{k}$ is the [[falling factorial|0SJNCJCCQG]] of $p$ of order $k$, that is $p(p-1)\cdots(p-k+1)$, divided by the [[factorial|0WFCGVMRRC]] $k!$. Here the falling factorial is written $P(p,k)$.

When $p$ is a natural number, this agrees with the usual count of $k$-element subsets of a $p$-element set. For other real $p$ the value need not be an integer. For example, $\binom{1/2}{2} = \frac{(1/2)(-1/2)}{2} = -\frac{1}{8}$.
