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

A matrix becomes a linear map only after bases are chosen, and the same matrix read in two bases gives two different maps.
Let $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ over $\mathbb{R}$.

First read $A$ in the standard basis $E = (e_1, e_2)$ of $\mathbb{R}^2$, on both sides.

1. The [[linear map of A|009892PZ30]] sends $e_1$ to $1 e_1 + 0 e_2 = (1, 0)$ and $e_2$ to $2 e_1 + 1 e_2 = (2, 1)$.
2. So this map is $S(x, y) = x(1, 0) + y(2, 1) = (x + 2y, y)$, a shear along the first axis.

Now read $A$ in the basis $B = (b_1, b_2)$ with $b_1 = (1, 1)$ and $b_2 = (0, 1)$, on both sides, and call the map $T$.

3. Column 1 gives $T(b_1) = 1 b_1 + 0 b_2 = (1, 1)$.
4. Column 2 gives $T(b_2) = 2 b_1 + 1 b_2 = (2, 2) + (0, 1) = (2, 3)$.
5. To find the standard formula of $T$, write $e_1 = b_1 - b_2$ and $e_2 = b_2$, and use linearity:
$$T(e_1) = T(b_1) - T(b_2) = (1, 1) - (2, 3) = (-1, -2), \qquad T(e_2) = (2, 3).$$
6. So the standard [[matrix|0YYMY95FWS]] of $T$ is $\begin{pmatrix} -1 & 2 \\ -2 & 3 \end{pmatrix}$, and $T(x, y) = (-x + 2y, -2x + 3y)$.
7. Check: $T(1, 1) = (-1 + 2, -2 + 3) = (1, 1)$ and $T(0, 1) = (2, 3)$, as in steps 3 and 4.
8. The two maps differ, since $S(1, 0) = (1, 0)$ but $T(1, 0) = (-1, -2)$.

## Remarks

So a matrix alone does not determine a map of an abstract space, and the bases are part of the data.
The two maps are still closely related.
The matrix $A$ is the matrix of $T$ in the basis $B$, and $\begin{pmatrix} -1 & 2 \\ -2 & 3 \end{pmatrix}$ is the matrix of $T$ in the basis $E$, so the two matrices are [[similar|0E89HQATM8]].
They share the trace, $1 + 1 = 2 = -1 + 3$, and the determinant, $1 \cdot 1 - 2 \cdot 0 = 1 = (-1) \cdot 3 - 2 \cdot (-2)$.

If we change only one of the two bases, the effect is different.
With $B$ on the domain and $E$ on the target, the map of $A$ sends $b_1$ to $(1, 0)$ and $b_2$ to $(2, 1)$.
Then $e_1 = b_1 - b_2$ goes to $(1, 0) - (2, 1) = (-1, -1)$ and $e_2$ goes to $(2, 1)$, so the standard matrix is $\begin{pmatrix} -1 & 2 \\ -1 & 1 \end{pmatrix}$, which has trace $0$ and is not similar to $A$.

## Explanations

### L1 human

A matrix becomes a linear map only when bases are fixed.
Here the same table of four numbers is a shear when you read it with the usual axes.
Read with the tilted axes $(1, 1)$ and $(0, 1)$, it moves $(1, 0)$ to $(-1, -2)$, which the shear never does.

### L2 human

Column $j$ of $A$ gives the coordinates of the image of $b_j$ in the basis of the target.
To get the standard formula of the map, compute the images of $b_1$ and $b_2$ as vectors, then write $e_1$ and $e_2$ in terms of $b_1$ and $b_2$ and use linearity.
This is the change of basis formula in action, and the [[change of basis formula|0MQXVZEBMT]] turns it into a product of three matrices.
Watch out: the columns of $A$ are not the images themselves when the basis is not standard, since column 2 stands for $2 b_1 + b_2 = (2, 3)$ and not for $(2, 1)$.
