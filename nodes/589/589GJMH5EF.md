---
tag: 589GJMH5EF
kind: statement
role: theorem
name: Griffiths transversality
msc: [32G20, 14D07]
uses: [YGNXQVTWP3, VKQSM3BCE4, X60JG9AEQJ, CYPA882RB9, EWZ1G10MAY]
about: [YGNXQVTWP3]
sources:
  - url: https://en.wikipedia.org/wiki/Period_mapping
---

## Statement

Let $\varpi \colon \mathcal{X} \to B$ be a complex analytic [[family|VKQSM3BCE4]] of compact [[Kähler manifolds|X60JG9AEQJ]] over a simply connected base $B$.
Fix $k$, let $H = H^k(X_0, \C)$, and let $\mathcal{P}^p \colon B \to \operatorname{Gr}(f^p, H)$, $t \mapsto F^p H^k(X_t)$, be the components of its [[period map|YGNXQVTWP3]].
Then:

1. Each $\mathcal{P}^p$ is holomorphic.
2. For each $t \in B$ and each tangent vector $v \in T_t B$, the differential $d\mathcal{P}^p_t(v)$, viewed in $T_{F^p}\operatorname{Gr}(f^p, H) = \Hom(F^p, H/F^p)$, has image in $F^{p-1}/F^p$, where $F^j = F^j H^k(X_t)$.

## Remarks

Equivalently, if $s(t)$ is a holomorphic family of classes with $s(t) \in F^p H^k(X_t)$, then the derivative of $s$ in any direction, taken in the fixed space $H$, lies in $F^{p-1} H^k(X_t)$.
The idea of the proof: represent $s(t)$ by closed forms of type $(r, k-r)$ with $r \ge p$ on $X_t$.
To first order, a change of complex structure replaces $dz_j$ by $dz_j + \sum_k \varphi_{jk} d\bar z_k$, so it lowers the holomorphic degree of a form by at most one.
Hence the derivative has components only in types $(r, k-r)$ with $r \ge p - 1$.

Example: for a family of curves and $k = 1$, $F^0 = H$, so condition 2 holds automatically.
For Calabi–Yau threefolds and $k = 3$, condition 2 says that the derivative of the line $F^3 = H^{3,0}$ lies in $F^2$, which is a genuine restriction.

## Explanations

### L1 human

The Hodge pieces of the cohomology move holomorphically as the complex structure varies.
Moreover, each step of the Hodge filtration can only move "one step down" to first order.
This restricts which curves in the period domain can come from families of manifolds.

### L2 human

Transversality is the key constraint of variations of Hodge structure; it is built into their definition.
Period domains are usually not Hermitian symmetric, and the transversality condition defines a horizontal distribution on them.
Curvature estimates along horizontal directions give the Griffiths–Schmid results on period maps, for instance that horizontal holomorphic maps from a disc are distance decreasing for a suitable metric.
The derivative of $\mathcal{P}^p$ is computed by the [[Kodaira–Spencer map|EWZ1G10MAY]] followed by cup product and contraction.
