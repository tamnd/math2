---
tag: XVP517QRH5
kind: concept
name: Semiprimary ring
msc: [16L30, 16N20]
specializes: [49Y9Q949PK]
sources:
  - url: https://en.wikipedia.org/wiki/Hopkins%E2%80%93Levitzki_theorem
---

## Summary

A semiprimary ring is a ring $R$ such that $R/J(R)$ is semisimple and the [[Jacobson radical|XA0DCNH7WY]] $J(R)$ is nilpotent.
Every left Artinian ring is semiprimary, because its [[Jacobson radical is nilpotent|H7RAXJV9CP]].
Semiprimary rings are left and right [[perfect|49Y9Q949PK]].
They are the setting of the [[Hopkins–Levitzki theorem|W29AA0266Z]]: a semiprimary ring is left Artinian exactly when it is left Noetherian.

## Explanations

### L1 human

A semiprimary ring is semisimple up to a radical that dies after finitely many multiplications.
This is the structure of a left Artinian ring, but without any chain condition.
For example, let $R$ be the ring $k[x_1, x_2, \ldots]$ with all products $x_i x_j$ set equal to $0$.
It is semiprimary: its radical is spanned by the $x_i$, it squares to zero, and the quotient is the field $k$.
This ring is not Artinian, because the ideals $(x_n, x_{n+1}, \ldots)$ form an infinite descending chain.
