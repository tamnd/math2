---
tag: 7YPGG6CK8N
kind: example
name: An upper triangular matrix with distinct diagonal entries is not a Jordan block
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
not_instance_of:
  - target: 07PH4RX0X5
    note: the diagonal entries 2 and 3 differ, while a Jordan block has one value on its diagonal
illustrates: [B9CHNGJV5K]
uses: [0PBFS92AJP, 07SQCNV233, 0MPAJRB23T]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_matrix
    locator: Definition
---

## Example

Let $A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}$ over $\mathbb{Q}$.
It is upper triangular with a $1$ just above the diagonal, so it looks like a Jordan block, but it is not one.

1. A [[Jordan block|0PBFS92AJP]] has one value on its whole diagonal, and the diagonal entries of $A$ are $2$ and $3$. So $A$ fails the definition.
2. The characteristic polynomial is $\det(xI - A) = (x - 2)(x - 3)$, since $xI - A$ is triangular. It has two distinct roots.
3. For the eigenvalue $2$, the matrix $A - 2I = \begin{pmatrix} 0 & 1 \\ 0 & 1 \end{pmatrix}$ has kernel spanned by $(1, 0)$.
4. For the eigenvalue $3$, the matrix $A - 3I = \begin{pmatrix} -1 & 1 \\ 0 & 0 \end{pmatrix}$ has kernel spanned by $(1, 1)$.
5. Put the two eigenvectors into the columns of $P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$. Then
$$AP = \begin{pmatrix} 2 & 3 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix} = P \operatorname{diag}(2, 3).$$
6. So $A$ is [[diagonalizable|07SQCNV233]], and its Jordan form is $J_1(2) \oplus J_1(3)$, two blocks of size $1$.

## Remarks

The $1$ above the diagonal does not create a Jordan block of size $2$, because the two eigenvalues differ.
A matrix whose minimal polynomial has distinct roots in $F$ is diagonalizable, by the [[criterion with the minimal polynomial|0MPAJRB23T]], and here the minimal polynomial is $(x - 2)(x - 3)$.

What changes when the diagonal entries become equal?
For $\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$ the matrix is the block $J_2(2)$, the kernel of $A - 2I$ is only the line through $(1, 0)$, and the matrix is not diagonalizable.
For $\begin{pmatrix} 2 & 5 \\ 0 & 2 \end{pmatrix}$ it is not a Jordan block, since the corner is $5$, but it is similar to $J_2(2)$.
So a Jordan block of size $2$ needs a repeated eigenvalue, and the value of a nonzero corner entry does not matter up to similarity.

## Explanations

### L1 human

This matrix looks like a Jordan block, but its two diagonal numbers are different.
Different diagonal numbers give two different eigenvalues, and each one has its own eigenvector.
Two independent eigenvectors in the plane form a basis, and in that basis the matrix is diagonal.

### L2 human

The quick test is the diagonal: a Jordan block repeats one value on it.
Here the eigenvectors $(1, 0)$ and $(1, 1)$ form a basis of $\mathbb{Q}^2$, and in that basis the matrix is $\operatorname{diag}(2, 3)$.
Check: $A(1, 1)^{\mathsf T} = (3, 3)^{\mathsf T} = 3 (1, 1)^{\mathsf T}$.
The trap is to read "upper triangular with ones above the diagonal" as "Jordan block", without looking at the diagonal.
