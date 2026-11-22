---
tag: PHVR0HP7M5
kind: example
name: Pseudoinverse of a rank-one 3 × 2 matrix
msc: [15A09]
topics: [SS4EVPKT3A]
audience: ug2
instance_of: [0YY8VX28JR]
illustrates: [Q9YN0F60ZW]
uses: [0PSRCMCM5X, 000NPTMX6J, 0BYTQ4X1HC]
sources:
  - url: https://en.wikipedia.org/wiki/Moore–Penrose_inverse
    locator: Singular value decomposition (SVD)
  - url: https://en.wikipedia.org/wiki/Moore–Penrose_inverse
    locator: Linear least-squares
---

## Example

Let
$$A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \\ 3 & 6 \end{pmatrix}.$$
The second column is twice the first, so $\operatorname{rank} A = 1$, and $A^{\mathsf{T}} A = \begin{pmatrix} 14 & 28 \\ 28 & 56 \end{pmatrix}$ has determinant $14 \cdot 56 - 28^2 = 784 - 784 = 0$.
So the formula $(A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}}$ cannot be used.
We write $A = u v^{\mathsf{T}}$ with $u = (1, 2, 3)$ and $v = (1, 2)$, so that $\norm{u}^2 = 14$ and $\norm{v}^2 = 5$, and we compute the pseudoinverse from the SVD.

1. A reduced [[SVD|000NPTMX6J]] has one term, $A = \sigma_1 u_1 v_1^{\mathsf{T}}$, with $\sigma_1 = \norm{u} \norm{v} = \sqrt{70}$, $u_1 = u / \sqrt{14}$ and $v_1 = v / \sqrt5$. Check: $\sigma_1 u_1 v_1^{\mathsf{T}} = \frac{\sqrt{70}}{\sqrt{14} \sqrt 5} u v^{\mathsf{T}} = u v^{\mathsf{T}}$.
2. The recipe $A^+ = \sigma_1^{-1} v_1 u_1^{\mathsf{T}}$ gives
$$A^+ = \frac{1}{\sqrt{70}} \cdot \frac{v u^{\mathsf{T}}}{\sqrt{5} \sqrt{14}} = \frac{v u^{\mathsf{T}}}{70} = \frac{1}{70} \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{pmatrix}.$$
3. The first product uses $v^{\mathsf{T}} v = 5$:
$$A A^+ = \frac{u (v^{\mathsf{T}} v) u^{\mathsf{T}}}{70} = \frac{u u^{\mathsf{T}}}{14} = \frac{1}{14} \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 3 & 6 & 9 \end{pmatrix}.$$
4. The second product uses $u^{\mathsf{T}} u = 14$:
$$A^+ A = \frac{v (u^{\mathsf{T}} u) v^{\mathsf{T}}}{70} = \frac{v v^{\mathsf{T}}}{5} = \frac15 \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}.$$
5. Condition 1 holds: $A A^+ A = \frac{u u^{\mathsf{T}}}{14} \, u v^{\mathsf{T}} = \frac{u (u^{\mathsf{T}} u) v^{\mathsf{T}}}{14} = u v^{\mathsf{T}} = A$.
6. Condition 2 holds: $A^+ A A^+ = \frac{v v^{\mathsf{T}}}{5} \cdot \frac{v u^{\mathsf{T}}}{70} = \frac{v (v^{\mathsf{T}} v) u^{\mathsf{T}}}{5 \cdot 70} = \frac{v u^{\mathsf{T}}}{70} = A^+$.
7. Conditions 3 and 4 hold, because the matrices of steps 3 and 4 are real and symmetric.
8. Now solve least squares for $b = (1, 1, 1)$. Since $u^{\mathsf{T}} b = 6$, we get $A^+ b = \frac{6}{70} v = \left(\frac{3}{35}, \frac{6}{35}\right)$.
9. The fitted vector is $A A^+ b = \frac{u^{\mathsf{T}} b}{14} u = \frac37 (1, 2, 3)$, and the residual is $b - A A^+ b = \frac17 (4, 1, -2)$. Check: the residual is orthogonal to $u$, since $4 + 2 - 6 = 0$.
10. Every $x$ with $A x = \frac37 u$ is also a [[least-squares|0BYTQ4X1HC]] solution, and $A x = (x_1 + 2 x_2) u$, so these are the $x$ with $x_1 + 2 x_2 = \frac37$. For example $x = (\frac37, 0)$ has norm $\frac37 \approx 0.429$, while $\norm{A^+ b} = \frac{3}{35} \sqrt{1 + 4} = \frac{3 \sqrt5}{35} \approx 0.192$ is smaller.

## Remarks

The normal equations $A^{\mathsf{T}} A x = A^{\mathsf{T}} b$ have a whole line of solutions here, so they cannot single out one answer.
The pseudoinverse picks the point of that line nearest the origin, which is the multiple of $v$ on it, because $v$ spans the row space of $A$.
The line $x_1 + 2 x_2 = \frac37$ has normal vector $v = (1, 2)$, so its closest point to $0$ is indeed a multiple of $v$.

The same computation works for every rank-one matrix $A = u v^*$ with $u \ne 0$ and $v \ne 0$, and it gives
$$A^+ = \frac{v u^*}{\norm{u}^2 \norm{v}^2}.$$
If we change $b$ to a vector orthogonal to $u$, such as $(2, -1, 0)$, then $u^{\mathsf{T}} b = 0$ and $A^+ b = 0$: no multiple of $u$ is closer to $b$ than $0$.

## Explanations

### L1 human

This matrix sends every vector to a multiple of $(1, 2, 3)$.
So the system $Ax = (1, 1, 1)$ has no solution, and we aim for the closest point $\frac37 (1, 2, 3)$ on that line instead.
Many vectors $x$ reach that point, and the pseudoinverse picks the shortest one.

### L2 human

For a rank-one matrix the SVD has a single term, and $A^+$ is a multiple of $A^{\mathsf{T}}$: here $A^+ = \frac{1}{70} A^{\mathsf{T}}$.
Steps 5 to 7 check the four Penrose conditions with the two numbers $u^{\mathsf{T}} u = 14$ and $v^{\mathsf{T}} v = 5$, so no large matrix products are needed.
This is the typical use of the pseudoinverse: a least-squares problem with dependent columns, where the normal equations have many solutions.
Watch out: one or two conditions are not enough, since the identity in [[the diagonal non-example|2GME1M2784]] satisfies three conditions and is still not the pseudoinverse.
