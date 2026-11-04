---
tag: P48CFDFAV9
kind: proof
name: Proof of the spectral theorem for normal matrices by deflation
msc: [15A21, 47B15]
proves: 04CW1P44VD
uses: [0XYKE8BE7X, 0EX045E2BP, 0D6RMJ10M9, 0Q9PGXD9E4, 076JGP6R3T, 01AXG9KZQF, 0753Y2X5K6, 0ZND7NQ970, 08CJB2NQ92, 02SJG1HC32, 0JP0W07Y9A, 0VGSYBWHV2, 0Y85GYEGSF]
sources:
  - url: https://ocw.mit.edu/courses/res-18-011-algebra-i-student-notes-fall-2021/mit18_701f21_lect28.pdf
    locator: Lemma 28.4 and proof of Theorem 28.1
---

## Proof

The converse is a direct computation. For the main direction, we argue by induction on $n$, splitting off one eigenvector at a time.

1. Write $M^*$ for the [[conjugate transpose|0EX045E2BP]]. For matrices of matching sizes, $(MN)^* = N^* M^*$ and $(M^*)^* = M$, by the formula $(M^*)_{ij} = \overline{m_{ji}}$.
2. Converse. Let $A = U D U^*$ with $U$ [[unitary|0D6RMJ10M9]] and $D$ [[diagonal|0Q9PGXD9E4]]. Then $U^* U = I$, so $U U^* = I$ by the [[one-sided inverse theorem|0753Y2X5K6]].
3. Diagonal matrices commute, so $D D^* = D^* D$. Hence $A A^* = U D U^* U D^* U^* = U D D^* U^* = U D^* D U^* = A^* A$. So $A$ is [[normal|0XYKE8BE7X]].
4. For the main direction, let $P(n)$ say: every normal $n \times n$ complex matrix is $U D U^*$ with $U$ unitary and $D$ diagonal. For $n = 1$, take $U = (1)$ and $D = A$.
5. Let $n \ge 2$, assume $P(n-1)$, and let $A$ be normal of size $n$. On $\C^n$, use the inner product $\ip{x}{y} = y^* x$, with norm $\norm{x}^2 = x^* x = \sum_i \abs{x_i}^2$.
6. $\C$ is [[algebraically closed|02SJG1HC32]] by the [[fundamental theorem of algebra|0JP0W07Y9A]]. So $A$ has an [[eigenvalue|08CJB2NQ92]] $\lambda$, with $A x = \lambda x$ for some $x \ne 0$. Set $u_1 = x / \norm{x}$, so $u_1^* u_1 = 1$.
7. Let $N = A - \lambda I$. Then $N^* = A^* - \overline{\lambda} I$. Expanding gives $N N^* = A A^* - \overline{\lambda} A - \lambda A^* + \abs{\lambda}^2 I$, and $N^* N$ is the same with $A^* A$ in place of $A A^*$.
8. Since $A A^* = A^* A$, step 7 gives $N N^* = N^* N$. Then $\norm{N^* u_1}^2 = u_1^* N N^* u_1 = u_1^* N^* N u_1 = \norm{N u_1}^2$. This is $0$, since $A u_1 = \lambda u_1$ gives $N u_1 = 0$.
9. So $N^* u_1 = 0$, that is, $A^* u_1 = \overline{\lambda} u_1$.
10. The map $\ip{\cdot}{\cdot}$ of step 5 is an [[inner product|0VGSYBWHV2]]. The family $(u_1)$ is orthonormal, so it [[extends to an orthonormal basis|0Y85GYEGSF]] $u_1, \dots, u_n$ of $\C^n$.
11. Let $U_1$ have columns $u_1, \dots, u_n$. The $(i, j)$ entry of $U_1^* U_1$ is $u_i^* u_j = \delta_{ij}$. So $U_1$ is unitary, and $U_1 U_1^* = I$ by the one-sided inverse theorem.
12. Let $B = U_1^* A U_1$. By [[matrix multiplication|076JGP6R3T]], its $(i, j)$ entry is $b_{ij} = u_i^* A u_j$.
13. First column: $b_{i1} = u_i^* (\lambda u_1) = \lambda \delta_{i1}$. First row: $b_{1j} = (A^* u_1)^* u_j = (\overline{\lambda} u_1)^* u_j = \lambda \delta_{1j}$, by steps 1 and 9.
14. So $B$ is the [[block matrix|01AXG9KZQF]] $\begin{pmatrix} \lambda & 0 \\ 0 & C \end{pmatrix}$ for some $(n-1) \times (n-1)$ complex matrix $C$.
15. By steps 1 and 11, $B B^* = U_1^* A U_1 U_1^* A^* U_1 = U_1^* A A^* U_1$. Likewise $B^* B = U_1^* A^* A U_1$. So $B$ is normal.
16. Multiplying blocks gives $B B^* = \begin{pmatrix} \abs{\lambda}^2 & 0 \\ 0 & C C^* \end{pmatrix}$ and $B^* B = \begin{pmatrix} \abs{\lambda}^2 & 0 \\ 0 & C^* C \end{pmatrix}$. So $C C^* = C^* C$, and $C$ is normal.
17. By $P(n-1)$, $C = V D' V^*$ with $V$ unitary of size $n - 1$ and $D'$ diagonal.
18. Let $U_2 = \begin{pmatrix} 1 & 0 \\ 0 & V \end{pmatrix}$ and $D = \begin{pmatrix} \lambda & 0 \\ 0 & D' \end{pmatrix}$. Then $D$ is diagonal, and $U_2^* U_2 = \begin{pmatrix} 1 & 0 \\ 0 & V^* V \end{pmatrix} = I$.
19. Multiplying blocks gives $U_2 D U_2^* = \begin{pmatrix} \lambda & 0 \\ 0 & V D' V^* \end{pmatrix} = B$.
20. By step 11, $A = U_1 U_1^* A U_1 U_1^* = U_1 B U_1^*$. With step 19, $A = (U_1 U_2) D (U_1 U_2)^*$.
21. Let $U = U_1 U_2$. Then $U^* U = U_2^* U_1^* U_1 U_2 = U_2^* U_2 = I$, so $U$ is unitary. Thus $A = U D U^*$, which proves $P(n)$.
22. By induction, $P(n)$ holds for all $n \ge 1$. With steps 2 and 3, $A$ is normal if and only if $A = U D U^*$ with $U$ unitary and $D$ diagonal.

## Idea

For a normal matrix, $\norm{A^* x} = \norm{A x}$ for every $x$, and the same holds for $A - \lambda I$. So an eigenvector of $A$ for $\lambda$ is an eigenvector of $A^*$ for $\overline{\lambda}$. In an orthonormal basis that starts with this vector, both the first row and the first column of $A$ vanish off the diagonal. The rest is a smaller normal matrix, and induction finishes.
