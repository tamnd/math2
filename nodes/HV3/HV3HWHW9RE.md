---
tag: HV3HWHW9RE
kind: example
name: The signed permutation matrices of size two
msc: ["15B10", "20G20"]
topics: [AZS5BPF5H3]
audience: ug2
instance_of: [0JZ27DMJ5D, 0X1JXT47GA]
illustrates: [WWK2E8BRGF]
uses: [0QRBVFJ50X, 0Q5SM60HTH, 0N0PXCTYA7, 09GK3DE0WV]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_group
    locator: Discrete subgroups
  - url: https://en.wikipedia.org/wiki/Dihedral_group
    locator: lead section
---

## Example

Let $G$ be the set of the eight real $2 \times 2$ matrices
$$\begin{pmatrix} \pm 1 & 0 \\ 0 & \pm 1 \end{pmatrix} \quad \text{and} \quad \begin{pmatrix} 0 & \pm 1 \\ \pm 1 & 0 \end{pmatrix},$$
with all choices of signs.
We check that $G$ is a [[subgroup|0N0PXCTYA7]] of the [[orthogonal group|WWK2E8BRGF]] $O(2)$, and that it is the symmetry group of a square.

1. Each matrix in $G$ has columns $\pm e_1$ and $\pm e_2$ in some order. These columns are orthonormal, so each matrix is [[orthogonal|0QRBVFJ50X]].
2. The matrices in $G$ are exactly the orthogonal matrices that send each of $\pm e_1, \pm e_2$ to one of $\pm e_1, \pm e_2$. A product of two such matrices has the same property, so $G$ is closed under products.
3. The identity $I_2$ is in $G$, and so is the inverse $Q^{-1} = Q^T$ of each $Q \in G$, because the transpose has the same pattern of zeros and signs.
4. So $G$ is a subgroup of $O(2)$ of order $8$.
5. The four matrices with determinant $1$ are $I$, $-I$, $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ and $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, the rotations by $0$, $\pi$, $\pi/2$ and $-\pi/2$.
6. The four matrices with determinant $-1$ are $\operatorname{diag}(1, -1)$, $\operatorname{diag}(-1, 1)$, $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ and $\begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$, the reflections in the lines $y = 0$, $x = 0$, $y = x$ and $y = -x$.
7. Each matrix of $G$ permutes the four points $(\pm 1, \pm 1)$, the corners of a square. A square has exactly $8$ symmetries that fix its center, so $G$ is its whole symmetry group, the [[dihedral group|09GK3DE0WV]] of order $8$.

## Remarks

The example shows a finite subgroup of $O(2)$ that contains both rotations and reflections.
Its four rotations form the cyclic subgroup $G \cap SO(2)$ of order $4$, and that subgroup has index $2$ in $G$, just as $SO(2)$ has index $2$ in $O(2)$.

The construction works in every size.
The $n \times n$ signed permutation matrices form a subgroup of $O(n)$ of order $2^n n!$, since there are $n!$ ways to place the nonzero entries and $2^n$ choices of signs.
For $n = 3$ this gives $8 \cdot 6 = 48$ matrices, the full symmetry group of the cube with corners $(\pm 1, \pm 1, \pm 1)$.
If an entry $\pm 1$ is replaced by any other nonzero number, the matrix is no longer orthogonal.

## Explanations

### L1 human

Put a square with its center at the origin and its sides parallel to the axes.
There are eight ways to move the square onto itself.
Four of them are turns: by nothing, a quarter turn, a half turn and three quarter turns.
The other four are mirror images: in the two axes and in the two diagonals.
Each way is one of the eight matrices.

### L2 human

Here is one product in each order, to see that the group is not commutative.
Take the quarter turn $A$ and the reflection $B$ in the $x$-axis:
$$A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \quad AB = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad BA = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}.$$
So $AB$ is the reflection in the line $y = x$ and $BA$ is the reflection in $y = -x$.
Check: $\det(AB) = \det A \det B = 1 \cdot (-1) = -1$, as it must be for a reflection.
Finite symmetry groups of figures are subgroups of $O(n)$ in the same way.
Watch out: $AB \ne BA$, so the order of the moves matters.
