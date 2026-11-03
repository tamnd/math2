---
tag: SXH3GJSP46
kind: definition
name: Carter constant
msc: [83C10, 83C57]
defines: FCP5DCFADW
uses: [X3FZC85THY, 2NJH36SR8A, RNRTS8WWNM]
sources:
  - url: https://en.wikipedia.org/wiki/Carter_constant
---

## Definition

Use units where the gravitational constant and the speed of light equal $1$.
Let $g$ be the [[Kerr metric|X3FZC85THY]] with mass $M$ and rotation parameter $a$, in [[Boyer–Lindquist coordinates|2NJH36SR8A]] $(t, r, \theta, \phi)$.
Let $\gamma$ be a [[geodesic|RNRTS8WWNM]] with momentum covector $p_\mu$, and set
$$\mu^2 = -g^{\mu\nu} p_\mu p_\nu, \qquad E = -p_t, \qquad L_z = p_\phi.$$
The *Carter constant* of $\gamma$ is
$$\mathcal{Q} = p_\theta^2 + \cos^2\theta\left(a^2\left(\mu^2 - E^2\right) + \frac{L_z^2}{\sin^2\theta}\right).$$
It is constant along $\gamma$.

## Remarks

Example: for $a = 0$ the Kerr metric is the Schwarzschild metric, and
$$\mathcal{Q} = p_\theta^2 + L_z^2 \cot^2\theta = \left(p_\theta^2 + \frac{p_\phi^2}{\sin^2\theta}\right) - p_\phi^2 = L^2 - L_z^2,$$
where $L^2$ is the squared total angular momentum.
Both $L^2$ and $L_z$ are conserved by spherical symmetry, so $\mathcal{Q}$ is conserved; an equatorial orbit has $\mathcal{Q} = 0$.

Non-example: $p_\theta$ alone is not conserved, even for $a = 0$.
On an inclined circular orbit around a Schwarzschild black hole, $p_\theta$ vanishes at the highest and lowest points and is nonzero in between.

Equivalent form: many texts use $K = \mathcal{Q} + (L_z - aE)^2$ instead.
Then $K = K^{\mu\nu} p_\mu p_\nu$ for a symmetric Killing tensor $K^{\mu\nu}$, and the conservation of $K$ along geodesics follows from the Killing tensor equation $\nabla_{(\alpha} K_{\beta\gamma)} = 0$.
The constants $\mu$, $E$, $L_z$ come from the metric and the [[Killing vector fields|5AKNNW3W4Z]] $\partial_t$ and $\partial_\phi$.
