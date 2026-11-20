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

A *rotation matrix* is a real square matrix $R$ with $R^TR = I$ and $\det R = 1$, an element of the [[special orthogonal group|6WBVP2PB1Y]].
In the plane, the rotation by the angle $\theta$ counterclockwise about the origin has the matrix
$$R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix},$$
and every $2 \times 2$ rotation matrix has this form.
In space, the *basic rotations* $R_x(\theta)$, $R_y(\theta)$ and $R_z(\theta)$ turn about the coordinate axes, and every $3 \times 3$ rotation matrix turns space about some axis.

## Motivation

Computer graphics, robotics and physics must turn objects and change coordinate frames.
A rotation about the origin is a linear map, so it has a matrix.
To turn a point, multiply its coordinate column by this matrix.
To do two turns one after the other, multiply their matrices.

## Notation

- The plane rotation is written $R(\theta)$ or $R_\theta$. Its columns are the images $(\cos\theta, \sin\theta)$ of $e_1$ and $(-\sin\theta, \cos\theta)$ of $e_2$.
- The basic rotations of space are
$$R_x(\theta) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{pmatrix}, \quad R_y(\theta) = \begin{pmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{pmatrix}, \quad R_z(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}.$$
- Each basic rotation is counterclockwise when the axis points toward the viewer, by the right-hand rule.

## Remarks

### Examples

- $R(\pi/2) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ sends $e_1$ to $e_2$ and $e_2$ to $-e_1$.
- [[The rotations by π/6 and π/3 compose to a quarter turn|V4CZJT5SEG]], because $R(\theta)R(\varphi) = R(\theta + \varphi)$.
- [[The basic rotations of space do not commute|F1KZ5GE4TC]]: $R_z(\pi/2)R_x(\pi/2) \neq R_x(\pi/2)R_z(\pi/2)$.
- $R(\pi) = -I_2$ is the half turn of the plane.
- [[The rotation by sixty degrees about the diagonal|TFWTJ9K6K7]] is a $3 \times 3$ rotation matrix that is not a basic rotation.

### Non-examples

- [[The swap matrix with rows (0, 1) and (1, 0)|27TY1G77KM]] is orthogonal, but its determinant is $-1$. It is a reflection, not a rotation.
- The matrix $2R(\theta)$ turns by $\theta$, but it also doubles lengths. Its columns have length $2$, so it is not orthogonal.
- The matrix $\begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ is not a rotation for $\sin\theta \neq 0$: its columns are not orthogonal.

### Basic properties

- $R(\theta)R(\varphi) = R(\theta + \varphi)$, by the addition formulas for $\cos$ and $\sin$. So plane rotations commute.
- $R(\theta)^{-1} = R(-\theta) = R(\theta)^T$.
- $\tr R(\theta) = 2\cos\theta$, and the eigenvalues of $R(\theta)$ are $e^{i\theta}$ and $e^{-i\theta}$.
- A $3 \times 3$ rotation matrix by the angle $\theta$ has trace $1 + 2\cos\theta$, see [[Euler's rotation theorem|2ZVG43GSKA]].
- Each $3 \times 3$ rotation matrix is a product of basic rotations, for example by the [[Euler angles|YRSV2AASVB]].

### Common errors

- The sign of $\sin\theta$: in $R(\theta)$, the entry $-\sin\theta$ is in the first row. The transpose $R(-\theta)$ turns the other way.
- In $R_y(\theta)$, the sign pattern differs from $R_x$ and $R_z$: the entry $-\sin\theta$ is in the third row. This keeps the right-hand rule.
- Rotations of space do not commute, so the order of the factors matters.
- Some books turn the frame and not the point. Then the matrix of the same turn is the transpose.

## Explanations

### L1 human

A rotation matrix turns a picture about the origin without stretching it.
In the plane, one angle is enough to describe the turn.
To turn the point $(x, y)$ by $\theta$, compute $(x\cos\theta - y\sin\theta, \ x\sin\theta + y\cos\theta)$.
For example, a quarter turn sends $(1, 0)$ to $(0, 1)$.

### L2 human

Worked example: we turn the point $(2, 1)$ by $\theta = \frac{\pi}{2}$.

1. $R(\pi/2) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, because $\cos\frac{\pi}{2} = 0$ and $\sin\frac{\pi}{2} = 1$.
2. $R(\pi/2)\begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \cdot 2 - 1 \cdot 1 \\ 1 \cdot 2 + 0 \cdot 1 \end{pmatrix} = \begin{pmatrix} -1 \\ 2 \end{pmatrix}$.
3. The lengths agree: $\norm{(2, 1)} = \sqrt{5} = \norm{(-1, 2)}$.
4. The dot product $(2, 1) \cdot (-1, 2) = 0$, so the angle between the point and its image is a right angle.

The typical use: to turn many points, put them as columns of one matrix and multiply once.
A trap: the angle is in radians in most formulas, and $\cos 90 \neq 0$.

### L3 human

The $2 \times 2$ rotation matrices form $SO(2)$, a circle group, and $R(\theta) = \exp\begin{pmatrix} 0 & -\theta \\ \theta & 0 \end{pmatrix}$.
The $3 \times 3$ rotation matrices form $SO(3)$, a compact Lie group of dimension $3$, and each element is $\exp$ of a skew-symmetric matrix, by [[Rodrigues' rotation formula|WS52X8SGC4]].
For general $n$, a rotation matrix is a product of rotations in perpendicular planes, by the [[normal form|QTY3VMFGY1]].
In numerical work, the Givens rotations are rotation matrices in a coordinate plane.
