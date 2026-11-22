---
tag: 1KF3RPY39H
kind: proof
name: Proof that Gram matrices are positive semidefinite
msc: [15B57, 15A63]
topics: [SS4EVPKT3A]
audience: ug1
proves: 0AM050KCAW
methods: [0NTF6DMVAP, 01XM7JEKHY, TFQ1845T84]
uses: [0880F9EQCP, 0QQCG3JWJ4, 0EKZCX4K3P, 0EX045E2BP, 09GK5PS824, 0EVHJFTG9Z, 0DGZBQWZWN, 0HYC2RHD3M, 0D6RMJ10M9, 0EB9N0S33C]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Decomposition
---

## Proof

We write the form of $B^* B$ as a squared length for parts 1 and 2, and we build a factor from the spectral theorem for parts 3 and 4.

*Parts 1 and 2.*

1. Let $B$ be an $m \times n$ complex matrix and $A = B^* B$, where $^*$ is the [[conjugate transpose|0EX045E2BP]]. Then $A$ is $n \times n$.
2. For matrices $X$ and $Y$ with $XY$ defined, $(XY)^* = Y^* X^*$, by the rule for the [[transpose of a product|09GK5PS824]] with all entries conjugated.
3. By step 2, $A^* = B^* (B^*)^* = B^* B = A$, so $A$ is [[Hermitian|0EKZCX4K3P]].
4. For $y \in \C^m$ we have $y^* y = \sum_{i=1}^m \abs{y_i}^2 \ge 0$, with equality only if $y = 0$.
5. Let $x \in \C^n$. By step 2,
$$x^* A x = x^* B^* B x = (Bx)^* (Bx).$$
6. By steps 4 and 5 with $y = Bx$, we get $x^* A x \ge 0$. So $A$ is [[positive semidefinite|0880F9EQCP]], which proves part 1.
7. By steps 4 and 5, $x^* A x = 0$ holds if and only if $Bx = 0$.
8. Let $b_1, \dots, b_n$ be the columns of $B$, so that $Bx = x_1 b_1 + \dots + x_n b_n$.
9. Suppose the columns are [[linearly independent|0EVHJFTG9Z]], and let $x \ne 0$. Then $Bx \ne 0$ by step 8, so $x^* A x > 0$ by step 7, and $A$ is [[positive definite|0QQCG3JWJ4]].
10. Suppose instead that the columns are dependent. Then some $x \ne 0$ has $x_1 b_1 + \dots + x_n b_n = 0$, that is, $Bx = 0$, and step 7 gives $x^* A x = 0$. So $A$ is not positive definite. Steps 9 and 10 prove part 2.

*Parts 3 and 4.*

11. Let $A$ be positive semidefinite. By the [[spectral theorem for Hermitian matrices|0DGZBQWZWN]], $A = U D U^*$ with $U$ [[unitary|0D6RMJ10M9]] and $D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ real.
12. By the [[eigenvalue test|0HYC2RHD3M]], every $\lambda_i \ge 0$. Let $D^{1/2} = \operatorname{diag}(\sqrt{\lambda_1}, \dots, \sqrt{\lambda_n})$ with nonnegative square roots, so that $D^{1/2}$ is real diagonal and $(D^{1/2})^2 = D$.
13. Put $B = D^{1/2} U^*$. By step 2, $B^* = U (D^{1/2})^* = U D^{1/2}$, since a real diagonal matrix equals its own conjugate transpose.
14. Then
$$B^* B = U D^{1/2} D^{1/2} U^* = U D U^* = A,$$
which proves part 3.
15. Let $A$ be positive definite with $A = B^* B$ for some $B$. If the columns of $B$ were dependent, step 10 would show that $A$ is not positive definite, so the columns of $B$ are independent.
16. For positive definite $A$, every $\lambda_i > 0$ by the eigenvalue test. So $D^{1/2}$ has a nonzero diagonal and is [[invertible|0EB9N0S33C]], and the matrix $B = D^{1/2} U^*$ of step 13 is a product of two invertible matrices. This proves part 4.
17. For real matrices, steps 1 to 10 hold with the transpose in place of $^*$. For real symmetric $A$, step 11 holds with a real orthogonal $Q$ in place of $U$, and then $B = D^{1/2} Q^{\mathsf{T}}$ is real.

## Idea

The number $x^* B^* B x$ is the squared length of the vector $Bx$.
A squared length is never negative, and it is zero only for the zero vector, so the form vanishes exactly on the null space of $B$, which gives parts 1 and 2.
For the converse, diagonalize $A$ and take the square roots of its nonnegative eigenvalues.

## Variants

For part 3 one can take $B$ to be the [[positive semidefinite square root|EQ98KW1ZN4]] of $A$, since then $B^* B = B^2 = A$; this is the matrix $U D^{1/2} U^*$ rather than $D^{1/2} U^*$.
For positive definite $A$, the [[Cholesky decomposition|0WKG8CYY6A]] gives a triangular $B$ by elimination alone, without the spectral theorem.
