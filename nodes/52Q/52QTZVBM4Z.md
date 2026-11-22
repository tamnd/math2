---
tag: 52QTZVBM4Z
kind: example
name: The square of the rotation by a right angle is minus the identity
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
instance_of: [032Q9FB8MT]
uses: [076JGP6R3T, 0CCQV3884B]
sources:
  - url: https://en.wikipedia.org/wiki/Rotation_matrix
    locator: In two dimensions
---

## Example

Let
$$R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$$
over $\mathbb{R}$.
We compute its powers with the [[product rule|076JGP6R3T]] and compare them with the geometry.

1. The [[matrix-vector product|0CCQV3884B]] gives
$$R \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \cdot x - 1 \cdot y \\ 1 \cdot x + 0 \cdot y \end{pmatrix} = \begin{pmatrix} -y \\ x \end{pmatrix}.$$
So $R$ sends $(1, 0)$ to $(0, 1)$ and $(0, 1)$ to $(-1, 0)$: it turns the plane by $90^\circ$ counterclockwise.
2. Multiply $R$ by itself, row times column:
$$R^2 = \begin{pmatrix} 0 \cdot 0 + (-1) \cdot 1 & 0 \cdot (-1) + (-1) \cdot 0 \\ 1 \cdot 0 + 0 \cdot 1 & 1 \cdot (-1) + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -I.$$
3. Geometrically, two quarter turns are a half turn, and a half turn sends every vector $v$ to $-v$. This agrees with step 2.
4. The higher powers follow from step 2 without new sums:
$$R^3 = R^2 R = -R, \qquad R^4 = (R^2)^2 = (-I)^2 = I.$$
5. Since $R \cdot R^3 = R^4 = I$ and $R^3 R = I$ as well, the inverse of $R$ is
$$R^{-1} = R^3 = -R = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix},$$
the quarter turn clockwise.

## Remarks

The powers of $R$ repeat with period 4: $R, -I, -R, I, R, \dots$.
So $R^k$ depends only on the remainder of $k$ on division by 4, and for example $R^{10} = R^2 = -I$.

The real matrix $R$ has square $-I$, so it plays the part of the imaginary unit $i$, although no real number has square $-1$.
The matrices $aI + bR = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ add and multiply like the complex numbers $a + bi$, and they form a [[copy of the complex numbers|GHV77C35RT]] inside the [[matrix ring|AB2MD5CD13]] $M_2(\mathbb{R})$.

If you replace the quarter turn by the turn through an angle $\theta$, with matrix $\begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$, then the square is the turn through $2\theta$.
For $\theta = 90^\circ$ this gives back $R^2 = -I$.

## Explanations

### L1 human

The matrix $R$ turns every arrow in the plane by a quarter turn to the left.
Doing it twice is a half turn, which points every arrow the opposite way.
So $R$ times $R$ is $-I$, the matrix that changes the sign of every vector.
Four quarter turns bring every arrow back, so $R^4 = I$.

### L2 human

Products of matrices compute composites of maps, and here the composite is easy to see.
The picture predicts $R^2 = -I$, and the row-times-column computation in step 2 confirms it.
This is a good habit: when a matrix has a geometric meaning, use the picture to check the arithmetic.
Watch out: the equation $X^2 = -I$ has many real solutions, not just two.
Both $R$ and $-R$ solve it, and so does every matrix $\begin{pmatrix} a & b \\ c & -a \end{pmatrix}$ with $a^2 + bc = -1$, since its square is $(a^2 + bc) I$.
