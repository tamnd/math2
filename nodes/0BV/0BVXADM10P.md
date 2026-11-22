---
tag: 0BVXADM10P
kind: definition
name: Matrix addition
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
defines: 0Y7H3SAVA1
uses: [0N1MY1T0W9]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_addition
    locator: Entrywise sum
  - book: isbn:9780321982384
    locator: Section 2.1
inventory: [NAYXFHVVCR]
---

## Definition

Two matrices of the same size are added by adding the entries that sit in the same position.
Let $R$ be a ring, and let $A = (a_{ij})$ and $B = (b_{ij})$ be [[matrices|0N1MY1T0W9]] of the same size $m \times n$ over $R$.
The *sum* $A + B$ is the $m \times n$ matrix with entries
$$(A + B)_{ij} = a_{ij} + b_{ij}, \qquad 1 \le i \le m, \ 1 \le j \le n.$$
The *negative* $-A$ has the entries $-a_{ij}$, and the *difference* is $A - B = A + (-B)$.
The sum of two matrices of different sizes is not defined.

## Notation

The set of all $m \times n$ matrices over $R$ is written $M_{m \times n}(R)$, or $R^{m \times n}$.
Addition is a [[binary operation|0M418FE7BB]] on this set, and there is one such operation for each size.
In Mathlib, `A + B` for `A B : Matrix m n α` is the pointwise sum, so `(A + B) i j = A i j + B i j` holds by definition.

## Remarks

Each part of the definition has a job.
The ring $R$ supplies the sum $a_{ij} + b_{ij}$, so only an addition on the entries is needed; the multiplication of $R$ plays no role here.
The equal sizes make the positions of $A$ and $B$ match one to one.
A $2 \times 2$ matrix and a $2 \times 3$ matrix have no common position $(1, 3)$, so the rule has nothing to add there; [[matrices of different sizes|VRD3P83FH7]] shows the failed attempt.

The laws of the addition of $R$ pass to matrices one position at a time.
So addition of matrices is commutative and associative, the [[zero matrix|0ZTKJJDGR7]] $0_{m \times n}$ is its identity element, and $-A$ is the inverse of $A$.
Thus $M_{m \times n}(R)$ is an abelian group under addition.

For a small case, take
$$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} - \begin{pmatrix} 0 & 5 \\ -3 & 1 \end{pmatrix} = \begin{pmatrix} 1 - 0 & 2 - 5 \\ 3 + 3 & 4 - 1 \end{pmatrix} = \begin{pmatrix} 1 & -3 \\ 6 & 3 \end{pmatrix}.$$

The name "sum" is used for other operations too.
The direct sum $A \oplus B$ places the two matrices as blocks of a [[block diagonal matrix|001T5FJDC1]], and it is defined for any sizes, but it is a different operation with a larger result.
The [[concept page|0Y7H3SAVA1]] puts addition together with scalar multiplication.

## Explanations

### L1 human

To add two matrices of the same size, add the entries in the same position.
For example,
$$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} + \begin{pmatrix} 0 & 5 \\ -3 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 7 \\ 0 & 5 \end{pmatrix}.$$
Two matrices of different sizes cannot be added.

### L2 human

Addition is defined position by position, so each law of the addition of $R$ gives the same law for matrices.
For instance, $(A + B)_{ij} = a_{ij} + b_{ij} = b_{ij} + a_{ij} = (B + A)_{ij}$ for every position, which proves $A + B = B + A$.
The typical use is to combine data tables or matrices of linear maps of the same shape.
The trap is to add a number to a matrix, as in $A + 2$, which this definition does not cover.
