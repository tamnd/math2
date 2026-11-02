---
tag: JXBSN6E2X5
kind: definition
name: Opposite structure
msc: [08A02, 20A05]
defines: D33V8HE0KY
uses: [0M418FE7BB, G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Opposite_group
---

## Definition

Let $\ast$ be a [[binary operation|0M418FE7BB]] on a set $S$.
The *opposite* of $(S, \ast)$ is $(S, \ast^{\mathrm{op}})$, where $a \ast^{\mathrm{op}} b = b \ast a$ for all $a, b \in S$.
For a structure with several operations, such as a ring, the opposite structure reverses the chosen multiplication and keeps all other operations and constants.

## Remarks

Example: if $(G, \cdot)$ is a [[group|G5S1M9]], then $(G, \cdot^{\mathrm{op}})$ is a group with the same identity and the same inverses.
Associativity holds since $(a \cdot^{\mathrm{op}} b) \cdot^{\mathrm{op}} c = c \cdot b \cdot a = a \cdot^{\mathrm{op}} (b \cdot^{\mathrm{op}} c)$.
The map $x \mapsto x^{-1}$ is an isomorphism from $G$ to its opposite, because $(xy)^{-1} = y^{-1} x^{-1}$.

Non-example: for $2 \times 2$ real matrices, the opposite multiplication is not the same operation as the usual one, because the matrices do not all commute.
The transpose $A \mapsto A^T$ is still an isomorphism from the matrix ring to its opposite, because $(AB)^T = B^T A^T$.

Common notations are $S^{\mathrm{op}}$ and $S^{\circ}$.
The opposite of the opposite is the original structure.
