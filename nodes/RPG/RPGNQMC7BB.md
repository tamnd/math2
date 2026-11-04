---
tag: RPGNQMC7BB
kind: proof
name: Proof that the eigenvalues of a positive definite matrix are positive
msc: [15B57, 15A18]
proves: 0HYC2RHD3M
uses: [0QQCG3JWJ4, 0ZND7NQ970, 0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Eigenvalues
---

## Proof

1. Let $A$ be a [[positive definite|0QQCG3JWJ4]] Hermitian $n \times n$ matrix, and let $\lambda$ be an [[eigenvalue|0ZND7NQ970]] of $A$.
2. By definition there is $x \in \C^n$ with $x \ne 0$ and $Ax = \lambda x$.
3. Let $x^*$ be the [[conjugate transpose|0EX045E2BP]] of $x$. Then $x^* x = \sum_{i=1}^n \abs{x_i}^2$, which is a real number.
4. Since $x \ne 0$, some $x_i \ne 0$, so $x^* x > 0$.
5. By step 2, $x^* A x = x^* (\lambda x) = \lambda\, x^* x$.
6. Since $A$ is positive definite and $x \ne 0$, the number $x^* A x$ is real and positive.
7. By steps 4 to 6, $\lambda = x^* A x / x^* x$ is a quotient of two positive reals. So $\lambda$ is a positive real number.

## Idea

Test the defining inequality $x^* A x > 0$ on an eigenvector. There $A$ acts as multiplication by $\lambda$, so the inequality becomes $\lambda \abs{x}^2 > 0$.
