---
tag: CWPWRR6NQA
kind: proof
name: Proof of the properties of reflections and generation of the orthogonal group
msc: ["15A04", "15B10", "51F15"]
topics: [AZS5BPF5H3]
audience: ug2
proves: FEER10D15S
uses: [0Y85GYEGSF, 0W4FSW1TVB, F7M8ZXB4P7]
methods: [0NTF6DMVAP, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Householder_transformation
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Orthogonal_group
    locator: Reflections
---

## Proof

Write $c(x) = \frac{\ip{x}{u}}{\ip{u}{u}}$, so that $s_u(x) = x - 2c(x)u$.

**Part 1.**

1. The map $x \mapsto \ip{x}{u}$ is linear, so $c$ is linear, and $s_u$ is linear.
2. For $x \in u^\perp$, $c(x) = 0$, so $s_u(x) = x$.
3. $c(u) = 1$, so $s_u(u) = u - 2u = -u$.

**Part 2.**

4. $c(s_u(x)) = c(x) - 2c(x)c(u) = -c(x)$, by step 1 and $c(u) = 1$.
5. So $s_u(s_u(x)) = s_u(x) - 2c(s_u(x))u = x - 2c(x)u + 2c(x)u = x$.
6. $\ip{s_u(x)}{y} = \ip{x}{y} - 2\frac{\ip{x}{u}\ip{u}{y}}{\ip{u}{u}}$. This expression is symmetric in $x$ and $y$, because the real inner product is symmetric.
7. So $\ip{s_u(x)}{y} = \ip{x}{s_u(y)}$, and $s_u$ is self-adjoint.
8. By steps 7 and 5, $\ip{s_u(x)}{s_u(y)} = \ip{x}{s_u(s_u(y))} = \ip{x}{y}$. So $s_u$ is a linear isometry.

**Part 3.**

9. The map $x \mapsto \ip{x}{u}$ from $V$ to $\R$ is linear and surjective, because it sends $u$ to $\ip{u}{u} \neq 0$. Its kernel is $u^\perp$, so $\dim u^\perp = n - 1$, by [[rank-nullity|0W4FSW1TVB]].
10. Choose a basis $e_2, \dots, e_n$ of $u^\perp$, by [[the existence of an orthonormal basis|0Y85GYEGSF]]. The vectors $u, e_2, \dots, e_n$ are linearly independent, because $u \notin u^\perp$. So they are a basis of $V$.
11. By steps 2 and 3, the matrix of $s_u$ in this basis is $\operatorname{diag}(-1, 1, \dots, 1)$.
12. The determinant of a linear map is the determinant of its matrix in any basis. So $\det s_u = -1$.

**Part 4.**

13. For a unit vector $u \in \R^n$, $\ip{u}{u} = 1$ and $\ip{x}{u} = u^Tx$. So $s_u(x) = x - 2u(u^Tx) = (I_n - 2uu^T)x$.
14. $H^T = I_n - 2(u^T)^Tu^T = H$, so $H$ is symmetric.
15. By step 5, $H^2 = I_n$. So $H^TH = H^2 = I_n$, and $H$ is orthogonal. By step 12, $\det H = -1$.

**Part 5.**

16. Let $u = x - y \neq 0$, and write $a = \norm{x}^2 = \norm{y}^2$ and $b = \ip{x}{y}$.
17. $\ip{x}{u} = a - b$, and $\ip{u}{u} = a - 2b + a = 2(a - b)$. Since $u \neq 0$, $a - b \neq 0$.
18. So $c(x) = \frac{1}{2}$, and $s_u(x) = x - u = y$.
19. By step 5, $s_u(y) = s_u(s_u(x)) = x$.

**Part 6.**

20. We prove by [[induction|0ASJVEFA9J]] on $n$ that each $Q \in O(n)$ is a product of at most $n$ reflections of $\R^n$.
21. For $n = 1$, $O(1) = \set{(1), (-1)}$. The matrix $(1)$ is the empty product, and $(-1) = s_{e_1}$.
22. Let $n \ge 2$, and assume the claim for $n - 1$. Let $Q \in O(n)$, and let $q = Qe_n$, the last column of $Q$. Then $\norm{q} = 1 = \norm{e_n}$.
23. If $q = e_n$, let $Q' = Q$. If $q \neq e_n$, let $H = s_{q - e_n}$ and $Q' = HQ$. By step 18, $Q'e_n = Hq = e_n$.
24. $Q'$ is orthogonal, and $Q'e_n = e_n$. Then $Q'^Te_n = Q'^{-1}e_n = e_n$, by [[the equivalent conditions|F7M8ZXB4P7]]. So the last row of $Q'$ is also $e_n^T$.
25. So $Q' = \begin{pmatrix} A & 0 \\ 0 & 1 \end{pmatrix}$ with an $(n - 1) \times (n - 1)$ block $A$. The columns of $A$ are orthonormal, because the columns of $Q'$ are. So $A \in O(n - 1)$.
26. By the induction hypothesis, $A = H'_1 \cdots H'_k$ with $k \le n - 1$, where $H'_j = s_{w_j}$ for some $w_j \in \R^{n - 1}$ with $w_j \neq 0$.
27. Let $\hat{w}_j = (w_j, 0) \in \R^n$. For $x = (x', x_n)$, $s_{\hat{w}_j}(x) = (x' - 2\frac{\ip{x'}{w_j}}{\ip{w_j}{w_j}}w_j, \ x_n) = (H'_jx', x_n)$. So $s_{\hat{w}_j} = \begin{pmatrix} H'_j & 0 \\ 0 & 1 \end{pmatrix}$.
28. Block matrices of this form multiply blockwise. So $Q' = s_{\hat{w}_1} \cdots s_{\hat{w}_k}$.
29. If $Q' = Q$, then $Q$ is a product of $k \le n - 1$ reflections. Otherwise $Q = H^{-1}Q' = HQ'$, by step 5, a product of $k + 1 \le n$ reflections.
30. This proves the claim for $n$, and part 6 follows. $\blacksquare$

## Idea

Choose the normal vector $u$, and use a basis of the mirror together with $u$: in this basis, $s_u$ is $\operatorname{diag}(-1, 1, \dots, 1)$.
For two vectors of the same length, the mirror halfway between them swaps them.
For part 6, one reflection moves the last column of $Q$ to $e_n$, and the rest is an orthogonal matrix of size $n - 1$.

## Variants

- Part 3 also follows from the eigenvalues: $s_u$ has the eigenvalue $1$ with multiplicity $n - 1$ and the eigenvalue $-1$ once.
- [[The proof of the Cartan-Dieudonné theorem|AYYJXYNT01]] runs the same induction without coordinates, on the hyperplane orthogonal to a fixed vector.
