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

If row operations and column operations are both allowed, a matrix can be simplified until only its rank is left.
Two $m \times n$ matrices $A$ and $B$ over a field are *equivalent* when $B = PAQ$ for [[invertible|0EB9N0S33C]] matrices $P$ of size $m \times m$ and $Q$ of size $n \times n$.
The formal definition is in [[equivalent matrices (definition)|0P21AVFFSP]].
By the [[rank normal form theorem|T2H2QV0M06]], each matrix of [[rank|0ZC9YTXZRY]] $r$ is equivalent to $\begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}$.
So two matrices of the same size are equivalent exactly when they have the same rank.

## Motivation

Multiplying by an invertible matrix on the left is doing row operations, and on the right it is doing column operations, because each invertible matrix is a product of [[elementary matrices|01REXW3WWE]].
Equivalence asks what is left of a matrix when both kinds of operations are free.
In terms of linear maps, $A$ and $PAQ$ describe the same linear map $F^n \to F^m$ in two pairs of bases, one for the domain and one for the codomain.
The answer to the question is that only the rank is left.

## Notation

We write $A \sim B$ for "$A$ is equivalent to $B$"; some books say *rank equivalent* or *equivalent under row and column operations*.
The $m \times n$ matrix $\begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}$ is written $N_r$ or $J_r$ in some books, and its blocks of zeros may be empty.
Books that start from a change of basis often write $B = Q^{-1}AP$ in place of $B = PAQ$.
Both give the same relation, because $Q^{-1}$ runs over all invertible matrices when $Q$ does.

## Remarks

### A first reduction

Take $A = \begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}$.
The row operations $R_1 \to \tfrac12 R_1$ and then $R_2 \to R_2 - R_1$, followed by the column operation $C_2 \to C_2 - 2C_1$, give
$$\begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix} \to \begin{pmatrix} 1 & 2 \\ 1 & 2 \end{pmatrix} \to \begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix} \to \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = N_1.$$
So $A \sim N_1$, which fits $\operatorname{rank} A = 1$.
The [[worked rank normal form|RX693922PV]] of $\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 7 \end{pmatrix}$ records $P$ and $Q$ as products of elementary matrices.

### The relation and its classes

Equivalence is an equivalence relation on the $m \times n$ matrices.
It is reflexive since $A = I_m A I_n$, symmetric since $B = PAQ$ gives $A = P^{-1}BQ^{-1}$, and transitive since $C = P'BQ'$ gives $C = (P'P)A(QQ')$.
Equivalent matrices have the same rank, by the [[rank of a product|02FDWY55AS]].
Over a field, the classes are indexed by $r = 0, 1, \dots, \min(m, n)$, so there are $\min(m, n) + 1$ classes.
For instance, each invertible $n \times n$ matrix $A$ is equivalent to $I_n$, with $P = A^{-1}$ and $Q = I_n$, and each nonzero column vector in $F^m$ is equivalent to $e_1$.

### Finer relations

[[Similarity|0E89HQATM8]] of square matrices is the special case $Q = P^{-1}$, and it is a much finer relation.
The [[upper unitriangular matrix and the identity|6CKAMR5WK9]] are equivalent but not similar.
Row equivalence, $B = PA$, is finer as well, and its classes are given by the reduced row echelon form.
Different relations keep different invariants: equivalence keeps only the rank, while similarity also keeps the trace, the determinant and the eigenvalues.

### Non-examples

The matrices [[$\operatorname{diag}(1, 0)$ and $I_2$|NEH45RWK66]] are not equivalent, because their ranks are $1$ and $2$.
Matrices of different sizes are never equivalent, even if their ranks agree, since $P$ and $Q$ must have the right sizes for $PAQ$ to be defined.

### Watch out

Equivalence is not similarity.
Equivalence allows two unrelated matrices $P$ and $Q$, so it forgets much more.
In $PAQ$ the matrix $P$ is $m \times m$ and $Q$ is $n \times n$, and for $m \ne n$ they cannot even be equal.

### History

Smith found a normal form for integer matrices under equivalence in 1861, now called the Smith normal form.
Frobenius introduced the term rank in 1879, and over a field the rank is the only invariant of equivalence.

### Try it

Find the normal form of $A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix}$ and give one pair $P$, $Q$.
Answer: $\operatorname{rank} A = 1$, so the normal form is $N_1 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$.
The row operation $R_2 \to R_2 - R_1$ is $P = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}$, and the column operations $C_2 \to C_2 - C_1$ and $C_3 \to C_3 - C_1$ are $Q = \begin{pmatrix} 1 & -1 & -1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$.
Check: $PA = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 0 & 0 \end{pmatrix}$, and $PAQ$ has columns $(1, 0)^{\mathsf{T}}$, $(1 - 1, 0)^{\mathsf{T}}$ and $(1 - 1, 0)^{\mathsf{T}}$, so $PAQ = N_1$.

## Explanations

### L1 human

Matrix equivalence allows independent changes of basis on the input side and on the output side.
With so much freedom, only the rank survives.
Every matrix of rank $r$ becomes the identity of size $r$, padded with zeros.

### L2 human

To find $P$ and $Q$, row reduce $A$ and record the row operations in $P$.
Then use column operations to move the pivot columns to the front and to clear the rest of each pivot row, and record these in $Q$.
To decide whether two matrices of the same size are equivalent, you need neither: compare their ranks.

### L3 human

In the language of linear maps, the theorem says that $\operatorname{Hom}(F^n, F^m)$ has $\min(m, n) + 1$ orbits under the action of $\mathrm{GL}_m(F) \times \mathrm{GL}_n(F)$.
The orbit of rank $r$ is a locally closed subset in the Zariski topology, and its closure is the set of matrices of rank at most $r$, a determinantal variety.
Over a principal ideal domain the rank is no longer enough.
There the Smith normal form gives the invariant factors, and this belongs to the theory of modules.
