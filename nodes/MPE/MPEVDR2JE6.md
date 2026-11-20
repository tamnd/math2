---
tag: MPEVDR2JE6
kind: proof
name: Proof that an orthogonal matrix has determinant plus or minus one and eigenvalues on the unit circle
msc: ["15B10", "15A18"]
topics: [AZS5BPF5H3]
audience: ug1
proves: QDZJMFATRW
uses: [0QRBVFJ50X, 04CPJ6AF00, 0ZZQ2E1MTE, 0ZND7NQ970, 039HF58KQ5, 0EX045E2BP]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_matrix
    locator: Matrix properties
---

## Proof

Let $Q$ be a real $n \times n$ matrix with $Q^TQ = I_n$.

**Part 1.**

1. By [[the multiplicativity of the determinant|04CPJ6AF00]], $\det(Q^TQ) = \det(Q^T)\det(Q)$.
2. By [[the determinant of the transpose|0ZZQ2E1MTE]], $\det(Q^T) = \det(Q)$.
3. So $(\det Q)^2 = \det(I_n) = 1$.
4. $\det Q$ is a real number with square $1$, so $\det Q = 1$ or $\det Q = -1$.

**Part 2.**

5. Let $\lambda \in \C$ be a root of the [[characteristic polynomial|039HF58KQ5]] $\det(tI - Q)$. Then $\det(\lambda I - Q) = 0$.
6. So $\lambda I - Q$ is not invertible as a complex matrix, and there is $z \in \C^n$ with $z \neq 0$ and $Qz = \lambda z$.
7. Let $z^*$ be the [[conjugate transpose|0EX045E2BP]] of $z$. Since $Q$ is real, $Q^* = Q^T$, and the conjugate transpose of $Qz = \lambda z$ is $z^*Q^T = \overline{\lambda}z^*$.
8. Multiply: $z^*Q^TQz = (\overline{\lambda}z^*)(\lambda z) = \abs{\lambda}^2 z^*z$.
9. By hypothesis $Q^TQ = I_n$, so the left side is $z^*z$.
10. $z^*z = \sum_j \abs{z_j}^2 > 0$, because $z \neq 0$. Divide by it: $\abs{\lambda}^2 = 1$, so $\abs{\lambda} = 1$.
11. A real [[eigenvalue|0ZND7NQ970]] $\lambda$ is a real root of the characteristic polynomial, so $\abs{\lambda} = 1$ gives $\lambda = \pm 1$.

**Part 3.**

12. $Q$ is real, so its characteristic polynomial $p(t)$ has real coefficients.
13. Conjugation of $p(\lambda) = 0$ gives $p(\overline{\lambda}) = 0$. The same holds for each derivative $p^{(k)}$, which also has real coefficients, so $\lambda$ and $\overline{\lambda}$ have the same multiplicity.
14. By part 2, $\lambda\overline{\lambda} = \abs{\lambda}^2 = 1$, so $\overline{\lambda} = \lambda^{-1}$.

## Idea

The determinant turns $Q^TQ = I$ into $(\det Q)^2 = 1$.
For eigenvalues, we take a complex eigenvector $z$ and compare the squared lengths of $z$ and $Qz$.
The matrix keeps lengths, so the eigenvalue cannot change the length of $z$.

## Variants

- Part 2 by norms: the map $z \mapsto Qz$ keeps the standard norm of $\C^n$, because $\norm{Qz}^2 = z^*Q^TQz = \norm{z}^2$. Then $\abs{\lambda}\norm{z} = \norm{Qz} = \norm{z}$.
- Part 1 from part 2: $\det Q$ is the product of the roots, the conjugate pairs contribute $\lambda\overline{\lambda} = 1$, and each real root is $\pm 1$.
