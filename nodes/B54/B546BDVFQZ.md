---
tag: B546BDVFQZ
kind: example
name: Full SVD of a 2 × 2 matrix
msc: [15A18, 15A23]
topics: [SS4EVPKT3A]
audience: ug1
instance_of: [09VMDSRXWJ]
illustrates: [000NPTMX6J, 6VXM1T8PG7]
uses: [0K2TX12X58, 0QRBVFJ50X]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_value_decomposition
    locator: Based on the spectral theorem
  - book: isbn:9780321982384
    locator: Section 7.4
---

## Example

Let $A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix}$.
We find its [[singular values|0K2TX12X58]] and an SVD $A = U \Sigma V^{\mathsf{T}}$, and then we multiply the three factors back.

1. Form the product
$$A^{\mathsf{T}} A = \begin{pmatrix} 3 & 4 \\ 0 & 5 \end{pmatrix} \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix} = \begin{pmatrix} 25 & 20 \\ 20 & 25 \end{pmatrix}.$$
2. Its characteristic polynomial is $(25 - t)^2 - 400 = (t - 45)(t - 5)$, so $\lambda_1 = 45$ and $\lambda_2 = 5$.
3. The singular values are $\sigma_1 = \sqrt{45} = 3\sqrt5$ and $\sigma_2 = \sqrt5$.
4. Unit eigenvectors are $v_1 = \tfrac{1}{\sqrt2}(1, 1)$, since $A^{\mathsf{T}} A (1, 1) = (45, 45)$, and $v_2 = \tfrac{1}{\sqrt2}(-1, 1)$, since $A^{\mathsf{T}} A (-1, 1) = (-5, 5)$.
5. The image $A v_1 = \tfrac{1}{\sqrt2}(3, 9)$ has length $\sqrt{90/2} = \sqrt{45} = \sigma_1$, so $u_1 = A v_1 / \sigma_1 = \tfrac{1}{\sqrt{10}}(1, 3)$.
6. The image $A v_2 = \tfrac{1}{\sqrt2}(-3, 1)$ has length $\sqrt{10/2} = \sqrt5 = \sigma_2$, so $u_2 = A v_2 / \sigma_2 = \tfrac{1}{\sqrt{10}}(-3, 1)$.
7. The vectors $u_1, u_2$ have length $1$ and $u_1 \cdot u_2 = \tfrac{1}{10}(-3 + 3) = 0$, so $U = \tfrac{1}{\sqrt{10}} \begin{pmatrix} 1 & -3 \\ 3 & 1 \end{pmatrix}$ is [[orthogonal|0QRBVFJ50X]]. In the same way $V = \tfrac{1}{\sqrt2} \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$ is orthogonal, and $\Sigma = \operatorname{diag}(3\sqrt5, \sqrt5)$.
8. Multiply the first two factors, using $\sqrt5 / \sqrt{10} = 1 / \sqrt2$:
$$U \Sigma = \frac{1}{\sqrt{10}} \begin{pmatrix} 3\sqrt5 & -3\sqrt5 \\ 9\sqrt5 & \sqrt5 \end{pmatrix} = \frac{1}{\sqrt2} \begin{pmatrix} 3 & -3 \\ 9 & 1 \end{pmatrix}.$$
9. Multiply by $V^{\mathsf{T}}$:
$$U \Sigma V^{\mathsf{T}} = \frac12 \begin{pmatrix} 3 & -3 \\ 9 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix} = \frac12 \begin{pmatrix} 6 & 0 \\ 8 & 10 \end{pmatrix} = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix} = A.$$

## Remarks

The numbers fit the general rules.
The product $\sigma_1 \sigma_2 = 3\sqrt5 \cdot \sqrt5 = 15$ equals $\abs{\det A} = 15$, and the sum $\sigma_1^2 + \sigma_2^2 = 50$ equals $9 + 0 + 16 + 25 = \norm{A}_F^2$.
Both $U$ and $V$ are rotations, since $\det U = \tfrac{1}{10}(1 + 9) = 1$ and $\det V = \tfrac12(1 + 1) = 1$.

The eigenvalues of $A$ are its diagonal entries $3$ and $5$, because $A$ is triangular.
They differ from the singular values $3\sqrt5 \approx 6.71$ and $\sqrt5 \approx 2.24$, because $A$ is not normal.
If we change the entry $4$ to $0$, then $A = \operatorname{diag}(3, 5)$ is normal, and the singular values become $5$ and $3$, the eigenvalues in decreasing order.

[[The ellipse example|JAEKA59DNZ]] draws the image of the unit circle under this $A$, and [[the rank-one example|RFHTECHY4J]] keeps only the first term $\sigma_1 u_1 v_1^{\mathsf{T}}$.

## Explanations

### L1 human

We split $A$ into three simple moves: a turn, a stretch along the two axes, and another turn.
The stretch factors are $3\sqrt5 \approx 6.71$ and $\sqrt5 \approx 2.24$.
Multiplying the three matrices back together gives $A$ again.

### L2 human

The steps follow the standard recipe.
Eigenvectors of $A^{\mathsf{T}} A$ give $V$, square roots of its eigenvalues give $\Sigma$, and $u_i = A v_i / \sigma_i$ gives $U$.
Steps 5 and 6 build $U$ from $V$, so the signs of $u_i$ and $v_i$ match and the product in step 9 comes out right.
Watch out: the eigenvectors of $A$ itself, $(1, -2)$ for $3$ and $(0, 1)$ for $5$, are not orthogonal, and they play no part in the SVD.
