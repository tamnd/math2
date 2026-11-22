---
tag: 06DW9BAWB1
kind: object
name: Identity matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
instance_of: [0VD9ZSWWJG]
uses: [0CP7YY6NAG]
sources:
  - url: https://en.wikipedia.org/wiki/Identity_matrix
    locator: lead section
same_as:
  wikidata: Q193794
  wikipedia: Identity matrix
---

## Description

The identity matrix is the matrix that plays the part of the number $1$: multiplying by it changes nothing.
Let $R$ be a ring with identity and let $n \ge 0$ be an integer.
The *identity matrix* $I_n$ is the $n \times n$ [[matrix|0VD9ZSWWJG]] over $R$ with $1$ at each position of the main diagonal and $0$ at every other position.
In symbols, $(I_n)_{ij} = \delta_{ij}$, the Kronecker delta, which is $1$ when $i = j$ and $0$ when $i \ne j$, as in the [[formal definition|6NHZRCKJNW]].
For example,
$$I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \qquad I_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}.$$
For every $m \times n$ matrix $A$, we have $I_m A = A$ and $A I_n = A$.

## Remarks

### Multiplying by the identity

Take $A = \begin{pmatrix} 2 & 3 \\ 4 & 5 \end{pmatrix}$ and multiply on the right by $I_2$, row times column:
$$A I_2 = \begin{pmatrix} 2 \cdot 1 + 3 \cdot 0 & 2 \cdot 0 + 3 \cdot 1 \\ 4 \cdot 1 + 5 \cdot 0 & 4 \cdot 0 + 5 \cdot 1 \end{pmatrix} = \begin{pmatrix} 2 & 3 \\ 4 & 5 \end{pmatrix}.$$
Each entry of the result picks out exactly one entry of $A$, because the column of $I_2$ has a single $1$.
In general, the entry $(i, j)$ of $A I_n$ is $\sum_k a_{ik} \delta_{kj}$, and only the term $k = j$ survives, which leaves $a_{ij}$.
The [[proof for all orders|FG3K8FHYNE]] writes this out on both sides.
So $I_n$ is the identity element of the [[matrix ring|AB2MD5CD13]] $M_n(R)$.

### The columns are the standard basis

Column $j$ of $I_n$ has a $1$ in row $j$ and zeros elsewhere, so it is the [[standard basis vector|0V7ZD6P7RK]] $e_j$.
The product $I_n x$ is the combination $x_1 e_1 + \dots + x_n e_n$ of the columns, which is $x$ itself.
This is the identity map $x \mapsto x$ in matrix form, and $I_n$ is the matrix of the identity map in every basis.
The [[columns of I₃|36GFGXK44K]] are worked out in full.

### What it is not

The all-ones matrix $J = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ is a common wrong guess.
For $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, each row of $JA$ is the sum $(4, 6)$ of the rows of $A$, so $JA \ne A$; see [[the all-ones matrix|QCV57HQ0PE]].
A rectangular matrix is never an identity for multiplication, because an identity must be square to keep the size of $A$.
The scalar multiples $c I_n$ with $c \ne 1$ are not identities either, since $(c I_n) A = cA$; they are the [[scalar matrices|067NKSBEWT]].

### Watch out

For a rectangular $A$, the two identities on the two sides have different sizes.
If $A$ is $2 \times 3$, then $I_2 A = A$ and $A I_3 = A$, but $A I_2$ and $I_3 A$ are not defined.
Some books write $E$ for the identity, from the German *Einheitsmatrix*, so do not confuse it with a [[matrix unit|A4HTT7JFD1]] $E_{ij}$.

### Try it

What is $I_3 (2, -1, 7)^{\mathsf{T}}$?
It is $2 e_1 - e_2 + 7 e_3 = (2, -1, 7)^{\mathsf{T}}$, the same vector.

Is $\begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix}$ an identity matrix?
No, because it is $3 \times 2$ and an identity matrix is square.

## Explanations

### L1 human

The identity matrix has ones on the main diagonal and zeros everywhere else.
It plays the role of the number $1$: multiplying a matrix by it changes nothing.
As a map, it leaves every vector where it is, like a photocopy at full size.

### L2 human

The typical use of $I_n$ is in the definition of an inverse: $B$ is the inverse of $A$ when $AB = BA = I_n$.
For $A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$, row times column gives
$$AB = \begin{pmatrix} 2 - 1 & -2 + 2 \\ 1 - 1 & -1 + 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2,$$
and $BA = I_2$ in the same way.
The trap is to use an identity of the wrong size next to a rectangular matrix.

### L3 human

The identity matrix is the identity element of the monoid $(M_n(R), \cdot)$ and of the [[general linear group|0FCHE902D7]] $\mathrm{GL}_n(R)$.
In the category whose objects are the integers $n \ge 0$ and whose morphisms are matrices, $I_n$ is the identity morphism of the object $n$.
Its entries $\delta_{ij}$ also define the standard inner product, since $x^{\mathsf{T}} I_n y = \sum_i x_i y_i$ is the [[dot product|0S52TNNTH9]].
