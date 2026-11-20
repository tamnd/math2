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

Let
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}, \qquad x = \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}.$$

1. $A$ has 3 columns and $x$ has 3 entries, so the [[product|0CCQV3884B]] $Ax$ is defined, and it has 2 entries.
2. Row view, entry 1: $(1, 2, 3) \cdot (1, 0, -1) = 1 + 0 - 3 = -2$.
3. Row view, entry 2: $(4, 5, 6) \cdot (1, 0, -1) = 4 + 0 - 6 = -2$.
4. Column view: $Ax = 1 \begin{pmatrix} 1 \\ 4 \end{pmatrix} + 0 \begin{pmatrix} 2 \\ 5 \end{pmatrix} - 1 \begin{pmatrix} 3 \\ 6 \end{pmatrix} = \begin{pmatrix} -2 \\ -2 \end{pmatrix}$.
5. Both views give $Ax = (-2, -2)^{\mathsf{T}}$.

## Remarks

The column view shows at once that $Ae_2 = (2, 5)^{\mathsf{T}}$, the second column.
The row view is faster for one entry, and the column view is better to see which vectors $Ax$ can reach.

## Explanations

### L1 human

We can compute $Ax$ one row at a time, or we can add up the columns of $A$ with the weights $1$, $0$ and $-1$.
The two ways give the same answer.

### L2 human

The equality of the two views is the exchange of the order in the finite sum $\sum_i \sum_j$.
Each entry $a_{ij} x_j$ appears once in each view.
