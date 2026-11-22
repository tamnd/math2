---
tag: HNY4CPEEJA
kind: concept
name: Rotation matrix
aliases: [plane-rotation-matrix, basic-rotation-matrices]
msc: ["15B10"]
topics: [AZS5BPF5H3]
audience: school
specializes: [0W02QESPJQ]
uses: [GPWRS6HSNR, 0QRBVFJ50X]
sources:
  - url: https://en.wikipedia.org/wiki/Rotation_matrix
    locator: In two dimensions
  - url: https://en.wikipedia.org/wiki/Rotation_matrix
    locator: Basic 3D rotations
  - url: https://en.wikipedia.org/wiki/Rotation_matrix
    locator: In three dimensions
---

## Summary

A rotation matrix turns every vector about the origin by the same angle, so it moves a figure without a change of size or shape and without a mirror image.
In the plane the turn by the angle $\theta$, counterclockwise, has the matrix
$$R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}.$$
In general, a *rotation matrix* is a real square matrix $R$ with $R^{\mathsf{T}} R = I$ and $\det R = 1$, that is, an element of the [[special orthogonal group|6WBVP2PB1Y]].
Every $2 \times 2$ rotation matrix is $R(\theta)$ for some $\theta$, and every $3 \times 3$ rotation matrix turns space about some axis.

## Motivation

Computer graphics, robotics, navigation and physics all need to turn objects and to change from one coordinate frame to another.
A turn about the origin is a linear map, so it has a matrix, and to turn a point we multiply its coordinate column by that matrix.
To do two turns, one after the other, we multiply the two matrices.
So all the arithmetic of turns becomes matrix arithmetic, and a computer can do it fast for many points at once.

The plane gives the first lesson: turns by $\theta$ and by $\varphi$ combine to a turn by $\theta + \varphi$.
Space gives the second lesson: turns about different axes do not commute.
Both facts return in the [[classification of O(2)|C97Z06HHB2]] and in [[Euler's rotation theorem|2ZVG43GSKA]].

## Notation

The plane rotation is written $R(\theta)$ or $R_\theta$.
Its columns are the images of the basis vectors: $e_1$ goes to $(\cos\theta, \sin\theta)$ and $e_2$ goes to $(-\sin\theta, \cos\theta)$.
In space, the *basic rotations* turn about the coordinate axes:
$$R_x(\theta) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{pmatrix}, \quad R_y(\theta) = \begin{pmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{pmatrix}, \quad R_z(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}.$$
Each one is counterclockwise when the axis points toward the viewer, which is the right-hand rule.
Some books call every orthogonal matrix an "orthogonal transformation", and others use that phrase only for rotations, so check which meaning a book uses.

## Remarks

### A first turn

Take the quarter turn, $\theta = \frac{\pi}{2}$, where $\cos\theta = 0$ and $\sin\theta = 1$:
$$R\left(\tfrac{\pi}{2}\right) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}.$$
It sends $e_1 = (1, 0)$ to $(0, 1)$ and $e_2 = (0, 1)$ to $(-1, 0)$.
For the point $(3, 4)$ we multiply:
$$R\left(\tfrac{\pi}{2}\right) \begin{pmatrix} 3 \\ 4 \end{pmatrix} = \begin{pmatrix} 0 \cdot 3 - 1 \cdot 4 \\ 1 \cdot 3 + 0 \cdot 4 \end{pmatrix} = \begin{pmatrix} -4 \\ 3 \end{pmatrix}.$$
Check: both points have length $5$, and $(3, 4) \cdot (-4, 3) = -12 + 12 = 0$, so the turn is a right angle.
The half turn $R(\pi) = -I_2$ sends every point $v$ to $-v$.

### Turns add up

Two turns of the plane combine by adding their angles:
$$R(\theta) R(\varphi) = R(\theta + \varphi).$$
The entries of the product are $\cos\theta\cos\varphi - \sin\theta\sin\varphi = \cos(\theta + \varphi)$ and $\sin\theta\cos\varphi + \cos\theta\sin\varphi = \sin(\theta + \varphi)$, which are the addition formulas.
The [[turns by 30 and 60 degrees|V4CZJT5SEG]] work this out with numbers and get the quarter turn.
Since $\theta + \varphi = \varphi + \theta$, plane rotations commute, and $R(\theta)^{-1} = R(-\theta) = R(\theta)^{\mathsf{T}}$.

### Turns of space

In space, the order matters.
The [[two products of R_z and R_x|F1KZ5GE4TC]] by quarter turns give two different matrices, with axes through $(1, 1, 1)$ and $(1, -1, 1)$.
Every $3 \times 3$ rotation matrix turns space by an angle $\theta$ about an axis, and its trace is $1 + 2\cos\theta$, by [[Euler's rotation theorem|2ZVG43GSKA]].
For example, the [[cyclic permutation matrix|E6SGA0X325]] has trace $0$, so $\cos\theta = -\frac{1}{2}$ and it turns by $\frac{2\pi}{3}$ about the axis through $(1, 1, 1)$.
Every rotation of space is also a product of three basic rotations, given by its [[Euler angles|YRSV2AASVB]].

### What it is not

The [[coordinate swap|27TY1G77KM]] $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is orthogonal, but its determinant is $-1$, so it is the mirror image in the line $y = x$, not a turn.
The matrix $2R(\theta)$ turns by $\theta$, but its columns have length $2$, so it doubles lengths and is not orthogonal.
The matrix $\begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ with $\sin\theta \ne 0$ is never a rotation.
If $\cos\theta \ne 0$, its columns have dot product $2\sin\theta\cos\theta \ne 0$, so they are not orthogonal.
If $\cos\theta = 0$, it is $\pm$ the coordinate swap, which has determinant $-1$.

### Watch out

The sign of $\sin\theta$ decides the direction.
In $R(\theta)$ the entry $-\sin\theta$ is in the first row, and the transpose $R(-\theta)$ turns the other way.
In $R_y(\theta)$ the entry $-\sin\theta$ is in the third row, unlike in $R_x$ and $R_z$, and this keeps the right-hand rule for the $y$-axis.
Some books turn the coordinate frame instead of the point, and then the matrix of the same turn is the transpose.
Finally, most formulas use radians: $\cos 90 \ne 0$, while $\cos \frac{\pi}{2} = 0$.

### Try it

First, turn the point $(1, 0)$ by $60$ degrees.
Since $\cos 60^\circ = \frac{1}{2}$ and $\sin 60^\circ = \frac{\sqrt{3}}{2}$, the image is the first column of $R(\pi/3)$, the point $\left(\frac{1}{2}, \frac{\sqrt{3}}{2}\right)$.

Second, decide whether $A = \frac{1}{5} \begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}$ is a rotation matrix, and find its angle.
It has the form $R(\theta)$ with $\cos\theta = \frac{3}{5}$ and $\sin\theta = \frac{4}{5}$, and $\det A = \frac{9 + 16}{25} = 1$, so it is the turn by about $53.13$ degrees.

## Explanations

### L1 human

A rotation matrix turns a picture about the origin without stretching it and without flipping it.
In the plane, one angle describes the turn.
To turn the point $(x, y)$ by $\theta$, compute the new point $(x\cos\theta - y\sin\theta, \ x\sin\theta + y\cos\theta)$.
For example, a quarter turn has $\cos\theta = 0$ and $\sin\theta = 1$, so it sends $(1, 0)$ to $(0, 1)$ and $(2, 1)$ to $(-1, 2)$.
A turn by $30$ degrees followed by a turn by $60$ degrees is a turn by $90$ degrees.

### L2 human

Here is a typical task: turn the triangle with corners $(1, 0)$, $(2, 0)$ and $(2, 1)$ by a quarter turn.
Put the corners as the columns of one matrix and multiply once:
$$\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 2 & 2 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 & -1 \\ 1 & 2 & 2 \end{pmatrix}.$$
So the new corners are $(0, 1)$, $(0, 2)$ and $(-1, 2)$.
Check: the side from $(2, 0)$ to $(2, 1)$ had length $1$, and the side from $(0, 2)$ to $(-1, 2)$ also has length $1$.
One matrix product turns any number of points, and that is why graphics programs store turns as matrices.
Watch out: to turn about a point other than the origin, first move that point to the origin, then turn, and then move back, since a rotation matrix always fixes $0$.

### L3 human

The $2 \times 2$ rotation matrices form $SO(2)$, a copy of the circle group, and $R(\theta) = \exp \begin{pmatrix} 0 & -\theta \\ \theta & 0 \end{pmatrix}$.
The $3 \times 3$ rotation matrices form $SO(3)$, a compact Lie group of dimension $3$, and each of them is the exponential of a skew-symmetric matrix, by [[Rodrigues' rotation formula|WS52X8SGC4]].
For general $n$, a rotation matrix is a product of turns in perpendicular planes, by the [[normal form of an orthogonal matrix|QTY3VMFGY1]].
In numerical linear algebra, the Givens rotations are rotation matrices that act in one coordinate plane, and they are used to create zeros in a matrix one entry at a time.
