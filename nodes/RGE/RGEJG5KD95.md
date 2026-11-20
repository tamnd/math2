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

Let $D = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$ and $E_{12} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.

1. The diagonal entries of $D$ are $1$ and $2$, which differ, so $D \neq cI$ for every $c$. Thus $D$ is not a [[scalar matrix|0FRM62SG7D]].
2. Multiplying on the left by $D$ multiplies row $i$ by $d_i$. So $DE_{12} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.
3. Multiplying on the right by $D$ multiplies column $j$ by $d_j$. So $E_{12}D = \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix}$.
4. The entries $(1, 2)$ are $1$ and $2$, so $DE_{12} \neq E_{12}D$.

## Remarks

In general, $DE_{ij} = d_i E_{ij}$ and $E_{ij}D = d_j E_{ij}$ for a diagonal $D$.
So $D$ commutes with $E_{ij}$ exactly when $d_i = d_j$, and with all [[matrix units|4H93XF4RVH]] exactly when $D$ is scalar.

## Explanations

### L1 human

This matrix stretches the second direction by $2$ and leaves the first direction alone.
Because the two stretches differ, the order of multiplication matters.

### L2 human

The matrix $E_{12}$ moves the second direction onto the first.
Stretching before the move gives the factor $2$, and stretching after the move gives the factor $1$.
