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

Let $R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ and
$$M_\theta = \operatorname{diag}(R_\theta, 1) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}.$$

1. For $x = (x_1, x_2, x_3)$, $M_\theta x = (x_1 \cos\theta - x_2 \sin\theta,\ x_1 \sin\theta + x_2 \cos\theta,\ x_3)$.
2. So $M_\theta$ turns the $(x_1, x_2)$ part by the angle $\theta$ and keeps $x_3$. It is the rotation about the $x_3$-axis.
3. The $x_1 x_2$-plane and the $x_3$-axis are [[invariant subspaces|0ACX5QT8TE]] of $M_\theta$.
4. By the [[block rule|WR3RCF5PSQ]], $M_\theta M_\varphi = \operatorname{diag}(R_\theta R_\varphi, 1) = \operatorname{diag}(R_{\theta + \varphi}, 1) = M_{\theta + \varphi}$.
5. With $\theta = \pi/2$: $M_{\pi/2} = \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ sends $e_1$ to $e_2$, $e_2$ to $-e_1$ and $e_3$ to $e_3$.

## Remarks

Every rotation of $\mathbb{R}^3$ has this form in an orthonormal basis whose third vector is on the axis.
This is a first example of a normal form found by choosing a basis adapted to invariant subspaces.

## Explanations

### L1 human

A turn about a vertical axis moves points around in the horizontal plane and keeps their height.
The matrix shows this: a $2 \times 2$ turn block for the plane and a $1$ for the height.

### L2 human

Step 4 reduces the addition of angles in space to the addition of angles in the plane.
The zero blocks say that the plane and the axis do not interact.
