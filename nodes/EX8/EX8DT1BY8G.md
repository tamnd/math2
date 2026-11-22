---
tag: EX8DT1BY8G
kind: example
name: A singular matrix is not a change of basis matrix
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
not_instance_of:
  - target: 0MKRHZB3WS
    note: the columns (1, 2) and (2, 4) are not a basis of the plane, so the matrix does not change coordinates between two bases
uses: [0KWXYZPJKN, 0VTQTPQGAV, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Change_of_basis
    locator: Change-of-basis formula
---

## Example

A square matrix with dependent columns cannot translate between two coordinate systems.
Let $M = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ over $\mathbb{R}$, and try to read its columns as a new basis $b'_1 = (1, 2)$, $b'_2 = (2, 4)$ of $\mathbb{R}^2$.

1. The second column is twice the first, $b'_2 = 2 b'_1$, so the two vectors are linearly dependent.
   They are not a [[basis|0VTQTPQGAV]] of $\mathbb{R}^2$.
2. The [[determinant|0C3CFHDN6R]] confirms this: $\det M = 1 \cdot 4 - 2 \cdot 2 = 0$, so $M$ is not invertible.
3. Some vectors get no coordinates at all.
   A combination $s(1, 2) + t(2, 4) = (s + 2t, 2s + 4t)$ always has second entry twice the first, and $(1, 0)$ does not, so $(1, 0)$ is not a combination of $b'_1$ and $b'_2$.
4. Other vectors get more than one set of coordinates.
   The vector $(2, 4)$ equals $2 b'_1 + 0 b'_2$ and also $0 b'_1 + 1 b'_2$.
5. So $M$ is not the [[change of basis matrix|0KWXYZPJKN]] between any two bases of $\mathbb{R}^2$.

## Remarks

The example isolates the one condition that a square matrix must meet.
A square matrix $P$ is a change of basis matrix exactly when it is invertible, because its columns are then a basis, and they can serve as the new basis.
If we change the entry $4$ to $5$, the determinant becomes $5 - 4 = 1$, the columns $(1, 2)$ and $(2, 5)$ form a basis, and the new matrix is a change of basis matrix.

The direction of a change of basis matrix depends on the book, but this does not matter here.
Every convention uses either $P$ or $P^{-1}$, and both are invertible.

## Explanations

### L1 human

A change of basis matrix must have independent columns, because its columns are the new basis vectors.
Here the second column is twice the first, so both new vectors point along the same line.
Two arrows on one line cannot reach every point of the plane.

### L2 human

The fastest test is the determinant: $\det M = 0$, so $M$ is singular.
A singular matrix sends some nonzero vector to $0$, here $M(2, -1) = (2 - 2, 4 - 4) = (0, 0)$.
So the two different coordinate lists $(2, -1)$ and $(0, 0)$ would describe the same vector, and coordinates would not be unique.
