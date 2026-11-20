---
tag: 0P21AVFFSP
kind: definition
name: Equivalent matrices
msc: [15A21]
defines: 0CMHSGTWXB
topics: [P8J6QR66TJ]
audience: ug1
uses: [0TWTS88TWN]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_equivalence
    locator: lead section
---

## Definition

Let $F$ be a field and let $A$ and $B$ be $m \times n$ matrices over $F$.
The matrix $B$ is *equivalent* to $A$ when there are an [[invertible|0TWTS88TWN]] $m \times m$ matrix $P$ and an invertible $n \times n$ matrix $Q$ over $F$ with
$$B = P A Q.$$

## Notation

We write $A \sim B$.
Some books write the condition as $B = Q^{-1} A P$, with $Q$ of size $m \times m$ and $P$ of size $n \times n$.
This is the form that comes from a change of bases.
The two conventions define the same relation, because the inverse of an invertible matrix is invertible.

## Remarks

Two matrices are equivalent if and only if they represent the same linear map $F^n \to F^m$ in two pairs of bases.
Two $m \times n$ matrices over a field are equivalent if and only if they have the same [[rank|0ZC9YTXZRY]], by the [[rank normal form theorem|T2H2QV0M06]].
A matrix of rank $r$ is equivalent to the block matrix $\begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}$.
[[Similarity|0E89HQATM8]] is a finer relation: similar matrices are equivalent, but equivalent square matrices need not be similar, as the [[unitriangular example|6CKAMR5WK9]] shows.

## Explanations

### L1 human

Matrix equivalence allows independent changes of basis on the input side and on the output side.
With so much freedom, only the rank survives.
Every matrix of rank $r$ becomes the identity of size $r$, padded with zeros.

### L2 human

The left factor $P$ acts on rows and the right factor $Q$ acts on columns.
For example, $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$.
So $\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ is equivalent to $\operatorname{diag}(1, 0)$.

### L3 human

Equivalence is the orbit relation of the group $\mathrm{GL}_m(F) \times \mathrm{GL}_n(F)$ acting by $(P, Q) \cdot A = PAQ^{-1}$.
Writing $Q^{-1}$ makes this a left action; as a relation it is the same as $B = PAQ$.
