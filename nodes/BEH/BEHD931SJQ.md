---
tag: BEHD931SJQ
kind: definition
name: Eta invariant
msc: [58J28, 58J50]
defines: PRJCH788AM
uses: [MT9P2X85V8, 0NEGN5CRSC, 0BQAA2BK3Q, 0M3YQJ81NB, G4SW7HJG88]
sources:
  - url: https://en.wikipedia.org/wiki/Eta_invariant
---

## Definition

Let $Y$ be a closed smooth manifold of dimension $n$ with a smooth positive density, and let $E$ be a Hermitian vector bundle over $Y$.
Let $A$ be a formally [[self-adjoint|0NEGN5CRSC]] [[elliptic differential operator|MT9P2X85V8]] of order $m \ge 1$ on sections of $E$.
Its spectrum is a discrete set of real [[eigenvalues|0BQAA2BK3Q]] $\lambda$ of finite multiplicity.
The *eta function* of $A$ is
$$\eta_A(s) = \sum_{\lambda \ne 0} \operatorname{sign}(\lambda) \, \abs{\lambda}^{-s},$$
summed over the nonzero eigenvalues counted with multiplicity.
It converges for $\operatorname{Re} s > n / m$, and it has a meromorphic [[continuation|0M3YQJ81NB]] to $\C$ that is holomorphic at $s = 0$.
The *eta invariant* of $A$ is $\eta_A(0)$.

## Remarks

The regularity at $s = 0$ was proved by Atiyah, Patodi and Singer, with the general case due to Gilkey.
Some authors call $\xi_A = \tfrac12(\eta_A(0) + \dim \ker A)$ the reduced eta invariant.

Example: on $S^1 = \R / 2\pi\Z$ let $A = -i \, d/d\theta + a$ with $0 < a < 1$.
The eigenfunctions are $e^{ik\theta}$, $k \in \Z$, with eigenvalues $k + a$.
So $\eta_A(s) = \sum_{k \ge 0} (k + a)^{-s} - \sum_{k \ge 1} (k - a)^{-s} = \zeta(s, a) - \zeta(s, 1 - a)$, with $\zeta(s, a)$ the [[Hurwitz zeta function|G4SW7HJG88]].
Since $\zeta(0, a) = \tfrac12 - a$, the eta invariant is $\eta_A(0) = 1 - 2a$.
For $a = 0$ the nonzero spectrum $\Z \setminus \{0\}$ is symmetric and $\eta_A(0) = 0$.

Non-example: $B = d/d\theta$ on $S^1$ is elliptic but not self-adjoint; its eigenvalues $ik$ are imaginary, so $\operatorname{sign}(\lambda)$ has no meaning and $B$ has no eta invariant.
