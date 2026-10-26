---
tag: 0XFZ1BMF5Q
kind: statement
role: theorem
name: Euler's partition theorem
msc: [05A17]
uses: [0404R9P9J3]
sources:
  - url: https://en.wikipedia.org/wiki/Integer_partition
    locator: Odd parts and distinct parts
---

## Statement

Let $n$ be a natural number.
Then the number of [[partitions|0404R9P9J3]] of $n$ into odd parts equals the number of partitions of $n$ into distinct parts.

## Remarks

For $n = 5$, the partitions into odd parts are $5$, $3 + 1 + 1$ and $1 + 1 + 1 + 1 + 1$. The partitions into distinct parts are $5$, $4 + 1$ and $3 + 2$.
A proof with generating functions: $\prod_{k \ge 1} (1 + x^k) = \prod_{k \ge 1} \frac{1 - x^{2k}}{1 - x^k} = \prod_{k \text{ odd}} \frac{1}{1 - x^k}$.
Glaisher gave a bijection. It merges equal parts in pairs, again and again, until all parts are distinct.

## Explanations

### L1 human

Count the ways to write $n$ with only odd summands, and the ways to write it with summands that are all different.
The two counts are always equal, although the partitions themselves are not the same.
