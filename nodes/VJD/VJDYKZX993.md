---
tag: VJDYKZX993
kind: definition
name: Opposite ring
msc: [16B99]
defines: M8Q24XB0AF
uses: [0894J980RK]
sources:
  - url: https://en.wikipedia.org/wiki/Opposite_ring
---

## Definition

Let $(R, +, \cdot)$ be a [[ring|0894J980RK]].
The *opposite ring* $R^{\mathrm{op}}$ is the set $R$ with the same addition and the product $*$ given by
$$a * b = b \cdot a$$
for all $a, b \in R$.

## Remarks

$R^{\mathrm{op}}$ is a ring with the same zero and the same unit element as $R$.
Associativity holds because $(a * b) * c = c \cdot (b \cdot a) = (c \cdot b) \cdot a = a * (b * c)$.
Example: for a commutative ring $K$, the transpose map $A \mapsto A^T$ is a ring isomorphism $M_n(K) \to M_n(K)^{\mathrm{op}}$, since $(AB)^T = B^T A^T = A^T * B^T$.
Non-example: for a nonzero commutative ring $K$, the identity map of $M_2(K)$ is not a ring isomorphism $M_2(K) \to M_2(K)^{\mathrm{op}}$, because it would need $AB = BA$ for all $A, B$.
A right $R$-module is the same thing as a left $R^{\mathrm{op}}$-module, with $r \cdot m = m r$.
