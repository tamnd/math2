---
tag: 0PCKBBMEXC
kind: statement
role: proposition
name: Order of the symmetric group
msc: [20B30]
uses: [0RJMNEN3BJ, 0SEX9F9J5Z]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_group
    locator: lead section
---

## Statement

Let $n$ be a positive integer.
The [[symmetric group|0515A6D2Y1]] $S_n$ has [[order|0B85S2V2DR]] $n!$.

## Remarks

A permutation $\sigma$ has $n$ choices for $\sigma(1)$, then $n - 1$ choices for $\sigma(2)$, and so on, down to $1$ choice for $\sigma(n)$.
For example, $|S_3| = 6$ and $|S_4| = 24$.

## Explanations

### L1 human

To make a permutation, you choose where each symbol goes, one symbol after the other.
Each choice removes one place from the next choices.
So the number of permutations is $n \cdot (n-1) \cdots 1 = n!$.
