---
tag: K9XQKT69WF
kind: definition
name: Heap
msc: [20N10, 08A62]
defines: V389A4WGH9
uses: [0SJ3RX9TXA, WC47MFR6GW, G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Heap_(mathematics)
---

## Definition

A *heap* is a [[set|0SJ3RX9TXA]] $H$ with a [[ternary operation|WC47MFR6GW]] $[\cdot, \cdot, \cdot] \colon H \times H \times H \to H$ such that, for all $a, b, c, d, e \in H$:

1. $[\,[a, b, c], d, e] = [a, b, [c, d, e]\,] = [a, [d, c, b], e]$ (para-associativity);
2. $[a, a, b] = b$ and $[b, a, a] = b$ (identity law).

## Remarks

Example: a [[group|G5S1M9]] $G$ with $[x, y, z] = x y^{-1} z$.
For clause 1, all three expressions equal $a b^{-1} c d^{-1} e$; the third one because $(d c^{-1} b)^{-1} = b^{-1} c d^{-1}$.
For clause 2, $a a^{-1} b = b$ and $b a^{-1} a = b$.

Non-example: $\Z$ with $[x, y, z] = x + y + z$.
Clause 1 holds, since all three expressions equal $a + b + c + d + e$.
Clause 2 fails: $[0, 1, 1] = 2 \ne 0$.

Conversely, let $H$ be a nonempty heap and fix $e \in H$.
Then $x \cdot y = [x, e, y]$ makes $H$ a group with identity $e$ and inverse $x^{-1} = [e, x, e]$, and the heap operation is recovered as $[x, y, z] = x y^{-1} z$.
Different choices of $e$ give isomorphic groups.
Some authors allow the empty heap, which corresponds to no group.
