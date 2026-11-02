---
tag: 8NMGMXNF02
kind: definition
name: Classical ring of quotients
msc: [16S85, 16U20, 16P60]
defines: C5971PGKPH
uses: [0B1261B5ED, 0NNRDW10RZ, SG7AQ9T8HD, TJP4ARC2X7, 0XVEZDE9J8, 0GNCRPYXYV]
sources:
  - url: https://en.wikipedia.org/wiki/Ore_condition
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity.
An element $c \in R$ is *regular* if $c$ is not a [[zero divisor|0NNRDW10RZ]] on either side: $c a = 0$ or $a c = 0$ implies $a = 0$.
Let $C$ be the set of regular elements of $R$.
A *right classical ring of quotients* of $R$ is a ring $Q$ containing $R$ as a [[subring|0GNCRPYXYV]] such that:

1. every regular element of $R$ is a [[unit|0XVEZDE9J8]] of $Q$;
2. every element of $Q$ has the form $a c^{-1}$ with $a \in R$ and $c \in C$.

The *left classical ring of quotients* is defined in the same way with elements $c^{-1} a$.
If $R$ has a right and a left classical ring of quotients, they coincide, and this ring is the *classical ring of quotients* of $R$.

## Remarks

The right classical ring of quotients is the [[Ore localization|SG7AQ9T8HD]] $R C^{-1}$.
It exists if and only if $C$ satisfies the right [[Ore condition|TJP4ARC2X7]]; reversibility holds automatically, since elements of $C$ are not zero divisors.
It is then unique up to an isomorphism that fixes $R$.

Example: for a commutative integral domain $R$, the set $C$ is $R \setminus \set{0}$, and the classical ring of quotients is the field of fractions.
For $R = \Z$ it is $\Q$: each nonzero integer is invertible in $\Q$, and each rational number is $a c^{-1}$ with $a, c \in \Z$ and $c \ne 0$.

Non-example: the free algebra $k\langle x, y \rangle$ over a field $k$ is a domain, so $C$ consists of all nonzero elements.
It has no right classical ring of quotients, because $C$ fails the right Ore condition: $x C \cap y R = \emptyset$.

A ring $R$ with a right classical ring of quotients $Q$ is called a *right order* in $Q$.
A right Ore domain has a right classical ring of quotients that is a division ring.
