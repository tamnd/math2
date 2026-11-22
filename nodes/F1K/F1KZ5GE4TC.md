---
tag: F1KZ5GE4TC
kind: example
name: The basic rotations of space do not commute
msc: ["15B10"]
topics: [AZS5BPF5H3]
audience: ug1
instance_of: [HNY4CPEEJA, 6WBVP2PB1Y]
uses: [GPWRS6HSNR, 0B5H4208Z9]
sources:
  - url: https://en.wikipedia.org/wiki/Rotation_matrix
    locator: Basic 3D rotations
---

## Example

Let $R_x(\theta)$ and $R_z(\theta)$ be the basic [[rotation matrices|HNY4CPEEJA]] of $\R^3$ about the $x$-axis and the $z$-axis.
With $c = \cos\theta$ and $s = \sin\theta$ they are
$$R_x(\theta) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & c & -s \\ 0 & s & c \end{pmatrix}, \qquad R_z(\theta) = \begin{pmatrix} c & -s & 0 \\ s & c & 0 \\ 0 & 0 & 1 \end{pmatrix}.$$
We compare the two products of the quarter turns $R_z(\pi/2)$ and $R_x(\pi/2)$.

1. For $\theta = \frac{\pi}{2}$ we have $c = 0$ and $s = 1$, so
$$R_z(\pi/2) = \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad R_x(\pi/2) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix}.$$
2. Multiply row by column. Row $1$ of $R_z(\pi/2)$ is $(0, -1, 0)$, so row $1$ of the product is minus row $2$ of $R_x(\pi/2)$, which is $(0, 0, 1)$. The other rows work the same way:
$$A = R_z(\pi/2) R_x(\pi/2) = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}.$$
3. In the other order, row $1$ of $R_x(\pi/2)$ is $(1, 0, 0)$, so row $1$ of the product is row $1$ of $R_z(\pi/2)$:
$$B = R_x(\pi/2) R_z(\pi/2) = \begin{pmatrix} 0 & -1 & 0 \\ 0 & 0 & -1 \\ 1 & 0 & 0 \end{pmatrix}.$$
4. The $(1, 3)$ entries are $1$ and $0$, so $A \ne B$, and the two basic rotations do not commute.
5. To find the axis of $A$, look for a fixed vector: $A(1, 1, 1) = (1, 1, 1)$, so the axis of $A$ is the line through $(1, 1, 1)$.
6. For $B$, the vector $(1, -1, 1)$ is fixed:
$$B \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \cdot 1 + (-1)(-1) + 0 \cdot 1 \\ 0 \cdot 1 + 0 \cdot (-1) + (-1) \cdot 1 \\ 1 \cdot 1 + 0 + 0 \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}.$$
So the axis of $B$ is the line through $(1, -1, 1)$.
7. Both traces are $0$. By [[Euler's rotation theorem|2ZVG43GSKA]] the trace is $1 + 2\cos\theta$, so $\cos\theta = -\frac{1}{2}$, and both products turn by $\frac{2\pi}{3}$.

Check: each basic rotation has orthonormal columns, and its determinant is $\cos^2\theta + \sin^2\theta = 1$, by expansion along the row of the fixed axis.

## Remarks

The example shows that the rotations of space do not form a commutative group, unlike the rotations of the plane.
The two products have the same angle but different axes.
A rotation by the same angle about another axis is a conjugate, so $A$ and $B$ are conjugate in $SO(3)$.

The product $A$ is the [[cyclic permutation matrix|E6SGA0X325]], which sends $e_1 \mapsto e_2 \mapsto e_3 \mapsto e_1$.
If we replace both angles by $\pi$, the products are $R_z(\pi) R_x(\pi) = \operatorname{diag}(-1, -1, 1) \operatorname{diag}(1, -1, -1) = \operatorname{diag}(-1, 1, -1)$ in both orders, so half turns about perpendicular axes do commute.
So the failure depends on the angles, not only on the axes.
Because of all this, a list of turns about axes, such as the [[Euler angles|YRSV2AASVB]], must always state the order of the factors.

## Explanations

### L1 human

Hold a book flat in front of you.
Give it a quarter turn about a line pointing up, and then a quarter turn about a line pointing at you.
Now start again and do the two turns in the other order.
The book ends in two different positions.
The matrices show the same thing: the two products are different matrices.

### L2 human

Here is the typical use: whenever you combine turns of space, as in a robot arm or a camera, keep the order of the factors.
The matrix $R_z R_x$ means "first turn about $x$, then about $z$", because the factor on the right acts first on a column vector.
Watch out: in $R_y(\theta)$ the entry $-\sin\theta$ is in the third row, not the first, so do not copy the sign pattern of $R_x$ and $R_z$ to $R_y$.
