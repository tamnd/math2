---
tag: Q7T3PFS02Z
kind: proof
name: Proof of the normal form of an orthogonal matrix
msc: ["15B10", "15A21"]
topics: [AZS5BPF5H3]
audience: grad
proves: QTY3VMFGY1
uses: [F7M8ZXB4P7, 0XYKE8BE7X, G6T1FNE3JC, WWK2E8BRGF, 0Q5SM60HTH, 191HBJ7PVZ, 0J9TVTNB4K, 039HF58KQ5]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_matrix
    locator: Canonical form
  - url: https://en.wikipedia.org/wiki/Orthogonal_group
    locator: Canonical form
---

## Proof

We apply the real normal form to $Q$, use orthogonality to pin down each block, and read the invariants from the characteristic polynomial.
Let $Q$ be a real $n \times n$ orthogonal matrix, and let $R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$.

**Part 1.**

1. From $Q^{\mathsf{T}}Q = I_n$ we get $Q^{\mathsf{T}} = Q^{-1}$ and so $QQ^{\mathsf{T}} = I_n$, by [[the equivalent conditions|F7M8ZXB4P7]]. Hence $QQ^{\mathsf{T}} = Q^{\mathsf{T}}Q$, and $Q$ is a [[normal matrix|0XYKE8BE7X]].
2. By part 1 of [[the real normal form|G6T1FNE3JC]], there is an orthogonal matrix $P_0$ such that $M = P_0^{\mathsf{T}}QP_0$ is block diagonal, and each block is a $1 \times 1$ block $(c)$ or a block $B = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ with $b > 0$.
3. The matrix $M$ is orthogonal, because it is a product of three orthogonal matrices and the orthogonal matrices form the [[group|WWK2E8BRGF]] $O(n)$.
4. For $M = \operatorname{diag}(B_1, \dots, B_r)$, block multiplication gives $M^{\mathsf{T}}M = \operatorname{diag}(B_1^{\mathsf{T}}B_1, \dots, B_r^{\mathsf{T}}B_r)$. Since $M^{\mathsf{T}}M = I_n$, each block satisfies $B_i^{\mathsf{T}}B_i = I$.
5. A $1 \times 1$ block $(c)$ with $c^2 = 1$ has $c = 1$ or $c = -1$.
6. A $2 \times 2$ block has $B^{\mathsf{T}}B = (a^2 + b^2)I_2$, by multiplying out. So $a^2 + b^2 = 1$, and $(a, b)$ is a point of the unit circle.
7. Since $b > 0$, this point lies on the upper half of the circle. So there is exactly one $\theta \in (0, \pi)$ with $a = \cos\theta$ and $b = \sin\theta$, and then $B = R(\theta)$.
8. Let $\Pi$ be a [[permutation matrix|0Q5SM60HTH]] that moves whole blocks of coordinates. Then $\Pi^{\mathsf{T}}M\Pi$ is block diagonal with the same blocks in a new order, because conjugation by $\Pi$ only renames the coordinates.
9. Choose $\Pi$ so that the blocks $R(\theta_j)$ come first with $\theta_1 \le \dots \le \theta_k$, then the $q$ blocks $(-1)$, then the $p$ blocks $(1)$.
10. Let $P = P_0\Pi$, which is orthogonal by step 3. Then $P^{\mathsf{T}}QP = \Pi^{\mathsf{T}}M\Pi = \operatorname{diag}(R(\theta_1), \dots, R(\theta_k), -I_q, I_p)$, and counting sizes gives $2k + q + p = n$.

**Part 2.**

11. The matrix $P^{\mathsf{T}}QP = P^{-1}QP$ is similar to $Q$, so it has the same [[characteristic polynomial|039HF58KQ5]] $\chi_Q$, by [[the similarity invariants|191HBJ7PVZ]].
12. The matrix $tI - P^{\mathsf{T}}QP$ is block diagonal, so by [[the block determinant formula|0J9TVTNB4K]] its determinant is the product of the determinants of its blocks.
13. For one rotation block,
$$\det(tI_2 - R(\theta)) = (t - \cos\theta)^2 + \sin^2\theta = t^2 - 2t\cos\theta + 1,$$
with the roots $e^{i\theta}$ and $e^{-i\theta}$, which are not real because $\sin\theta > 0$ for $0 < \theta < \pi$.
14. By steps 11 to 13, $\chi_Q(t) = \prod_{j=1}^{k}(t^2 - 2t\cos\theta_j + 1) \cdot (t + 1)^q(t - 1)^p$.
15. The roots of $\chi_Q$ with positive imaginary part are the numbers $e^{i\theta_j}$, counted with multiplicity. Each $\theta_j \in (0, \pi)$ is the argument of its root, so the sorted list $\theta_1 \le \dots \le \theta_k$ is determined by $\chi_Q$.
16. The numbers $q$ and $p$ are the multiplicities of the roots $-1$ and $1$ of $\chi_Q$, and then $k = (n - q - p)/2$. So all of $k$, $q$, $p$ and the angles depend only on $Q$.

**Part 3.**

17. We have $\det(P^{\mathsf{T}}QP) = \det P^{\mathsf{T}} \det Q \det P = \det Q$, because $\det P^{\mathsf{T}} \det P = \det(P^{\mathsf{T}}P) = 1$.
18. By [[the block determinant formula|0J9TVTNB4K]], $\det(P^{\mathsf{T}}QP)$ is also the product of the determinants of the blocks, and $\det R(\theta_j) = \cos^2\theta_j + \sin^2\theta_j = 1$, $\det(-I_q) = (-1)^q$ and $\det I_p = 1$.
19. So $\det Q = (-1)^q$ by steps 17 and 18, and $\det Q = 1$ exactly when $q$ is even.

**The converse remark.**

20. If $Q_1 = P_1 N P_1^{\mathsf{T}}$ and $Q_2 = P_2 N P_2^{\mathsf{T}}$ have the same normal form $N$, then $Q_2 = (P_2P_1^{\mathsf{T}})Q_1(P_2P_1^{\mathsf{T}})^{\mathsf{T}}$, and $P_2P_1^{\mathsf{T}}$ is orthogonal by step 3.
21. Conversely, if $Q_1$ and $Q_2$ are similar, then they have the same characteristic polynomial, and so the same normal form by part 2. $\blacksquare$

## Idea

An orthogonal matrix commutes with its transpose, so it is normal, and the real normal form applies to it.
That form already has the right shape: blocks of size $1$ and rotation-like blocks of size $2$.
Orthogonality then forces each block to keep lengths, so the $1 \times 1$ blocks are $\pm 1$ and the $2 \times 2$ blocks are true rotations.
The characteristic polynomial, which does not see the change of basis, records every angle and every sign.

## Variants

A complex proof avoids the real normal form.
The matrix $Q$ is unitary, so $\C^n$ has an orthonormal basis of eigenvectors, by [[the properties of unitary matrices|GZ7NG7J3J8]].
Let $v = x + iy$ be an eigenvector for $e^{i\theta}$ with $0 < \theta < \pi$.
Then $\overline{v}$ is an eigenvector for $e^{-i\theta}$, a different eigenvalue, so $v$ and $\overline{v}$ are orthogonal.
Writing out $\sum_j v_j^2 = 0$ shows that $x$ and $y$ are orthogonal and have the same length.
Comparing real and imaginary parts of $Qv = e^{i\theta}v$ shows that, in the basis $y, x$ of their plane, the matrix of $Q$ is $R(\theta)$.

An inductive proof is also common.
A real matrix has a real eigenvector or a two-dimensional invariant subspace, from a real or a complex root of its characteristic polynomial.
The orthogonal complement of an invariant subspace of $Q$ is again invariant, because $Q^{\mathsf{T}} = Q^{-1}$ maps the subspace onto itself.
Induction on $n$ then gives the blocks.
