---
tag: 8KQWBCCG24
kind: statement
role: theorem
name: Least missing positive integer
msc: [03F30]
uses: [01BX15HSRR, 0AANKKNHS4]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_background_decimal.ptx#L67
    locator: source/s_background_decimal.ptx:67
---

## Statement

Let $M$ be a set of positive integers, and suppose that $M$ is not the set of all positive integers.
Then some positive integer lies outside $M$, and among the positive integers outside $M$ there is exactly one that is smaller than all the others.

## Remarks

The set of positive integers outside $M$ is nonempty, so it has a [[least element|0AANKKNHS4]] by the [[well-ordering principle|01BX15HSRR]].
A least element of a set is unique, because the order is antisymmetric.
For example, if $M$ contains $1, 2, 3$ and $5$ but not $4$, the least positive integer outside $M$ is $4$ or smaller, and here it is $4$.
