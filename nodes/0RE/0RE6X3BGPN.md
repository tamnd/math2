---
tag: 0RE6X3BGPN
kind: example
name: Space of matrices
msc: [15A03]
instance_of: [000AYPA9AJ]
uses: [0N1MY1T0W9, 0BVXADM10P, 0K28YXMS7Q]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_(mathematics)
    locator: lead section
---

## Example

Let $F$ be a field and let $m, n \ge 1$.
The set $M_{m \times n}(F)$ of $m \times n$ [[matrices|0VD9ZSWWJG]] over $F$ is a [[vector space|000AYPA9AJ]] over $F$, with [[matrix addition|0Y7H3SAVA1]] and [[scalar multiplication|09V6DDACXR]].
Its zero vector is the [[zero matrix|0ZTKJJDGR7]].
The matrices $E_{ij}$, with entry $1$ in position $(i, j)$ and $0$ elsewhere, form a basis, so $\dim M_{m \times n}(F) = mn$.

## Remarks

The map that lists the entries of a matrix row by row is a linear isomorphism $M_{m \times n}(F) \to F^{mn}$.
The space $M_{m \times n}(F)$ is isomorphic to the [[space of linear maps|0X9MBPP2Z3]] from $F^n$ to $F^m$.
The symmetric $n \times n$ matrices form a subspace of dimension $n(n+1)/2$.

## Explanations

### L1 human

Matrices of one fixed size can be added and scaled, so they form a vector space.
A $2 \times 2$ matrix holds four numbers, so this space has dimension $4$.
It is $F^4$ written as a square instead of a row.
