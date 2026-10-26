---
tag: 0D1R4SVMBQ
kind: statement
role: theorem
name: Correspondence theorem for rings
aliases: [fourth-isomorphism-theorem-for-rings, lattice-theorem-for-rings]
msc: [16D25]
uses: [0VFW4Y69BT, 0MYSA6MYNA]
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem C (rings)
---

## Statement

Let $R$ be a [[ring|0894J980RK]], let $I$ be a two-sided ideal of $R$ and let $\pi \colon R \to R/I$ be the quotient map.
Let $\mathcal{A}$ be the set of the left [[ideals|0MYSA6MYNA]] $J$ of $R$ with $I \subseteq J$.
Let $\mathcal{B}$ be the set of the left ideals of $R/I$.
The map $\mathcal{A} \to \mathcal{B}$, $J \mapsto J/I = \pi(J)$, is a bijection.
Its inverse is $K \mapsto \pi^{-1}(K)$.
This bijection and its inverse preserve inclusion.

## Remarks

The same bijection holds for right ideals, for two-sided ideals, and for subrings that contain $I$.
For two-sided ideals $J \supseteq I$, the [[third isomorphism theorem|073C80EC63]] gives $(R/I)/(J/I) \cong R/J$.
The ideals of $\mathbb{Z}/12\mathbb{Z}$ correspond to the ideals $d\mathbb{Z}$ with $d \mid 12$, so there are six of them.

## Explanations

### L1 human

The ideals of a quotient ring $R/I$ are the ideals of $R$ that contain $I$, seen in the quotient.
So you can understand the ideals of $R/I$ from the ideals of $R$.
For example, the ideals of $\mathbb{Z}/12\mathbb{Z}$ come from the divisors $1, 2, 3, 4, 6, 12$ of $12$.
