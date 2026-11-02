---
tag: 1TJXANASFE
kind: counterexample
name: Rossi's non-embeddable CR structure
msc: [32V30, 32V05]
uses: [ZC78JKZX9S, JFKYYK2CEB, P9CM4GQ2T0, ZAH4SK5YX7]
sources:
  - url: https://en.wikipedia.org/wiki/CR_manifold
---

## Counterexample

Let $S^3 = \set{(z_1, z_2) \in \C^2 : \abs{z_1}^2 + \abs{z_2}^2 = 1}$ be the unit [[sphere|P9CM4GQ2T0]].
Its standard [[CR structure|ZC78JKZX9S]] is spanned by the vector field
$$\bar L = z_2 \frac{\partial}{\partial \bar z_1} - z_1 \frac{\partial}{\partial \bar z_2},$$
which is tangent to $S^3$, and its conjugate is $L = \bar z_2 \frac{\partial}{\partial z_1} - \bar z_1 \frac{\partial}{\partial z_2}$.
For a real number $t$ with $0 < \abs{t} < 1$, let $\bar L_t = \bar L + t L$, and let $S^3_t$ be $S^3$ with the CR structure spanned by $\bar L_t$.
Then $S^3_t$ is a compact strongly pseudoconvex CR manifold of real dimension $3$.
Every [[CR function|JFKYYK2CEB]] $f$ on $S^3_t$, that is every $f$ with $\bar L_t f = 0$, is even: $f(-p) = f(p)$ for all $p \in S^3$.
So CR functions cannot separate the antipodal points $p$ and $-p$, and there is no CR embedding of $S^3_t$ into any $\C^N$.

## Remarks

The parity follows by expanding $f$ in spherical harmonics of bidegree $(a, b)$ in $(z, \bar z)$.
Both $L$ and $\bar L$ preserve the total degree $a + b$.
So the equation $\bar L_t f = 0$ splits into one equation for each total degree.
For odd total degree this equation has only the zero solution.
For $t = 0$ the structure is the standard one, and the coordinate functions $z_1, z_2$ embed it.
So arbitrarily small deformations destroy embeddability in dimension $3$.
This shows that the dimension hypothesis in [[Boutet de Monvel's embedding theorem|ZAH4SK5YX7]] cannot be dropped.

## Explanations

### L1 human

The round three-sphere sits in $\C^2$, and its CR structure is inherited from there.
Tilting this structure by a tiny amount gives a new abstract CR structure on the same sphere.
For the tilted structure, every function compatible with it takes the same value at opposite points.
So no collection of such functions can tell opposite points apart, and the tilted sphere cannot be placed inside any complex space as a hypersurface.
