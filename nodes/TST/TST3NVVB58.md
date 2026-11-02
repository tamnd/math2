---
tag: TST3NVVB58
kind: definition
name: Strict hyperbolicity
msc: [35L40, 35L45, 35L65]
defines: P3VXR8FW17
uses: [92C3S03AQZ, 0BQAA2BK3Q, F31T650DKY]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperbolic_partial_differential_equation
---

## Definition

Let $\Omega \subseteq \R^n \times \R$ be open, let $N \ge 1$, and let $A_1, \ldots, A_n \colon \Omega \to \R^{N \times N}$ be continuous.
The first-order system
$$\partial_t u + \sum_{j=1}^{n} A_j(x, t)\, \partial_{x_j} u = 0$$
for $u \colon \Omega \to \R^N$ is *strictly hyperbolic* if for every $(x, t) \in \Omega$ and every $\xi \in \R^n \setminus \set{0}$, the matrix $A(x, t, \xi) = \sum_{j=1}^{n} \xi_j A_j(x, t)$ has $N$ real and distinct [[eigenvalues|0BQAA2BK3Q]].

Let $P u = 0$ be a scalar linear equation of order $m$ in the variables $(x, t)$, with [[principal symbol|F31T650DKY]] $p_m(x, t; \xi, \tau)$.
It is *strictly hyperbolic* with respect to $t$ if, for every $(x, t)$ and every $\xi \ne 0$, the polynomial $\tau \mapsto p_m(x, t; \xi, \tau)$ has $m$ real and distinct roots.

## Remarks

Example: the [[hyperbolic|92C3S03AQZ]] system $u_t + \begin{pmatrix} 0 & -1 \\ -c^2 & 0 \end{pmatrix} u_x = 0$ with $c > 0$, obtained from $w_{tt} = c^2 w_{xx}$ by setting $u = (w_x, w_t)$, has eigenvalues $\pm c$, which are real and distinct.
For the wave operator $\partial_t^2 - c^2 \Delta$, the principal symbol is $-\tau^2 + c^2 \abs{\xi}^2$, with the two distinct real roots $\tau = \pm c\abs{\xi}$ when $\xi \ne 0$.
Non-example: the system $u_t + \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} u_x = 0$ has the double eigenvalue $1$, so it is not strictly hyperbolic; it is not even diagonalizable.
Strict hyperbolicity implies that $A(x, t, \xi)$ is diagonalizable over $\R$, so a strictly hyperbolic system is hyperbolic.
The converse fails: $u_t + I u_x = 0$ with $I$ the $2 \times 2$ identity is hyperbolic but not strictly hyperbolic.
