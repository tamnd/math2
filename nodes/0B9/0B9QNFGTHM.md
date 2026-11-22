---
tag: 0B9QNFGTHM
kind: example
name: Rotation matrix
msc: [15B10]
topics: [AZS5BPF5H3]
audience: ug1
instance_of: [0CGYNDCWRR]
uses: [0QRBVFJ50X, 0CGYNDCWRR]
sources:
  - url: https://en.wikipedia.org/wiki/Rotation_matrix
    locator: In two dimensions
same_as:
  wikidata: Q1256564
  wikipedia: Rotation matrix
---

## Example

A rotation of the plane about the origin is a linear map, and its matrix has a fixed shape built from the cosine and the sine of the angle.
Every element of the special orthogonal group $SO(2)$ has this shape.

Let $\theta \in \mathbb{R}$.
The *rotation matrix* of angle $\theta$ is
$$R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}.$$
The map $x \mapsto R(\theta) x$ turns the plane $\mathbb{R}^2$ about the origin by the angle $\theta$, counterclockwise.
For $\theta = 90$ degrees the matrix is $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, and it sends $(3, 1)$ to $(-1, 3)$.
Check: both vectors have length $\sqrt{10}$, and their dot product is $-3 + 3 = 0$, so the vector turned by a right angle.

We check that $R(\theta)$ is an element of the [[special orthogonal group|0CGYNDCWRR]] $SO(2)$.

1. Each column has length $1$, because $\cos^2\theta + \sin^2\theta = 1$.
2. The columns are perpendicular, because $\cos\theta \cdot (-\sin\theta) + \sin\theta \cos\theta = 0$.
3. So $R(\theta)^{\mathsf{T}} R(\theta) = I_2$, and $R(\theta)$ is an [[orthogonal matrix|0QRBVFJ50X]].
4. Its determinant is $\cos\theta \cos\theta - (-\sin\theta) \sin\theta = 1$.

## Remarks

### Where the columns come from

The columns of a matrix are the images of the [[standard basis|0V7ZD6P7RK]] vectors.
Turning $e_1 = (1, 0)$ by $\theta$ gives the point $(\cos\theta, \sin\theta)$ on the unit circle, which is the first column.
The vector $e_2 = (0, 1)$ is $e_1$ turned by $90$ degrees, so its image is the first column turned by $90$ degrees, namely $(-\sin\theta, \cos\theta)$.
So the shape of $R(\theta)$ follows from the definition of cosine and sine, and nothing has to be memorized except the place of the minus sign.

### Angles add

Multiply two rotation matrices and use the addition formulas:
$$R(\alpha) R(\beta) = \begin{pmatrix} \cos\alpha \cos\beta - \sin\alpha \sin\beta & -(\cos\alpha \sin\beta + \sin\alpha \cos\beta) \\ \sin\alpha \cos\beta + \cos\alpha \sin\beta & \cos\alpha \cos\beta - \sin\alpha \sin\beta \end{pmatrix} = R(\alpha + \beta).$$
Check with $\alpha = 30$ degrees and $\beta = 60$ degrees: the product is $R(90^\circ)$, the quarter turn, as worked out in the [[thirty and sixty degree example|V4CZJT5SEG]].
So rotations of the plane commute, and $R(\theta)^{-1} = R(-\theta)$.
Since $\cos(-\theta) = \cos\theta$ and $\sin(-\theta) = -\sin\theta$, this inverse is also the transpose $R(\theta)^{\mathsf{T}}$.

### Complex numbers and eigenvalues

Write a point $(x, y)$ as $z = x + iy$.
Then $R(\theta)$ sends it to $(x\cos\theta - y\sin\theta) + i(x\sin\theta + y\cos\theta)$, which is $e^{i\theta} z$.
So rotation by $\theta$ is multiplication by $e^{i\theta}$, and $R(\theta) \mapsto e^{i\theta}$ matches $SO(2)$ with the [[circle group|04EAFVFTF7]].

The characteristic polynomial is $t^2 - 2\cos\theta \, t + 1$, with the roots $\cos\theta \pm i \sin\theta = e^{\pm i\theta}$.
These are real only when $\sin\theta = 0$, that is for $R(0) = I_2$ and $R(\pi) = -I_2$.
Every other rotation moves every nonzero vector off its own line, so it has no real [[eigenvalue|0BQAA2BK3Q]].

### Rotations of space

In $\mathbb{R}^3$ the rotations about the coordinate axes are built from $R(\theta)$ by adding a row and a column of the identity:
$$R_z(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad R_y(\theta) = \begin{pmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{pmatrix}.$$
The matrix $R_x(\theta)$ puts the block $R(\theta)$ in the last two rows and columns.
In $R_y$ the minus sign moves to the lower row, so that the turn is counterclockwise when seen from the positive $y$-axis.
Unlike the plane case, these rotations do not commute, as the [[basic rotations of space|F1KZ5GE4TC]] show, and the [[rotation matrix concept|HNY4CPEEJA]] treats rotations of $\mathbb{R}^n$ in general.

### What it is not

The matrix $\begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix}$ is orthogonal, but its determinant is $-\cos^2\theta - \sin^2\theta = -1$, so it is a reflection, not a rotation.
The matrix $2 R(\theta)$ turns the plane by $\theta$ and also doubles every length, so it is not orthogonal, and its determinant is $4$.

### Watch out

The direction of the turn depends on the convention.
The matrix $R(\theta)$ turns column vectors counterclockwise, but a row vector multiplied on the right, $x \mapsto x R(\theta)$, turns clockwise.
In the same way, if the coordinate axes turn by $\theta$, then the new coordinates of a fixed point are given by $R(-\theta) = R(\theta)^{\mathsf{T}}$.
A calculator set to degrees and a formula written in radians is the other common slip.

### Try it

First, write $R(60^\circ)$ and turn the point $(2, 0)$.
The matrix is $\frac{1}{2} \begin{pmatrix} 1 & -\sqrt{3} \\ \sqrt{3} & 1 \end{pmatrix}$, and the image is $(1, \sqrt{3})$, again at distance $2$ from the origin.

Second, for which angles $\theta$ is $R(\theta)^3 = I_2$?
Since $R(\theta)^3 = R(3\theta)$, we need $3\theta$ to be a multiple of $360$ degrees, so $\theta$ is $0$, $120$ or $240$ degrees, up to full turns.

## Explanations

### L1 human

Think of a clock hand fixed at the center of the clock face.
When the hand turns, its tip moves on a circle, and its length stays the same.
A rotation matrix is a table of four numbers that does this turn for every point of the plane at once.
Its first column says where the point $(1, 0)$ goes, and its second column says where $(0, 1)$ goes.
For a quarter turn, $(1, 0)$ goes to $(0, 1)$ and $(0, 1)$ goes to $(-1, 0)$, so the matrix is $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.

### L2 human

Here is a typical problem: turn the point $p = (3, 2)$ by $90$ degrees counterclockwise about the center $c = (1, 1)$, not about the origin.
A rotation matrix turns about the origin, so first move the center to the origin:
$$p - c = (2, 1), \qquad R(90^\circ)(2, 1) = (-1, 2), \qquad (-1, 2) + c = (0, 3).$$
So the image is $(0, 3)$.
Check: the distance from $c$ is $\sqrt{4 + 1} = \sqrt{5}$ before and $\sqrt{1 + 4} = \sqrt{5}$ after.
The whole map is $x \mapsto R(\theta)(x - c) + c$, which is not linear when $c \ne 0$, since it does not fix the origin.
This is the typical use of the matrix: move the problem to the origin, turn, and move back.

### L3 human

Let $J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = R(90^\circ)$, so that $J^2 = -I_2$.
The [[matrix exponential|020M04FN1H]] series then splits into even and odd powers, which gives $\exp(\theta J) = \cos\theta \, I_2 + \sin\theta \, J = R(\theta)$.
So $\theta \mapsto R(\theta)$ is the one-parameter group generated by $J$, and the skew-symmetric matrices $tJ$ form the Lie algebra of $SO(2)$.
In $\mathbb{R}^3$ the same idea gives Rodrigues' formula $\exp(\theta K) = I + \sin\theta \, K + (1 - \cos\theta) K^2$ for the rotation about a unit axis $u$, where $K$ is the matrix of $x \mapsto u \times x$.
The map $\theta \mapsto R(\theta)$ from $\mathbb{R}$ onto $SO(2)$ is a homomorphism with kernel $2\pi\mathbb{Z}$, so $SO(2) \cong \mathbb{R} / 2\pi\mathbb{Z}$.
