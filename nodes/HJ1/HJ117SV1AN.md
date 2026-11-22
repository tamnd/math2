---
tag: HJ117SV1AN
kind: example
name: Projections, reflections and shears of the plane
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
instance_of: [0N6960W0BV, 0G0RFPG8HR]
illustrates: [053QVHF6N7]
uses: [0ZND7NQ970, 0B5H4208Z9, 0AYEPBQMAW, 039HF58KQ5, 053QVHF6N7]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Overview
  - book: isbn:9781733146678
---

## Example

We find the [[eigenvectors|0B5H4208Z9]] of three maps of $\mathbb{R}^2$: a projection, a reflection and a shear.
For each one we guess the eigenvectors from the geometry and then check them with the matrix.

*A projection.*

1. Let $P = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$.
   It sends $(x, y)$ to $(x + y, 0)$, so it moves each point along the direction $(1, -1)$ onto the horizontal axis, and $P^2 = P$.
2. Its characteristic polynomial is
$$\det(tI - P) = \det \begin{pmatrix} t - 1 & -1 \\ 0 & t \end{pmatrix} = (t - 1)t.$$
   Check: $\tr P = 1$ and $\det P = 0$ give $t^2 - t$ as well.
3. The points of the axis stay fixed: $P(1, 0) = (1, 0)$, so $(1, 0)$ is an eigenvector for $1$.
4. The direction of the motion is killed: $P(1, -1) = (1 - 1, 0) = (0, 0)$, so $(1, -1)$ is an eigenvector for $0$.

*A reflection.*

5. Let $S = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, the reflection in the line $y = x$.
   Its characteristic polynomial is $\det(tI - S) = t \cdot t - (-1)(-1) = t^2 - 1$, and $\tr S = 0$, $\det S = -1$ agree.
6. The mirror line stays fixed: $S(1, 1) = (1, 1)$, so $(1, 1)$ is an eigenvector for $1$.
7. The perpendicular line is reversed: $S(1, -1) = (-1, 1) = -(1, -1)$, so $(1, -1)$ is an eigenvector for $-1$.

*A shear.*

8. Let $H = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, which sends $(x, y)$ to $(x + y, y)$.
   The matrix $tI - H$ is triangular, so $\det(tI - H) = (t - 1)^2$, and $\tr H = 2$, $\det H = 1$ agree.
9. The only eigenvalue is $1$, and $(H - I)(x, y) = (y, 0)$.
   So the [[eigenspace|0AYEPBQMAW]] $E_1 = \ker(H - I)$ is the horizontal axis, the line spanned by $(1, 0)$.

## Remarks

For the projection, the eigenspace $E_1$ is the image of $P$ and $E_0$ is its kernel.
Every projection has only $0$ and $1$ as possible [[eigenvalues|0ZND7NQ970]]: from $P^2 = P$ and $Pv = \lambda v$ we get $\lambda^2 v = \lambda v$, so $\lambda^2 = \lambda$.
For the reflection, $E_1$ is the mirror line and $E_{-1}$ is the line perpendicular to it.
In the same way, $S^2 = I$ forces $\lambda^2 = 1$, so every reflection has only $1$ and $-1$ as possible eigenvalues.

The projection and the reflection each have two independent eigenvectors, so each has a basis of eigenvectors.
The shear has only one line of eigenvectors, too few for a basis; the [[shear of the plane|HTAWRAC3QE]] studies this defect.
Changing the shear to $\begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$ with $k \ne 0$ gives the same eigenspace, since $(H - I)(x, y) = (ky, 0)$.
Only for $k = 0$, the identity, does every nonzero vector become an eigenvector.

## Explanations

### L1 human

A projection is like a shadow on the floor: points on the floor stay put, and all points on one ray of light land on the same spot.
So the floor directions are eigenvectors for $1$, and the direction of the light is an eigenvector for $0$.
A mirror keeps its own line and reverses the line at a right angle to it.
A shear slides each horizontal row of points sideways by an amount that grows with the height, and only the bottom row of directions keeps its line.

### L2 human

The typical use of these maps is to read eigenvectors from geometry and then confirm them with one matrix product.
That is faster than solving $\det(tI - A) = 0$ and then a linear system.
Watch out with the shear: it looks as if the vertical direction might also be kept, but $H(0, 1) = (1, 1)$, which is not on the vertical axis.
