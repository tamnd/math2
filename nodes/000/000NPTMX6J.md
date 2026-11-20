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

Let $A$ be an $m \times n$ complex matrix of rank $r$, and let $p = \min(m, n)$.

1. Full form. There are a [[unitary matrix|0AR68JTMDT]] $U$ of size $m \times m$, a unitary matrix $V$ of size $n \times n$, and an $m \times n$ matrix $\Sigma$ with
$$A = U \Sigma V^*.$$
Here $\Sigma_{ij} = 0$ for $i \ne j$, and $\Sigma_{11} \ge \Sigma_{22} \ge \cdots \ge \Sigma_{pp} \ge 0$ are the first $p$ [[singular values|09VMDSRXWJ]] $\sigma_1, \dots, \sigma_p$ of $A$.
2. Reduced form. Let $u_i$ and $v_i$ be the columns of $U$ and $V$. Then $\sigma_1, \dots, \sigma_r > 0 = \sigma_{r+1}$, and
$$A = U_r \Sigma_r V_r^* = \sum_{i=1}^r \sigma_i u_i v_i^*,$$
where $U_r = (u_1 \cdots u_r)$ is $m \times r$, $V_r = (v_1 \cdots v_r)$ is $n \times r$, and $\Sigma_r = \operatorname{diag}(\sigma_1, \dots, \sigma_r)$ is $r \times r$.
3. Four subspaces. The vectors $u_1, \dots, u_r$ are an orthonormal basis of the [[column space|03AJKXH1AV]] of $A$, and $u_{r+1}, \dots, u_m$ of the null space of $A^*$. The vectors $v_1, \dots, v_r$ are an orthonormal basis of the column space of $A^*$, and $v_{r+1}, \dots, v_n$ of the [[null space|0PHDYNR24D]] of $A$.
4. In every decomposition as in part 1, the diagonal of $\Sigma$ consists of the singular values of $A$. If $A$ is real, then $U$ and $V$ can be chosen real orthogonal, and $A = U \Sigma V^T$.

## Remarks

Warning on shapes: $\Sigma$ is $m \times n$ in the full form and square, $r \times r$, in the reduced form.
Some books use a third, thin form with $U_p$ of size $m \times p$ and $\Sigma_p$ of size $p \times p$.
For a real matrix the column space of $A^* = A^T$ is the [[row space|069MCGX635]] of $A$.
The real version of part 3 is also stated as [[the SVD and the four fundamental subspaces|AF6KN2T3EX]], and the real reduced form as [[the reduced SVD|AAB852BV8Q]].

### Why each hypothesis is needed

- There is no hypothesis on $A$: every matrix has an SVD, also a rectangular or singular one.
- $U$ and $V$ are not unique. For $A = I_n$, every $U = V$ unitary gives $I = U I U^*$. Changing the signs of $u_i$ and $v_i$ together also keeps $A$.
- The order of the $\sigma_i$ is a convention. Without it, $\Sigma$ is unique only up to a permutation.

### Consequences

- [[The $2 \times 2$ example|~ab3b9c7a]] and [[the $3 \times 2$ example|~461482fa]] compute full SVDs and multiply them back.
- [[The unit circle goes to an ellipse|~16170aab]] with semi-axes $\sigma_1 u_1$ and $\sigma_2 u_2$.
- The rank of $A$ is the number of nonzero singular values.
- The [[polar decomposition|0J2C7BDJQA]] of a square $A$ is $A = (U V^*)(V \Sigma V^*)$.
- The [[Moore-Penrose inverse|0YY8VX28JR]] is $A^+ = V \Sigma^+ U^*$, by [[its SVD formula|~724d9669]].
- Truncating the sum in part 2 after $k$ terms gives the best rank-$k$ approximation, by the [[Eckart-Young-Mirsky theorem|JJT6GC055J]].
- The SVD of $A^*$ is $V \Sigma^T U^*$; see [[the transpose of an SVD|TTJBJ9H02C]].
- The reduced form solves [[least squares problems|SBP2PCHH9M]].
- In statistics, the SVD of a centred data matrix gives [[principal component analysis|ABXD13M340]].

### Converse

If $A = U \Sigma V^*$ with $U$, $V$ unitary and $\Sigma$ as in part 1, then $A^* A = V (\Sigma^T \Sigma) V^*$.
So the columns of $V$ are eigenvectors of $A^* A$, and the squares $\sigma_i^2$ are its eigenvalues.
This is part 4.

### Generalizations

- For a linear map $T \colon V \to W$ between finite-dimensional inner product spaces, there are orthonormal bases of $V$ and $W$ in which $T$ has the matrix $\Sigma$.
- Compact operators on Hilbert spaces have a Schmidt decomposition $T = \sum_i \sigma_i \ip{\cdot}{v_i} u_i$; this belongs to functional analysis.

## History

According to the Wikipedia article on the SVD, Beltrami in 1873 and Jordan in 1874 found it independently, for real bilinear forms.
The same article says that Sylvester found it for real square matrices in 1889, and Autonne in 1915 by the polar decomposition.
It says that the first proof for rectangular and complex matrices seems to be by Eckart and Young in 1936.

## Explanations

### L1 human

Every matrix is a rotation, then a stretch along the axes, then another rotation.
The stretch factors are the singular values.
In the plane, the matrix turns the unit circle into an ellipse.
The columns of $V$ are the directions that go to the axes of the ellipse, and the columns of $U$ are the directions of those axes.

### L2 human

Recipe for the full SVD of a real $A$:

1. Compute $A^T A$ and an orthonormal basis $v_1, \dots, v_n$ of eigenvectors, with eigenvalues in decreasing order.
2. Put $\sigma_i = \sqrt{\lambda_i}$, and $u_i = A v_i / \sigma_i$ for $\sigma_i > 0$.
3. Complete $u_1, \dots, u_r$ to an orthonormal basis of $\R^m$, for example by a basis of the null space of $A^T$.
4. Check $A = U \Sigma V^T$ by multiplying back.

A trap: computing $U$ and $V$ separately from $A A^T$ and $A^T A$ can give wrong signs.
Always compute $u_i = A v_i / \sigma_i$.
Another trap: $\Sigma$ has the shape of $A$ in the full form, and the shape $r \times r$ in the reduced form.

### L3 human

The SVD is the spectral theorem for the pair $(A^* A, A A^*)$, joined by $A$.
It says that $U(m) \times U(n)$ acting on $m \times n$ matrices by $(W, X) \cdot A = W A X^*$ has the diagonal matrices with decreasing nonnegative entries as a set of orbit representatives.
The rank-one expansion $A = \sum \sigma_i u_i v_i^*$ is the finite form of the Schmidt decomposition, and in quantum information it is the Schmidt decomposition of a pure state of two systems.
In numerical linear algebra the SVD is computed without forming $A^* A$, for reasons of accuracy.
