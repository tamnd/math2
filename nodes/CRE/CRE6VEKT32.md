---
tag: CRE6VEKT32
kind: definition
name: Projective module
msc: [13C10, 16D40]
defines: BFFA03GE3V
uses: [0310REJJY8, 0NZ8JA25WK, 0NRYHJPQG2, 0DZ9DKAKZR, JB7ZBFBA9C]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_module
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] and let $P$ be an [[$R$-module|0NZ8JA25WK]].
The module $P$ is *projective* if it satisfies the following lifting property.
Let $M$, $N$ be $R$-modules, $g \colon M \to N$ a surjective $R$-[[linear map|0NRYHJPQG2]], and $f \colon P \to N$ an $R$-linear map.
Then there is an $R$-linear map $h \colon P \to M$ with $g \circ h = f$.

## Remarks

The following are equivalent for an $R$-module $P$:

1. $P$ is projective.
2. Every surjective linear map $M \to P$ has a right inverse, that is, it splits.
3. $P$ is a direct summand of a [[free module|0DZ9DKAKZR]]: there is a module $Q$ with $P \oplus Q$ free.
4. The functor $\Hom_R(P, -)$ takes [[exact sequences|JB7ZBFBA9C]] to exact sequences.

The same definition works over any ring, commutative or not.

Example: every free module $F$ with basis $(e_i)$ is projective.
Given $g$ and $f$, choose $m_i \in M$ with $g(m_i) = f(e_i)$ and let $h(e_i) = m_i$; then $g \circ h$ and $f$ agree on a basis, so they are equal.
Over $R = \Z/6\Z$, the module $\Z/2\Z$ is projective but not free, since $R \cong \Z/2\Z \oplus \Z/3\Z$ as $R$-modules.

Non-example: over $R = \Z$, the module $\Z/2\Z$ is not projective.
Take $g \colon \Z \to \Z/2\Z$ the reduction and $f$ the identity of $\Z/2\Z$.
A lift $h \colon \Z/2\Z \to \Z$ must be zero, because $2h(1) = h(0) = 0$ and $\Z$ has no nonzero element of order $2$; then $g \circ h = 0 \ne f$.
