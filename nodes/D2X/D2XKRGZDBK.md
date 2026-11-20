---
tag: D2XKRGZDBK
kind: example
name: Four views of the product of two 2 × 2 matrices
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
instance_of: [032Q9FB8MT]
uses: [076JGP6R3T, 0CCQV3884B]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_multiplication
    locator: Definitions
  - book: isbn:9780321982384
    locator: Section 2.1
---

## Example

Let
$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \qquad B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}.$$
We compute $AB$ in four ways from the [[definition|076JGP6R3T]].

1. Entries: $(AB)_{11} = 1 \cdot 5 + 2 \cdot 7 = 19$, $(AB)_{12} = 1 \cdot 6 + 2 \cdot 8 = 22$, $(AB)_{21} = 3 \cdot 5 + 4 \cdot 7 = 43$, $(AB)_{22} = 3 \cdot 6 + 4 \cdot 8 = 50$.
2. Columns: $A(5, 7)^{\mathsf{T}} = 5(1, 3)^{\mathsf{T}} + 7(2, 4)^{\mathsf{T}} = (19, 43)^{\mathsf{T}}$, and $A(6, 8)^{\mathsf{T}} = (6 + 16, 18 + 32)^{\mathsf{T}} = (22, 50)^{\mathsf{T}}$.
3. Rows: row 1 of $AB$ is $1 \cdot (5, 6) + 2 \cdot (7, 8) = (19, 22)$, and row 2 is $3 \cdot (5, 6) + 4 \cdot (7, 8) = (43, 50)$.
4. Outer products: $\begin{pmatrix} 1 \\ 3 \end{pmatrix}\begin{pmatrix} 5 & 6 \end{pmatrix} + \begin{pmatrix} 2 \\ 4 \end{pmatrix}\begin{pmatrix} 7 & 8 \end{pmatrix} = \begin{pmatrix} 5 & 6 \\ 15 & 18 \end{pmatrix} + \begin{pmatrix} 14 & 16 \\ 28 & 32 \end{pmatrix}$.
5. All four views give $AB = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$.
6. In the other order, $BA = \begin{pmatrix} 5 + 18 & 10 + 24 \\ 7 + 24 & 14 + 32 \end{pmatrix} = \begin{pmatrix} 23 & 34 \\ 31 & 46 \end{pmatrix} \neq AB$.

## Remarks

Each view sums the same eight products $a_{ik} b_{kj}$, grouped in a different way.
The column view shows that the columns of $AB$ are combinations of the columns of $A$.
The row view shows that the rows of $AB$ are combinations of the rows of $B$.

## Explanations

### L1 human

The usual rule is "row times column" for each entry.
We can also build the product one column at a time, or one row at a time.
All the ways give the same matrix.

### L2 human

The outer product view writes $AB$ as a sum of $n$ matrices of rank at most one.
This view is the basis of [[block multiplication|0ASDFEQS6P]] and of many fast algorithms.
