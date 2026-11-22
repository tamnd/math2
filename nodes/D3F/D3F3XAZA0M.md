---
tag: D3F3XAZA0M
kind: example
name: Determinants of rotations and reflections of the plane
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
instance_of: [00KDZRW4C0]
uses: [0ZN2J42SK7, 0B9QNFGTHM, 027MBSVPY3, 0QJJAQ6ZYZ]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Orientation
---

## Example

Let $\theta \in \mathbb{R}$, and consider the two real matrices
$$R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}, \qquad S_\theta = \begin{pmatrix} \cos 2\theta & \sin 2\theta \\ \sin 2\theta & -\cos 2\theta \end{pmatrix}.$$
The matrix $R_\theta$ is the [[rotation|0B9QNFGTHM]] by the angle $\theta$, and $S_\theta$ is the [[reflection|027MBSVPY3]] in the line through $0$ at angle $\theta$.
We compute their [[determinants|00KDZRW4C0]].

1. The [[2 by 2 formula|0ZN2J42SK7]] $ad - bc$ gives
$$\det R_\theta = \cos\theta \cos\theta - (-\sin\theta)\sin\theta = \cos^2\theta + \sin^2\theta = 1.$$
2. The same formula gives
$$\det S_\theta = \cos 2\theta \cdot (-\cos 2\theta) - \sin 2\theta \cdot \sin 2\theta = -(\cos^2 2\theta + \sin^2 2\theta) = -1.$$
3. Check with $\theta = \pi/2$.
   The rotation by a right angle is $R_{\pi/2} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, with determinant $0 \cdot 0 - (-1) \cdot 1 = 1$.
4. Check with $\theta = 0$.
   The reflection in the $x$-axis is $S_0 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$, with determinant $1 \cdot (-1) - 0 = -1$.

So every rotation has determinant $1$, and every reflection in a line through $0$ has determinant $-1$.

## Remarks

Both kinds of map keep lengths and areas, so the absolute value of the determinant is $1$ in both cases.
The sign tells them apart.
A rotation keeps the turning direction, from the first basis vector toward the second, while a reflection reverses it, so a reflection changes the [[orientation|0QJJAQ6ZYZ]].

Products behave as the product rule predicts.
Multiply the reflection $S_\theta$ by the reflection $S_0$:
$$S_\theta S_0 = \begin{pmatrix} \cos 2\theta & -\sin 2\theta \\ \sin 2\theta & \cos 2\theta \end{pmatrix} = R_{2\theta}.$$
Two reflections give a rotation, and the determinants agree, since $(-1)(-1) = 1$.
If we scale the rotation by a real number $c$, then $\det(c R_\theta) = c^2 \cos^2\theta + c^2 \sin^2\theta = c^2$, and areas grow by the factor $c^2$.

## Explanations

### L1 human

Turning a picture of the plane does not change its sizes, and it does not change clockwise into counterclockwise.
Its determinant is $1$.
A mirror also keeps sizes, but it swaps clockwise and counterclockwise.
Its determinant is $-1$, and the minus sign records the flip.

### L2 human

The orthogonal $2 \times 2$ matrices, those whose columns are perpendicular unit vectors, are exactly the rotations and the reflections.
The determinant sorts them in one line of arithmetic: $+1$ for a rotation and $-1$ for a reflection.
For example, $\frac{1}{5}\begin{pmatrix} 3 & 4 \\ 4 & -3 \end{pmatrix}$ has determinant $\frac{1}{25}(-9 - 16) = -1$, so it is a reflection.
Watch out: a determinant of $1$ alone does not make a matrix a rotation.
The shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has determinant $1$ too, but it changes lengths, so it is not orthogonal.
