---
tag: MKM42YWBN6
kind: proof
name: Proof of the existence and uniqueness of the positive semidefinite square root
msc: [15A16, 15B57]
topics: [SS4EVPKT3A]
audience: ug2
proves: EQ98KW1ZN4
methods: [01XM7JEKHY, GQHHNV79PA]
uses: [0DGZBQWZWN, 0HYC2RHD3M, 0880F9EQCP, 0D6RMJ10M9, 0ZND7NQ970, 068BZBXE0C, Y7KSGE97GK, 0W4FSW1TVB, 0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/Square_root_of_a_matrix
    locator: Positive semidefinite matrices
  - book: isbn:9783031410253
    locator: Chapter 7
---

## Proof

We build a root in an eigenbasis of $A$, show that it is a polynomial $p(A)$, and then show that every positive semidefinite root equals the same $p(A)$.
Let $A$ be an $n \times n$ positive semidefinite matrix, and let $^*$ be the [[conjugate transpose|0EX045E2BP]].

*Existence and the construction.*

1. By the [[spectral theorem for Hermitian matrices|0DGZBQWZWN]], $A = U D U^*$ with $U$ [[unitary|0D6RMJ10M9]] and $D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ real.
2. By the [[eigenvalue test|0HYC2RHD3M]], every $\lambda_i \ge 0$. So the [[square roots of nonnegative reals|068BZBXE0C]] give a real diagonal matrix $D^{1/2} = \operatorname{diag}(\sqrt{\lambda_1}, \dots, \sqrt{\lambda_n})$.
3. Let $B = U D^{1/2} U^*$. Then $B^* = U (D^{1/2})^* U^* = B$, because $D^{1/2}$ is real and diagonal, so $B$ is Hermitian with the eigenvalues $\sqrt{\lambda_i} \ge 0$.
4. By the eigenvalue test, $B$ is [[positive semidefinite|0880F9EQCP]]. Since $U^* U = I$, we get $B^2 = U D^{1/2} U^* U D^{1/2} U^* = U D U^* = A$. This proves existence and part 3.

*The root is a polynomial in $A$.*

5. Let $\mu_1, \dots, \mu_m$ be the distinct eigenvalues of $A$, that is, the distinct numbers among the $\lambda_i$. Let $p$ be the [[Lagrange interpolation polynomial|Y7KSGE97GK]]
$$p(t) = \sum_{k=1}^m \sqrt{\mu_k} \prod_{j \ne k} \frac{t - \mu_j}{\mu_k - \mu_j}.$$
6. The polynomial $p$ has real coefficients, and $p(\mu_k) = \sqrt{\mu_k}$ for each $k$. Indeed, at $t = \mu_k$ the $k$-th product is $1$, and every other product contains the factor $\mu_k - \mu_k = 0$.
7. For a unitary $W$ and a diagonal $E = \operatorname{diag}(e_1, \dots, e_n)$, we have $(W E W^*)^r = W E^r W^*$ for every integer $r \ge 0$, because each inner product $W^* W$ is $I$. Also $E^r = \operatorname{diag}(e_1^r, \dots, e_n^r)$.
8. Taking linear combinations in step 7 gives $q(W E W^*) = W \operatorname{diag}(q(e_1), \dots, q(e_n)) W^*$ for every polynomial $q$.
9. Step 8 with $W = U$, $E = D$ and $q = p$ gives $p(A) = U \operatorname{diag}(p(\lambda_1), \dots, p(\lambda_n)) U^* = U D^{1/2} U^* = B$, by step 6.

*Uniqueness.*

10. Let $C$ be any positive semidefinite matrix with $C^2 = A$. By the spectral theorem and the eigenvalue test, $C = W E W^*$ with $W$ unitary and $E = \operatorname{diag}(\varepsilon_1, \dots, \varepsilon_n)$, all $\varepsilon_i \ge 0$.
11. By step 7, $A = C^2 = W E^2 W^*$. So $A w_i = \varepsilon_i^2 w_i$ for the nonzero column $w_i$ of $W$, and each $\varepsilon_i^2$ is an [[eigenvalue|0ZND7NQ970]] of $A$, that is, one of the $\mu_k$.
12. By step 6, $p(\varepsilon_i^2) = \sqrt{\varepsilon_i^2} = \varepsilon_i$, where the last equality uses $\varepsilon_i \ge 0$.
13. Step 8 with $q = p$ and $E^2$ in place of $E$, together with step 12, gives $p(A) = W \operatorname{diag}(p(\varepsilon_1^2), \dots, p(\varepsilon_n^2)) W^* = W E W^* = C$.
14. Steps 9 and 13 give $C = p(A) = B$. This proves part 1.
15. If $XA = AX$, then $X A^r = A^r X$ for every $r \ge 0$ by induction on $r$, so $X p(A) = p(A) X$. This proves part 2.

*Kernel, rank and the real case.*

16. If $Bx = 0$, then $Ax = B(Bx) = 0$. If $Ax = 0$, then $\norm{Bx}^2 = x^* B^* B x = x^* A x = 0$, so $Bx = 0$. So $A$ and $B$ have the same null space.
17. By the [[rank-nullity theorem|0W4FSW1TVB]], $A$ and $B$ have the same rank. A positive semidefinite matrix is positive definite exactly when its null space is $\{0\}$, by the eigenvalue test, so part 4 follows.
18. If $A$ is real, then $p(A)$ is real, since $p$ has real coefficients. By step 14 this proves part 5.

## Idea

To find a square root, look at $A$ in a basis of eigenvectors, where it is diagonal, and take the square root of each eigenvalue.
Uniqueness needs one more idea.
A single polynomial $p$ sends each eigenvalue $\mu$ of $A$ to $\sqrt \mu$.
Any positive semidefinite root $C$ has eigenvalues whose squares are eigenvalues of $A$, so $p(C^2) = C$, that is, $p(A) = C$.
So every such root is the same matrix $p(A)$.

## Variants

Uniqueness can also be proved with eigenspaces.
If $C^2 = A$ with $C$ positive semidefinite, then $C$ commutes with $A = C^2$, so $C$ maps each eigenspace of $A$ into itself.
On the eigenspace for $\mu$, the restriction of $C$ is positive semidefinite with square $\mu I$, so all its eigenvalues equal $\sqrt \mu$, and a diagonalizable map with one eigenvalue is a multiple of the identity.
So $C$ acts as $\sqrt \mu$ on that eigenspace, and $C$ is determined.

For positive definite $A$, the Newton iteration $X_{k+1} = \tfrac12 (X_k + X_k^{-1} A)$ from $X_0 = I$ converges to $A^{1/2}$ in exact arithmetic, and its study belongs to numerical linear algebra.
