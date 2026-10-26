---
tag: 0FHVPRAE60
kind: object
name: Matrix ring
msc: [15A99, 16S50]
instance_of: [0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_ring
    locator: lead section
same_as:
  wikidata: Q2915729
  wikipedia: Matrix ring
---

## Description

Let $R$ be a ring and let $n \ge 1$ be an integer.
The *matrix ring* $M_n(R)$ is the set of $n \times n$ [[matrices|0VD9ZSWWJG]] over $R$, with [[matrix addition|0Y7H3SAVA1]] and [[matrix multiplication|032Q9FB8MT]].
It is a ring, with the [[zero matrix|0ZTKJJDGR7]] as zero and the [[identity matrix|06DW9BAWB1]] $I_n$ as unit.
If $R$ is commutative, then $M_n(R)$ is also an algebra over $R$, with [[scalar multiplication|09V6DDACXR]].

## Remarks

For $n \ge 2$ and $R \ne 0$, the ring $M_n(R)$ is not commutative and has nonzero elements whose product is zero.
The units of $M_n(R)$ are the [[invertible matrices|0EB9N0S33C]], and they form the [[general linear group|0FCHE902D7]].
For a field $F$, the ring $M_n(F)$ is isomorphic to the ring of endomorphisms of $F^n$.

## Explanations

### L1 human

Square matrices of one fixed size can be added and multiplied, and the result is again a square matrix of that size.
They follow most of the rules of numbers.
The main differences are that $AB$ can differ from $BA$, and that $AB$ can be zero when $A$ and $B$ are not.
