---
tag: XH1RXBEEWH
kind: definition
name: Preconditioner
msc: [65F08, 65F10]
defines: KE98SW3SBD
uses: [0GT4WWGWH2, 0EB9N0S33C, AB3S6MHJ8X, 0KX66CZMBB, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Preconditioner
---

## Definition

Let $A$ be an [[invertible|0EB9N0S33C]] real $n \times n$ matrix, and consider the [[linear system|0GT4WWGWH2]] $A x = b$.
A *preconditioner* for $A$ is an invertible $n \times n$ matrix $P$, used through the map $r \mapsto P^{-1} r$.
The *left preconditioned* system is $P^{-1} A x = P^{-1} b$.
The *right preconditioned* system is $A P^{-1} y = b$ with $x = P^{-1} y$.
If $P = P_1 P_2$, the *split preconditioned* system is $P_1^{-1} A P_2^{-1} y = P_1^{-1} b$ with $x = P_2^{-1} y$.

## Remarks

All three systems have the same solution $x$ as $A x = b$.
The definition is formal; a preconditioner is useful when two informal requirements hold.
First, $P^{-1} r$ is cheap to compute for any $r$.
Second, $P^{-1} A$ is close to the identity, for example it has a small [[condition number|AB3S6MHJ8X]] or few clusters of [[eigenvalues|0BQAA2BK3Q]].
The two extremes are $P = I$, which is cheap but changes nothing, and $P = A$, which is ideal but as costly as the original problem.
Example: the Jacobi preconditioner $P = \operatorname{diag}(a_{11}, \dots, a_{nn})$ is invertible when all diagonal entries are nonzero.
For $A$ with rows $(100, 1)$ and $(1, 1)$, the ratio of the extreme eigenvalues of $A$ is about $101$.
The matrix $P^{-1} A$ has rows $(1, 0.01)$ and $(1, 1)$ and eigenvalues $0.9$ and $1.1$, with ratio about $1.2$.
Non-example: the matrix $P$ with rows $(1, 1)$ and $(1, 1)$ is singular, so it is not a preconditioner.
For a symmetric [[positive definite|0KX66CZMBB]] $A$ one takes $P$ symmetric positive definite, so that methods for symmetric systems still apply.
