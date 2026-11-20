---
tag: ~decfb3fa
kind: example
name: An upper triangular matrix with distinct diagonal entries is not a Jordan block
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
not_instance_of:
  - target: 07PH4RX0X5
    note: the diagonal entries 2 and 3 differ, while a Jordan block has one value on its diagonal
illustrates: [~d1324a3e]
uses: [0PBFS92AJP, 07SQCNV233, 0MPAJRB23T]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_matrix
    locator: Definition
---

## Example

Let $A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}$.

1. $A$ is upper triangular with $1$ just above the diagonal, but its diagonal entries $2$ and $3$ differ. So $A$ is not a [[Jordan block|0PBFS92AJP]].
2. Its characteristic polynomial is $(x - 2)(x - 3)$, with two distinct roots.
3. $A - 2I = \begin{pmatrix} 0 & 1 \\ 0 & 1 \end{pmatrix}$ has kernel spanned by $(1, 0)$.
4. $A - 3I = \begin{pmatrix} -1 & 1 \\ 0 & 0 \end{pmatrix}$ has kernel spanned by $(1, 1)$.
5. With $P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, $AP = \begin{pmatrix} 2 & 3 \\ 0 & 3 \end{pmatrix} = P \operatorname{diag}(2, 3)$.
6. So $A$ is [[diagonalisable|07SQCNV233]], with Jordan form $J_1(2) \oplus J_1(3)$, two blocks of size $1$.

## Remarks

By the [[criterion with the minimal polynomial|0MPAJRB23T]], a matrix whose minimal polynomial has distinct roots is diagonalisable.
The entry $1$ above the diagonal looks like a Jordan block, but it does not matter here, because the eigenvalues differ.
A Jordan block of size $2$ needs a repeated eigenvalue.

## Explanations

### L1 human

This matrix looks like a Jordan block, but its two diagonal numbers are different.
Because of that, it has two independent eigenvectors and you can make it diagonal.

### L2 human

The test is the diagonal: a Jordan block has one value repeated on it.
Here the eigenvectors $(1, 0)$ and $(1, 1)$ form a basis, and in that basis the matrix is $\operatorname{diag}(2, 3)$.
