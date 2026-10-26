---
tag: 0C019SDTER
kind: statement
role: theorem
name: Recurrence for Stirling numbers of the second kind
msc: [11B73]
uses: [0ZN07RQ3JS]
sources:
  - url: https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind
    locator: Recurrence relation
---

## Statement

Let $n$ and $k$ be natural numbers, and let $S(n, k)$ be the [[Stirling numbers of the second kind|0ZN07RQ3JS]].
Then
$$S(n + 1, k + 1) = (k + 1)\, S(n, k + 1) + S(n, k).$$

## Remarks

Proof idea: look at the element $n + 1$. Either it forms a block by itself, and the rest is a partition into $k$ blocks. Or it joins one of the $k + 1$ blocks of a partition of the rest.
Example: $S(4, 2) = 2\, S(3, 2) + S(3, 1) = 2 \cdot 3 + 1 = 7$.

## Explanations

### L1 human

Add a new element to a partition problem.
The new element is alone, or it joins one of the existing $k + 1$ groups, and these two cases give the two terms.
