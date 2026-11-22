---
tag: EYAWYR6572
kind: proof
name: Proof of the Cayley transform theorem
msc: ["15B10", "15A16"]
topics: [AZS5BPF5H3]
audience: grad
proves: R9Z3W1CFPP
uses: [03RNVFDEAN, ACDFDABVQK, 0ZZQ2E1MTE, 0C3CFHDN6R, F7M8ZXB4P7, 0ZND7NQ970]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley_transform
    locator: Matrix map
---

## Proof

We first show that $I - M$ and $I + M$ commute, then compute $Q^{\mathsf{T}}$ and $A^{\mathsf{T}}$ with the transpose rules, and finally check that $C$ undoes itself.

**A lemma on commuting factors.**

1. Let $M$ be a real $n \times n$ matrix with $I + M$ invertible. Then $(I - M)(I + M) = I - M^2 = (I + M)(I - M)$.
2. Multiply this identity by $(I + M)^{-1}$ on the left and on the right. This gives $(I + M)^{-1}(I - M) = (I - M)(I + M)^{-1}$, so the two forms of $C(M)$ agree.

**Part 1.**

3. Let $A$ be skew-symmetric, and let $x \in \R^n$. The number $x^{\mathsf{T}}Ax$ equals its transpose $x^{\mathsf{T}}A^{\mathsf{T}}x = -x^{\mathsf{T}}Ax$, so $x^{\mathsf{T}}Ax = 0$.
4. If $(I + A)x = 0$, then $0 = x^{\mathsf{T}}(I + A)x = x^{\mathsf{T}}x + x^{\mathsf{T}}Ax = x^{\mathsf{T}}x$ by step 3, so $x = 0$.
5. So the null space of $I + A$ is $\{ 0 \}$, and $I + A$ is invertible by [[the invertible matrix theorem|ACDFDABVQK]].
6. The matrix $-A$ is also skew-symmetric, so $I - A$ is invertible by steps 3 to 5 with $-A$ in place of $A$.

**Part 2.**

7. Let $Q = C(A)$. Then $Q^{\mathsf{T}} = ((I + A)^{-1})^{\mathsf{T}}(I - A)^{\mathsf{T}} = (I + A^{\mathsf{T}})^{-1}(I - A^{\mathsf{T}}) = (I - A)^{-1}(I + A)$, because $A^{\mathsf{T}} = -A$.
8. So $Q^{\mathsf{T}}Q = (I - A)^{-1}(I + A)(I - A)(I + A)^{-1}$. By step 1, $(I + A)(I - A) = (I - A)(I + A)$, so $Q^{\mathsf{T}}Q = (I - A)^{-1}(I - A)(I + A)(I + A)^{-1} = I$.
9. Hence $Q$ is orthogonal.
10. We have $I - A = I + A^{\mathsf{T}} = (I + A)^{\mathsf{T}}$, so $\det(I - A) = \det(I + A)$ by [[the determinant of the transpose|0ZZQ2E1MTE]].
11. By the product rule for [[determinants|0C3CFHDN6R]] and step 10, $\det Q = \det(I - A)\det(I + A)^{-1} = 1$.
12. We have $I + Q = (I + A)(I + A)^{-1} + (I - A)(I + A)^{-1} = 2(I + A)^{-1}$, which is invertible.
13. So $Qx = -x$ gives $(I + Q)x = 0$ and then $x = 0$. Hence $-1$ is not an [[eigenvalue|0ZND7NQ970]] of $Q$.

**Part 3.**

14. Let $Q$ be orthogonal without the eigenvalue $-1$. Then $(I + Q)x = 0$ only for $x = 0$, so $I + Q$ is invertible by the invertible matrix theorem.
15. By [[the equivalent conditions|F7M8ZXB4P7]], $Q^{\mathsf{T}} = Q^{-1}$. So $I + Q^{\mathsf{T}} = Q^{-1}(Q + I)$ and $I - Q^{\mathsf{T}} = Q^{-1}(Q - I)$.
16. Let $A = C(Q)$. As in step 7, $A^{\mathsf{T}} = (I + Q^{\mathsf{T}})^{-1}(I - Q^{\mathsf{T}})$.
17. By step 15, $A^{\mathsf{T}} = (I + Q)^{-1}QQ^{-1}(Q - I) = (I + Q)^{-1}(Q - I) = -(I + Q)^{-1}(I - Q)$.
18. By step 2, $(I + Q)^{-1}(I - Q) = C(Q) = A$. So $A^{\mathsf{T}} = -A$, and $A$ is skew-symmetric.

**Part 4.**

19. Let $N = C(M)$. As in step 12, $I + N = 2(I + M)^{-1}$, which is invertible, so $C(N)$ is defined.
20. In the same way, $I - N = (I + M)(I + M)^{-1} - (I - M)(I + M)^{-1} = 2M(I + M)^{-1}$.
21. Hence $C(N) = (I - N)(I + N)^{-1} = 2M(I + M)^{-1} \cdot \frac{1}{2}(I + M) = M$.

**Part 5.**

22. Let $\mathcal{K}$ be the set of real skew-symmetric $n \times n$ matrices, and let $\mathcal{U}$ be the set of $Q \in O(n)$ without the eigenvalue $-1$.
23. By parts 1 and 2, $C$ maps $\mathcal{K}$ into $\mathcal{U}$, and by part 3, $C$ maps $\mathcal{U}$ into $\mathcal{K}$.
24. By part 4, the two maps are inverse to each other. So $C \colon \mathcal{K} \to \mathcal{U}$ is a bijection, and its inverse is $C$.
25. Each $Q \in \mathcal{U}$ is $C(A)$ with $A = C(Q) \in \mathcal{K}$, so $\det Q = 1$ by step 11. Hence $\mathcal{U} \subseteq SO(n)$. $\blacksquare$

## Idea

The factors $I - M$ and $I + M$ commute, so the Cayley transform behaves like the function $z \mapsto \frac{1 - z}{1 + z}$ of one variable.
This function sends the imaginary axis to the unit circle, and it is its own inverse.
The transpose turns $A$ into $-A$, and this matches the inverse of $Q$, which is $Q^{\mathsf{T}}$.

## Variants

Part 1 also follows from eigenvalues.
The complex eigenvalues of a real skew-symmetric matrix are purely imaginary, so $-1$ is not one of them, and $I + A$ is invertible.

Part 2 also follows from a normal form.
By [[the real normal form|G6T1FNE3JC]], $A$ is orthogonally similar to a block diagonal matrix with blocks $(0)$ and $\begin{pmatrix} 0 & -b \\ b & 0 \end{pmatrix}$.
The Cayley transform respects orthogonal similarity and block sums.
It sends $(0)$ to $(1)$ and each $2 \times 2$ block to the rotation $R(-\theta)$ with $b = \tan\frac{\theta}{2}$ and $0 < \abs{\theta} < \pi$.
So $C(A)$ is orthogonally similar to a block rotation with no entry $-1$, which gives part 2 at a glance.
