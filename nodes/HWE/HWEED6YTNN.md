---
tag: HWEED6YTNN
kind: definition
name: Griffiths positivity
msc: [32L05, 53C55]
defines: FVCDGMNSAN
uses: [TKA958Z4KZ, Q6X6W2N29G, 7RC9CN2Q49, JSGWAN2RJV]
sources:
  - url: https://en.wikipedia.org/wiki/Ample_line_bundle
---

## Definition

Let $X$ be a [[complex manifold|JSGWAN2RJV]] of dimension $n$ and let $E \to X$ be a [[holomorphic vector bundle|TKA958Z4KZ]] of rank $r$ with a [[Hermitian metric|Q6X6W2N29G]] $h$.
Let $\Theta$ be the curvature of the [[Chern connection|7RC9CN2Q49]] of $(E, h)$.
Near a point $x$, choose local coordinates $z_1, \dots, z_n$ and a frame $e_1, \dots, e_r$ of $E$ that is orthonormal at $x$, and write
$$i \Theta(x) = i \sum_{j,k=1}^{n} \sum_{\lambda,\mu=1}^{r} c_{jk\lambda\mu}\, dz_j \wedge d\bar z_k \otimes e_\lambda^* \otimes e_\mu.$$
The bundle $(E, h)$ is *Griffiths positive* if at every point $x \in X$
$$\sum_{j,k,\lambda,\mu} c_{jk\lambda\mu}\, \xi_j \bar\xi_k v_\lambda \bar v_\mu > 0$$
for all nonzero $\xi = (\xi_1, \dots, \xi_n) \in \C^n$ and all nonzero $v = (v_1, \dots, v_r) \in \C^r$.

## Remarks

Intrinsically, the condition says that $h(i\Theta(\xi, \bar\xi) v, v) > 0$ for every nonzero tangent vector $\xi \in T_x X$ and every nonzero $v \in E_x$.
A holomorphic vector bundle is called Griffiths positive if it admits a metric with this property.
For $r = 1$ the condition is exactly that of a [[positive line bundle|J45KWFHENP]].

Example: let $L$ be a positive line bundle with metric $h_L$ and curvature $i\Theta_L = i \sum a_{jk} dz_j \wedge d\bar z_k$, and let $E = L^{\oplus r}$ with the direct sum metric.
Then $c_{jk\lambda\mu} = a_{jk} \delta_{\lambda\mu}$, and the sum equals $\left(\sum a_{jk} \xi_j \bar \xi_k\right) \abs{v}^2 > 0$.

Non-example: $E = L \oplus \mathcal{O}_X$ with the sum of the metric of $L$ and the trivial metric.
The curvature vanishes on the second summand, so the sum is $0$ for $v = (0, 1)$, and the condition fails.

Quotient bundles of Griffiths positive bundles are Griffiths positive, and Griffiths positive bundles on compact manifolds are ample.
