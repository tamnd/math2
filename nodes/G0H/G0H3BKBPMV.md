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

Let $N = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix}$ and $D = \operatorname{diag}(1, -1)$.

**Part 1.**

1. $R - I_3 = R - RR^T = R(I_3 - R^T) = R(I_3 - R)^T$, because $RR^T = I_3$ by [[the equivalent conditions|F7M8ZXB4P7]].
2. So $\det(R - I_3) = \det R \det(I_3 - R)$, by [[multiplicativity|04CPJ6AF00]] and [[the transpose rule|0ZZQ2E1MTE]].
3. $\det R = 1$, and $\det(I_3 - R) = (-1)^3\det(R - I_3)$, because the size is $3$.
4. So $\det(R - I_3) = -\det(R - I_3)$, and $\det(R - I_3) = 0$.
5. So $R - I_3$ is not invertible, by [[the determinant test|FBSAPTP1PR]], and there is $x \neq 0$ with $Rx = x$. Let $u = x/\norm{x}$.

**Part 2.**

6. Let $W = u^\perp$. For $x \in W$, $\ip{Rx}{u} = \ip{Rx}{Ru} = \ip{x}{u} = 0$, because $R$ keeps dot products. So $R(W) \subseteq W$.
7. Choose a unit vector $v \in W$, and let $w = u \times v$. Then $u, v, w$ is an orthonormal basis, and $u \times v = w$, $v \times w = u$ and $w \times u = v$.
8. Let $P$ be the matrix with columns $u, v, w$. It is orthogonal, and $\det P = \ip{u \times v}{w} = \ip{w}{w} = 1$. So $P \in SO(3)$.
9. Let $B = P^TRP$, the matrix of $R$ in the basis $u, v, w$. It is orthogonal, and $\det B = \det R = 1$.
10. $Be_1 = P^TRu = P^Tu = e_1$. Also $B^Te_1 = B^{-1}e_1 = e_1$. So the first column and the first row of $B$ are $e_1$ and $e_1^T$.
11. So $B = \begin{pmatrix} 1 & 0 \\ 0 & A \end{pmatrix}$ with $A$ orthogonal of size $2$ and $\det A = \det B = 1$.
12. By part 3 of [[the index-two theorem|XAVVA317M0]], $A = R(\varphi)$ for some $\varphi \in (-\pi, \pi]$.
13. If $\varphi \ge 0$, let $\theta = \varphi$. If $\varphi < 0$, replace $u, v, w$ by $-u, v, -w$. The new basis again has $(-u) \times v = -w$, and $P$ becomes $P\operatorname{diag}(-1, 1, -1)$.
14. In the new basis, the block $A$ becomes $DAD = R(-\varphi)$, by direct multiplication. Let $\theta = -\varphi \in (0, \pi)$.
15. In both cases, $\theta \in [0, \pi]$, and the columns of $B = \operatorname{diag}(1, R(\theta))$ give $Ru = u$, $Rv = \cos\theta\,v + \sin\theta\,w$ and $Rw = -\sin\theta\,v + \cos\theta\,w$.

**Part 3.**

16. $R = PBP^T$ is similar to $B$. Similar matrices have the same trace, by [[this theorem|191HBJ7PVZ]].
17. So $\tr R = \tr B = 1 + 2\cos\theta$.

**Part 4.**

18. $B - B^T = \begin{pmatrix} 0 & 0 \\ 0 & R(\theta) - R(-\theta) \end{pmatrix} = 2\sin\theta\,N$.
19. By step 7, the map $x \mapsto u \times x$ sends $u$ to $0$, $v$ to $w$ and $w$ to $u \times w = -v$. So its matrix in the basis $u, v, w$ is $N$, and $[u]_\times = PNP^T$.
20. So $R - R^T = P(B - B^T)P^T = 2\sin\theta\,PNP^T = 2\sin\theta\,[u]_\times$.
21. The entries $(3, 2)$, $(1, 3)$ and $(2, 1)$ of $[u]_\times$ are $u_1$, $u_2$ and $u_3$. For $0 < \theta < \pi$, $\sin\theta > 0$, and this gives the formula for $u$.

**Part 5.**

22. Let $Q \in O(3)$ with $\det Q = -1$. Then $-Q$ is orthogonal, and $\det(-Q) = (-1)^3\det Q = 1$. So $-Q \in SO(3)$.
23. Apply part 2 to $-Q$: in an orthonormal basis $u, v, w$ with $w = u \times v$, the matrix of $-Q$ is $\operatorname{diag}(1, R(\theta))$ with $\theta \in [0, \pi]$.
24. So the matrix of $Q$ is $\operatorname{diag}(-1, -R(\theta)) = \operatorname{diag}(-1, R(\theta + \pi))$, because $-R(\theta) = R(\pi)R(\theta)$.
25. Replace $u, v, w$ by $-u, v, -w$ as in steps 13 and 14. The first entry stays $-1$, and the block becomes $R(-\theta - \pi) = R(\pi - \theta)$. Let $\psi = \pi - \theta \in [0, \pi]$.
26. For $\psi = 0$, the matrix is $\operatorname{diag}(-1, 1, 1)$: $Q$ fixes $u^\perp$ and negates $u$, so $Q$ is the reflection in $u^\perp$.
27. For $\psi = \pi$, the matrix is $-I_3$, so $Q = -I_3$. $\blacksquare$

## Idea

In odd dimension, $\det(R - I) = -\det(R - I)$ forces the eigenvalue $1$.
The plane perpendicular to the axis is mapped to itself, and there $R$ is a plane rotation.
The trace does not change under a change of orthonormal basis, and the skew part $R - R^T$ changes like the matrix of $x \mapsto u \times x$.
So the trace gives the angle, and the skew part gives the axis.

## Variants

- Part 1 also follows from the eigenvalues: the non-real roots of the characteristic polynomial come in pairs $\lambda, \overline{\lambda}$ with $\lambda\overline{\lambda} = 1$, so the real roots have product $1$, see [[the determinant theorem|QDZJMFATRW]].
- Part 2 is the case $n = 3$ of [[the normal form of orthogonal matrices|QTY3VMFGY1]].
