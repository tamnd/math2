---
tag: JAEKA59DNZ
kind: example
name: Geometry of the SVD - the unit circle goes to an ellipse
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

Let $A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix}$, with the SVD $A = U \Sigma V^T$ of [[the $2 \times 2$ example|B546BDVFQZ]]: $\sigma_1 = 3\sqrt5$, $\sigma_2 = \sqrt5$, $v_1 = \tfrac{1}{\sqrt2}(1, 1)$, $v_2 = \tfrac{1}{\sqrt2}(-1, 1)$, $u_1 = \tfrac{1}{\sqrt{10}}(1, 3)$, $u_2 = \tfrac{1}{\sqrt{10}}(-3, 1)$.
We find the image of the unit circle $\set{x : \norm x = 1}$.

1. Write a unit vector as $x = \cos\theta \, v_1 + \sin\theta \, v_2$. This is possible because $v_1, v_2$ is an orthonormal basis.
2. Then $Ax = \sigma_1 \cos\theta \, u_1 + \sigma_2 \sin\theta \, u_2$, since $A v_i = \sigma_i u_i$.
3. In the coordinates $(s_1, s_2)$ along $u_1, u_2$, the image point is $(s_1, s_2) = (\sigma_1 \cos\theta, \sigma_2 \sin\theta)$. So $\frac{s_1^2}{\sigma_1^2} + \frac{s_2^2}{\sigma_2^2} = 1$.
4. So the image is an [[ellipse|0VKCCEXBJ1]] with semi-axes of lengths $\sigma_1 = 3\sqrt5 \approx 6.71$ along $u_1$ and $\sigma_2 = \sqrt5 \approx 2.24$ along $u_2$.
5. In the standard coordinates $y = Ax$, we have $x = A^{-1} y$, and $\norm x^2 = 1$ becomes $y^T (A A^T)^{-1} y = 1$. Here $A A^T = \begin{pmatrix} 9 & 12 \\ 12 & 41 \end{pmatrix}$, with determinant $369 - 144 = 225$.
6. So $(A A^T)^{-1} = \tfrac{1}{225} \begin{pmatrix} 41 & -12 \\ -12 & 9 \end{pmatrix}$, and the ellipse is $41 y_1^2 - 24 y_1 y_2 + 9 y_2^2 = 225$.
7. Check at $x = e_1$: $y = A e_1 = (3, 4)$ gives $41 \cdot 9 - 24 \cdot 12 + 9 \cdot 16 = 369 - 288 + 144 = 225$.
8. Check at the end of the long axis: $x = v_1$ gives $y = \sigma_1 u_1 = \tfrac{3\sqrt5}{\sqrt{10}}(1, 3) = \left(\tfrac{3}{\sqrt2}, \tfrac{9}{\sqrt2}\right)$. Then $41 \cdot \tfrac92 - 24 \cdot \tfrac{27}{2} + 9 \cdot \tfrac{81}{2} = \tfrac{369 - 648 + 729}{2} = 225$.
9. Its length is $\sqrt{\tfrac{9}{2} + \tfrac{81}{2}} = \sqrt{45} = \sigma_1$, as step 4 says.

## Remarks

- The three factors act in turn: $V^T$ rotates $v_1, v_2$ onto $e_1, e_2$; $\Sigma$ stretches the axes by $3\sqrt5$ and $\sqrt5$; $U$ rotates $e_1, e_2$ onto $u_1, u_2$.
- The area of the ellipse is $\pi \sigma_1 \sigma_2 = 15\pi = \abs{\det A} \cdot \pi$.
- $\sigma_1 = \max_{\norm x = 1} \norm{Ax}$ is the longest distance from the origin to the ellipse, and $\sigma_2$ is the shortest. This is part 4 of [[the theorem on singular values and rank|6VXM1T8PG7]].

## Explanations

### L1 human

A $2 \times 2$ matrix turns the unit circle into an ellipse.
The long half-axis has length $\sigma_1$ and points along $u_1$.
The short half-axis has length $\sigma_2$ and points along $u_2$.
The points of the circle that go to the ends of the axes are $\pm v_1$ and $\pm v_2$.

### L2 human

The SVD reads the ellipse directly: lengths from $\Sigma$, directions from $U$, and preimages from $V$.
The equation in step 6 comes from $(A A^T)^{-1}$, and its eigenvectors are again $u_1, u_2$.
A trap: the axes of the ellipse are not the images $A e_1$ and $A e_2$ of the standard basis; $A e_1 = (3, 4)$ has length $5$, which is neither $\sigma_1$ nor $\sigma_2$.
