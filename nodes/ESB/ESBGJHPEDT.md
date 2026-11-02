---
tag: ESBGJHPEDT
kind: definition
name: Nakano positivity
msc: [32L05, 32L20, 53C55]
defines: WJ8TRE4F1K
uses: [TKA958Z4KZ, Q6X6W2N29G, 7RC9CN2Q49, FVCDGMNSAN, JSGWAN2RJV]
sources:
  - url: https://en.wikipedia.org/wiki/Kodaira_vanishing_theorem
---

## Definition

Let $X$ be a [[complex manifold|JSGWAN2RJV]] of dimension $n$ and let $E \to X$ be a [[holomorphic vector bundle|TKA958Z4KZ]] of rank $r$ with a [[Hermitian metric|Q6X6W2N29G]] $h$.
At a point $x$, write the curvature $\Theta$ of the [[Chern connection|7RC9CN2Q49]] in local coordinates and a frame orthonormal at $x$ as
$$i \Theta(x) = i \sum_{j,k=1}^{n} \sum_{\lambda,\mu=1}^{r} c_{jk\lambda\mu}\, dz_j \wedge d\bar z_k \otimes e_\lambda^* \otimes e_\mu.$$
The bundle $(E, h)$ is *Nakano positive* if at every point $x \in X$
$$\sum_{j,k,\lambda,\mu} c_{jk\lambda\mu}\, \tau_{j\lambda} \bar\tau_{k\mu} > 0$$
for every nonzero complex $n \times r$ matrix $\tau = (\tau_{j\lambda})$.
Such a matrix is the same as a tensor $\tau \in T_x X \otimes E_x$.

## Remarks

Taking $\tau_{j\lambda} = \xi_j v_\lambda$ recovers the condition of [[Griffiths positivity|FVCDGMNSAN]], so Nakano positive bundles are Griffiths positive.
For $r = 1$ or $n = 1$ every tensor $\tau$ is of this form, and the two notions agree.

Example: $E = L^{\oplus r}$, where $L$ is a positive line bundle with curvature $i \sum a_{jk} dz_j \wedge d\bar z_k$, with the direct sum metric.
Then $c_{jk\lambda\mu} = a_{jk} \delta_{\lambda\mu}$, and the sum is $\sum_\lambda \sum_{j,k} a_{jk} \tau_{j\lambda} \bar\tau_{k\lambda}$.
Each inner sum is $\ge 0$ because $(a_{jk})$ is positive definite, and some inner sum is $> 0$ because $\tau \ne 0$.

Non-example: a trivial bundle $X \times \C^r$ with the standard metric has $\Theta = 0$, so the sum is $0$ for every $\tau$.

Nakano's vanishing theorem: if $X$ is compact Kähler and $E$ is Nakano positive, then $H^q(X, K_X \otimes E) = 0$ for $q \ge 1$, where $K_X$ is the canonical bundle.
