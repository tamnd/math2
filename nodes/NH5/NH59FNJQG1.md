---
tag: NH59FNJQG1
kind: definition
name: Radial basis function interpolation
msc: [65D12, 41A05, 41A63]
defines: XZ33P3HBB9
uses: [ZBSXSTQM2J, BM703GV34G, 0GT4WWGWH2, 0KX66CZMBB]
sources:
  - url: https://en.wikipedia.org/wiki/Radial_basis_function_interpolation
---

## Definition

Let $d \ge 1$, let $x_1, \dots, x_N \in \R^d$ be pairwise distinct, let $y_1, \dots, y_N \in \R$, and let $\varphi \colon [0, \infty) \to \R$ define a [[radial basis function|ZBSXSTQM2J]].
Let $A$ be the $N \times N$ matrix with entries $A_{ij} = \varphi(\norm{x_i - x_j})$.
If $A$ is invertible, the *radial basis function interpolant* of the data is
$$s(x) = \sum_{j=1}^{N} \lambda_j \, \varphi(\norm{x - x_j}),$$
where $\lambda = (\lambda_1, \dots, \lambda_N)$ is the solution of the [[linear system|0GT4WWGWH2]] $A \lambda = y$.

## Remarks

By construction $s(x_i) = (A\lambda)_i = y_i$, so $s$ is a [[multivariate interpolant|BM703GV34G]] of the data.
For the Gaussian $\varphi(r) = e^{-(\varepsilon r)^2}$ the matrix $A$ is a [[positive definite matrix|0KX66CZMBB]], hence invertible, for all distinct points in every dimension.
For conditionally positive definite functions such as the thin plate spline, a low-degree polynomial is added to $s$, with matching side conditions on $\lambda$, to get a uniquely solvable system.

Example: $d = 1$, $\varphi(r) = r$, nodes $0, 1$, values $y_1 = 0$, $y_2 = 1$.
Then $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ and $\lambda = (1, 0)$, so $s(x) = \abs{x}$, and indeed $s(0) = 0$, $s(1) = 1$.

Non-example: take $\varphi(r) = r^2$ on $\R$ and the four nodes $0, 1, 2, 3$.
Each translate $(x - x_j)^2$ lies in the space of polynomials of degree at most $2$, which has dimension $3$.
So the four columns of $A$, the values of these translates at the nodes, are linearly dependent, and $A$ is not invertible.
Then the interpolant is not defined.
