---
tag: RACSNQXDQV
kind: statement
role: theorem
name: Weyl's inequality
msc: [15A42, 15A18]
uses: [0P17NGQQMQ, 0BQAA2BK3Q, CJK2HS2508, 06EKW1AKXF]
about: [0BQAA2BK3Q, 0P17NGQQMQ]
sources:
  - url: https://en.wikipedia.org/wiki/Weyl%27s_inequality
---

## Statement

Let $A$ and $B$ be $n \times n$ [[Hermitian matrices|0P17NGQQMQ]].
For a Hermitian matrix $M$, let $\lambda_1(M) \ge \dots \ge \lambda_n(M)$ be its [[eigenvalues|0BQAA2BK3Q]], listed with multiplicity.
Then, for all $i, j \ge 1$ with $i + j - 1 \le n$,
$$\lambda_{i+j-1}(A + B) \le \lambda_i(A) + \lambda_j(B).$$

## Remarks

The proof uses the [[Courant–Fischer min-max theorem|CJK2HS2508]].
The span of the eigenvectors for $\lambda_i(A), \dots, \lambda_n(A)$ and the span of those for $\lambda_j(B), \dots, \lambda_n(B)$ meet in a subspace of dimension at least $n - i - j + 2$.
On this subspace the Rayleigh quotient of $A + B$ is at most $\lambda_i(A) + \lambda_j(B)$, and the min-max formula gives the bound.

Taking $j = 1$ and applying the result also to $(A + B) + (-B)$ gives
$$\lambda_k(A) + \lambda_n(B) \le \lambda_k(A + B) \le \lambda_k(A) + \lambda_1(B).$$
Hence $\abs{\lambda_k(A + B) - \lambda_k(A)} \le \norm{B}_2$, where $\norm{B}_2$ is the [[operator norm|06EKW1AKXF]] induced by the Euclidean norm.

Example: $A = \operatorname{diag}(1, 0)$ and $B = \operatorname{diag}(0, 1)$ give $A + B = I_2$, and $\lambda_2(A + B) = 1 \le \lambda_1(A) + \lambda_2(B) = 1$, with equality.

## Explanations

### L1 human

Adding two symmetric matrices cannot move the eigenvalues in an arbitrary way.
Each eigenvalue of the sum is bounded by sums of eigenvalues of the two parts.
In particular, a small symmetric perturbation moves each eigenvalue by at most the size of the perturbation.

### L2 human

The corollary $\abs{\lambda_k(A + B) - \lambda_k(A)} \le \norm{B}_2$ says that the eigenvalues of Hermitian matrices are stable under perturbation.
For non-Hermitian matrices this fails, and bounds such as the [[Bauer–Fike theorem|AK9J4RNZ51]] are needed instead.
Weyl's inequalities are among the inequalities in Horn's problem on the eigenvalues of a sum of Hermitian matrices.
