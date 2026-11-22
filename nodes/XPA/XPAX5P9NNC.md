---
tag: XPAX5P9NNC
kind: example
name: The two quarter-turn rotations are similar
msc: ["15A21"]
topics: [S6559D61BP]
audience: ug1
instance_of: [0E89HQATM8]
uses: [027KDW2K72, 0TWTS88TWN, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_similarity
    locator: lead section
---

## Example

A quarter turn to the left, seen in a mirror, is a quarter turn to the right, and similarity makes this exact.
Over $\mathbb{R}$, let
$$R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad S = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \qquad P = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$$
The matrix $R$ is the rotation by $90$ degrees counterclockwise, $S$ is the rotation by $90$ degrees clockwise, and $P$ is the reflection in the horizontal axis.

1. The reflection undoes itself: $P^2 = I_2$, so $P$ is [[invertible|0TWTS88TWN]] and $P^{-1} = P$.
2. We compute the [[product|076JGP6R3T]] $RP$ entry by entry:
   $$RP = \begin{pmatrix} 0 \cdot 1 + (-1) \cdot 0 & 0 \cdot 0 + (-1)(-1) \\ 1 \cdot 1 + 0 \cdot 0 & 1 \cdot 0 + 0 \cdot (-1) \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.$$
3. Multiplying on the left by $P^{-1} = P$ changes the sign of the second row:
   $$P^{-1}(RP) = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = S.$$
4. So $S = P^{-1}RP$, and $S$ is [[similar|027KDW2K72]] to $R$.
5. The invariants agree, as they must: $\operatorname{tr} R = 0 = \operatorname{tr} S$, and $\det R = 0 \cdot 0 - (-1) \cdot 1 = 1 = 0 \cdot 0 - 1 \cdot (-1) = \det S$.
6. Both characteristic polynomials are $x^2 + 1$, which has no real root, so neither matrix is similar over $\mathbb{R}$ to a diagonal matrix.

## Remarks

The matrix $P$ is the change of basis to $(e_1, -e_2)$.
This basis has the opposite orientation, and in it a counterclockwise turn looks clockwise.

A rotation cannot do the job of $P$.
Rotations of the plane commute with each other, so $Q^{-1}RQ = R \ne S$ for every rotation $Q$.
In fact every invertible real $P$ with $P^{-1}RP = S$ has a negative determinant.
If $P$ and $P'$ both work, then $P^{-1}P'$ commutes with $S$, and the real matrices that commute with $S$ have the form $aI + bS$, with determinant $a^2 + b^2 > 0$.
So $\det P'$ has the sign of $\det P = -1$.

Over $\mathbb{C}$ the picture changes: both matrices have the eigenvalues $i$ and $-i$, so both are similar to $\operatorname{diag}(i, -i)$.

## Explanations

### L1 human

The rotation by a quarter turn to the left looks like a quarter turn to the right in a mirror.
The matrix $P$ is that mirror, the reflection in the horizontal axis.
So the two rotations are the same motion, described from two sides of the mirror.

### L2 human

Similar matrices can look different, here with the signs of the off-diagonal entries exchanged.
The trace $0$ and the determinant $1$ agree, so the invariants give no objection.
In size $2$, the characteristic polynomial $x^2 + 1$ has no real root and so is also the minimal polynomial, and over $\mathbb{R}$ every $2 \times 2$ matrix with this characteristic polynomial is similar to $R$.
Watch out: this does not make all rotations similar, since the rotation by $\theta$ has trace $2\cos\theta$, and two rotations with different traces are not similar.
