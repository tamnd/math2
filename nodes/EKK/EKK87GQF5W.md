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
We show that $Q$ is orthogonal with $Q^2 = I_3$, but it is not a [[reflection|025158VEYZ]].

1. The columns $-e_1$, $-e_2$ and $e_3$ are orthonormal, so $Q$ is orthogonal.
2. $Q^2 = \operatorname{diag}(1, 1, 1) = I_3$.
3. $\det Q = (-1)(-1)(1) = 1$. A reflection has [[determinant|0C3CFHDN6R]] $-1$, so $Q$ is not a reflection.
4. A second check: a reflection of $\R^3$ fixes a plane. The fixed vectors of $Q$ are the solutions of $Qx = x$, which are the multiples of $e_3$. This is a line, not a plane.
5. $Q = R_z(\pi)$, the basic rotation by $\pi$ about the $z$-axis, because $\cos\pi = -1$ and $\sin\pi = 0$. So $Q$ is in the [[special orthogonal group|6WBVP2PB1Y]] $SO(3)$.
6. $Q = s_{e_1}s_{e_2}$, where $s_{e_1} = \operatorname{diag}(-1, 1, 1)$ and $s_{e_2} = \operatorname{diag}(1, -1, 1)$. So $Q$ is a product of two reflections.

## Remarks

- $Q$ is the reflection $2P_W - \id$ in the $z$-axis $W$, in the general sense of a subspace. But $W$ is not a hyperplane.
- In $\R^3$, the orthogonal involutions are $I$, the reflections, the half turns and $-I$. They negate a subspace of dimension $0$, $1$, $2$ and $3$.
- The half turn about the axis through a unit vector $a$ is $2aa^T - I_3$. For $a = e_3$, this gives $Q$.

## Explanations

### L1 human

This matrix turns space by half a turn about the vertical axis.
Doing it twice gives the identity, like a reflection.
But it does not turn a right hand into a left hand, so it is a rotation and not a mirror image.

### L2 human

The worked check is in the Example.
The typical use: to test whether an orthogonal involution is a reflection, count the eigenvalues $-1$.
A reflection has exactly one.
A trap: the condition $Q^2 = I$ alone does not make $Q$ a reflection.
