---
tag: DPR9DJRPAF
kind: definition
name: Stiffness matrix
msc: [65N30, 74S05]
defines: G8ZTW9JVX1
uses: [HM2HHE3J51, 0SQZMXB6GP, Y5B0PEBKE8, 98GZ9DVHTA]
sources:
  - url: https://en.wikipedia.org/wiki/Stiffness_matrix
---

## Definition

Let $V$ be a real [[Hilbert space|HM2HHE3J51]], let $a \colon V \times V \to \R$ be a bounded [[bilinear form|0SQZMXB6GP]], and let $\ell \colon V \to \R$ be a bounded linear functional.
Let $V_h \subseteq V$ be a finite-dimensional subspace with a basis $\varphi_1, \ldots, \varphi_N$, as in the [[Galerkin method|Y5B0PEBKE8]] or the [[finite element method|98GZ9DVHTA]].
The *stiffness matrix* is the $N \times N$ matrix $K$ with entries
$$K_{ij} = a(\varphi_j, \varphi_i), \qquad 1 \le i, j \le N.$$
The vector $F$ with $F_i = \ell(\varphi_i)$ is the *load vector*.

## Remarks

The function $u_h = \sum_j c_j \varphi_j$ satisfies $a(u_h, v) = \ell(v)$ for all $v \in V_h$ exactly when $K c = F$.
If $a$ is symmetric, then $K$ is symmetric.
If $a$ is coercive, $a(v, v) \ge \alpha \norm{v}^2$ with $\alpha > 0$, then $c^T K c = a(v, v) > 0$ for $v = \sum_j c_j \varphi_j \ne 0$, so $K$ is positive definite in the symmetric case and invertible in general.
If $\varphi_i$ and $\varphi_j$ have disjoint supports and $a$ is an integral of local terms, then $K_{ij} = 0$.

Example: for $-u'' = f$ on $(0, 1)$ with $u(0) = u(1) = 0$, take $a(u, v) = \int_0^1 u' v' \, dx$, nodes $x_i = ih$ with $h = 1/(N + 1)$, and hat functions $\varphi_i$ with $\varphi_i(x_j) = \delta_{ij}$.
On each of its two intervals $\varphi_i'$ equals $\pm 1/h$, so $K_{ii} = 2/h$, $K_{i, i \pm 1} = -1/h$, and all other entries are $0$.
So $K = h^{-1} \operatorname{tridiag}(-1, 2, -1)$.

Non-example: the matrix $M_{ij} = \int_0^1 \varphi_j \varphi_i \, dx$ is built from the $L^2$ inner product, not from the form $a$ of the problem.
It is the mass matrix, which has $M_{ii} = 2h/3$ and $M_{i, i \pm 1} = h/6$ for the hat functions above.
