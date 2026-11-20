---
tag: RPGNQMC7BB
kind: proof
name: Proof of the eigenvalue test for definiteness
msc: [15B57, 15A18]
topics: [SS4EVPKT3A]
audience: ug1
proves: 0HYC2RHD3M
methods: [0NTF6DMVAP, TFQ1845T84]
uses: [0DGZBQWZWN, 0QQCG3JWJ4, 0880F9EQCP, 0ZND7NQ970, 0EX045E2BP, 0D6RMJ10M9]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Eigenvalues
  - book: isbn:9783031410253
    locator: Chapter 7
---

## Proof

1. Let $A$ be a Hermitian $n \times n$ matrix. By the [[spectral theorem for Hermitian matrices|0DGZBQWZWN]], $A = U D U^*$ with $U$ [[unitary|0D6RMJ10M9]] and $D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ real. The $\lambda_i$ are the eigenvalues of $A$, repeated by multiplicity.
2. Let $x \in \C^n$ and put $y = U^* x$. Then $x^* A x = x^* U D U^* x = (U^* x)^* D (U^* x) = y^* D y$, by the rule $(XY)^* = Y^* X^*$ for the [[conjugate transpose|0EX045E2BP]].
3. Since $D$ is diagonal, $y^* D y = \sum_{i=1}^n \lambda_i \abs{y_i}^2$.
4. The map $x \mapsto U^* x$ is a bijection of $\C^n$ with inverse $y \mapsto Uy$, because $U U^* = U^* U = I$. It sends $0$ to $0$, so it maps the nonzero vectors onto the nonzero vectors.
5. Suppose $A$ is [[positive definite|0QQCG3JWJ4]]. Let $e_i$ be the $i$-th standard basis vector and $x = U e_i$. Then $x \ne 0$ and $y = e_i$ by step 4. Steps 2 and 3 give $0 < x^* A x = \lambda_i$. So every eigenvalue is positive.
6. Suppose every $\lambda_i > 0$, and let $x \ne 0$. By step 4, $y \ne 0$, so some $\abs{y_j}^2 > 0$. Every term of the sum in step 3 is at least $0$, and the term $j$ is positive. So $x^* A x > 0$, and $A$ is positive definite. This proves part 1.
7. Suppose $A$ is [[positive semidefinite|0880F9EQCP]]. The vector $x = U e_i$ of step 5 gives $\lambda_i = x^* A x \ge 0$. So every eigenvalue is nonnegative.
8. Suppose every $\lambda_i \ge 0$, and let $x \in \C^n$. Every term of the sum in step 3 is at least $0$, so $x^* A x \ge 0$. So $A$ is positive semidefinite. This proves part 2.
9. For a real symmetric $A$, step 1 holds with a real orthogonal $Q$ in place of $U$, by the same theorem. Steps 2 to 8 then work with real vectors and the transpose in place of $^*$.

## Idea

In an orthonormal basis of eigenvectors, the form $x^* A x$ becomes $\sum \lambda_i \abs{y_i}^2$.
A weighted sum of squares is positive for every nonzero $y$ exactly when all weights are positive.
Testing the form on the eigenvectors themselves gives the other direction.

## Variants

- The direction "positive definite implies positive eigenvalues" needs no spectral theorem. If $Ax = \lambda x$ with $x \ne 0$, then $0 < x^* A x = \lambda \, x^* x$, and $x^* x > 0$, so $\lambda > 0$.
- The other direction can also be proved with the [[Rayleigh quotient|06WHP8SE98]]. For $x \ne 0$, the quotient $x^* A x / x^* x$ is at least the smallest eigenvalue, which is positive.
