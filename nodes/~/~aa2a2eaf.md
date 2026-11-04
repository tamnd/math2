---
tag: ~aa2a2eaf
kind: statement
role: theorem
name: Sum of the first n odd positive integers
msc: [05A19]
uses: [0ASJVEFA9J]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_induction_proofs.ptx#L104
    locator: source/s_induction_proofs.ptx:104
---

## Statement

Let $n$ be a positive integer. Then the $n$ smallest odd positive integers add up to the square of $n$:
$$1 + 3 + 5 + \dots + (2n - 1) = \sum_{i=1}^{n} (2i - 1) = n^2.$$

## Remarks

For $n = 1, 2, 3, 4$ the sums are $1, 4, 9, 16$.
A proof by [[induction|0ASJVEFA9J]] uses $n^2 + (2n + 1) = (n + 1)^2$.
