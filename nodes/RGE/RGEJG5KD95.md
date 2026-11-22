---
tag: RGEJG5KD95
kind: example
name: A diagonal matrix that is not scalar does not commute with a matrix unit
msc: ["15A27"]
topics: [Y1ESNQ2V52]
audience: school
not_instance_of:
  - target: 067NKSBEWT
    note: diag(1, 2) has two different diagonal entries, and diag(1, 2) E_12 = (0, 1; 0, 0) differs from E_12 diag(1, 2) = (0, 2; 0, 0)
uses: [0FRM62SG7D, 4H93XF4RVH, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonal_matrix
    locator: Scalar matrix
---

## Example

A diagonal matrix with two different diagonal entries is close to a scalar matrix, but it already fails to commute with a very simple matrix.
Let
$$D = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}, \qquad E_{12} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}.$$

1. The diagonal entries of $D$ are $1$ and $2$, which differ, so $D \ne cI$ for every number $c$. Thus $D$ is not a [[scalar matrix|0FRM62SG7D]].
2. Multiplying on the left by a diagonal matrix multiplies row $i$ by the diagonal entry $d_i$. So $D E_{12}$ is $E_{12}$ with row 1 multiplied by $1$ and row 2 multiplied by $2$:
$$D E_{12} = \begin{pmatrix} 1 \cdot 0 + 0 \cdot 0 & 1 \cdot 1 + 0 \cdot 0 \\ 0 \cdot 0 + 2 \cdot 0 & 0 \cdot 1 + 2 \cdot 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}.$$
3. Multiplying on the right by a diagonal matrix multiplies column $j$ by $d_j$. So $E_{12} D$ is $E_{12}$ with column 2 multiplied by $2$:
$$E_{12} D = \begin{pmatrix} 0 \cdot 1 + 1 \cdot 0 & 0 \cdot 0 + 1 \cdot 2 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix}.$$
4. The entries in position $(1, 2)$ are $1$ and $2$, so $D E_{12} \ne E_{12} D$.

## Remarks

### The general pattern

For a diagonal matrix $D = \operatorname{diag}(d_1, \dots, d_n)$ and a [[matrix unit|4H93XF4RVH]] $E_{ij}$, the same reasoning gives
$$D E_{ij} = d_i E_{ij}, \qquad E_{ij} D = d_j E_{ij}.$$
So $D$ commutes with $E_{ij}$ exactly when $d_i = d_j$, and with all matrix units exactly when all its diagonal entries agree, that is, when $D$ is scalar.

### Try it

Does $\operatorname{diag}(5, 5, 7)$ commute with $E_{12}$ in $M_3(\mathbb{R})$, and with $E_{13}$?
Answer: with $E_{12}$ yes, since $d_1 = d_2 = 5$, and with $E_{13}$ no, since $d_1 = 5 \ne 7 = d_3$.

## Explanations

### L1 human

The matrix $D$ leaves the first direction alone and stretches the second direction by $2$.
Because the two stretches differ, the order of multiplication matters.
A matrix that stretches every direction by the same amount would commute with $E_{12}$.

### L2 human

The matrix $E_{12}$ sends the second basis vector onto the first and sends the first to $0$.
In $E_{12} D$, the stretch comes first, so the second basis vector is doubled before it is moved, and we get the factor $2$.
In $D E_{12}$, the move comes first and lands on the first direction, which $D$ does not stretch, and we get the factor $1$.
The typical use of this example is as a quick test showing that a matrix is not central.
