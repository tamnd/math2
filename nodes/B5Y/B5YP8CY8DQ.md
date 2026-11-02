---
tag: B5YP8CY8DQ
kind: definition
name: Symplectic manifold
msc: [53D05]
defines: CAN490EPRT
uses: [F45VQ47GPV, 0E3G0GRPZ6, 0ZV14XRNF0, PQ7JJY0VPH, 004FRCXH6M]
sources:
  - url: https://en.wikipedia.org/wiki/Symplectic_manifold
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]].
A *symplectic form* on $M$ is a [[differential $2$-form|0E3G0GRPZ6]] $\omega$ on $M$ such that:

1. $\omega$ is [[closed|0ZV14XRNF0]]: $d\omega = 0$, where $d$ is the [[exterior derivative|004FRCXH6M]];
2. $\omega$ is nondegenerate: for each $p \in M$ and each nonzero $v \in T_p M$ there is $w \in T_p M$ with $\omega_p(v, w) \ne 0$.

A *symplectic manifold* is a pair $(M, \omega)$ of a smooth manifold and a symplectic form on it.

## Remarks

Example: $\R^{2n}$ with coordinates $(x_1, \ldots, x_n, y_1, \ldots, y_n)$ and $\omega_0 = \sum_{k=1}^n dx_k \wedge dy_k$.
It has constant coefficients, so $d\omega_0 = 0$.
If $v \ne 0$ has a nonzero component $v_{x_k}$, then $\omega_0(v, \partial_{y_k}) = v_{x_k} \ne 0$, and similarly if $v_{y_k} \ne 0$ one pairs with $\partial_{x_k}$; so $\omega_0$ is nondegenerate.

Non-example: the sphere $S^4$ has no symplectic form.
On a closed manifold of dimension $2n$, $\omega^n$ is a volume form, so the class $[\omega]^n$ is nonzero and hence $[\omega] \ne 0$ in $H^2_{dR}(M)$; but $H^2_{dR}(S^4) = 0$.

Clause 2 says that each $(T_p M, \omega_p)$ is a [[symplectic vector space|PQ7JJY0VPH]], so $\dim M$ is even.
Other standard examples are oriented surfaces with an area form and cotangent bundles $T^* Q$ with the form $-d\theta$ built from the tautological one-form $\theta$.
Darboux's theorem says that near each point there are coordinates in which $\omega = \omega_0$.
