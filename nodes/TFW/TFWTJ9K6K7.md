---
tag: TFWTJ9K6K7
kind: example
name: A rotation of space by sixty degrees about the diagonal
msc: ["15B10"]
topics: [AZS5BPF5H3]
audience: ug1
instance_of: [0W02QESPJQ, 6WBVP2PB1Y]
illustrates: [F7M8ZXB4P7, QDZJMFATRW, 2ZVG43GSKA]
uses: [0QRBVFJ50X, 0C3CFHDN6R, 07PTPSZPME]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_matrix
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Rotation_matrix
    locator: Conversion from rotation matrix to axis–angle
---

## Example

Let
$$Q = \frac{1}{3}\begin{pmatrix} 2 & -1 & 2 \\ 2 & 2 & -1 \\ -1 & 2 & 2 \end{pmatrix}.$$
We check that $Q$ is an [[orthogonal matrix|0QRBVFJ50X]] with determinant $1$, and we find its axis, its angle and its sense of turning.

1. The columns are $c_1 = \frac{1}{3}(2, 2, -1)$, $c_2 = \frac{1}{3}(-1, 2, 2)$ and $c_3 = \frac{1}{3}(2, -1, 2)$. Each has squared length $\frac{4 + 4 + 1}{9} = 1$.
2. The dot products are $c_1 \cdot c_2 = \frac{-2 + 4 - 2}{9} = 0$, $c_1 \cdot c_3 = \frac{4 - 2 - 2}{9} = 0$ and $c_2 \cdot c_3 = \frac{-2 - 2 + 4}{9} = 0$. These are the entries of $Q^TQ$, so $Q^TQ = I_3$.
3. Expand the [[determinant|0C3CFHDN6R]] of the integer matrix $3Q$ along its first row: $2(4 + 2) + 1(4 - 1) + 2(4 + 2) = 12 + 3 + 12 = 27$. So $\det Q = \frac{27}{27} = 1$, and $Q$ is a rotation.
4. For the axis, $Q(1, 1, 1)^T = \frac{1}{3}(2 - 1 + 2,\ 2 + 2 - 1,\ -1 + 2 + 2) = (1, 1, 1)$. So $Q$ fixes the line through $(1, 1, 1)$.
5. For the angle, the [[trace|07PTPSZPME]] is $\frac{2 + 2 + 2}{3} = 2$. A rotation of $\R^3$ by $\theta$ has trace $1 + 2\cos\theta$, so $\cos\theta = \frac{1}{2}$.
6. For the sense, $Q - Q^T = \begin{pmatrix} 0 & -1 & 1 \\ 1 & 0 & -1 \\ -1 & 1 & 0 \end{pmatrix}$. For a rotation by $\theta$ about the unit vector $u$, the matrix $Q - Q^T$ is $2\sin\theta$ times the cross product matrix of $u$.
7. With $u = \frac{1}{\sqrt{3}}(1, 1, 1)$, the cross product matrix of $u$ is $\frac{1}{\sqrt 3}$ times the matrix of step 6, so $2\sin\theta = \sqrt{3}$ and $\sin\theta = \frac{\sqrt{3}}{2}$.
8. So $\theta = \pi/3$, and $Q$ turns by $60$ degrees counterclockwise when we look from the tip of $u$ back to the origin.

## Remarks

The example shows a rotation of $\R^3$ that is not about a coordinate axis, and how to read off its axis and angle: the axis from the eigenvector for $1$, the angle from the trace, and the sense from $Q - Q^T$.
The characteristic polynomial is $(t - 1)(t^2 - t + 1)$, with the roots $1$ and $\frac{1}{2}(1 \pm i\sqrt{3}) = e^{\pm i\pi/3}$.
All three lie on the unit circle, as the [[eigenvalue theorem|QDZJMFATRW]] says.
In an orthonormal basis $f_1, f_2, u$ with $f_1, f_2$ in the plane $x + y + z = 0$ and $f_1 \times f_2 = u$, the [[normal form|QTY3VMFGY1]] of $Q$ is the rotation $R(\pi/3)$ in the first two coordinates and $1$ in the third.

Change one thing at a time.
The power $Q^3$ is the half turn about the same axis, and $Q^6 = I$.
The negative $-Q$ still has orthonormal columns, but $\det(-Q) = (-1)^3 = -1$, so $-Q$ is an improper rotation: a rotation by $\pi/3$ followed by the point reflection $x \mapsto -x$.

## Explanations

### L1 human

Hold a cube by two opposite corners and turn it about the line through these corners.
This matrix turns all of space about such a line, the line through $(0, 0, 0)$ and $(1, 1, 1)$.
The angle of the turn is $60$ degrees, and the points on the line stay where they are.
After six such turns, everything is back in place.

### L2 human

The same steps work for every $3 \times 3$ matrix that you suspect is a rotation.
Check that the columns are orthonormal, and compute the determinant, which must be $1$.
Solve $Qx = x$ for the axis, use $\tr Q = 1 + 2\cos\theta$ for the angle, and use $Q - Q^T$ for the sense.
For $Q$ above, the trace step reads
$$1 + 2\cos\theta = 2, \qquad \cos\theta = \tfrac{1}{2}, \qquad \theta = \pm\tfrac{\pi}{3}.$$
Watch out: the trace gives only $\cos\theta$, so it cannot tell $\theta$ from $-\theta$, and the sign comes from $Q - Q^T$ and the chosen direction of the axis.
