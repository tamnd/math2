---
tag: FG3K8FHYNE
kind: example
name: The identity matrix is the identity for matrix multiplication
msc: [08A02, 15A99]
topics: [BAZT8JJ70S, Y1ESNQ2V52]
audience: school
instance_of: [07WYQPB8E3, 06DW9BAWB1]
uses: [06DW9BAWB1, 032Q9FB8MT, 0JXZKX526R]
sources:
  - url: https://en.wikipedia.org/wiki/Identity_matrix
    locator: lead section
---

## Example

Let $n \geq 1$, and let $I_n$ be the $n \times n$ [[identity matrix|06DW9BAWB1]]: its entry in row $i$ and column $j$ is $\delta_{ij}$, where $\delta_{ij} = 1$ if $i = j$ and $\delta_{ij} = 0$ if $i \neq j$.
We check that $I_n$ is an [[identity element|07WYQPB8E3]] for [[matrix multiplication|032Q9FB8MT]] on the [[square matrices|0JXZKX526R]] of size $n$ with real entries.
Let $A = (a_{ij})$ be such a matrix.

1. By the definition of the product, the entry of $A I_n$ in row $i$ and column $j$ is $\sum_{k=1}^{n} a_{ik}\delta_{kj}$.
2. In this sum, $\delta_{kj} = 0$ for $k \neq j$, and $\delta_{jj} = 1$. So the sum is $a_{ij}$. Thus $A I_n = A$.
3. The entry of $I_n A$ in row $i$ and column $j$ is $\sum_{k=1}^{n} \delta_{ik}a_{kj}$.
4. In this sum, only the term $k = i$ is not zero, so the sum is $a_{ij}$. Thus $I_n A = A$.
5. By steps 2 and 4, $I_n$ is both a right identity and a left identity, so it is an identity element.

A numerical check with $n = 2$:

6. $\begin{pmatrix} 2 & 3 \\ 4 & 5 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2 \cdot 1 + 3 \cdot 0 & 2 \cdot 0 + 3 \cdot 1 \\ 4 \cdot 1 + 5 \cdot 0 & 4 \cdot 0 + 5 \cdot 1 \end{pmatrix} = \begin{pmatrix} 2 & 3 \\ 4 & 5 \end{pmatrix}$.

## Remarks

The same computation works for entries in $\mathbb{Q}$, $\mathbb{C}$ or any field.
For an $m \times n$ matrix $A$ that is not square, $I_m A = A$ and $A I_n = A$, but the two identity matrices have different sizes.
The identity matrix is also the identity of the [[general linear group|0FCHE902D7]] of invertible $n \times n$ matrices.
A smaller set of matrices can have a different identity.
On the set of matrices $\begin{pmatrix} a & 0 \\ 0 & 0 \end{pmatrix}$ with $a \in \mathbb{R}$, the identity is $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, and $I_2$ is not in this set.

## Explanations

### L1 human

The identity matrix has $1$ on the diagonal from the top left to the bottom right, and $0$ in the other places.
When we multiply a matrix by it, each entry of the result picks exactly one entry of the matrix, so the matrix does not change.
It plays the role of the number $1$ for matrices.

### L2 human

The symbol $\delta_{ij}$ makes the computation short: a sum $\sum_k x_k \delta_{kj}$ keeps only the term $k = j$.
The typical use is in the definition of an inverse matrix: $B$ is an inverse of $A$ when $AB = BA = I_n$.
A trap is to use $I_n$ of the wrong size with a matrix that is not square.
