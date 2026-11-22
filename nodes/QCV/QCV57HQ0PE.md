---
tag: QCV57HQ0PE
kind: example
name: The all-ones matrix is not an identity for multiplication
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
not_instance_of:
  - target: 06DW9BAWB1
    note: the matrix J with all entries 1 gives JA = (4, 6; 4, 6) for A = (1, 2; 3, 4), so JA is not A
uses: [6NHZRCKJNW, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_of_ones
    locator: Properties
---

## Example

Since the number $1$ is the identity for numbers, a table full of ones looks like a natural identity for matrices, but it is not.
Let
$$J = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}, \qquad A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}.$$

1. Each row of $J$ is $(1, 1)$. Row times column then adds the two entries of each column of $A$, so each row of $JA$ is the sum of the rows of $A$:
$$JA = \begin{pmatrix} 1 + 3 & 2 + 4 \\ 1 + 3 & 2 + 4 \end{pmatrix} = \begin{pmatrix} 4 & 6 \\ 4 & 6 \end{pmatrix} \neq A.$$
2. Each column of $J$ is $(1, 1)^{\mathsf{T}}$, so each column of $AJ$ is the sum of the columns of $A$:
$$AJ = \begin{pmatrix} 1 + 2 & 1 + 2 \\ 3 + 4 & 3 + 4 \end{pmatrix} = \begin{pmatrix} 3 & 3 \\ 7 & 7 \end{pmatrix} \neq A.$$
3. The [[identity matrix|6NHZRCKJNW]] $I_2$ satisfies $I_2 A = A I_2 = A$. Steps 1 and 2 fail this on both sides, so $J$ is not an identity for the [[matrix product|076JGP6R3T]].

## Remarks

The example shows that the identity matrix is defined by where its ones sit, not by its entries being $1$.
The off-diagonal ones of $J$ mix the rows or the columns of $A$, and the zeros of $I_2$ are what prevent this mixing.

The all-ones matrix is the identity for a different product.
For the entrywise product, the [[Hadamard product|SQT6QCEXZ8]], each entry of $A$ is multiplied by $1$, so $J$ leaves $A$ unchanged there.
For the matrix product, $J$ satisfies
$$J^2 = \begin{pmatrix} 1 + 1 & 1 + 1 \\ 1 + 1 & 1 + 1 \end{pmatrix} = 2J,$$
so $P = \tfrac{1}{2} J$ has $P^2 = \tfrac{1}{4} J^2 = \tfrac{1}{2} J = P$, and $P$ is an [[idempotent matrix|0KCE8CG86P]].
For the $n \times n$ all-ones matrix the same count gives $J^2 = nJ$.

## Explanations

### L1 human

The number $1$ is the identity for multiplying numbers.
A table full of ones is not the identity for multiplying matrices.
Multiplying by it adds up rows or columns, so the matrix changes.
The identity matrix has ones only on the diagonal, and zeros elsewhere.

### L2 human

Multiplying by $J$ on the left adds the rows, and multiplying on the right adds the columns.
This makes $J$ useful in statistics: for a column of data $x$, the vector $\tfrac{1}{n} J x$ has the mean of $x$ in every entry.
The only matrix that leaves every $A$ unchanged is $I_2$, because the identity element of a monoid is unique.
The trap is to think of matrix multiplication as entrywise, where $J$ would indeed be the identity.
