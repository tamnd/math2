---
tag: 000NPTMX6J
kind: statement
role: theorem
name: Singular value decomposition
msc: [15A18, 15A23]
topics: [SS4EVPKT3A]
audience: ug1
about: [09VMDSRXWJ, 0AR68JTMDT]
uses: [0K2TX12X58, 0D6RMJ10M9, 0EX045E2BP, 0F0RPPJ2TT, 0PQ2GGY1QV]
proofs: [31AT4VJF68]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_value_decomposition
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Singular_value_decomposition
    locator: Reduced SVDs
  - url: https://en.wikipedia.org/wiki/Singular_value_decomposition
    locator: Relation to the four fundamental subspaces
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section7-4.xml#L1216
    locator: src/section7-4.xml:1216
  - book: isbn:9780321982384
    locator: Section 7.4
  - book: isbn:9781733146678
    locator: Chapter 7
same_as:
  wikidata: Q420904
  wikipedia: Singular value decomposition
---

## Statement

Every matrix, square or rectangular, is a unitary change of coordinates, then a scaling of the axes by nonnegative numbers, then another unitary change of coordinates.

Let $A$ be an $m \times n$ complex matrix of rank $r$, and let $p = \min(m, n)$.

1. Full form. There are a [[unitary matrix|0AR68JTMDT]] $U$ of size $m \times m$, a unitary matrix $V$ of size $n \times n$, and an $m \times n$ matrix $\Sigma$ with
$$A = U \Sigma V^*.$$
Here $\Sigma_{ij} = 0$ for $i \ne j$, and the diagonal entries $\Sigma_{11} \ge \Sigma_{22} \ge \cdots \ge \Sigma_{pp} \ge 0$ are the first $p$ [[singular values|09VMDSRXWJ]] $\sigma_1, \dots, \sigma_p$ of $A$.
2. Reduced form. Let $u_i$ and $v_i$ be the columns of $U$ and $V$. Then $\sigma_i > 0$ for $i \le r$ and $\sigma_i = 0$ for $i > r$, and
$$A = U_r \Sigma_r V_r^* = \sum_{i=1}^r \sigma_i u_i v_i^*,$$
where $U_r = (u_1 \cdots u_r)$ is $m \times r$, $V_r = (v_1 \cdots v_r)$ is $n \times r$, and $\Sigma_r = \operatorname{diag}(\sigma_1, \dots, \sigma_r)$ is $r \times r$.
3. Four subspaces. The vectors $u_1, \dots, u_r$ are an orthonormal basis of the [[column space|03AJKXH1AV]] of $A$, and $u_{r+1}, \dots, u_m$ are one of the null space of $A^*$. The vectors $v_1, \dots, v_r$ are an orthonormal basis of the column space of $A^*$, and $v_{r+1}, \dots, v_n$ are one of the [[null space|0PHDYNR24D]] of $A$.
4. Uniqueness of $\Sigma$ and the real case. In every decomposition as in part 1, the diagonal of $\Sigma$ consists of the singular values of $A$. If $A$ is real, then $U$ and $V$ can be chosen real orthogonal, so that $A = U \Sigma V^{\mathsf{T}}$.

The [[proof from the spectral theorem|31AT4VJF68]] diagonalizes $A^* A$ to find $V$ and then builds $U$ from the vectors $A v_i$.

## Remarks

### A first decomposition

Take $A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix}$.
The [[worked 2 by 2 example|B546BDVFQZ]] finds the eigenvalues $45$ and $5$ of $A^{\mathsf{T}} A$, the eigenvectors $v_1 = \tfrac{1}{\sqrt2}(1, 1)$ and $v_2 = \tfrac{1}{\sqrt2}(-1, 1)$, and the vectors $u_i = A v_i / \sigma_i$.
The result is
$$\begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix} = \frac{1}{\sqrt{10}} \begin{pmatrix} 1 & -3 \\ 3 & 1 \end{pmatrix} \begin{pmatrix} 3\sqrt5 & 0 \\ 0 & \sqrt5 \end{pmatrix} \frac{1}{\sqrt2} \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}.$$
Check: the first two factors give $\tfrac{1}{\sqrt2} \begin{pmatrix} 3 & -3 \\ 9 & 1 \end{pmatrix}$, and multiplying by the last factor gives $\tfrac12 \begin{pmatrix} 6 & 0 \\ 8 & 10 \end{pmatrix}$, which is $A$.
In the plane, $V^{\mathsf{T}}$ and $U$ are rotations and $\Sigma$ stretches the two axes, so [[the unit circle goes to an ellipse|JAEKA59DNZ]] with semi-axes $3\sqrt5$ and $\sqrt5$.

### Full, reduced and thin forms

The shape of $\Sigma$ depends on the form, and books do not agree on which form they mean.
In the full form, $\Sigma$ has the shape $m \times n$ of $A$, and $U$ and $V$ are square.
In the reduced form, $\Sigma_r$ is square of size $r \times r$, and $U_r$ and $V_r$ keep only the first $r$ columns.
Some books also use a thin form with $U_p$ of size $m \times p$ and a square $\Sigma_p$ of size $p \times p$.
All forms give the same product, because the extra columns of $U$ and $V$ meet only zeros of $\Sigma$.
The [[full and reduced SVD of a 3 by 2 matrix|GK1B93DKD3]] shows a $3 \times 2$ matrix $\Sigma$ in the full form and a $2 \times 2$ one in the reduced form.
The real reduced form is also stated as [[the reduced SVD|AAB852BV8Q]].

### The four subspaces in the singular vectors

Part 3 gives orthonormal bases of all four fundamental subspaces at once.
For a real matrix the column space of $A^{\mathsf{T}}$ is the [[row space|069MCGX635]] of $A$, so the first $r$ columns of $V$ span the row space and the last $n - r$ span the null space.
In the same way the first $r$ columns of $U$ span the column space and the last $m - r$ span the null space of $A^{\mathsf{T}}$.
For the $3 \times 2$ example, $u_1, u_2$ span the plane $x_1 - x_2 - x_3 = 0$, and $u_3 = \tfrac{1}{\sqrt3}(1, -1, -1)$ spans the null space of $A^{\mathsf{T}}$.
The real version of part 3 is also stated as [[the SVD and the four fundamental subspaces|AF6KN2T3EX]].

### What is unique and what is not

The theorem has no hypothesis on $A$: every matrix has an SVD, including rectangular and singular ones.
The factor $\Sigma$ is unique by part 4, but $U$ and $V$ are not.
Changing the signs of $u_i$ and $v_i$ together keeps every term $\sigma_i u_i v_i^*$.
For $A = I_n$, every unitary $W$ gives $I_n = W I_n W^*$, so there are infinitely many choices.
The decreasing order of the $\sigma_i$ is a convention; without it, $\Sigma$ is unique only up to a reordering of its diagonal.

### What it gives you

The SVD is the source of most of the later results of the sub-area.
The rank of $A$ is the number of nonzero singular values.
For a square $A$, regrouping gives the [[polar decomposition|0J2C7BDJQA]] $A = (U V^*)(V \Sigma V^*)$.
Inverting the nonzero singular values gives the [[Moore-Penrose inverse|0YY8VX28JR]] $A^+ = V \Sigma^+ U^*$, by [[its SVD formula|Q9YN0F60ZW]], and the reduced form solves [[least squares problems|SBP2PCHH9M]].
Cutting the sum of part 2 after $k$ terms gives the best rank-$k$ approximation, by the [[Eckart-Young-Mirsky theorem|JJT6GC055J]].
Taking adjoints gives the SVD $A^* = V \Sigma^{\mathsf{T}} U^*$, as in [[the transpose of an SVD|TTJBJ9H02C]].
In statistics, the SVD of a centered data matrix gives [[principal component analysis|ABXD13M340]].

### The converse

If $A = U \Sigma V^*$ with $U$, $V$ unitary and $\Sigma$ as in part 1, then
$$A^* A = V \Sigma^{\mathsf{T}} U^* U \Sigma V^* = V (\Sigma^{\mathsf{T}} \Sigma) V^*.$$
So the columns of $V$ are eigenvectors of $A^* A$, and the eigenvalues are the squares of the diagonal entries of $\Sigma$.
In the same way $A A^* = U (\Sigma \Sigma^{\mathsf{T}}) U^*$, so the columns of $U$ are eigenvectors of $A A^*$.
This is why part 4 holds.

### Watch out

The singular values are not the absolute values of the eigenvalues unless $A$ is [[normal|0MR0BYF0K2]].
For $A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix}$ the eigenvalues are $3$ and $5$, while the singular values are $3\sqrt5 \approx 6.71$ and $\sqrt5 \approx 2.24$.
A second trap is to compute $U$ and $V$ separately, from $A A^*$ and $A^* A$.
Each eigenvector is fixed only up to sign, so the product can come out wrong: for the example above, replacing $u_1$ by $-u_1$ and keeping $v_1$ changes $A$.
The safe move is to compute $u_i = A v_i / \sigma_i$ for $\sigma_i > 0$.

### Generalizations

For a linear map $T \colon V \to W$ between finite-dimensional inner product spaces, there are orthonormal bases of $V$ and $W$ in which the matrix of $T$ is $\Sigma$.
Compact operators on Hilbert spaces have a Schmidt decomposition $T = \sum_i \sigma_i \ip{\cdot}{v_i} u_i$, which belongs to functional analysis.

### Try it

First, find an SVD of $A = \operatorname{diag}(-3, 2)$.
Take $V = I$, $\Sigma = \operatorname{diag}(3, 2)$ and $U = \operatorname{diag}(-1, 1)$; then $U \Sigma V^{\mathsf{T}} = \operatorname{diag}(-3, 2)$.

Second, find the full SVD of the column $A = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$.
Here $A^{\mathsf{T}} A = (25)$, so $\sigma_1 = 5$, $V = (1)$, $u_1 = \tfrac15(3, 4)$, $u_2 = \tfrac15(-4, 3)$, and $\Sigma = \begin{pmatrix} 5 \\ 0 \end{pmatrix}$ has the shape $2 \times 1$ of $A$.

## History

Beltrami in 1873 and Jordan in 1874 found the decomposition independently, for real bilinear forms.
Sylvester found it for real square matrices in 1889, and Autonne in 1915 reached it through the polar decomposition.
The first proof for rectangular and complex matrices seems to be the one of Eckart and Young in 1936.

## Explanations

### L1 human

Every matrix is a turn, then a stretch along two perpendicular axes, then another turn.
The stretch factors are the singular values.
In the plane, the matrix turns the unit circle into an ellipse.
The columns of $V$ are the arrows on the circle that go to the ends of the axes of the ellipse, and the columns of $U$ point along those axes.

### L2 human

Here is the typical recipe for the full SVD of a real matrix $A$.
First compute $A^{\mathsf{T}} A$ and an orthonormal basis $v_1, \dots, v_n$ of its eigenvectors, with the eigenvalues in decreasing order.
Then put $\sigma_i = \sqrt{\lambda_i}$, and $u_i = A v_i / \sigma_i$ for each $\sigma_i > 0$.
Complete $u_1, \dots, u_r$ to an orthonormal basis of $\R^m$, for example with an orthonormal basis of the null space of $A^{\mathsf{T}}$.
Finally check $A = U \Sigma V^{\mathsf{T}}$ by multiplying back, as in the first decomposition above.
Watch out: give $\Sigma$ the shape of $A$ in the full form, and the shape $r \times r$ in the reduced form.

### L3 human

The SVD is the spectral theorem for the pair $A^* A$ and $A A^*$, joined by $A$.
It says that the group $U(m) \times U(n)$, acting on $m \times n$ matrices by $(W, X) \cdot A = W A X^*$, has the diagonal matrices with decreasing nonnegative entries as a set of orbit representatives.
The rank-one expansion $A = \sum \sigma_i u_i v_i^*$ is the finite form of the Schmidt decomposition, and in quantum information it is the Schmidt decomposition of a pure state of two systems.
In numerical linear algebra the SVD is computed without forming $A^* A$, because forming it squares the condition number.
