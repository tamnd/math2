---
tag: 0E89HQATM8
kind: concept
name: Similar matrices
aliases: [conjugate-matrices]
msc: ["15A21"]
topics: [S6559D61BP]
audience: ug1
uses: [0VD9ZSWWJG, 0EB9N0S33C, 0YQSGNYE3K, 0J7H0YBFDJ]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_similarity
    locator: lead section
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section4-3.xml#L1057
    locator: src/section4-3.xml:1057
  - book: isbn:9780134860244
    locator: Section 2.5
same_as:
  wikidata: Q254491
  wikipedia: Matrix similarity
---

## Summary

Two square [[matrices|0VD9ZSWWJG]] $A$ and $B$ over a field $F$ are similar when $B = P^{-1} A P$ for an [[invertible matrix|0EB9N0S33C]] $P$.
Equivalently, $A$ and $B$ are the [[matrices|0YQSGNYE3K]] of the same [[endomorphism|0J7H0YBFDJ]] in two bases, with $P$ the change of basis matrix.
Similarity is an equivalence relation on $M_n(F)$.
Similar matrices share the rank, trace, determinant, and characteristic and minimal polynomials.

## Motivation

The matrix of an endomorphism $T$ of $V$ depends on the chosen basis.
A change of basis replaces $[T]_B$ by $P^{-1}[T]_B P$.
So the properties of $T$ itself are exactly the properties of matrices that do not change under similarity.
The search for a simple matrix in each similarity class leads to diagonalization and to the Jordan and rational canonical forms.

## Notation

The [[definition|027KDW2K72]] says that $B$ is similar to $A$ when $B = P^{-1} A P$ with $P$ invertible.
Some books write $B = P A P^{-1}$ instead.
The two forms give the same relation, with $P$ replaced by $P^{-1}$.
One writes $A \sim B$, but the same symbol also denotes row equivalence and other relations in some books.
The similarity class of $A$ is the orbit of $A$ under the conjugation action of $GL_n(F)$ on $M_n(F)$.

## Remarks

### Examples

- [[A diagonalization|~fcc4cf33]]: $\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$ is similar to $\operatorname{diag}(1, 2)$, with $P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.
- [[Rotations by a quarter turn|~a154582b]]: $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ is similar to $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, with $P = \operatorname{diag}(1, -1)$.
- [[Similar matrices are conjugate in GL2(R)|ATXHWJGTJV]]: similarity is conjugation in the group of invertible matrices.
- Every matrix is similar to itself, with $P = I_n$.
- A scalar matrix $cI_n$ is similar only to itself, since $P^{-1}(cI_n)P = cI_n$ for every invertible $P$.

### Non-examples

- [[A Jordan block and the identity|~1ebbf521]]: $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $I_2$ share the trace, determinant and characteristic polynomial, but they are not similar.
- [[Matrices with the same five invariants|~d351ee64]]: two $4 \times 4$ matrices share the rank, trace, determinant, and characteristic and minimal polynomials, but they are not similar.
- [[Equivalent matrices that are not similar|6CKAMR5WK9]]: $B = QAP$ with two different invertible matrices is a weaker relation.
- Matrices of different sizes are never similar.

### Basic properties

- Similarity is reflexive, symmetric and transitive, by the [[theorem on the equivalence relation|~e995afb1]].
- Similar matrices have the same rank, trace, determinant, and characteristic and minimal polynomials, by the [[theorem on similarity invariants|~b354e4d1]].
- By the [[change of basis formula|0MQXVZEBMT]], $A$ and $B$ are similar if and only if they are the matrices of one endomorphism of $F^n$ in two bases.
- If $B = P^{-1} A P$, then $B^k = P^{-1} A^k P$ for every $k \ge 0$, and $q(B) = P^{-1} q(A) P$ for every polynomial $q$.
- If $A$ is invertible, then $A^{-1}$ and $B^{-1}$ are similar, with the same $P$.

### History

The relation is the matrix form of a change of coordinates for a linear substitution.
Its classification by canonical forms was developed in the nineteenth century, with the Jordan normal form named after Jordan.

### Common errors

- Taking $P^{-1} A Q$ with two different matrices. That is [[equivalence|0CMHSGTWXB]], which only preserves the rank.
- Thinking that the same characteristic polynomial implies similarity. The [[Jordan block|~1ebbf521]] shows that it does not.
- Forgetting that $P$ must be invertible. With a singular $P$, the product $P^{-1} A P$ is not defined.
- Mixing up $P^{-1} A P$ and $P A P^{-1}$ inside one computation.

## Explanations

### L1 human

Two matrices are similar when one can be turned into the other by a change of basis.
They describe the same linear map from two points of view.
So they share every property that belongs to the map, such as the trace and the determinant.

### L2 human

Let $T$ be an endomorphism of $V$, and let $P$ be the change of basis matrix from $B$ to $B'$.
Then $[T]_{B'} = P^{-1}[T]_B P$, by the change of basis formula.
Conversely, every invertible $P$ is the change of basis matrix to some basis, namely the basis given by its columns.
So the similarity class of $A$ is the set of all matrices of the map $x \mapsto Ax$.

### L3 human

The group $GL_n(F)$ acts on $M_n(F)$ by conjugation, and the similarity classes are its orbits.
Over an algebraically closed field, the Jordan normal form gives one representative in each class.
Over any field, the rational canonical form does the same, and two matrices are similar if and only if they have the same invariant factors.
Similarity does not change under a field extension: two matrices over $F$ that are similar over a larger field are already similar over $F$.
