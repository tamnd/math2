---
about:
- 0RBQS1JJCR
- 0VR671PHE5
kind: statement
msc:
- 15A18
- 15A63
name: Extreme values of a quadratic form on unit vectors
role: proposition
sources:
- locator: src/section7-2.xml:839
  url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section7-2.xml#L839
tag: YS4HT1EYE5
uses:
- 0RBQS1JJCR
- 0VR671PHE5
- 0BQAA2BK3Q
---

## Statement

Let $A$ be a real [[symmetric matrix|0VR671PHE5]] of size $m \times m$. Let $q_A(\mathbf u) = \mathbf u^T A \mathbf u$ be its [[quadratic form|0RBQS1JJCR]].

List the [[eigenvalues|0BQAA2BK3Q]] of $A$ in decreasing order, $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_m$. Choose a basis $\mathbf u_1, \dots, \mathbf u_m$ of $\mathbb R^m$ with $A \mathbf u_i = \lambda_i \mathbf u_i$.

Then, over all unit vectors $\mathbf u$, the largest value of $q_A(\mathbf u)$ is $\lambda_1$. It is reached by the unit vector in the direction of $\mathbf u_1$.

Likewise, the smallest value of $q_A(\mathbf u)$ over all unit vectors is $\lambda_m$. It is reached by the unit vector in the direction of $\mathbf u_m$.

## Remarks

The proof diagonalizes $A$ in an orthonormal basis of eigenvectors. In those coordinates, $q_A$ is a weighted sum of squares with weights $\lambda_i$, and the squares add up to $1$ on a unit vector. A weighted average of the $\lambda_i$ lies between $\lambda_m$ and $\lambda_1$.
