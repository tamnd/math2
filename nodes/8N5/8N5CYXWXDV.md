---
tag: 8N5CYXWXDV
kind: definition
name: Pseudospectral optimal control
msc: [49M37, 49M25, 65M70]
defines: FZ4BRYJ0YZ
uses: [T58W34D60G, 58895A7T4H, 237KR6FRCK, QFYGJVA996]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudospectral_optimal_control
---

## Definition

Consider a [[trajectory optimization|58895A7T4H]] problem on $[t_0, t_f]$ with dynamics $x' = f(x, u, t)$, cost $\phi(x(t_f)) + \int_{t_0}^{t_f} L(x, u, t) \, dt$, and boundary conditions.
Map the interval to $[-1, 1]$ by $t = \frac{t_f - t_0}{2} \tau + \frac{t_f + t_0}{2}$.
Let $N \ge 2$ and let $-1 = \tau_0 < \tau_1 < \cdots < \tau_N = 1$ be the Legendre–Gauss–Lobatto nodes, where $\tau_1, \dots, \tau_{N-1}$ are the zeros of $P_N'$ and $P_N$ is the [[Legendre polynomial|QFYGJVA996]] of degree $N$.
Let $w_0, \dots, w_N$ be the corresponding quadrature weights, and let $\ell_0, \dots, \ell_N$ be the [[Lagrange basis polynomials|237KR6FRCK]] of the nodes.
Let $D$ be the $(N + 1) \times (N + 1)$ matrix with $D_{kj} = \ell_j'(\tau_k)$.
The *Legendre pseudospectral method* replaces the problem by the nonlinear program with unknowns $x_0, \dots, x_N \in \R^n$ and $u_0, \dots, u_N \in \R^m$:

1. minimise $\phi(x_N) + \frac{t_f - t_0}{2} \sum_{k=0}^N w_k L(x_k, u_k, t(\tau_k))$;
2. subject to $\sum_{j=0}^N D_{kj} x_j = \frac{t_f - t_0}{2} f(x_k, u_k, t(\tau_k))$ for $k = 0, \dots, N$;
3. and to the boundary conditions on $x_0$ and $x_N$ and the path constraints at the nodes.

The state is then approximated by $x(\tau) \approx \sum_j x_j \ell_j(\tau)$.
*Pseudospectral optimal control* is the family of such methods, with Legendre, Chebyshev or other Gaussian nodes.

## Remarks

It is [[direct collocation|T58W34D60G]] with one interval and the nodes of a Gaussian rule as collocation points.
The Lobatto rule with $N + 1$ nodes integrates polynomials of degree up to $2N - 1$ exactly.
Variants use Legendre–Gauss nodes, which omit both endpoints, or Legendre–Gauss–Radau nodes, which omit one endpoint.

Example: $N = 2$ gives $P_2'(\tau) = 3\tau$, so the nodes are $-1, 0, 1$, with weights $\frac{1}{3}, \frac{4}{3}, \frac{1}{3}$ (Simpson's rule).
The differentiation matrix is
$$D = \begin{pmatrix} -3/2 & 2 & -1/2 \\ -1/2 & 0 & 1/2 \\ 1/2 & -2 & 3/2 \end{pmatrix}.$$
For instance, the first row gives the derivative at $-1$ of the parabola through $(-1, a)$, $(0, b)$, $(1, c)$, which is $(-3a + 4b - c) / 2$.

Non-example: collocation at equally spaced nodes with one global polynomial of high degree is not a pseudospectral method, and it suffers from the Runge phenomenon.

## Explanations

### L1 human

The method approximates the whole trajectory by one polynomial through special nodes and enforces the dynamics at those nodes.
