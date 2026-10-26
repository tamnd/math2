---
tag: 0MS8QGA6S5
kind: statement
role: proposition
name: A quotient is abelian iff the subgroup contains the commutator subgroup
msc: [20F12]
uses: [08SJ5K2CBG, 0YYWCNTPWR, 0W77CVBCHQ]
sources:
  - url: https://en.wikipedia.org/wiki/Commutator_subgroup
    locator: Abelianization
---

## Statement

Let $G$ be a [[group|G5S1M9]] and let $N$ be a [[normal subgroup|0CB0DX5BVV]] of $G$.
Then the [[quotient group|0KYX2N69J0]] $G/N$ is [[abelian|082GHNPJ53]] if and only if $[G, G] \subseteq N$, where $[G, G]$ is the [[commutator subgroup|0ASGSTXSBW]].

## Remarks

The cosets $gN$ and $hN$ commute exactly when $g^{-1} h^{-1} g h \in N$.
Thus $[G, G]$ is the smallest normal subgroup of $G$ with an abelian quotient.
A subgroup that contains $[G, G]$ is automatically normal.

## Explanations

### L1 human

To make a group abelian by a quotient, you must send each commutator to the identity.
So the subgroup that you divide by must contain all commutators.
If it does, the quotient is abelian.
