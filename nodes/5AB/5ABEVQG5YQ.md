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
We compute their [[principal angles|YHVD3773AW]] with the [[singular value characterization|VC8KCEGAZA]], and then we check the answer by geometry.

1. Choose [[orthonormal bases|0S9GGTR0EX]]: $\frac{1}{\sqrt 2}(1, -1, 0)$ and $(0, 0, 1)$ for $U$, and $(1, 0, 0)$ and $\frac{1}{\sqrt 2}(0, 1, -1)$ for $W$.
2. Each vector satisfies the equation of its plane, and the two vectors of each pair have dot product $0$ and length $1$.
3. The entry $(i, j)$ of $M = Q_1^{\mathsf{T}} Q_2$ is the dot product of basis vector $i$ of $U$ with basis vector $j$ of $W$:
$$M = \begin{pmatrix} 1/\sqrt 2 & -1/2 \\ 0 & -1/\sqrt 2 \end{pmatrix}.$$
4. Multiply out $M^{\mathsf{T}} M$:
$$M^{\mathsf{T}} M = \begin{pmatrix} 1/2 & -1/(2\sqrt 2) \\ -1/(2\sqrt 2) & 3/4 \end{pmatrix}, \qquad \tr = \tfrac{5}{4}, \qquad \det = (\det M)^2 = \left( -\tfrac{1}{2} \right)^2 = \tfrac{1}{4}.$$
5. The eigenvalues solve $\lambda^2 - \frac{5}{4} \lambda + \frac{1}{4} = 0$, which factors as $(\lambda - 1)(\lambda - \frac{1}{4}) = 0$.
6. Since $M$ is square, $M M^{\mathsf{T}}$ has the same eigenvalues $1$ and $\frac{1}{4}$.
7. So the [[singular values|09VMDSRXWJ]] are $\sigma_1 = 1$ and $\sigma_2 = \frac{1}{2}$, and the principal angles are $\theta_1 = 0$ and $\theta_2 = \pi/3$.
8. Principal vectors for $\theta_1$: the vector $u_1 = w_1 = \frac{1}{\sqrt 3}(1, -1, 1)$ satisfies both $x + y = 0$ and $y + z = 0$, so it spans $U \cap W$.
9. This agrees with the count of zero angles in the theorem: one zero angle, and $\dim (U \cap W) = 1$.
10. Principal vectors for $\theta_2$: the unit vectors of $U$ and of $W$ orthogonal to $(1, -1, 1)$ are, up to sign, $u_2 = \frac{1}{\sqrt 6}(1, -1, -2)$ and $w_2 = \frac{1}{\sqrt 6}(2, 1, -1)$.
11. Their dot product is
$$u_2 \cdot w_2 = \frac{2 - 1 + 2}{6} = \frac{1}{2} = \cos \frac{\pi}{3}.$$
12. Check with the normals $n_1 = (1, 1, 0)$ and $n_2 = (0, 1, 1)$:
$$\cos \varphi = \frac{n_1 \cdot n_2}{\norm{n_1} \, \norm{n_2}} = \frac{1}{\sqrt 2 \cdot \sqrt 2} = \frac{1}{2},$$
so the dihedral angle is $\pi/3$, as in [[the classical computation|P0VS33VRSR]] for the parallel planes $x + y = 1$ and $y + z = 2$.
13. Check the distance formula: the theorem predicts $\norm{P_U - P_W}_F^2 = 2 (\sin^2 0 + \sin^2 \frac{\pi}{3}) = 2 \cdot \frac{3}{4} = \frac{3}{2}$.
14. Directly, $P_U = I - \frac{1}{2} n_1 n_1^{\mathsf{T}}$ and $P_W = I - \frac{1}{2} n_2 n_2^{\mathsf{T}}$, so $P_U - P_W = \frac{1}{2} (n_2 n_2^{\mathsf{T}} - n_1 n_1^{\mathsf{T}})$.
15. The squared [[Frobenius norm|JT8Q204E4R]] of $n_2 n_2^{\mathsf{T}} - n_1 n_1^{\mathsf{T}}$ is $\norm{n_2}^4 + \norm{n_1}^4 - 2 (n_1 \cdot n_2)^2 = 4 + 4 - 2 = 6$, so $\norm{P_U - P_W}_F^2 = \frac{6}{4} = \frac{3}{2}$.

## Remarks

In the bases of steps 8 and 10, the matrix of dot products becomes $\operatorname{diag}(1, \frac{1}{2})$, so those bases show the angles directly.
In the bases of step 1, the entries $\frac{1}{\sqrt 2}$, $-\frac{1}{2}$, $0$ and $-\frac{1}{\sqrt 2}$ are cosines of angles between basis vectors, and none of them is the cosine of a principal angle; see [[the non-example|G00QE6RH12]].

What changes when one plane turns?
Replace $W$ by the plane $y + cz = 0$ with $c > 0$.
The two planes still share a line, so one angle stays $0$, and the other is the angle between the normals $(1, 1, 0)$ and $(0, 1, c)$, with cosine $1 / \sqrt{2(1 + c^2)}$.
For $c = 1$ this is $\frac{1}{2}$ again, and as $c$ grows the second angle tends to $\pi/2$, because $W$ tends to the plane $z = 0$, which is orthogonal to... no plane through the line of $U$ at a right angle except one, and the normals become orthogonal.

## Explanations

### L1 human

The two planes share a line, so one principal angle is $0$, along that line.
Across the line they open like the pages of a book.
The second principal angle is the angle between the pages, here $60$ degrees.
You can see it from the two normal arrows $(1, 1, 0)$ and $(0, 1, 1)$, which also meet at $60$ degrees.

### L2 human

The method has four steps: orthonormal bases, the small matrix $Q_1^{\mathsf{T}} Q_2$, its singular values, and then the arccosine.
For two distinct planes in $\R^3$ the answer is always $0$ and the dihedral angle, so the normals give a quick check.
The singular value method is the one that still works in higher dimensions, where planes need not share a line and no normal vector exists.
Watch out: do not stop at step 3 and read angles from the entries of $M$, because those entries depend on the bases.
