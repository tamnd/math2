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

**A lemma on commuting factors.**

1. Let $M$ be a real $n \times n$ matrix with $I + M$ invertible. Then $(I - M)(I + M) = I - M^2 = (I + M)(I - M)$.
2. Multiply this identity by $(I + M)^{-1}$ on the left and on the right. This gives $(I + M)^{-1}(I - M) = (I - M)(I + M)^{-1}$. So the two forms of $C(M)$ agree.

**Part 1.**

3. Let $A$ be skew-symmetric, and let $x \in \R^n$. The number $x^TAx$ equals its transpose $x^TA^Tx = -x^TAx$. So $x^TAx = 0$.
4. If $(I + A)x = 0$, then $0 = x^T(I + A)x = x^Tx + x^TAx = x^Tx$, by step 3. So $x = 0$.
5. So $I + A$ has the null space $\set{0}$, and it is invertible, by [[the invertible matrix theorem|ACDFDABVQK]].
6. $-A$ is also skew-symmetric, so $I - A$ is invertible by steps 3 to 5 with $-A$ in place of $A$.

**Part 2.**

7. Let $Q = C(A)$. Then $Q^T = ((I + A)^{-1})^T(I - A)^T = (I + A^T)^{-1}(I - A^T) = (I - A)^{-1}(I + A)$, because $A^T = -A$.
8. $Q^TQ = (I - A)^{-1}(I + A)(I - A)(I + A)^{-1}$. By step 1, $(I + A)(I - A) = (I - A)(I + A)$, so $Q^TQ = (I - A)^{-1}(I - A)(I + A)(I + A)^{-1} = I$.
9. So $Q$ is orthogonal.
10. $I - A = I + A^T = (I + A)^T$. So $\det(I - A) = \det(I + A)$, by [[the determinant of the transpose|0ZZQ2E1MTE]].
11. $\det Q = \det(I - A)\det(I + A)^{-1} = 1$, by step 10 and the product rule for [[determinants|0C3CFHDN6R]].
12. $I + Q = (I + A)(I + A)^{-1} + (I - A)(I + A)^{-1} = 2(I + A)^{-1}$. This matrix is invertible.
13. So $Qx = -x$ gives $(I + Q)x = 0$ and $x = 0$. So $-1$ is not an [[eigenvalue|0ZND7NQ970]] of $Q$.

**Part 3.**

14. Let $Q$ be orthogonal without the eigenvalue $-1$. Then $(I + Q)x = 0$ only for $x = 0$, so $I + Q$ is invertible, by the invertible matrix theorem.
15. $Q^T = Q^{-1}$, by [[the equivalent conditions|F7M8ZXB4P7]]. So $I + Q^T = Q^{-1}(Q + I)$ and $I - Q^T = Q^{-1}(Q - I)$.
16. Let $A = C(Q)$. Then $A^T = (I + Q^T)^{-1}(I - Q^T)$, as in step 7.
17. By step 15, $A^T = (I + Q)^{-1}QQ^{-1}(Q - I) = (I + Q)^{-1}(Q - I) = -(I + Q)^{-1}(I - Q)$.
18. By step 2, $(I + Q)^{-1}(I - Q) = C(Q) = A$. So $A^T = -A$, and $A$ is skew-symmetric.

**Part 4.**

19. Let $N = C(M)$. As in step 12, $I + N = 2(I + M)^{-1}$, which is invertible. So $C(N)$ is defined.
20. In the same way, $I - N = (I + M)(I + M)^{-1} - (I - M)(I + M)^{-1} = 2M(I + M)^{-1}$.
21. $C(N) = (I - N)(I + N)^{-1} = 2M(I + M)^{-1} \cdot \frac{1}{2}(I + M) = M$.

**Part 5.**

22. Let $\mathcal{K}$ be the set of skew-symmetric matrices, and let $\mathcal{U}$ be the set of $Q \in O(n)$ without the eigenvalue $-1$.
23. $C$ maps $\mathcal{K}$ into $\mathcal{U}$, by parts 1 and 2, and $C$ maps $\mathcal{U}$ into $\mathcal{K}$, by part 3.
24. By part 4, the two maps are inverse to each other. So $C \colon \mathcal{K} \to \mathcal{U}$ is a bijection, and its inverse is $C$.
25. Each $Q \in \mathcal{U}$ is $C(A)$ with $A = C(Q) \in \mathcal{K}$, so $\det Q = 1$ by step 11. So $\mathcal{U} \subseteq SO(n)$.

## Idea

The factors $I - M$ and $I + M$ commute, so the Cayley transform behaves like the function $z \mapsto \frac{1 - z}{1 + z}$ of one variable.
This function sends the imaginary axis to the unit circle, and it is its own inverse.
The transpose turns $A$ into $-A$, and this matches the inverse of $Q$.

## Variants

- A proof of part 1 with eigenvalues: the complex eigenvalues of a real skew-symmetric matrix are purely imaginary, so $-1$ is not one of them.
- A proof of part 2 with the normal form: by [[the real normal form|G6T1FNE3JC]], $A$ is orthogonally similar to blocks $(0)$ and $\begin{pmatrix} 0 & -b \\ b & 0 \end{pmatrix}$. The Cayley transform of such a block is a rotation $R(-\theta)$ with $b = \tan\frac{\theta}{2}$.
