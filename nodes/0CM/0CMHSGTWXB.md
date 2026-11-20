---
tag: 0CMHSGTWXB
kind: concept
name: Equivalent matrices
msc: [15A21]
topics: [P8J6QR66TJ]
audience: ug1
uses: [0P21AVFFSP, 0EB9N0S33C, 0ZC9YTXZRY, 01REXW3WWE]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_equivalence
    locator: lead section
  - book: isbn:9780521548236
    locator: Section 0.4
same_as:
  wikidata: Q256151
  wikipedia: Matrix equivalence
---

## Summary

Two $m \times n$ matrices $A$ and $B$ over a field are *equivalent* when $B = PAQ$ for [[invertible|0EB9N0S33C]] matrices $P$ of size $m \times m$ and $Q$ of size $n \times n$.
The formal definition is in [[equivalent matrices (definition)|0P21AVFFSP]].
By the [[rank normal form theorem|T2H2QV0M06]], each matrix of [[rank|0ZC9YTXZRY]] $r$ is equivalent to $\begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}$.
So two matrices of the same size are equivalent exactly when they have the same rank.

## Motivation

Multiplying by invertible matrices on the left is doing row operations, and on the right it is doing column operations.
The reason is that each invertible matrix is a product of [[elementary matrices|01REXW3WWE]].
Equivalence asks what is left of a matrix when both kinds of operations are free.
In terms of linear maps, $A$ and $PAQ$ describe the same linear map $F^n \to F^m$ in two pairs of bases.
One basis is for the domain and one is for the codomain.
The answer to the question is that only the rank is left.

## Notation

- We write $A \sim B$ for "$A$ is equivalent to $B$". Some books say *rank equivalent* or *equivalent under row and column operations*.
- The matrix $\begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}$ of size $m \times n$ is written $N_r$ or $J_r$ in some books. Its blocks of zeros may be empty.
- Some books, for example in the language of change of basis, write $B = Q^{-1}AP$ in place of $B = PAQ$. Both give the same relation, because $Q^{-1}$ runs over all invertible matrices when $Q$ does.

## Remarks

### Examples

- The [[worked rank normal form|RX693922PV]] of $\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 7 \end{pmatrix}$ is $(I_2 \ 0)$, with $P$ and $Q$ found by row and column operations.
- Each invertible $n \times n$ matrix $A$ is equivalent to $I_n$, with $P = A^{-1}$ and $Q = I_n$.
- The [[upper unitriangular matrix and the identity|6CKAMR5WK9]] are equivalent but not similar.
- Each nonzero column vector in $F^m$ is equivalent to $e_1$, since both have rank $1$.

### Non-examples

- The matrices [[$\operatorname{diag}(1, 0)$ and $I_2$|NEH45RWK66]] are not equivalent, because their ranks are $1$ and $2$.
- Matrices of different sizes are never equivalent, even if their ranks agree.

### Basic properties

- Equivalence is an equivalence relation on the $m \times n$ matrices: $A = I_m A I_n$; if $B = PAQ$ then $A = P^{-1}BQ^{-1}$; and $C = P'BQ'$ gives $C = (P'P)A(QQ')$.
- Equivalent matrices have the same rank, by the [[rank of a product|02FDWY55AS]].
- Over a field, the classes are indexed by $r = 0, 1, \dots, \min(m, n)$, so there are $\min(m, n) + 1$ classes.
- [[Similarity|0E89HQATM8]] is a finer relation on square matrices: $B = PAP^{-1}$ is the special case $Q = P^{-1}$.
- Row equivalence, $B = PA$, is finer as well; its classes are given by the reduced row echelon form.

### History

Smith found a normal form for integer matrices under equivalence in 1861, now called the Smith normal form.
Frobenius introduced the rank of a matrix in 1879, and over a field the rank is the only invariant of equivalence.

### Common errors

- Students confuse equivalence with similarity. Equivalence allows two unrelated matrices $P$ and $Q$, so it forgets much more.
- Students use the same letter for the two sides. In $PAQ$ the matrix $P$ is $m \times m$ and $Q$ is $n \times n$, and for $m \ne n$ they cannot be equal.

## Explanations

### L1 human

Matrix equivalence allows independent changes of basis on the input side and on the output side.
With so much freedom, only the rank survives.
Every matrix of rank $r$ becomes the identity of size $r$, padded with zeros.

### L2 human

To find $P$ and $Q$, row reduce $A$ and record the row operations in $P$.
Then use column operations to move the pivot columns to the front and to clear the rest of each pivot row; record these in $Q$.
For $A = \begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}$, the row operation $R_1 \to \tfrac12 R_1$ and then $R_2 \to R_2 - R_1$ give $\begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix}$.
The column operation $C_2 \to C_2 - 2C_1$ gives $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, which is the normal form for rank $1$.

### L3 human

In the language of linear maps, the theorem says that $\operatorname{Hom}(F^n, F^m)$ has $\min(m, n) + 1$ orbits under the action of $\mathrm{GL}_m(F) \times \mathrm{GL}_n(F)$.
The orbit of rank $r$ is a locally closed subset in the Zariski topology.
Its closure is the set of matrices of rank at most $r$, a determinantal variety.
Over a principal ideal domain the rank is no longer enough.
There the Smith normal form gives the invariant factors, and this belongs to the theory of modules.
