---
tag: GK1B93DKD3
kind: example
name: Full and reduced SVD of a 3 × 2 matrix
msc: [15A18, 15A23]
topics: [SS4EVPKT3A]
audience: ug1
instance_of: [09VMDSRXWJ]
illustrates: [000NPTMX6J, 6VXM1T8PG7]
uses: [0K2TX12X58, 0QRBVFJ50X, 03AJKXH1AV, 0PHDYNR24D]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_value_decomposition
    locator: Reduced SVDs
  - book: isbn:9780321982384
    locator: Section 7.4
---

## Example

Let $A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \\ 0 & 1 \end{pmatrix}$, so $m = 3$ and $n = 2$.
We find its [[singular values|0K2TX12X58]], its full SVD and its reduced SVD, and we multiply the factors back.

1. The small product is $A^{\mathsf{T}} A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$. Its characteristic polynomial is $(2 - t)^2 - 1 = (t - 3)(t - 1)$, so $\lambda_1 = 3$ and $\lambda_2 = 1$.
2. The singular values are $\sigma_1 = \sqrt3$ and $\sigma_2 = 1$. Both are nonzero, so $\rank A = 2$.
3. Unit eigenvectors of $A^{\mathsf{T}} A$ are $v_1 = \tfrac{1}{\sqrt2}(1, 1)$ for $3$ and $v_2 = \tfrac{1}{\sqrt2}(1, -1)$ for $1$.
4. The image $A v_1 = \tfrac{1}{\sqrt2}(2, 1, 1)$ has length $\sqrt{6/2} = \sqrt3 = \sigma_1$, so $u_1 = A v_1 / \sigma_1 = \tfrac{1}{\sqrt6}(2, 1, 1)$.
5. The image $A v_2 = \tfrac{1}{\sqrt2}(0, 1, -1)$ has length $1 = \sigma_2$, so $u_2 = \tfrac{1}{\sqrt2}(0, 1, -1)$.
6. A third unit vector orthogonal to $u_1$ and $u_2$ is $u_3 = \tfrac{1}{\sqrt3}(1, -1, -1)$. Check: $(1, -1, -1) \cdot (2, 1, 1) = 2 - 1 - 1 = 0$ and $(1, -1, -1) \cdot (0, 1, -1) = 0 - 1 + 1 = 0$.
7. The full SVD uses the $3 \times 3$ [[orthogonal matrix|0QRBVFJ50X]] $U = (u_1 \; u_2 \; u_3)$, the $2 \times 2$ orthogonal matrix $V = (v_1 \; v_2)$, and the $3 \times 2$ matrix
$$\Sigma = \begin{pmatrix} \sqrt3 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix}.$$
8. Multiply back. The zero row of $\Sigma$ removes $u_3$, so $U \Sigma = (\sqrt3 \, u_1 \;\; u_2)$, and
$$U \Sigma V^{\mathsf{T}} = \frac{1}{\sqrt2} \begin{pmatrix} 2 & 0 \\ 1 & 1 \\ 1 & -1 \end{pmatrix} \cdot \frac{1}{\sqrt2} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \frac12 \begin{pmatrix} 2 & 2 \\ 2 & 0 \\ 0 & 2 \end{pmatrix} = A.$$
9. The reduced SVD drops $u_3$ and the zero row: $A = U_2 \Sigma_2 V^{\mathsf{T}}$ with $U_2 = (u_1 \; u_2)$ of size $3 \times 2$ and the square matrix $\Sigma_2 = \operatorname{diag}(\sqrt3, 1)$. Step 8 is also the check of this product.

## Remarks

The example shows all four fundamental subspaces in the singular vectors.
The vectors $u_1, u_2$ span the [[column space|03AJKXH1AV]], which is the plane $x_1 - x_2 - x_3 = 0$ with normal vector $u_3$; both columns $(1, 1, 0)$ and $(1, 0, 1)$ satisfy this equation.
The vector $u_3$ spans the null space of $A^{\mathsf{T}}$, since $A^{\mathsf{T}} (1, -1, -1) = (1 - 1, \, 1 - 1) = (0, 0)$.
The vectors $v_1, v_2$ span the row space, which is all of $\R^2$, and the [[null space|0PHDYNR24D]] of $A$ is $\{0\}$.

The shape of $\Sigma$ changes from $3 \times 2$ in the full form to $2 \times 2$ in the reduced form, while the product stays the same.
The vector $u_3$ is the only part of the full SVD that no formula $A v / \sigma$ produces, and any unit normal of the column space works, so here it is unique up to sign.
If we add a third column $(2, 1, 1)$, the sum of the first two, the rank stays $2$ and a third singular value $0$ appears.
The same matrix returns in [[the pseudoinverse with independent columns|SYDSCH64X8]].

## Explanations

### L1 human

The matrix $A$ takes points of the plane to points of space.
All the images lie in one tilted plane through the origin.
The unit circle goes to an ellipse in that plane, with half-axes $\sqrt3 \approx 1.73$ and $1$.
The third column $u_3$ of $U$ points straight out of the tilted plane, and no point is sent in that direction.

### L2 human

For a tall matrix, $A^{\mathsf{T}} A$ is the small matrix, so we start there and find $V$ first.
The vectors $u_1$ and $u_2$ come from $A v_i / \sigma_i$, which keeps the signs of $u_i$ and $v_i$ matched.
The last vector $u_3$ comes from the null space of $A^{\mathsf{T}}$: solve $x_1 + x_2 = 0$ and $x_1 + x_3 = 0$ and normalize.
Watch out: if you took $U_2$ for the full $U$, you would have $U_2^{\mathsf{T}} U_2 = I_2$ but $U_2 U_2^{\mathsf{T}} \ne I_3$, so $U_2$ is not an orthogonal matrix.
