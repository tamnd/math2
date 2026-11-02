---
tag: YATEFAKZYB
kind: definition
name: Dirichlet eigenvalue
msc: [35P15, 35P05, 35J05]
defines: 4VD8XXQ4P3
uses: [0E0B6RA8K0, M4CEZ5K9HP, SJZX81A783, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_eigenvalue
---

## Definition

Let $\Omega \subseteq \R^n$ be a nonempty bounded open set and let $H^1_0(\Omega)$ be the [[Sobolev space|M4CEZ5K9HP]] of functions with zero boundary values.
Let $\Delta$ be the [[Laplacian|0E0B6RA8K0]].
A real number $\lambda$ is a *Dirichlet eigenvalue* of $\Omega$ if some $u \in H^1_0(\Omega)$ with $u \ne 0$ is a [[weak solution|SJZX81A783]] of
$$-\Delta u = \lambda u \quad \text{in } \Omega.$$
That is, $\int_\Omega \nabla u \cdot \nabla v \, dx = \lambda \int_\Omega u v \, dx$ for every $v \in H^1_0(\Omega)$.
Such a $u$ is a *Dirichlet eigenfunction* for $\lambda$.

## Remarks

The Dirichlet eigenvalues form a sequence $0 < \lambda_1(\Omega) < \lambda_2(\Omega) \le \lambda_3(\Omega) \le \dots \to \infty$, listed with multiplicity, when $\Omega$ is connected.
They are the [[eigenvalues|0BQAA2BK3Q]] of the Dirichlet Laplacian, a self-adjoint operator with compact inverse.
The first one is the minimum of the Rayleigh quotient: $\lambda_1(\Omega) = \min \set{ \int_\Omega \abs{\nabla u}^2 \, dx / \int_\Omega u^2 \, dx : u \in H^1_0(\Omega), u \ne 0 }$.

Example: for $\Omega = (0, \pi)$, the function $u(x) = \sin(kx)$ with $k \ge 1$ an integer vanishes at $0$ and $\pi$ and satisfies $-u'' = k^2 u$.
So $k^2$ is a Dirichlet eigenvalue, and these are all of them.

Non-example: on $(0, \pi)$, the number $0$ is not a Dirichlet eigenvalue.
The solutions of $-u'' = 0$ are $u = a + bx$, and the boundary conditions force $a = b = 0$.
With the Neumann condition $u' = 0$ instead, the constant function shows that $0$ is a Neumann eigenvalue.
