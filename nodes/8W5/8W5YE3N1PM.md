---
tag: 8W5YE3N1PM
kind: definition
name: Simple ring
msc: [16D60, 16D25]
defines: 62M0NC3E2T
uses: [0B1261B5ED, 0CD87SFM2N]
sources:
  - url: https://en.wikipedia.org/wiki/Simple_ring
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with $1$.
The ring $R$ is *simple* if $R \ne 0$ and the only [[two-sided ideals|0CD87SFM2N]] of $R$ are $0$ and $R$.

## Remarks

Example: let $F$ be a field and $R = M_2(F)$.
Let $I$ be a nonzero two-sided ideal and $A \in I$ with an entry $a_{ij} \ne 0$.
With the matrix units $E_{kl}$, one has $E_{ki} A E_{jl} = a_{ij} E_{kl}$, so every $E_{kl}$ lies in $I$, hence $I = R$.

Non-example: $\Z$ is not simple, since $2\Z$ is a two-sided ideal different from $0$ and $\Z$.

A commutative ring is simple if and only if it is a field.
A simple ring need not be Artinian: the Weyl algebra over a field of characteristic $0$ is simple and has no zero divisors, but it is not a division ring.
The center of a simple ring is a field.
Some authors require a simple ring to be Artinian as well; here no such condition is imposed.
