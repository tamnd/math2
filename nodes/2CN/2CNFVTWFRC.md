---
tag: 2CNFVTWFRC
kind: definition
name: Geodesic
msc: [53C22]
defines: NSYMQMHPDN
uses: [GH6CXWFNDJ, CAZYGE1T4E, 5FZDQQHQKM]
sources:
  - url: https://en.wikipedia.org/wiki/Geodesic
---

## Definition

Let $(M, g)$ be a [[pseudo-Riemannian manifold|GH6CXWFNDJ]] with [[Levi-Civita connection|CAZYGE1T4E]] $\nabla$, and let $I \subseteq \R$ be an interval.
A smooth curve $\gamma \colon I \to M$ is a *geodesic* if
$$D_t \gamma'(t) = 0 \quad \text{for all } t \in I,$$
where $D_t$ is the [[covariant derivative|5FZDQQHQKM]] along $\gamma$ induced by $\nabla$.

## Remarks

In local coordinates, with Christoffel symbols $\Gamma^k_{ij}$, the condition is the geodesic equation
$$\ddot\gamma^k + \sum_{i,j} \Gamma^k_{ij}(\gamma) \, \dot\gamma^i \dot\gamma^j = 0, \qquad k = 1, \ldots, n.$$

Example: in $\R^n$ with the Euclidean metric all $\Gamma^k_{ij}$ vanish, so the geodesics are the curves with $\ddot\gamma = 0$, that is $\gamma(t) = p + tv$.

Non-example: in $\R^2$, the curve $\gamma(t) = (t^2, 0)$ traces a straight line, but $\ddot\gamma = (2, 0) \ne 0$, so it is not a geodesic: a geodesic must have constant speed.

The quantity $g(\gamma', \gamma')$ is constant along a geodesic.
On a Riemannian manifold, every geodesic is locally length-minimizing: each $t \in I$ has a neighbourhood in $I$ on which $\gamma$ is a shortest curve between its endpoints.
For each $p \in M$ and $v \in T_pM$ there is a unique maximal geodesic $\gamma_v$ with $\gamma_v(0) = p$ and $\gamma_v'(0) = v$.
