---
tag: CP0TQ5ZWSP
kind: definition
name: Finite element method
msc: [65N30, 65M60]
defines: 98GZ9DVHTA
uses: [Y5B0PEBKE8, SJZX81A783, HM2HHE3J51, 0SQZMXB6GP, M4CEZ5K9HP]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_element_method
---

## Definition

Let $V$ be a real [[Hilbert space|HM2HHE3J51]] of functions on a bounded polygonal domain $\Omega \subset \R^d$, for example the [[Sobolev space|M4CEZ5K9HP]] $H^1_0(\Omega)$.
Let $a \colon V \times V \to \R$ be a bounded [[bilinear form|0SQZMXB6GP]] and $\ell \colon V \to \R$ a bounded linear functional.
The [[weak form|SJZX81A783]] of the problem is: find $u \in V$ with $a(u, v) = \ell(v)$ for all $v \in V$.
The *finite element method* consists of:

1. A mesh $\mathcal{T}_h$: a partition of $\overline{\Omega}$ into finitely many closed simplices of diameter at most $h$, meeting face to face.
2. A finite-dimensional space $V_h \subseteq V$ of functions that are polynomials of degree at most $k$ on each element of $\mathcal{T}_h$, with a locally supported basis.
3. The discrete problem: find $u_h \in V_h$ with $a(u_h, v_h) = \ell(v_h)$ for all $v_h \in V_h$.

## Remarks

In a basis $\varphi_1, \ldots, \varphi_N$ of $V_h$, the discrete problem is the linear system $A c = b$ with $A_{ij} = a(\varphi_j, \varphi_i)$ and $b_i = \ell(\varphi_i)$, and $u_h = \sum_j c_j \varphi_j$.
If $a$ is coercive, $a(v, v) \ge \alpha \norm{v}^2$, and $\abs{a(u, v)} \le M \norm{u} \norm{v}$, then $u_h$ exists, is unique, and Céa's lemma gives $\norm{u - u_h} \le (M / \alpha) \min_{v_h \in V_h} \norm{u - v_h}$.
Example: $-u'' = f$ on $(0, 1)$ with $u(0) = u(1) = 0$, $V = H^1_0(0, 1)$, $a(u, v) = \int_0^1 u' v'$, nodes $x_i = ih$ with $h = 1/(N+1)$, and hat functions $\varphi_i$ with $\varphi_i(x_j) = \delta_{ij}$.
Then $\int \varphi_i'^2 = 2/h$ and $\int \varphi_i' \varphi_{i \pm 1}' = -1/h$, so $A = h^{-1} \operatorname{tridiag}(-1, 2, -1)$.
Non-example: the Galerkin method with $V_N$ spanned by $\sin(\pi x), \ldots, \sin(N \pi x)$ satisfies clause 3 but not clause 2.
These functions are not piecewise polynomials on a mesh, so this is a spectral method.
