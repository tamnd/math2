---
tag: TYXYM9HAS2
kind: statement
role: theorem
name: Monotonic law for multiplication of integers
msc: [06F25]
uses: [0C4JS9RF5M, 07J9ZJFECP]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_background_prop-integers.ptx#L102
    locator: source/s_background_prop-integers.ptx:102
---

## Statement

Let $x$, $y$ and $z$ be [[integers|0C4JS9RF5M]] with $x < y$ in the [[order on the integers|07J9ZJFECP]]. Then the product with $z$ behaves as follows.

If $z > 0$, then $xz < yz$.

If $z = 0$, then $xz = yz = 0$.

If $z < 0$, then $xz > yz$.

So multiplying by a positive integer keeps the direction of a strict inequality, and multiplying by a negative integer turns it around.
