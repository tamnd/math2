---
tag: K5G3VB3DEZ
kind: definition
name: Magma
msc: [20N02, 08A62]
defines: 9689SFPVE9
uses: [0SJ3RX9TXA, 0M418FE7BB]
sources:
  - url: https://en.wikipedia.org/wiki/Magma_(algebra)
---

## Definition

A *magma* is a pair $(M, \cdot)$, where $M$ is a [[set|0SJ3RX9TXA]] and $\cdot \colon M \times M \to M$ is a [[binary operation|0M418FE7BB]] on $M$.
A *homomorphism* of magmas $(M, \cdot)$ and $(N, *)$ is a map $h \colon M \to N$ with $h(x \cdot y) = h(x) * h(y)$ for all $x, y \in M$.

## Remarks

Example: $(\Z, -)$ is a magma, since the difference of two integers is an integer.
It is not associative: $(1 - 1) - 1 = -1$ but $1 - (1 - 1) = 1$.

Non-example: $(\N, -)$ is not a magma, since $1 - 2 \notin \N$, so subtraction is not a binary operation on $\N$.

The empty set with the empty operation is a magma.
The word *groupoid* is an older name for a magma.
