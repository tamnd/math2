---
tag: MXXTYV1J2N
kind: definition
name: Semisimple ring
msc: [16D60, 16K99, 16P20]
defines: NY25HXA478
uses: [0B1261B5ED, 0NZ8JA25WK, N3MRHDKDGC, 20QEAM8AX2, XA0DCNH7WY]
sources:
  - url: https://en.wikipedia.org/wiki/Semisimple_module
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with $1$.
The ring $R$ is *(left) semisimple* if $R$, viewed as a left [[module|0NZ8JA25WK]] over itself, is a [[semisimple module|N3MRHDKDGC]].
That is, $R$ is a direct sum of minimal nonzero left ideals.

## Remarks

Example: for a field $F$, the ring $R = M_2(F)$ is semisimple.
The left ideals $L_1$ and $L_2$ of matrices that vanish outside the first and the second column are minimal, and $R = L_1 \oplus L_2$.

Non-example: $\Z$ is not semisimple.
A minimal nonzero ideal of $\Z$ would be some $n\Z$ with $n \ne 0$, but $2n\Z$ lies strictly inside it, so $\Z$ has no minimal nonzero ideal.

A ring is left semisimple if and only if it is right semisimple, so one simply says semisimple.
Equivalent conditions: every left $R$-module is semisimple; every left $R$-module is projective; $R$ is left [[Artinian|20QEAM8AX2]] and its [[Jacobson radical|XA0DCNH7WY]] is $0$.
A semisimple ring is a finite direct sum of minimal left ideals, because $1$ lies in a finite partial sum.
