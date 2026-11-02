---
tag: WBYJ7A0HY7
kind: definition
name: Hyperbolic conservation law
msc: [35L65, 35L40]
defines: XN081NCPF5
uses: [8RA7AMWSAF, 92C3S03AQZ]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperbolic_partial_differential_equation
---

## Definition

Let $\partial_t u + \sum_{j=1}^n \partial_{x_j} F_j(u) = 0$ be a system of [[conservation laws|8RA7AMWSAF]], with $C^1$ fluxes $F_j \colon \R^m \to \R^m$ and unknown $u$ with values in an open set $\mathcal{U} \subseteq \R^m$.
For $u \in \mathcal{U}$ and $\xi \in \R^n$ let $B(u; \xi) = \sum_{j=1}^n \xi_j\, DF_j(u)$, an $m \times m$ real matrix, where $DF_j$ is the Jacobian matrix of $F_j$.
The system is *hyperbolic* on $\mathcal{U}$ if, for every $u \in \mathcal{U}$ and every unit vector $\xi \in \R^n$, the matrix $B(u; \xi)$ is diagonalizable over $\R$.
That is, $B(u; \xi)$ has $m$ real eigenvalues $\lambda_1(u; \xi) \le \cdots \le \lambda_m(u; \xi)$ and a basis of $\R^m$ of corresponding eigenvectors.

## Remarks

It is *strictly hyperbolic* if moreover the eigenvalues are distinct, $\lambda_1 < \cdots < \lambda_m$.
In one space dimension $B(u; \xi) = \xi\, DF(u)$, and the condition is that $DF(u)$ is diagonalizable with real eigenvalues; these are the characteristic speeds.
The definition makes the system a [[hyperbolic|92C3S03AQZ]] system of first-order equations when written in the non-conservative form $u_t + \sum_j DF_j(u)\, u_{x_j} = 0$.

Example: every scalar conservation law ($m = 1$) is hyperbolic, since $B(u; \xi) = F'(u) \cdot \xi$ is a real $1 \times 1$ matrix.
Example: the $p$-system $v_t - w_x = 0$, $w_t + p(v)_x = 0$ with $p' < 0$ has $DF = \begin{pmatrix} 0 & -1 \\ p'(v) & 0 \end{pmatrix}$.
Its eigenvalues $\pm \sqrt{-p'(v)}$ are real and distinct, so the system is strictly hyperbolic.

Non-example: the linear system $u_t + A u_x = 0$ with $A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, so that $F(u) = Au$.
The eigenvalues of $A$ are $\pm i$, which are not real, so the system is not hyperbolic; its components satisfy the Cauchy–Riemann equations, which are elliptic.
