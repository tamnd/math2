---
tag: 1NYHYECE0A
kind: example
name: A 2 × 3 matrix times a vector, by rows and by columns
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
instance_of: [0PDVQEP0ZC]
uses: [0CCQV3884B, 0V8F3E48E6]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_multiplication
    locator: Definition
  - book: isbn:9780321982384
    locator: Section 1.4
---

## Example

The same product $Ax$ can be computed by rows or by columns, and the two answers must agree.
Let
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}, \qquad x = \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}.$$

1. $A$ has 3 columns and $x$ has 3 entries, so the [[product|0CCQV3884B]] $Ax$ is defined, and it has 2 entries, one for each row.
2. Row view, entry 1: $(1, 2, 3) \cdot (1, 0, -1) = 1 + 0 - 3 = -2$.
3. Row view, entry 2: $(4, 5, 6) \cdot (1, 0, -1) = 4 + 0 - 6 = -2$.
4. Column view: $Ax$ is the [[linear combination|0V8F3E48E6]] of the columns with the weights $1, 0, -1$:
$$Ax = 1 \begin{pmatrix} 1 \\ 4 \end{pmatrix} + 0 \begin{pmatrix} 2 \\ 5 \end{pmatrix} - 1 \begin{pmatrix} 3 \\ 6 \end{pmatrix} = \begin{pmatrix} -2 \\ -2 \end{pmatrix}.$$
5. Both views give $Ax = (-2, -2)^{\mathsf{T}}$.

## Remarks

The two views add the same six products $a_{ij} x_j$.
The row view groups them by $i$ first, the column view by $j$ first, and a finite sum does not depend on how its terms are grouped.

Each view has its use.
The row view is faster for one entry: the second entry of $A(2, 1, 1)^{\mathsf{T}}$ is $8 + 5 + 6 = 19$ without computing the first.
The column view shows at once that $Ae_2 = (2, 5)^{\mathsf{T}}$, the second column, and it shows which vectors $Ax$ can reach.

Changing $x$ to $(1, -2, 1)^{\mathsf{T}}$ gives
$$Ax = \begin{pmatrix} 1 - 4 + 3 \\ 4 - 10 + 6 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix},$$
so the first column minus twice the second plus the third is zero, and the columns of $A$ are linearly dependent.

## Explanations

### L1 human

We can compute $Ax$ one row at a time, or we can add up the columns of $A$ with the weights $1$, $0$ and $-1$.
The first way gives $-2$ and $-2$ as two separate sums.
The second way gives the column $(1, 4)$ minus the column $(3, 6)$, which is $(-2, -2)$ as well.

### L2 human

The equality of the two views is the exchange of the order in the finite double sum over $i$ and $j$.
Each product $a_{ij} x_j$ appears once in each view.
The typical use of the column view is to test whether a vector $b$ is a combination of the columns, which is the question whether $Ax = b$ can be solved.
The trap is to weight the rows of $A$ by the entries of $x$, which does not even fit here, since $A$ has 2 rows and $x$ has 3 entries.
