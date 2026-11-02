---
tag: MR4D29XAPB
kind: definition
name: Galerkin method
msc: [65N30, 35A15]
defines: Y5B0PEBKE8
uses: [HM2HHE3J51, 0SQZMXB6GP, 4A82S5FVRT, 85KK79FCN5, 86KRHS6X22]
sources:
  - url: https://en.wikipedia.org/wiki/Galerkin_method
---

## Definition

Let $H$ be a real [[Hilbert space|HM2HHE3J51]], and let $B \colon H \times H \to \R$ be a bounded [[bilinear form|0SQZMXB6GP]].
Let $f$ be a bounded linear functional on $H$, an element of the [[continuous dual space|4A82S5FVRT]].
Consider the problem of finding $u \in H$ with $B(u, v) = f(v)$ for all $v \in H$.
Let $V_N$ be a finite-dimensional subspace of $H$.
The *Galerkin method* replaces this problem by the following one: find $u_N \in V_N$ such that
$$B(u_N, v) = f(v) \quad \text{for all } v \in V_N.$$
The element $u_N$ is the *Galerkin approximation* of $u$ in $V_N$.

## Remarks

If $\varphi_1, \ldots, \varphi_N$ is a basis of $V_N$ and $u_N = \sum_j c_j \varphi_j$, the problem is the linear system $\sum_{j=1}^{N} B(\varphi_j, \varphi_i) \, c_j = f(\varphi_i)$ for $i = 1, \ldots, N$.
If $B$ is [[coercive|86KRHS6X22]] with constant $\alpha$ and bounded with constant $M$, the [[Lax–Milgram theorem|85KK79FCN5]] applied on $V_N$ gives a unique $u_N$.
Subtracting the two problems gives Galerkin orthogonality: $B(u - u_N, v) = 0$ for all $v \in V_N$.
From it follows Céa's lemma: $\norm{u - u_N} \le \frac{M}{\alpha} \inf_{v \in V_N} \norm{u - v}$.

Example: for $-u'' = 1$ on $(0, 1)$ with $u(0) = u(1) = 0$, take $H = H^1_0(0, 1)$, $B(u, v) = \int_0^1 u' v' \, dx$, $f(v) = \int_0^1 v \, dx$ and $V_1$ spanned by $\varphi(x) = x(1 - x)$.
Then $B(\varphi, \varphi) = \int_0^1 (1 - 2x)^2 \, dx = 1/3$ and $f(\varphi) = 1/6$, so $u_1 = \frac{1}{2} x(1 - x)$.
This is the exact solution, as Céa's lemma predicts, since the exact solution lies in $V_1$.

Non-example: choosing $u_N \in V_N$ so that $B(u_N, w) = f(w)$ for all $w$ in a different subspace $W_N \ne V_N$ is not the Galerkin method in the sense above.
It is called a Petrov–Galerkin method, and its analysis needs an inf-sup condition instead of coercivity.
