---
tag: ~d3bfaf4e
kind: statement
role: theorem
name: Recurrence for Bell numbers
msc: [11B73]
uses: [~b1f658a8, ~cefb9eb6]
sources:
  - url: https://en.wikipedia.org/wiki/Bell_number
    locator: Summation formulas
---

## Statement

Let $n$ be a natural number, and let $B_m$ be the [[Bell numbers|~cefb9eb6]].
Then
$$B_{n+1} = \sum_{k=0}^{n} \binom{n}{k} B_k.$$

## Remarks

Proof idea: in a partition of $\{1, \dots, n + 1\}$, the block of $n + 1$ contains $n - k$ other elements, for some $k$. The remaining $k$ elements form an arbitrary partition.
Example: $B_4 = 1 \cdot 1 + 3 \cdot 1 + 3 \cdot 2 + 1 \cdot 5 = 15$.

## Explanations

### L1 human

Fix the last element and decide which other elements share its group.
For each choice, the elements left over can be split in any way, so you add a Bell number for each case.
