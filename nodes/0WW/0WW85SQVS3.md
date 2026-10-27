---
tag: 0WW85SQVS3
kind: definition
name: Bell numbers
msc: [11B73]
defines: 0TKP3TDD02
uses: [0ZN07RQ3JS]
sources:
  - url: https://en.wikipedia.org/wiki/Bell_number
    locator: Set partitions
inventory: [4KX686PWJ0]
---

## Definition

Let $n$ be a natural number.
The Bell number $B_n$ is the number of partitions of an $n$-element set into nonempty blocks.
Equivalently, it is the sum of [[Stirling numbers of the second kind|0ZN07RQ3JS]]:
$$B_n = \sum_{k=0}^{n} S(n, k).$$

## Remarks

The first values, for $n = 0, 1, \dots, 6$, are $1, 1, 2, 5, 15, 52, 203$.
$B_0 = 1$, because the empty set has exactly one partition, the partition with no blocks.
The values satisfy a [[recurrence|0110GBHPPB]] with binomial coefficients.

## Explanations

### L1 human

The Bell number $B_n$ counts all ways to split $n$ labelled objects into groups, with any number of groups.
For $\{1, 2, 3\}$ there are $5$ ways: $123$, $1|23$, $2|13$, $3|12$ and $1|2|3$.
