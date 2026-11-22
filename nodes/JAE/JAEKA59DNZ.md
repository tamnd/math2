---
tag: JAEKA59DNZ
kind: example
name: Geometry of the singular value decomposition
msc: [15A18, 51N10]
topics: [SS4EVPKT3A]
audience: ug1
illustrates: [000NPTMX6J, 6VXM1T8PG7]
uses: [0K2TX12X58, 0VKCCEXBJ1, 0QRBVFJ50X]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_value_decomposition
    locator: Rotation/reflection, coordinate scaling, rotation/reflection
  - url: https://en.wikipedia.org/wiki/Singular_value_decomposition
    locator: Singular values as semiaxes of an ellipse or ellipsoid
---

## Example

Let $A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix}$, with the SVD $A = U \Sigma V^{\mathsf{T}}$ of [[the 2 by 2 example|B546BDVFQZ]].
There $\sigma_1 = 3\sqrt5$ and $\sigma_2 = \sqrt5$, with $v_1 = \tfrac{1}{\sqrt2}(1, 1)$, $v_2 = \tfrac{1}{\sqrt2}(-1, 1)$, $u_1 = \tfrac{1}{\sqrt{10}}(1, 3)$ and $u_2 = \tfrac{1}{\sqrt{10}}(-3, 1)$.
We find the image of the unit circle $\{x \in \R^2 : \norm x = 1\}$, first through the three factors and then as an equation.

1. Write a unit vector as $x = \cos\theta \, v_1 + \sin\theta \, v_2$. Every unit vector has this form, because $v_1, v_2$ is an orthonormal basis.
2. The first factor $V^{\mathsf{T}}$ sends $v_1$ to $e_1$ and $v_2$ to $e_2$, so $V^{\mathsf{T}} x = (\cos\theta, \sin\theta)$. Since $\det V = 1$, this is a rotation, by $45$ degrees clockwise, and the circle stays a circle.
3. The second factor $\Sigma$ stretches the axes, so $\Sigma V^{\mathsf{T}} x = (\sigma_1 \cos\theta, \sigma_2 \sin\theta)$. These points form the ellipse $s_1^2 / \sigma_1^2 + s_2^2 / \sigma_2^2 = 1$ with semi-axes $\sigma_1$ and $\sigma_2$ along the coordinate axes.
4. The third factor $U$ sends $e_1$ to $u_1$ and $e_2$ to $u_2$, and $\det U = 1$, so it rotates the ellipse. So $Ax = \sigma_1 \cos\theta \, u_1 + \sigma_2 \sin\theta \, u_2$, and the image is an [[ellipse|0VKCCEXBJ1]] with semi-axes of length $\sigma_1 = 3\sqrt5 \approx 6.71$ along $u_1$ and $\sigma_2 = \sqrt5 \approx 2.24$ along $u_2$.
5. For the equation in the standard coordinates, put $y = Ax$. Then $x = A^{-1} y$, and $\norm x^2 = 1$ becomes $y^{\mathsf{T}} (A A^{\mathsf{T}})^{-1} y = 1$. Here
$$A A^{\mathsf{T}} = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix} \begin{pmatrix} 3 & 4 \\ 0 & 5 \end{pmatrix} = \begin{pmatrix} 9 & 12 \\ 12 & 41 \end{pmatrix}, \qquad \det = 369 - 144 = 225.$$
6. So $(A A^{\mathsf{T}})^{-1} = \tfrac{1}{225} \begin{pmatrix} 41 & -12 \\ -12 & 9 \end{pmatrix}$, and the ellipse is
$$41 y_1^2 - 24 y_1 y_2 + 9 y_2^2 = 225.$$
7. Check at $x = e_1$: the point $y = (3, 4)$ gives $41 \cdot 9 - 24 \cdot 12 + 9 \cdot 16 = 369 - 288 + 144 = 225$.
8. Check at the end of the long axis: $x = v_1$ gives $y = \sigma_1 u_1 = \tfrac{3\sqrt5}{\sqrt{10}}(1, 3) = \tfrac{1}{\sqrt2}(3, 9)$, and
$$41 \cdot \tfrac92 - 24 \cdot \tfrac{27}{2} + 9 \cdot \tfrac{81}{2} = \tfrac{369 - 648 + 729}{2} = 225.$$
Its length is $\sqrt{9/2 + 81/2} = \sqrt{45} = \sigma_1$, as step 4 says.

## Remarks

The example shows the three moves of every SVD: a rotation or reflection $V^{\mathsf{T}}$, a scaling $\Sigma$ of the axes, and a rotation or reflection $U$.
Here both orthogonal factors have determinant $1$, so both are rotations; a factor with determinant $-1$ would be a reflection.
Because rotations keep lengths, the long semi-axis $\sigma_1$ is the largest distance from the origin to the ellipse, and $\sigma_2$ is the smallest.
This is part 4 of [[the theorem on singular values and rank|6VXM1T8PG7]]: $\sigma_1 = \max_{\norm x = 1} \norm{Ax}$ and $\sigma_2 = \min_{\norm x = 1} \norm{Ax}$.
The area of the ellipse is $\pi \sigma_1 \sigma_2 = 15\pi$, which is $\abs{\det A}$ times the area $\pi$ of the disc.

The same picture holds in every dimension.
An invertible $n \times n$ real matrix sends the unit sphere to an ellipsoid with semi-axes $\sigma_1 u_1, \dots, \sigma_n u_n$.
If some $\sigma_i$ are $0$, the ellipsoid is flat: the [[3 by 2 example|GK1B93DKD3]] sends the unit circle to an ellipse inside a plane in $\R^3$.
If we change the entry $4$ of $A$ to $0$, then $A = \operatorname{diag}(3, 5)$, both factors $U$ and $V$ become permutations of the axes, and the ellipse $y_1^2 / 9 + y_2^2 / 25 = 1$ has its axes along the coordinate axes.

## Explanations

### L1 human

A $2 \times 2$ matrix turns the unit circle into an ellipse.
It does this in three moves: it turns the circle, it stretches the circle along the two axes, and it turns the result.
The long half-axis has length $\sigma_1$ and points along $u_1$, and the short half-axis has length $\sigma_2$ and points along $u_2$.
The points of the circle that land on the ends of the axes are $\pm v_1$ and $\pm v_2$.

### L2 human

The SVD reads off the whole ellipse: the lengths from $\Sigma$, the directions of the axes from $U$, and the points that go there from $V$.
The equation in step 6 comes from $(A A^{\mathsf{T}})^{-1}$, whose eigenvectors are again $u_1$ and $u_2$, with eigenvalues $1/\sigma_1^2$ and $1/\sigma_2^2$.
Watch out: the axes of the ellipse are not the images $A e_1$ and $A e_2$ of the standard basis.
The image $A e_1 = (3, 4)$ has length $5$, which is neither $\sigma_1$ nor $\sigma_2$, and $A e_1 \cdot A e_2 = 0 + 20 = 20 \ne 0$.
