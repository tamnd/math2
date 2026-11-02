---
tag: B9X31R5EGG
kind: definition
name: Chern connection
msc: [53C07, 32L05, 53C55]
defines: 7RC9CN2Q49
uses: [TKA958Z4KZ, Q6X6W2N29G, 5ZYRRVE8BW, M1VKCW3RFW, JSGWAN2RJV]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_connection
---

## Definition

Let $X$ be a [[complex manifold|JSGWAN2RJV]], let $E \to X$ be a [[holomorphic vector bundle|TKA958Z4KZ]], and let $h$ be a [[Hermitian metric|Q6X6W2N29G]] on $E$.
Let $\bar\partial_E$ be the [[$\bar\partial$-operator|M1VKCW3RFW]] of $E$, which sends a smooth section to an $E$-valued $(0,1)$-form and kills exactly the holomorphic sections.
The *Chern connection* of $(E, h)$ is the [[connection|5ZYRRVE8BW]] $\nabla$ on $E$ such that:

1. $\nabla$ is compatible with $h$: $d\, h(s, t) = h(\nabla s, t) + h(s, \nabla t)$ for all smooth sections $s, t$.
2. The $(0,1)$-part of $\nabla$ is $\bar\partial_E$: $\nabla^{0,1} = \bar\partial_E$.

Such a connection exists and is unique.

## Remarks

Write $\nabla = \nabla^{1,0} + \nabla^{0,1}$ for the splitting by type.
In a local holomorphic frame $e_1, \dots, e_r$, let $H$ be the matrix with entries $H_{ij} = h(e_j, e_i)$.
Then the connection matrix is $\theta = H^{-1} \partial H$ in a suitable index convention, and the curvature is $\Theta = \bar\partial \theta$, a $(1,1)$-form with values in $\operatorname{End} E$.

Example: let $L$ be a holomorphic line bundle with local holomorphic frame $e$, and let $H = h(e, e) > 0$.
Put $\nabla e = \partial \log H \otimes e$.
Clause 2 holds because $\bar\partial_E e = 0$ and $\partial \log H$ has type $(1,0)$.
Clause 1 holds because $h(\nabla e, e) + h(e, \nabla e) = (\partial \log H + \bar\partial \log H) H = dH$.
The curvature is $\Theta = d \partial \log H = -\partial \bar\partial \log H$.

Non-example: on the trivial line bundle over $\C$ with the standard metric, let $\nabla s = ds + i s\, dx$, where $x = \operatorname{Re} z$.
Since $i\, dx$ is purely imaginary, clause 1 holds.
But $i\, dx = \tfrac{i}{2}(dz + d\bar z)$, so $\nabla^{0,1} = \bar\partial + \tfrac{i}{2} d\bar z \ne \bar\partial$, and clause 2 fails.
