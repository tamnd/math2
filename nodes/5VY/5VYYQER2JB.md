---
tag: 5VYYQER2JB
kind: definition
name: Dedekind-finite ring
msc: [16U99, 16U60]
defines: GV1HKEAWVN
uses: [0B1261B5ED, 0FHVPRAE60]
sources:
  - url: https://en.wikipedia.org/wiki/Dedekind-finite_ring
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with $1$.
The ring $R$ is *Dedekind-finite* if, for all $a, b \in R$, the equation $ab = 1$ implies $ba = 1$.

## Remarks

Example: for a field $F$ and $n \ge 1$, the [[matrix ring|0FHVPRAE60]] $M_n(F)$ is Dedekind-finite.
Indeed, if $AB = I$, then $\det A \det B = 1$, so $A$ is invertible, and $B = A^{-1}(AB) = A^{-1}$, hence $BA = I$.

Non-example: let $V$ be the vector space of sequences $(x_1, x_2, \dots)$ over a field and $R = \End(V)$.
Let $a(x_1, x_2, \dots) = (x_2, x_3, \dots)$ and $b(x_1, x_2, \dots) = (0, x_1, x_2, \dots)$.
Then $ab = 1$, but $ba(x_1, x_2, \dots) = (0, x_2, x_3, \dots)$, so $ba \ne 1$.

Other names are *directly finite* and *von Neumann finite*.
Equivalently, $R$ is not isomorphic as a left $R$-module to $R \oplus N$ for any nonzero module $N$.
Every commutative ring, every finite ring, and every left Noetherian ring is Dedekind-finite.
