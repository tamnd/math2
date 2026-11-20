---
tag: 5ABEVQG5YQ
kind: example
name: The principal angles between two planes in R3
msc: [15A18]
topics: [8GQVME4SZZ]
audience: grad
instance_of: [YHVD3773AW]
illustrates: [VC8KCEGAZA]
uses: [0S9GGTR0EX, 09VMDSRXWJ, P0VS33VRSR, JT8Q204E4R]
sources:
  - url: https://en.wikipedia.org/wiki/Angles_between_flats
---

## Example

Let $U$ be the plane $x + y = 0$ and $W$ the plane $y + z = 0$ in $\R^3$.
We compute their [[principal angles|YHVD3773AW]] with the [[singular value characterization|VC8KCEGAZA]].

1. [[Orthonormal bases|0S9GGTR0EX]]: $U$ has $\frac{1}{\sqrt 2} (1, -1, 0)$ and $(0, 0, 1)$; $W$ has $(1, 0, 0)$ and $\frac{1}{\sqrt 2} (0, 1, -1)$. Each pair is orthogonal, and each vector satisfies the equation of its plane.
2. The entries of $M = Q_1^{\mathsf{T}} Q_2$ are the dot products of these vectors:
$$M = \begin{pmatrix} 1/\sqrt 2 & -1/2 \\ 0 & -1/\sqrt 2 \end{pmatrix}.$$
3. $M^{\mathsf{T}} M = \begin{pmatrix} 1/2 & -1/(2\sqrt 2) \\ -1/(2\sqrt 2) & 3/4 \end{pmatrix}$, with trace $5/4$ and determinant $(\det M)^2 = 1/4$.
4. Its eigenvalues solve $\lambda^2 - \frac{5}{4} \lambda + \frac{1}{4} = 0$, so they are $1$ and $1/4$. The eigenvalues of $M M^{\mathsf{T}}$ are the same, because $M$ is square.
5. The [[singular values|09VMDSRXWJ]] are $\sigma_1 = 1$ and $\sigma_2 = 1/2$, so the principal angles are $\theta_1 = 0$ and $\theta_2 = \pi/3$.
6. Principal vectors for $\theta_1$: $u_1 = w_1 = \frac{1}{\sqrt 3} (1, -1, 1)$, which lies in both planes and spans $U \cap W$. This agrees with part 3 of the theorem: one zero angle, and $\dim (U \cap W) = 1$.
7. Principal vectors for $\theta_2$: the unit vectors of $U$ and $W$ orthogonal to $(1, -1, 1)$ are, up to sign, $u_2 = \frac{1}{\sqrt 6} (1, -1, -2)$ and $w_2 = \frac{1}{\sqrt 6} (2, 1, -1)$. Then $u_2 \cdot w_2 = (2 - 1 + 2)/6 = 1/2 = \cos (\pi/3)$.
8. Check with the normals $n_1 = (1, 1, 0)$ and $n_2 = (0, 1, 1)$: $\cos \varphi = \frac{n_1 \cdot n_2}{\norm{n_1} \norm{n_2}} = \frac{1}{2}$, so the dihedral angle is $\pi/3$, as in [[the classical computation|P0VS33VRSR]] for the parallel planes $x + y = 1$ and $y + z = 2$.
9. Chordal distance: by part 5, $\norm{P_U - P_W}_F^2 = 2 (\sin^2 0 + \sin^2 (\pi/3)) = 3/2$. Directly, $P_U - P_W = \frac{1}{2} (n_2 n_2^{\mathsf{T}} - n_1 n_1^{\mathsf{T}})$, and its squared [[Frobenius norm|JT8Q204E4R]] is $\frac{1}{4} (4 + 4 - 2 (n_1 \cdot n_2)^2) = \frac{6}{4} = \frac{3}{2}$.

## Remarks

In the bases of step 6 and step 7, the matrix $Q_1^{\mathsf{T}} Q_2$ becomes $\operatorname{diag}(1, 1/2)$.
In the bases of step 1, its entries $1/\sqrt 2$, $-1/2$, $0$ and $-1/\sqrt 2$ are not the cosines of the principal angles; see [[the non-example|G00QE6RH12]].

## Explanations

### L1 human

The two planes share a line, so one principal angle is $0$.
Across that line they open like the pages of a book, and the second principal angle is the angle between the pages, here $60°$.

### L2 human

The method is: orthonormal bases, the small matrix $Q_1^{\mathsf{T}} Q_2$, its singular values, and then $\arccos$.
For two different planes in $\R^3$ the answer is always $0$ and the dihedral angle.
The trap is to stop at step 2 and read angles from the entries of $M$.
