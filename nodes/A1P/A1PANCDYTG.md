---
tag: A1PANCDYTG
kind: statement
role: theorem
name: Courant–Fischer characterization of characteristic values
msc: [45C05, 47A75]
uses: [WWMWX7AD4V, 2ZB3NFZ94T, HRCQ3JHYY0, DC7HMHVREP, 4NSACSWRJZ, CJK2HS2508, A1G25R99PY]
about: [DC7HMHVREP, HRCQ3JHYY0]
sources:
  - url: https://en.wikipedia.org/wiki/Min-max_theorem
---

## Statement

Let $a < b$ and let $K \in L^2([a, b] \times [a, b])$ be a [[square-integrable kernel|WWMWX7AD4V]] that is [[Hermitian|2ZB3NFZ94T]].
Let $R_K$ be its [[Rayleigh quotient|HRCQ3JHYY0]] on $L^2[a, b]$.
List the positive [[characteristic values|DC7HMHVREP]] of $K$ as $0 < \lambda_1 \le \lambda_2 \le \cdots$.
Each $\lambda$ is repeated as often as the dimension of the space of solutions of $\varphi = \lambda T_K \varphi$.
Let $k \ge 1$ be such that there are at least $k$ of them.
Then
$$\frac{1}{\lambda_k} = \max_{\dim V = k} \; \min_{\varphi \in V \setminus \set{0}} R_K(\varphi) = \min_{\psi_1, \dots, \psi_{k-1} \in L^2[a, b]} \; \sup \set{R_K(\varphi) : \varphi \ne 0, \ \ip{\varphi}{\psi_j} = 0 \text{ for } j < k},$$
where $V$ runs over the linear subspaces of $L^2[a, b]$ of dimension $k$.

## Remarks

Let $\varphi_1, \varphi_2, \dots$ be orthonormal [[eigenfunctions|4NSACSWRJZ]] with $T_K \varphi_j = \varphi_j / \lambda_j$, from the [[spectral theorem for compact self-adjoint operators|A1G25R99PY]].
On the span of $\varphi_1, \dots, \varphi_k$, the quotient is at least $1/\lambda_k$; so the max-min is at least $1/\lambda_k$.
Any $k$-dimensional $V$ contains a nonzero $\varphi$ orthogonal to $\varphi_1, \dots, \varphi_{k-1}$, and on that orthogonal complement $R_K \le 1/\lambda_k$; so the max-min is exactly $1/\lambda_k$.
The min-max form is proved in the same way, with the choice $\psi_j = \varphi_j$ attaining the minimum.

Example: for $K(x, y) = \min(x, y)$ on $[0, 1]$, $\lambda_k = (k - \tfrac12)^2 \pi^2$.
For $k = 1$ the theorem says $\int_0^1 \int_0^1 \min(x, y) \varphi(x) \varphi(y) \, dx \, dy \le \frac{4}{\pi^2} \int_0^1 \varphi^2$ for real $\varphi$, with equality for $\varphi(x) = \sin(\pi x / 2)$.

The symmetry of $K$ is needed: without it the quotient is not real, and the characteristic values need not be real or exist at all.
The negative characteristic values satisfy the same formulas applied to the kernel $-K$.

## Explanations

### L1 human

The characteristic values of a symmetric kernel can be found by optimization.
The smallest positive one corresponds to the largest stretching of a single function by the integral operator.
The next ones are the best stretching that one can guarantee when some directions are forbidden.

### L2 human

This is the integral form of the [[Courant–Fischer min-max theorem|CJK2HS2508]] for Hermitian matrices.
It allows one to compare characteristic values of two kernels without computing them: if $R_{K_1} \le R_{K_2}$ everywhere, then the $k$-th positive characteristic value of $K_1$ is at least that of $K_2$.
It is the basis of the Rayleigh–Ritz method, which gives bounds for characteristic values by restricting the quotient to finite-dimensional trial spaces.
