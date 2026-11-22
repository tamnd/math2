---
tag: EKK87GQF5W
kind: example
name: The half turn of space is an involution but not a reflection
msc: ["15A04", "15B10"]
topics: [AZS5BPF5H3]
audience: ug2
instance_of: [6WBVP2PB1Y]
not_instance_of:
  - target: 06BRDF3F0E
    note: the matrix diag(-1, -1, 1) squares to the identity but has determinant 1 and fixes only a line
uses: [025158VEYZ, GPWRS6HSNR, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Reflection_(mathematics)
    locator: Reflection through a hyperplane in n dimensions
  - url: https://en.wikipedia.org/wiki/Rotation_matrix
    locator: Basic 3D rotations
---

## Example

Let $Q = \operatorname{diag}(-1, -1, 1)$.
We show that $Q$ is orthogonal with $Q^2 = I_3$, like a reflection, but that $Q$ is a rotation and not a [[reflection|025158VEYZ]].

1. The columns $-e_1$, $-e_2$ and $e_3$ are orthonormal, so $Q$ is orthogonal.
2. Squaring the diagonal entries gives $Q^2 = \operatorname{diag}(1, 1, 1) = I_3$.
3. The [[determinant|0C3CFHDN6R]] is $(-1)(-1)(1) = 1$. A reflection has determinant $-1$, so $Q$ is not a reflection.
4. A second check uses fixed vectors. A reflection of $\R^3$ fixes a whole plane, but $Qx = x$ means $(-x_1, -x_2, x_3) = (x_1, x_2, x_3)$, so $x_1 = x_2 = 0$, and $Q$ fixes only the $z$-axis.
5. The basic rotation about the $z$-axis by the angle $\pi$ is
$$R_z(\pi) = \begin{pmatrix} \cos\pi & -\sin\pi & 0 \\ \sin\pi & \cos\pi & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} -1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = Q,$$
so $Q$ is in the [[special orthogonal group|6WBVP2PB1Y]] $SO(3)$.
6. With $s_{e_1} = \operatorname{diag}(-1, 1, 1)$ and $s_{e_2} = \operatorname{diag}(1, -1, 1)$, the product of diagonal matrices gives $Q = s_{e_1} s_{e_2}$, a product of two reflections.

## Remarks

The example shows that the condition $Q^2 = I$ does not make an orthogonal matrix a reflection.
An orthogonal $Q$ with $Q^2 = I$ satisfies $Q^{\mathsf{T}} = Q^{-1} = Q$, so it is symmetric with eigenvalues $1$ and $-1$ and orthogonal eigenspaces.
In $\R^3$ the possible dimensions of the $-1$ eigenspace are $0$, $1$, $2$ and $3$, and they give the identity, the reflections, the half turns and $-I_3$.
So the half turn is the case where the matrix negates a plane, and a reflection negates only a line.

In the language of subspaces, $Q = 2P_W - I_3$, where $P_W = \operatorname{diag}(0, 0, 1)$ is the orthogonal projection onto the $z$-axis $W$.
Some books call this the reflection in the line $W$, but $W$ is not a hyperplane.
The half turn about the line through a unit vector $a$ is $2 a a^{\mathsf{T}} - I_3$, and $a = e_3$ gives $Q$ back.

## Explanations

### L1 human

This matrix turns space by half a turn about the vertical axis.
Doing it twice brings every point back, which is also true of a mirror.
But a half turn does not change a right hand into a left hand, so it is a rotation and not a mirror image.

### L2 human

The typical test of whether an orthogonal involution is a reflection is to count the eigenvalues equal to $-1$.
A reflection has exactly one, and $Q$ has two, the entries in positions $(1, 1)$ and $(2, 2)$.
The determinant gives the same answer in one step, because it is $(-1)^k$ when $k$ eigenvalues are $-1$.
Watch out: in the plane the matrix $\operatorname{diag}(-1, -1)$ is also a half turn, and it fixes only the origin.
