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

We take determinants of $Q^TQ = I_n$ for part 1, compare the lengths of a complex eigenvector and its image for part 2, and conjugate the characteristic polynomial for part 3.
Let $Q$ be a real $n \times n$ matrix with $Q^TQ = I_n$.

**Part 1.**

1. By the [[multiplicativity of the determinant|04CPJ6AF00]], $\det(Q^TQ) = \det(Q^T)\det(Q)$.
2. By the [[determinant of the transpose|0ZZQ2E1MTE]], $\det(Q^T) = \det(Q)$. So $(\det Q)^2 = \det(I_n) = 1$.
3. The number $\det Q$ is real with square $1$, so $\det Q = 1$ or $\det Q = -1$.

**Part 2.**

4. Let $\lambda \in \C$ be a root of the [[characteristic polynomial|039HF58KQ5]] $\det(tI - Q)$. Then $\lambda I - Q$ is not invertible as a complex matrix, so there is $z \in \C^n$ with $z \ne 0$ and $Qz = \lambda z$.
5. Let $z^*$ be the [[conjugate transpose|0EX045E2BP]] of $z$. Since $Q$ is real, $Q^* = Q^T$, so taking the conjugate transpose of $Qz = \lambda z$ gives $z^*Q^T = \bar\lambda z^*$.
6. Multiply the two equations: $z^*Q^TQz = (\bar\lambda z^*)(\lambda z) = \abs{\lambda}^2 z^*z$.
7. By hypothesis $Q^TQ = I_n$, so the left side is $z^*z$.
8. Since $z \ne 0$, we have $z^*z = \sum_j \abs{z_j}^2 > 0$. Dividing by it gives $\abs{\lambda}^2 = 1$, so $\abs{\lambda} = 1$.
9. A real [[eigenvalue|0ZND7NQ970]] is a real root of the characteristic polynomial, and a real number of absolute value $1$ is $1$ or $-1$.

**Part 3.**

10. Since $Q$ is real, its characteristic polynomial $p(t)$ has real coefficients, and so does each derivative $p^{(k)}$.
11. Conjugating $p^{(k)}(\lambda) = 0$ gives $p^{(k)}(\bar\lambda) = 0$. The multiplicity of a root is the number of derivatives, starting with $p$ itself, that vanish there, so $\lambda$ and $\bar\lambda$ have the same multiplicity.
12. By part 2, $\lambda\bar\lambda = \abs{\lambda}^2 = 1$, so $\bar\lambda = \lambda^{-1}$.

## Idea

Taking determinants turns $Q^TQ = I$ into $(\det Q)^2 = 1$.
For the eigenvalues we must allow complex eigenvectors, because a real rotation may have none in $\R^n$.
The matrix keeps the length of a complex vector too, so an eigenvalue cannot change the length of its eigenvector, and it has absolute value $1$.

## Variants

Part 2 can be phrased with norms.
The map $z \mapsto Qz$ keeps the standard norm of $\C^n$, because $\norm{Qz}^2 = z^*Q^TQz = \norm{z}^2$.
Then $Qz = \lambda z$ gives $\abs{\lambda}\norm{z} = \norm{Qz} = \norm{z}$.

Part 1 also follows from parts 2 and 3.
The determinant is the product of the roots, each conjugate pair contributes $\lambda\bar\lambda = 1$, and each real root is $\pm 1$.
