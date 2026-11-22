---
tag: G0H3BKBPMV
kind: proof
name: Proof of the classification of O(3) and Euler's rotation theorem
msc: ["15B10", "51F25"]
topics: [AZS5BPF5H3]
audience: ug2
proves: 2ZVG43GSKA
uses: [04CPJ6AF00, 0ZZQ2E1MTE, FBSAPTP1PR, F7M8ZXB4P7, XAVVA317M0, 191HBJ7PVZ]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_rotation_theorem
    locator: Matrix proof
  - url: https://en.wikipedia.org/wiki/Rotation_matrix
    locator: Determining the angle
---

## Proof

We find the axis from a determinant identity, then change to an orthonormal basis adapted to the axis, and read the trace and the skew part in that basis.
Throughout, let $N = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix}$ and $D = \operatorname{diag}(1, -1)$.

**Part 1.**

1. Since $RR^{\mathsf{T}} = I_3$ by [[the equivalent conditions|F7M8ZXB4P7]], we can write $R - I_3 = R - RR^{\mathsf{T}} = R(I_3 - R^{\mathsf{T}}) = R(I_3 - R)^{\mathsf{T}}$.
2. By [[multiplicativity|04CPJ6AF00]] and [[the transpose rule|0ZZQ2E1MTE]], $\det(R - I_3) = \det R \cdot \det(I_3 - R)$.
3. Here $\det R = 1$, and $\det(I_3 - R) = (-1)^3\det(R - I_3)$ because negating all three rows changes the sign three times.
4. So $\det(R - I_3) = -\det(R - I_3)$, and therefore $\det(R - I_3) = 0$.
5. By [[the determinant test|FBSAPTP1PR]], $R - I_3$ is not invertible, so there is $x \neq 0$ with $Rx = x$. Let $u = x / \norm{x}$.

**Part 2.**

6. Let $W = u^\perp$. For $x \in W$ we have $\ip{Rx}{u} = \ip{Rx}{Ru} = \ip{x}{u} = 0$, because $R$ keeps dot products. So $R(W) \subseteq W$.
7. Choose a unit vector $v \in W$ and let $w = u \times v$. Then $u, v, w$ is an orthonormal basis, with $u \times v = w$, $v \times w = u$ and $w \times u = v$.
8. Let $P$ be the matrix with columns $u, v, w$. It is orthogonal, and $\det P = \ip{u \times v}{w} = \ip{w}{w} = 1$, so $P \in SO(3)$.
9. Let $B = P^{\mathsf{T}}RP$, the matrix of $R$ in the basis $u, v, w$. It is orthogonal as a product of orthogonal matrices, and $\det B = \det R = 1$.
10. We have $Be_1 = P^{\mathsf{T}}Ru = P^{\mathsf{T}}u = e_1$, and then $B^{\mathsf{T}}e_1 = B^{-1}e_1 = e_1$. So the first column of $B$ is $e_1$ and the first row is $e_1^{\mathsf{T}}$.
11. So $B = \begin{pmatrix} 1 & 0 \\ 0 & A \end{pmatrix}$ with $A$ orthogonal of size $2$ and $\det A = \det B = 1$.
12. By part 3 of [[the index-two theorem|XAVVA317M0]], $A = R(\varphi)$ for some $\varphi \in (-\pi, \pi]$.
13. If $\varphi \ge 0$, let $\theta = \varphi$. If $\varphi < 0$, replace the basis $u, v, w$ by $-u, v, -w$; it is again orthonormal with $(-u) \times v = -w$, and $P$ becomes $P\operatorname{diag}(-1, 1, -1)$.
14. In the new basis the first entry of $B$ is still $1$, and the block $A$ becomes $DAD = R(-\varphi)$, by multiplying out the three $2 \times 2$ matrices. Let $\theta = -\varphi \in (0, \pi)$.
15. In both cases $\theta \in [0, \pi]$ and $B = \operatorname{diag}(1, R(\theta))$. Reading the columns of $B$ gives $Ru = u$, $Rv = \cos\theta\,v + \sin\theta\,w$ and $Rw = -\sin\theta\,v + \cos\theta\,w$.

**Part 3.**

16. Since $R = PBP^{\mathsf{T}} = PBP^{-1}$, the matrix $R$ is similar to $B$, and similar matrices have the same trace by [[the similarity invariants|191HBJ7PVZ]].
17. So $\tr R = \tr B = 1 + 2\cos\theta$.

**Part 4.**

18. We compute $B - B^{\mathsf{T}} = \begin{pmatrix} 0 & 0 \\ 0 & R(\theta) - R(-\theta) \end{pmatrix}$, and $R(\theta) - R(-\theta) = \begin{pmatrix} 0 & -2\sin\theta \\ 2\sin\theta & 0 \end{pmatrix}$. So $B - B^{\mathsf{T}} = 2\sin\theta\,N$.
19. By step 7, the map $x \mapsto u \times x$ sends $u$ to $0$, $v$ to $w$ and $w$ to $u \times w = -v$. So its matrix in the basis $u, v, w$ is $N$, and $[u]_\times = PNP^{\mathsf{T}}$.
20. So $R - R^{\mathsf{T}} = P(B - B^{\mathsf{T}})P^{\mathsf{T}} = 2\sin\theta\,PNP^{\mathsf{T}} = 2\sin\theta\,[u]_\times$.
21. The entries $(3, 2)$, $(1, 3)$ and $(2, 1)$ of $[u]_\times$ are $u_1$, $u_2$ and $u_3$. For $0 < \theta < \pi$ we have $\sin\theta > 0$, and dividing by $2\sin\theta$ gives the formula for $u$.

**Part 5.**

22. Let $Q \in O(3)$ with $\det Q = -1$. Then $-Q$ is orthogonal, and $\det(-Q) = (-1)^3\det Q = 1$, so $-Q \in SO(3)$.
23. Apply part 2 to $-Q$: in an orthonormal basis $u, v, w$ with $w = u \times v$, the matrix of $-Q$ is $\operatorname{diag}(1, R(\theta))$ with $\theta \in [0, \pi]$.
24. So the matrix of $Q$ is $\operatorname{diag}(-1, -R(\theta)) = \operatorname{diag}(-1, R(\theta + \pi))$, because $-R(\theta) = R(\pi)R(\theta)$.
25. Replace $u, v, w$ by $-u, v, -w$ as in steps 13 and 14. The first entry stays $-1$, and the block becomes $R(-\theta - \pi) = R(\pi - \theta)$. Let $\psi = \pi - \theta \in [0, \pi]$.
26. For $\psi = 0$ the matrix is $\operatorname{diag}(-1, 1, 1)$, so $Q$ fixes $u^\perp$ and negates $u$, and $Q$ is the reflection in $u^\perp$.
27. For $\psi = \pi$ the matrix is $-I_3$, and so $Q = -I_3$. $\blacksquare$

## Idea

In odd dimension, the identity $\det(R - I) = -\det(R - I)$ forces the eigenvalue $1$, and that eigenvector is the axis.
The plane perpendicular to the axis is mapped to itself, and on that plane $R$ is a rotation of the plane.
The trace does not change under a change of orthonormal basis, and the skew part $R - R^{\mathsf{T}}$ changes in the same way as the matrix of $x \mapsto u \times x$.
So the trace gives the angle, and the skew part gives the axis.

## Variants

Part 1 also follows from the eigenvalues.
The non-real roots of the characteristic polynomial come in pairs $\lambda, \overline{\lambda}$ with $\lambda\overline{\lambda} = 1$, and all roots have modulus $1$ by [[the determinant theorem|QDZJMFATRW]].
So each real root is $1$ or $-1$, and there is at least one real root, since the degree $3$ is odd.
The product of all three roots is $\det R = 1$, and the pairs contribute $1$, so the real roots multiply to $1$ and one of them is $1$.
Part 2 is also the case $n = 3$ of [[the normal form of orthogonal matrices|QTY3VMFGY1]].
