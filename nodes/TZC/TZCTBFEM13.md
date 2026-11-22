---
tag: TZCTBFEM13
kind: example
name: A rotation about an axis in R³ as a block diagonal matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [001T5FJDC1]
uses: [0M0SNKZ482, WR3RCF5PSQ, 0ACX5QT8TE]
sources:
  - url: https://en.wikipedia.org/wiki/Rotation_matrix
    locator: Basic 3D rotations
---

## Example

A rotation of space about the vertical axis is a plane rotation glued to the identity on the axis, and its matrix shows this as two diagonal blocks.
Let
$$R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}, \qquad M_\theta = \operatorname{diag}(R_\theta, 1) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}.$$

1. For $x = (x_1, x_2, x_3)$ the product is
$$M_\theta x = (x_1 \cos\theta - x_2 \sin\theta,\ x_1 \sin\theta + x_2 \cos\theta,\ x_3).$$
2. So $M_\theta$ turns the part $(x_1, x_2)$ by the angle $\theta$ and keeps $x_3$, which makes it the rotation about the $x_3$-axis.
3. The $x_1 x_2$-plane and the $x_3$-axis are [[invariant subspaces|0ACX5QT8TE]] of $M_\theta$, because the zero blocks say that neither part leaks into the other.
4. The [[block rule|WR3RCF5PSQ]] multiplies block by block, $M_\theta M_\varphi = \operatorname{diag}(R_\theta R_\varphi, 1)$.
5. The top left entry of $R_\theta R_\varphi$ is $\cos\theta \cos\varphi - \sin\theta \sin\varphi = \cos(\theta + \varphi)$, and the other entries follow from the addition formulas in the same way, so $R_\theta R_\varphi = R_{\theta + \varphi}$ and
$$M_\theta M_\varphi = \operatorname{diag}(R_{\theta + \varphi}, 1) = M_{\theta + \varphi}.$$
6. With $\theta = \pi/2$ the matrix is
$$M_{\pi/2} = \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix},$$
which sends $e_1$ to $e_2$, $e_2$ to $-e_1$ and $e_3$ to $e_3$.
7. Check step 5 with numbers: $M_{\pi/2}^2 = \operatorname{diag}(R_\pi, 1) = \operatorname{diag}(-1, -1, 1)$, the half turn about the $x_3$-axis.

## Remarks

### Every rotation looks like this

Every rotation of $\mathbb{R}^3$ fixes a line, its axis, and turns the plane orthogonal to the axis.
In an orthonormal basis whose third vector lies on the axis, its matrix is $\operatorname{diag}(R_\varphi, 1)$ for some angle $\varphi$.
This is a first normal form found by choosing a basis adapted to invariant subspaces.

### Watch out

The block form depends on the basis.
The cyclic permutation matrix
$$P = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}$$
is orthogonal with determinant $1$ and fixes $(1, 1, 1)$, so it is a rotation of order $3$ about that axis.
In the standard basis it sends $e_1 \mapsto e_2 \mapsto e_3 \mapsto e_1$, so no consecutive group of coordinates is kept, and $P$ is not block diagonal for any partition with two or more blocks.
In an orthonormal basis with third vector $(1, 1, 1)/\sqrt{3}$ it becomes $\operatorname{diag}(R_\varphi, 1)$ with $\varphi = \pm 2\pi/3$.

## Explanations

### L1 human

A turn about a vertical axis moves points around in the horizontal plane and keeps their height.
The matrix shows this with a $2 \times 2$ turning block for the plane and a $1$ for the height.
Doing two turns one after the other adds the angles, and the height stays the same.

### L2 human

Steps 4 and 5 reduce the addition of angles in space to the addition of angles in the plane.
The zero blocks say that the plane and the axis do not interact, so a product, a power or an inverse of $M_\theta$ can be computed on the plane alone.
For example, $M_\theta^{-1} = \operatorname{diag}(R_{-\theta}, 1) = M_{-\theta}$, since $R_\theta R_{-\theta} = R_0 = I_2$.
