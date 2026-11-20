---
tag: V8J40J1DKG
kind: example
name: One matrix gives different linear maps in different bases
msc: ["15A04"]
topics: [S6559D61BP]
audience: ug1
instance_of: [06HMCTAQH3]
uses: [009892PZ30, 0YYMY95FWS]
sources:
  - url: https://en.wikipedia.org/wiki/Transformation_matrix
    locator: lead section
---

## Example

Let $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ over $\R$.

1. In the standard basis $E = (e_1, e_2)$ of $\R^2$, the [[linear map of $A$|009892PZ30]] sends $e_1 \mapsto 1 e_1 + 0 e_2 = (1, 0)$ and $e_2 \mapsto 2 e_1 + 1 e_2 = (2, 1)$.
2. So this map is $S(x, y) = (x + 2y,\ y)$, a shear. Its matrix in the standard basis is $A$.
3. Now take the basis $B = (b_1, b_2)$ with $b_1 = (1, 1)$ and $b_2 = (0, 1)$, on both sides.
4. The linear map $T$ of $A$ in $B$ sends $b_1 \mapsto 1 b_1 + 0 b_2 = (1, 1)$ and $b_2 \mapsto 2 b_1 + 1 b_2 = (2, 2) + (0, 1) = (2, 3)$.
5. Since $e_1 = b_1 - b_2$ and $e_2 = b_2$, linearity gives $T(e_1) = (1, 1) - (2, 3) = (-1, -2)$ and $T(e_2) = (2, 3)$.
6. So the standard [[matrix|0YYMY95FWS]] of $T$ is $\begin{pmatrix} -1 & 2 \\ -2 & 3 \end{pmatrix}$, and $T(x, y) = (-x + 2y,\ -2x + 3y)$.
7. Check: $T(1, 1) = (-1 + 2,\ -2 + 3) = (1, 1)$ and $T(0, 1) = (2, 3)$, as in step 4.
8. The maps differ: $S(1, 0) = (1, 0)$, but $T(1, 0) = (-1, -2)$.

## Remarks

- Both matrices $A$ and $\begin{pmatrix} -1 & 2 \\ -2 & 3 \end{pmatrix}$ have trace $2$ and determinant $1$. They are [[similar|0E89HQATM8]], since they are the matrices of one map $T$ in two bases.
- So a matrix alone does not determine a map of an abstract space. The bases are part of the data.

## Explanations

### L1 human

A matrix becomes a linear map only when bases are fixed.
The same table of numbers, read in two bases, gives two different maps.

### L2 human

Column $j$ of $A$ gives the coordinates of the image of $b_j$ in the basis of the target.
To get the standard formula of the map, compute the images of $b_1$ and $b_2$, and then write $e_1$ and $e_2$ in terms of $b_1$ and $b_2$.
