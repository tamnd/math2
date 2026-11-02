---
tag: MHGZEW6RBM
kind: definition
name: Link of a singularity
msc: [32S55, 32S50, 14B05]
defines: C831AN3RFM
uses: [3RWWZYPAFV, P9CM4GQ2T0, 0QT00PB5G2]
sources:
  - url: https://en.wikipedia.org/wiki/Milnor_map
---

## Definition

Let $V$ be a complex [[analytic set|3RWWZYPAFV]] in an open subset of $\C^N$ and let $p \in V$.
For $\varepsilon > 0$, let $S_\varepsilon(p)$ be the [[sphere|P9CM4GQ2T0]] of radius $\varepsilon$ centred at $p$, and let $K_\varepsilon = V \cap S_\varepsilon(p)$.
There is $\varepsilon_0 > 0$ such that, for $0 < \varepsilon < \varepsilon' \le \varepsilon_0$, the spaces $K_\varepsilon$ and $K_{\varepsilon'}$ are [[homeomorphic|0QT00PB5G2]].
The *link* of $V$ at $p$ is $K_\varepsilon$ for any such $\varepsilon$, defined up to homeomorphism.

## Remarks

For $\varepsilon$ small, $V \cap B_\varepsilon(p)$, where $B_\varepsilon(p)$ is the closed ball, is homeomorphic to the cone over $K_\varepsilon$ with vertex $p$; this is the conic structure theorem.
If $V$ is smooth at $p$ of complex dimension $d$, the link is a sphere $S^{2d - 1}$.
If $V = f^{-1}(0) \subset \C^{n+1}$ with an isolated singularity at $p$, the link is a smooth closed manifold of dimension $2n - 1$, and Milnor showed that it is $(n-2)$-connected.

Example: $V = \set{x^2 = y^3} \subset \C^2$ at $0$.
The map $t \mapsto (t^3, t^2)$ is a bijection from $\C$ onto $V$.
On the sphere $S_\varepsilon$, the points of $V$ are $(t^3, t^2)$ with $\abs{t}$ fixed, which trace the torus knot of type $(2, 3)$, the trefoil.

Non-example of the condition on $\varepsilon$: $V = \set{x y (y - 1) = 0} \subset \C^2$ at $0$.
For $\varepsilon < 1$, $K_\varepsilon$ consists of the two circles cut out by $x = 0$ and $y = 0$, a Hopf link.
For $\varepsilon > 1$, the line $y = 1$ also meets $S_\varepsilon$ in a third circle, so this sphere is too large to give the link.
