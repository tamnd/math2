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

1. $A^T A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$. Its characteristic polynomial is $(2 - t)^2 - 1 = (t - 3)(t - 1)$, so $\lambda_1 = 3$ and $\lambda_2 = 1$.
2. The singular values are $\sigma_1 = \sqrt3$ and $\sigma_2 = 1$. Both are nonzero, so $\rank A = 2$.
3. Unit eigenvectors: $v_1 = \tfrac{1}{\sqrt2}(1, 1)$ and $v_2 = \tfrac{1}{\sqrt2}(1, -1)$.
4. $A v_1 = \tfrac{1}{\sqrt2}(2, 1, 1)$ has length $\tfrac{\sqrt6}{\sqrt2} = \sqrt3$. So $u_1 = \tfrac{1}{\sqrt6}(2, 1, 1)$.
5. $A v_2 = \tfrac{1}{\sqrt2}(0, 1, -1)$ has length $1$. So $u_2 = \tfrac{1}{\sqrt2}(0, 1, -1)$.
6. Complete with a unit vector orthogonal to $u_1$ and $u_2$: $u_3 = \tfrac{1}{\sqrt3}(1, -1, -1)$. Check: $2 - 1 - 1 = 0$ and $0 - 1 + 1 = 0$.
7. The full SVD has the $3 \times 3$ orthogonal $U = (u_1\ u_2\ u_3)$, the $2 \times 2$ orthogonal $V = (v_1\ v_2)$, and the $3 \times 2$ matrix
$$\Sigma = \begin{pmatrix} \sqrt3 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix}.$$
8. Multiply back: $U \Sigma = (\sqrt3 u_1\ \ u_2) = \tfrac{1}{\sqrt2} \begin{pmatrix} 2 & 0 \\ 1 & 1 \\ 1 & -1 \end{pmatrix}$. Then $U \Sigma V^T = \tfrac12 \begin{pmatrix} 2 & 0 \\ 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \tfrac12 \begin{pmatrix} 2 & 2 \\ 2 & 0 \\ 0 & 2 \end{pmatrix} = A$.
9. The reduced SVD drops $u_3$ and the zero row: $A = U_2 \Sigma_2 V^T$ with $U_2 = (u_1\ u_2)$ of size $3 \times 2$ and the square $\Sigma_2 = \operatorname{diag}(\sqrt3, 1)$.

## Remarks

- The four subspaces: $u_1, u_2$ span the [[column space|03AJKXH1AV]], which is the plane $x_1 - x_2 - x_3 = 0$. Both columns $(1, 1, 0)$ and $(1, 0, 1)$ satisfy this equation.
- $u_3$ spans the null space of $A^T$: $A^T (1, -1, -1) = (1 - 1,\ 1 - 1) = (0, 0)$.
- $v_1, v_2$ span the row space $\R^2$, and the [[null space|0PHDYNR24D]] of $A$ is $\set{0}$.
- The shape of $\Sigma$ changes: it is $3 \times 2$ in step 7 and $2 \times 2$ in step 9. The product is the same.
- The same $A$ appears in [[the pseudoinverse with independent columns|SYDSCH64X8]].

## Explanations

### L1 human

The matrix $A$ maps the plane into space.
The image is a tilted plane, and the unit circle goes to an ellipse in that plane, with semi-axes $\sqrt3$ and $1$.
The third column $u_3$ of $U$ points out of the plane, and nothing is mapped onto it.

### L2 human

For a tall matrix, $A^T A$ is the small matrix, so we start there.
The vectors $u_1$ and $u_2$ come from $A v_i / \sigma_i$, and the last vector $u_3$ comes from the null space of $A^T$.
A trap: $u_3$ is not determined by a formula $A v / \sigma$, because there is no third singular value; any unit vector orthogonal to the column space works, here up to sign.
