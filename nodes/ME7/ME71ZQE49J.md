---
tag: ME71ZQE49J
kind: definition
name: Commutative magma
msc: [20N02]
defines: XAC78GN2YJ
uses: [9689SFPVE9, 099E72KTF8]
sources:
  - url: https://en.wikipedia.org/wiki/Commutative_magma
---

## Definition

Let $(M, \cdot)$ be a [[magma|9689SFPVE9]].
It is a *commutative magma* if $x \cdot y = y \cdot x$ for all $x, y \in M$, that is, if the operation has the [[commutativity|099E72KTF8]] property.

## Remarks

Example: $\Q$ with $x \circ y = (x + y)/2$.
The value is rational, and $(x + y)/2 = (y + x)/2$.
The magma is not associative: $(0 \circ 4) \circ 8 = 5$ but $0 \circ (4 \circ 8) = 3$.

Non-example: $(\Z, -)$, since $1 - 0 = 1$ but $0 - 1 = -1$.

In Mathlib this structure is the class `CommMagma`.
