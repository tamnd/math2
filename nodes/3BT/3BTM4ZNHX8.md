---
tag: 3BTM4ZNHX8
kind: example
name: Multiplying by a diagonal matrix scales the rows or the columns
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
instance_of: [044JNC7ZAA]
uses: [0Q9PGXD9E4, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonal_matrix
    locator: Matrix operations
---

## Example

Let
$$D = \operatorname{diag}(2, 3) = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}, \qquad A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}.$$
We compute $DA$ and $AD$ and compare them.

1. By the [[product rule|076JGP6R3T]], $(DA)_{ij} = \sum_k d_{ik} a_{kj} = d_i a_{ij}$, because only $k = i$ gives a nonzero $d_{ik}$. So row $i$ of $A$ is multiplied by $d_i$:
$$DA = \begin{pmatrix} 2 \cdot 1 & 2 \cdot 2 \\ 3 \cdot 3 & 3 \cdot 4 \end{pmatrix} = \begin{pmatrix} 2 & 4 \\ 9 & 12 \end{pmatrix}.$$
2. In the same way, $(AD)_{ij} = \sum_k a_{ik} d_{kj} = a_{ij} d_j$. So column $j$ of $A$ is multiplied by $d_j$:
$$AD = \begin{pmatrix} 1 \cdot 2 & 2 \cdot 3 \\ 3 \cdot 2 & 4 \cdot 3 \end{pmatrix} = \begin{pmatrix} 2 & 6 \\ 6 & 12 \end{pmatrix}.$$
3. The entries at $(1, 2)$ are $4$ and $6$, so $DA \ne AD$, although $D$ is [[diagonal|0Q9PGXD9E4]].
4. For a second diagonal matrix $D' = \operatorname{diag}(5, 7)$, both orders give the same result:
$$DD' = \operatorname{diag}(2 \cdot 5, 3 \cdot 7) = \operatorname{diag}(10, 21) = D'D.$$

## Remarks

The example shows the two halves of one rule: a diagonal factor on the left acts on rows, and a diagonal factor on the right acts on columns.
The diagonal entries of $DA$ and $AD$ agree, since $d_i a_{ii} = a_{ii} d_i$, and only the off-diagonal entries differ.

When do $D$ and $A$ commute?
Steps 1 and 2 show that $DA = AD$ exactly when $a_{ij}(d_i - d_j) = 0$ for all $i$ and $j$.
Here $a_{12} = 2$ and $d_1 - d_2 = -1$, so the condition fails.
If we change $D$ to $\operatorname{diag}(3, 3) = 3I$, then $d_1 = d_2$ and $D$ commutes with $A$, as every [[scalar matrix|067NKSBEWT]] does.

Scaling on both sides is common in numerical work, where rows and columns are rescaled to balance a matrix before elimination.

## Explanations

### L1 human

A diagonal matrix on the left multiplies each row of the other matrix by a number: the first row by $2$, the second row by $3$.
A diagonal matrix on the right multiplies each column instead.
Rows and columns are different things, so the two results are usually different.

### L2 human

To compute a product with a diagonal factor, do not use the full row-times-column rule.
Read off the scaling instead: on the left, scale row $i$ by $d_i$; on the right, scale column $j$ by $d_j$.
Watch out: it is a common slip to scale rows when the diagonal matrix is on the right.
A quick test is the entry $(1, 2)$: on the left it gets the factor $d_1$, on the right the factor $d_2$.
