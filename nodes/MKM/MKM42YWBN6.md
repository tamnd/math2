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

Let $A$ be positive semidefinite of size $n$.

1. By the [[spectral theorem for Hermitian matrices|0DGZBQWZWN]], $A = U D U^*$ with $U$ [[unitary|0D6RMJ10M9]] and $D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ real.
2. By the [[eigenvalue test|0HYC2RHD3M]], every $\lambda_i \ge 0$. By the [[existence of square roots of nonnegative reals|068BZBXE0C]], let $D^{1/2} = \operatorname{diag}(\sqrt{\lambda_1}, \dots, \sqrt{\lambda_n})$.
3. Let $B = U D^{1/2} U^*$. Then $B^* = U (D^{1/2})^* U^* = B$, since $D^{1/2}$ is real diagonal. So $B$ is Hermitian, with the eigenvalues $\sqrt{\lambda_i} \ge 0$.
4. By the eigenvalue test, $B$ is [[positive semidefinite|0880F9EQCP]]. Since $U^* U = I$, we get $B^2 = U D^{1/2} U^* U D^{1/2} U^* = U D U^* = A$. This proves existence and part 3.
5. Let $\mu_1, \dots, \mu_m$ be the distinct eigenvalues of $A$, which are the distinct numbers among the $\lambda_i$. Let $p$ be the [[Lagrange polynomial|Y7KSGE97GK]]
$$p(t) = \sum_{k=1}^m \sqrt{\mu_k} \prod_{j \ne k} \frac{t - \mu_j}{\mu_k - \mu_j}.$$
It has real coefficients, and $p(\mu_k) = \sqrt{\mu_k}$ for each $k$, since the product is $1$ at $t = \mu_k$ and $0$ at $t = \mu_j$ for $j \ne k$.
6. For a unitary $W$ and a diagonal $E = \operatorname{diag}(e_1, \dots, e_n)$, we have $(W E W^*)^r = W E^r W^*$ for every $r \ge 0$, because the inner factors $W^* W$ are $I$. Also $E^r = \operatorname{diag}(e_1^r, \dots, e_n^r)$.
7. Taking linear combinations in step 6 gives $q(W E W^*) = W \operatorname{diag}(q(e_1), \dots, q(e_n)) W^*$ for every polynomial $q$.
8. By step 7 with $W = U$ and $E = D$, $p(A) = U \operatorname{diag}(p(\lambda_1), \dots, p(\lambda_n)) U^* = U D^{1/2} U^* = B$. This proves part 2 for $B$.
9. Uniqueness: let $C$ be positive semidefinite with $C^2 = A$. By the spectral theorem and the eigenvalue test, $C = W E W^*$ with $W$ unitary and $E = \operatorname{diag}(\varepsilon_1, \dots, \varepsilon_n)$, all $\varepsilon_i \ge 0$.
10. By step 6, $A = C^2 = W E^2 W^*$. So $A w_i = \varepsilon_i^2 w_i$ for the column $w_i \ne 0$ of $W$. So each $\varepsilon_i^2$ is an [[eigenvalue|0ZND7NQ970]] of $A$, that is, one of the $\mu_k$.
11. By step 5, $p(\varepsilon_i^2) = \sqrt{\varepsilon_i^2} = \varepsilon_i$, since $\varepsilon_i \ge 0$.
12. By steps 7, 10 and 11, $p(A) = p(W E^2 W^*) = W \operatorname{diag}(p(\varepsilon_i^2)) W^* = W E W^* = C$.
13. By steps 8 and 12, $C = p(A) = B$. This proves uniqueness and part 1.
14. If $XA = AX$, then $X A^r = A^r X$ for all $r$, so $X p(A) = p(A) X$. This finishes part 2.
15. If $Bx = 0$, then $Ax = B(Bx) = 0$. If $Ax = 0$, then $\norm{Bx}^2 = x^* B^* B x = x^* A x = 0$, so $Bx = 0$. So $A$ and $B$ have the same null space.
16. By the [[rank-nullity theorem|0W4FSW1TVB]], they have the same rank. A positive semidefinite matrix is positive definite exactly when its null space is $\set{0}$, by the eigenvalue test. This proves part 4.
17. If $A$ is real, then $p(A)$ is real, since $p$ has real coefficients. This proves part 5.

## Idea

The square root is built in an eigenbasis, by taking the square root of each eigenvalue.
For uniqueness, one polynomial $p$ with $p(\mu) = \sqrt\mu$ at the eigenvalues of $A$ gives $p(A) = C$ for every positive semidefinite root $C$.
So all such roots equal $p(A)$.

## Variants

- Uniqueness can also be proved with eigenspaces. If $C^2 = A$ with $C \succeq 0$, then $C$ maps each eigenspace of $A$ to itself, and on the eigenspace for $\mu$ it acts as $\sqrt\mu$ times the identity.
- For positive definite $A$, the Newton iteration $X_{k+1} = \tfrac12 (X_k + X_k^{-1} A)$ from $X_0 = I$ converges to $A^{1/2}$; this belongs to numerical linear algebra.
