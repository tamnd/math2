---
tag: ~ab3b9c7a
kind: example
name: Full SVD of a 2 × 2 matrix
msc: [15A18, 15A23]
topics: [SS4EVPKT3A]
audience: ug1
instance_of: [09VMDSRXWJ]
illustrates: [000NPTMX6J, ~f8b3ecc3]
uses: [0K2TX12X58, 0QRBVFJ50X]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_value_decomposition
    locator: Based on the spectral theorem
  - book: isbn:9780321982384
    locator: Section 7.4
---

## Example

Let $A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix}$.

1. $A^T A = \begin{pmatrix} 3 & 4 \\ 0 & 5 \end{pmatrix} \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix} = \begin{pmatrix} 25 & 20 \\ 20 & 25 \end{pmatrix}$.
2. Its characteristic polynomial is $(25 - t)^2 - 400 = (t - 45)(t - 5)$. So $\lambda_1 = 45$ and $\lambda_2 = 5$.
3. The singular values are $\sigma_1 = \sqrt{45} = 3\sqrt5$ and $\sigma_2 = \sqrt5$.
4. Unit eigenvectors: $v_1 = \tfrac{1}{\sqrt2}(1, 1)$, since $A^T A (1, 1) = (45, 45)$, and $v_2 = \tfrac{1}{\sqrt2}(-1, 1)$, since $A^T A(-1, 1) = (-5, 5)$.
5. $A v_1 = \tfrac{1}{\sqrt2}(3, 9)$ has length $\tfrac{\sqrt{90}}{\sqrt2} = \sqrt{45} = \sigma_1$. So $u_1 = A v_1 / \sigma_1 = \tfrac{1}{\sqrt{10}}(1, 3)$.
6. $A v_2 = \tfrac{1}{\sqrt2}(-3, 1)$ has length $\tfrac{\sqrt{10}}{\sqrt2} = \sqrt5 = \sigma_2$. So $u_2 = A v_2 / \sigma_2 = \tfrac{1}{\sqrt{10}}(-3, 1)$.
7. $u_1 \cdot u_2 = \tfrac{1}{10}(-3 + 3) = 0$, so $U = \tfrac{1}{\sqrt{10}} \begin{pmatrix} 1 & -3 \\ 3 & 1 \end{pmatrix}$ is [[orthogonal|0QRBVFJ50X]]. Also $V = \tfrac{1}{\sqrt2} \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$ is orthogonal.
8. Multiply back: $U \Sigma = \tfrac{1}{\sqrt{10}} \begin{pmatrix} 3\sqrt5 & -3\sqrt5 \\ 9\sqrt5 & \sqrt5 \end{pmatrix} = \tfrac{1}{\sqrt2} \begin{pmatrix} 3 & -3 \\ 9 & 1 \end{pmatrix}$.
9. Then $U \Sigma V^T = \tfrac12 \begin{pmatrix} 3 & -3 \\ 9 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix} = \tfrac12 \begin{pmatrix} 6 & 0 \\ 8 & 10 \end{pmatrix} = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix} = A$.

## Remarks

- $\sigma_1 \sigma_2 = 3\sqrt5 \cdot \sqrt5 = 15 = \abs{\det A}$, and $\sigma_1^2 + \sigma_2^2 = 50 = 9 + 0 + 16 + 25 = \norm{A}_F^2$.
- The eigenvalues of $A$ are $3$ and $5$, since $A$ is triangular. They differ from the singular values $3\sqrt5 \approx 6.71$ and $\sqrt5 \approx 2.24$.
- Both $U$ and $V$ are rotations, with determinant $1$: $\det U = \tfrac{1}{10}(1 + 9) = 1$ and $\det V = \tfrac12(1 + 1) = 1$.
- [[The ellipse example|~16170aab]] draws the image of the unit circle, and [[the rank-one example|~90df945c]] truncates this SVD.

## Explanations

### L1 human

We split $A$ into a rotation, a stretch and another rotation.
The stretch factors are $3\sqrt5$ and $\sqrt5$.
Multiplying the three matrices back gives $A$ again.

### L2 human

The steps are the standard recipe: eigenvectors of $A^T A$ give $V$, square roots of its eigenvalues give $\Sigma$, and $u_i = A v_i / \sigma_i$ gives $U$.
Steps 5 and 6 compute $U$ from $V$, so the signs of $u_i$ and $v_i$ match.
A trap: the eigenvectors of $A$ itself, $(0, 1)$ and $(1, -2)$, are not orthogonal, and they are not used.
