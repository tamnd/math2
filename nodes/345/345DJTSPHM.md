---
tag: 345DJTSPHM
kind: statement
role: theorem
name: Cauchy–Pompeiu formula
msc: ["30E20", 32W05]
uses: [698R12MY4G, 0DG10TVYPN, 06SKCHDQT5, 0HR3N02317]
about: [0DG10TVYPN, WMXDVF36ZT]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_integral_formula
---

## Statement

Let $D \subset \C$ be a bounded open set whose boundary $\partial D$ consists of finitely many piecewise $C^1$ closed curves.
Orient $\partial D$ so that $D$ lies on the left.
Let $f$ be a [[continuously differentiable|06SKCHDQT5]] complex-valued function on an open set that contains the closure $\bar D$.
Then for each $z \in D$,
$$f(z) = \frac{1}{2\pi i} \oint_{\partial D} \frac{f(\zeta)}{\zeta - z} \, d\zeta - \frac{1}{\pi} \iint_D \frac{\partial f / \partial \bar \zeta \, (\zeta)}{\zeta - z} \, dA(\zeta),$$
where $\partial f / \partial \bar \zeta$ is the [[Wirtinger derivative|698R12MY4G]] and $dA$ is the area measure.

## Remarks

Proof idea: apply [[Green's theorem|0HR3N02317]], in the form $\oint_{\partial \Omega} g \, d\zeta = 2i \iint_\Omega \partial g / \partial \bar \zeta \, dA$, to $g(\zeta) = f(\zeta)/(\zeta - z)$ on $D$ minus a small disc around $z$.
Since $1/(\zeta - z)$ is holomorphic there, $\partial g / \partial \bar \zeta = (\partial f / \partial \bar \zeta)/(\zeta - z)$; the small circle contributes $2\pi i f(z)$ in the limit.
If $f$ is holomorphic, then $\partial f / \partial \bar \zeta = 0$ and the formula is [[Cauchy's integral formula|0DG10TVYPN]].
If $f$ has compact support in $\C$, the boundary term vanishes and $f(z) = \frac{1}{\pi} \iint \frac{\partial f / \partial \bar \zeta}{z - \zeta} \, dA(\zeta)$.
One deduces from it that, for $g$ of class $C^1$ with compact support, $u(z) = \frac{1}{\pi} \iint \frac{g(\zeta)}{z - \zeta} \, dA(\zeta)$ solves $\partial u / \partial \bar z = g$.

## Explanations

### L1 human

Cauchy's formula recovers a holomorphic function inside a region from its values on the boundary.
For a smooth function that is not holomorphic, the boundary values are not enough.
The Cauchy–Pompeiu formula adds an area integral that measures how far the function is from being holomorphic.

### L2 human

The formula is the basic tool for the inhomogeneous Cauchy–Riemann equation $\partial u / \partial \bar z = g$.
The kernel $\frac{1}{\pi z}$ is a fundamental solution of the operator $\partial / \partial \bar z$.
This is the starting point of the $\bar\partial$ method, of the theory of the Beltrami equation through the Cauchy and Beurling transforms, and of generalizations to several complex variables.
