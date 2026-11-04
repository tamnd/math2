---
tag: 4FYR5VFZGH
kind: proof
name: Proof of the Catalan recurrence from the definition
msc: [05A15]
proves: 0Y1MG9R5VN
uses: [092DRBFKMG]
sources:
  - url: https://en.wikipedia.org/wiki/Catalan_number
    locator: Properties
---

## Proof

1. Let $n$ be a natural number.
2. The node [[Catalan numbers|092DRBFKMG]] defines the sequence $(C_m)$ by $C_0 = 1$ and, for every natural number $m$, $C_{m+1} = \sum_{i=0}^{m} C_i\, C_{m-i}$.
3. Taking $m = n$ in this defining rule gives $C_{n+1} = \sum_{i=0}^{n} C_i\, C_{n-i}$, which is the claim.

## Idea

Here the Catalan numbers are defined by this recursion, so the recurrence is part of the definition. Its real content lies in the families that satisfy it, such as Dyck words and binary trees.
