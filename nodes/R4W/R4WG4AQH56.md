---
tag: R4WG4AQH56
kind: definition
name: Multidimensional scaling
msc: [62H25, 62H30]
defines: EZ596QFCKY
uses: [0VR671PHE5, 0BQAA2BK3Q, 0N6960W0BV, 01MMVW8CKC, 0NPPGHQNXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Multidimensional_scaling
---

## Definition

Let $D = (d_{ij})$ be an $n \times n$ [[symmetric matrix|0VR671PHE5]] with $d_{ii} = 0$ and $d_{ij} \ge 0$, the dissimilarities of $n$ objects, and let $1 \le k < n$.
*Multidimensional scaling* seeks points $x_1, \ldots, x_n \in \R^k$ whose distances $\abs{x_i - x_j}$ approximate the $d_{ij}$.
*Classical multidimensional scaling* computes them as follows:

1. Let $D^{(2)} = (d_{ij}^2)$ and $J = I_n - \tfrac{1}{n} \mathbf{1} \mathbf{1}^T$, where $\mathbf{1}$ is the vector of ones, and let $B = -\tfrac{1}{2} J D^{(2)} J$.
2. Let $\lambda_1 \ge \cdots \ge \lambda_k$ be the $k$ largest [[eigenvalues|0BQAA2BK3Q]] of $B$, assumed positive, with orthonormal [[eigenvectors|0N6960W0BV]] $e_1, \ldots, e_k$.
3. Let $x_i \in \R^k$ be the $i$-th row of the $n \times k$ matrix $\begin{pmatrix} \sqrt{\lambda_1} e_1 & \cdots & \sqrt{\lambda_k} e_k \end{pmatrix}$.

## Remarks

The matrix $D$ is the matrix of [[Euclidean distances|0NPPGHQNXQ]] of some points in $\R^k$ exactly when $B$ is [[positive semidefinite|01MMVW8CKC]] of rank at most $k$.
In that case classical scaling recovers the points up to a translation and an orthogonal transformation, since $B$ is then the Gram matrix of the centred points.
Example: three points on a line at distances $d_{12} = d_{23} = 1$, $d_{13} = 2$.
The centred configuration $-1, 0, 1$ has Gram matrix $B = \begin{pmatrix} 1 & 0 & -1 \\ 0 & 0 & 0 \\ -1 & 0 & 1 \end{pmatrix}$, with largest eigenvalue $2$ and eigenvector $(1, 0, -1)/\sqrt{2}$.
Step 3 gives the coordinates $1, 0, -1$, the original points after a reflection.
Non-example: if $d_{12} = d_{23} = 1$ and $d_{13} = 3$, the triangle inequality fails, so no points in any $\R^k$ realise $D$, and $B$ has a negative eigenvalue.
Metric and non-metric scaling instead minimise a stress function, such as $\sum_{i < j} (d_{ij} - \abs{x_i - x_j})^2$, by iteration.
