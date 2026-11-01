---
tag: 10FGGCQ6TS
kind: definition
name: Power iteration
msc: [65F15, 15A18]
defines: H4MQD841BR
uses: [0VD9ZSWWJG, 0BQAA2BK3Q, 0N6960W0BV, 06WHP8SE98]
sources:
  - url: https://en.wikipedia.org/wiki/Power_iteration
---

## Definition

Let $A$ be an $n \times n$ complex [[matrix|0VD9ZSWWJG]] and let $x_0 \in \C^n$ be a nonzero starting vector.
*Power iteration* is the sequence defined by
$$x_{k+1} = \frac{A x_k}{\norm{A x_k}}, \qquad k \ge 0,$$
as long as $A x_k \ne 0$, together with the eigenvalue estimates $\mu_k = x_k^* A x_k / (x_k^* x_k)$.

## Remarks

The numbers $\mu_k$ are [[Rayleigh quotients|06WHP8SE98]].
Convergence: suppose $A$ is diagonalizable with [[eigenvalues|0BQAA2BK3Q]] $\abs{\lambda_1} > \abs{\lambda_2} \ge \cdots \ge \abs{\lambda_n}$, and $x_0$ has a nonzero component along an [[eigenvector|0N6960W0BV]] $v_1$ for $\lambda_1$ in the eigenbasis.
Then the direction of $x_k$ tends to that of $v_1$, up to a scalar factor of modulus $1$, with error of order $\abs{\lambda_2 / \lambda_1}^k$, and $\mu_k \to \lambda_1$.
Example: $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ has eigenvalues $3$ and $1$ with eigenvectors $(1, 1)$ and $(1, -1)$; for $x_0 = (1, 0) = \tfrac12 (1, 1) + \tfrac12 (1, -1)$, one gets $A^k x_0 = \tfrac12 (3^k + 1, 3^k - 1)$, whose direction tends to $(1, 1)$ with error of order $3^{-k}$.
Non-example of convergence: for $A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$, the condition $\abs{\lambda_1} > \abs{\lambda_2}$ fails, and from $x_0 = (1, 1)$ the iterates alternate between the directions of $(1, -1)$ and $(1, 1)$.
Applying the method to $(A - \sigma I)^{-1}$ gives inverse iteration, which finds the eigenvalue closest to a shift $\sigma$.
