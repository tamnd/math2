---
tag: NEZYP9HJB9
kind: definition
name: Completely positive map
msc: [46L07, 46L05, 81P47]
defines: CGY299QMC3
uses: [NA8DF5X3M4, 0FHVPRAE60]
sources:
  - url: https://en.wikipedia.org/wiki/Completely_positive_map
---

## Definition

Let $A$ and $B$ be C*-algebras, and let $\varphi \colon A \to B$ be a linear map.
For $n \ge 1$, let $M_n(A)$ be the [[matrix ring|0FHVPRAE60]] of $n \times n$ matrices with entries in $A$, which is again a C\*-algebra.
Let $\varphi_n \colon M_n(A) \to M_n(B)$ be the map $[a_{ij}] \mapsto [\varphi(a_{ij})]$.
The map $\varphi$ is *$n$-positive* if $\varphi_n$ sends [[positive elements|NA8DF5X3M4]] of $M_n(A)$ to positive elements of $M_n(B)$.
It is *completely positive* if it is $n$-positive for every $n \ge 1$.

## Remarks

Equivalently, $\varphi \otimes \id_{M_n}$ is positive for every $n$.
Every $*$-homomorphism $\pi$ is completely positive, since $\pi_n$ is a $*$-homomorphism and maps $x^* x$ to $\pi_n(x)^* \pi_n(x)$.

Example: for a fixed $m \times k$ complex matrix $V$, the map $\varphi \colon M_m(\C) \to M_k(\C)$, $\varphi(a) = V^* a V$, is completely positive.
Indeed $\varphi_n(x) = W^* x W$ with $W = \operatorname{diag}(V, \ldots, V)$, and $W^* y^* y W = (y W)^* (y W) \ge 0$.

Non-example: the transpose $\theta(a) = a^T$ on $M_2(\C)$ is positive, since $a$ and $a^T$ have the same eigenvalues.
It is not $2$-positive: the matrix $x = [E_{ij}]_{i,j=1}^2 \in M_2(M_2(\C))$, with $E_{ij}$ the matrix units, equals $v v^*$ with $v = e_1 \otimes e_1 + e_2 \otimes e_2$, so it is positive.
But $\theta_2(x) = [E_{ji}]_{i,j}$ is the swap matrix, which has the eigenvalue $-1$.
