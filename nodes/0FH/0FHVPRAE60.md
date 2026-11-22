---
tag: 0FHVPRAE60
kind: object
name: Matrix ring
msc: ["15A99", "16S50"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [0B1261B5ED]
uses: [0CP7YY6NAG, 0BVXADM10P, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_ring
    locator: lead section
same_as:
  wikidata: Q2915729
  wikipedia: Matrix ring
---

## Description

Let $R$ be a ring and let $n \ge 1$ be an integer.
The *matrix ring* $M_n(R)$ is the set of $n \times n$ [[matrices|0VD9ZSWWJG]] with entries in $R$, with [[matrix addition|0Y7H3SAVA1]] and [[matrix multiplication|032Q9FB8MT]] as its operations.
Its zero is the [[zero matrix|0ZTKJJDGR7]] $0_n$, and its identity is the [[identity matrix|06DW9BAWB1]] $I_n$.
If $R$ is commutative, then $M_n(R)$ is also an algebra over $R$, with [[scalar multiplication|09V6DDACXR]] $c \cdot A = (cI_n)A$.
This page records the structure, and the [[concept page|AB2MD5CD13]] explains it with examples and the main theorems.

## Remarks

### Why the ring axioms hold

Addition is entrywise, so the axioms for addition come from those of $R$: the sum is associative and commutative, $0_n$ is neutral, and $-A = (-a_{ij})$ is the additive inverse.
The product is [[associative|073E4XC016]], it [[distributes over addition|0RXD6EZYBK]] on both sides, and $I_n A = A = A I_n$.
These are all the axioms of a [[ring|0894J980RK]].

### Basic facts

For $n \ge 2$ and $R \ne 0$, the ring $M_n(R)$ is not commutative, and it has nonzero elements with product $0$, such as $E_{12} E_{12} = 0$.
Its units are the [[invertible matrices|0EB9N0S33C]], and they form the [[general linear group|0FCHE902D7]] $GL_n(R)$.
For a field $F$, sending $A$ to the map $x \mapsto Ax$ is a ring isomorphism from $M_n(F)$ to the ring of linear maps from $F^n$ to itself.
The center of $M_n(R)$ is given by the [[center theorem|DVZ1V4A884]].

## Explanations

### L1 human

Square matrices of one fixed size can be added and multiplied, and the result is again a square matrix of that size.
They follow most of the rules of numbers.
The two main differences are that $AB$ can differ from $BA$, and that $AB$ can be the zero matrix when $A$ and $B$ are not.
