---
tag: VC8KCEGAZA
kind: statement
role: theorem
name: Principal angles from singular values
msc: [15A18, 65F15]
topics: [8GQVME4SZZ]
audience: grad
about: [YHVD3773AW]
uses: [YHVD3773AW, 09VMDSRXWJ, 0S9GGTR0EX, 0Q8HZTJC7G, 0W809K6AW0, JT8Q204E4R, 000NPTMX6J]
sources:
  - url: https://en.wikipedia.org/wiki/Angles_between_flats
---

## Statement

The cosines of the principal angles between two subspaces are the singular values of one small matrix built from orthonormal bases, and the singular vectors give the principal vectors.

Let $U$ and $W$ be subspaces of $\R^n$ with $1 \le p = \dim U \le q = \dim W$, and let $\theta_1 \le \dots \le \theta_p$ be their [[principal angles|YHVD3773AW]].
Let $Q_1$ be an $n \times p$ matrix and $Q_2$ an $n \times q$ matrix whose columns are [[orthonormal bases|0S9GGTR0EX]] of $U$ and of $W$.
Let $\sigma_1 \ge \dots \ge \sigma_p \ge 0$ be the [[singular values|09VMDSRXWJ]] of the $p \times q$ matrix $M = Q_1^{\mathsf{T}} Q_2$, that is, the square roots of the eigenvalues of $M M^{\mathsf{T}}$.
Let $P_U$ and $P_W$ be the [[orthogonal projections|0Q8HZTJC7G]] onto $U$ and $W$.
Then the following hold.

1. We have $\sigma_1 \le 1$ and $\cos \theta_k = \sigma_k$ for $k = 1, \dots, p$. In particular, the principal angles depend neither on the choice of the maximizing pairs nor on the choice of $Q_1$ and $Q_2$.
2. If $M = Y \Sigma Z^{\mathsf{T}}$ is a [[singular value decomposition|000NPTMX6J]] with columns $y_k$ of $Y$ and $z_k$ of $Z$, then $u_k = Q_1 y_k$ and $w_k = Q_2 z_k$, for $k = 1, \dots, p$, are principal vectors.
3. The number of indices $k$ with $\theta_k = 0$ equals $\dim (U \cap W)$.
4. If $p = 1$ and $U = \R u$ with $\norm{u} = 1$, then $\cos \theta_1 = \norm{P_W u}$.
5. In the [[Frobenius norm|JT8Q204E4R]], $\norm{P_U - P_W}_F^2 = p + q - 2 \sum_{k=1}^{p} \cos^2 \theta_k$, and for $p = q$ this equals $2 \sum_{k=1}^{p} \sin^2 \theta_k$.

The [[proof|G36R5Q7NA0]] turns the search over unit vectors into the maximization of $a^{\mathsf{T}} M c$ and splits off one singular value at a time.

## Remarks

### A worked use

For the planes $x + y = 0$ and $y + z = 0$ in $\R^3$, orthonormal bases give
$$M = \begin{pmatrix} 1/\sqrt 2 & -1/2 \\ 0 & -1/\sqrt 2 \end{pmatrix},$$
and the [[two-plane example|5ABEVQG5YQ]] finds the singular values $1$ and $\frac{1}{2}$.
Part 1 turns them into the angles $0$ and $\pi/3$ at once.
Part 3 predicts one zero angle, and indeed the planes meet in the line $\R(1, -1, 1)$.
Part 5 predicts $\norm{P_U - P_W}_F^2 = 2 \left( 0 + \frac{3}{4} \right) = \frac{3}{2}$, and the example confirms this by a direct computation.

### Why each hypothesis is needed

The columns of $Q_1$ and $Q_2$ must be orthonormal.
For $U = W = \R^1$ with $Q_1 = Q_2 = (2)$, the matrix $Q_1^{\mathsf{T}} Q_2 = (4)$ has singular value $4$, which is not a cosine.
With bases that are not orthonormal, the singular values mix lengths with angles.

The order $p \le q$ only fixes the roles of the two subspaces.
The definition pairs each of the $p$ directions of the smaller subspace with a direction of the larger one, and for $p > q$ we exchange $U$ and $W$.
The matrix $M^{\mathsf{T}} = Q_2^{\mathsf{T}} Q_1$ has the same nonzero singular values as $M$, so nothing is lost.

### What it gives you

Two subspaces are equal if and only if $p = q$ and all principal angles are $0$, because by part 3 all $p$ angles are $0$ exactly when $U \subseteq W$.
Two subspaces are orthogonal if and only if $M = 0$, since all singular values vanish only for the zero matrix, and then every angle is $\pi/2$.
Two distinct planes through the origin in $\R^3$ meet in a line, since their sum is $\R^3$, so by part 3 one angle is $0$ and the other is the dihedral angle.
Part 4 says that for a line no singular value decomposition is needed at all, as the [[line and plane example|4QPRPFVH6C]] shows.

### Generalizations

Over $\C$ the same statement holds with $Q_1^* Q_2$ in place of $Q_1^{\mathsf{T}} Q_2$ and with $\abs{\ip{u}{w}}$ in the definition.
In computation, $Q_1$ and $Q_2$ come from a [[QR decomposition|0ERWG4NXQ9]] of matrices whose columns span $U$ and $W$.
When some angles are very small, their cosines are all close to $1$ and lose accuracy, so numerical codes compute the small angles from the sines, which come from the singular values of $(I - Q_2 Q_2^{\mathsf{T}}) Q_1$.

## Explanations

### L1 human

To find the angles between two subspaces, write orthonormal bases of both as the columns of two matrices.
Multiply the transpose of the first matrix by the second.
The result is a small table of dot products, of size $2 \times 2$ for two planes.
Its singular values are the cosines of the principal angles.
For two planes in space that share a line, the answer is always $1$ and the cosine of the angle between the planes.

### L2 human

Take the line $\R(1, 1, 1)$ and the plane $z = 0$ in $\R^3$.
Here $Q_1 = \frac{1}{\sqrt 3}(1, 1, 1)^{\mathsf{T}}$ and $Q_2$ has columns $e_1$ and $e_2$, so
$$M = Q_1^{\mathsf{T}} Q_2 = \tfrac{1}{\sqrt 3} \begin{pmatrix} 1 & 1 \end{pmatrix}, \qquad M M^{\mathsf{T}} = \tfrac{2}{3}.$$
So $\sigma_1 = \sqrt{2/3}$ and $\theta_1 = \arccos \sqrt{2/3} \approx 35.26^\circ$.
Part 4 gives the same number as the length of the projection $\frac{1}{\sqrt 3}(1, 1, 0)$.
The typical use is to compare two subspaces, for example the column spaces of two data matrices, by a few numbers that do not depend on the bases.
Watch out: the bases must be orthonormal, or the singular values are not cosines.

### L3 human

Part 5 shows that the distance $\norm{P_U - P_W}_F$ between subspaces of the same dimension depends only on the principal angles.
Part 2 gives bases of $U$ and $W$ in which the map $u \mapsto P_W u$ from $U$ to $W$ has a diagonal matrix with entries $\cos \theta_k$.
The same idea, a singular value decomposition of the cross matrix of two orthonormal bases, gives the canonical correlations of statistics and the sine bounds for perturbed invariant subspaces in numerical analysis.
