---
tag: VEFN58C4D0
kind: example
name: Lemaître–Tolman metric
msc: [83C15, 83F05, 83C55]
instance_of: [BY4QYYS788]
uses: [3MCZ97SW6V, 6Y50T68WKY, ECJMS4VDTF]
sources:
  - url: https://en.wikipedia.org/wiki/Lemaître–Tolman_metric
same_as:
  wikidata: Q6521045
  wikipedia: Lemaître–Tolman metric
---

## Example

Use units where the gravitational constant and the speed of light equal $1$, and take the cosmological constant to be $0$.
Let $E(r) > -\frac12$ and $M(r)$ be smooth functions, and let $R(t, r) > 0$ be a function with $\partial_r R > 0$.
In coordinates $(t, r, \theta, \phi)$, the *Lemaître–Tolman metric* is
$$g = -dt^2 + \frac{(\partial_r R)^2}{1 + 2E(r)}\, dr^2 + R(t, r)^2\left(d\theta^2 + \sin^2\theta\, d\phi^2\right).$$
It solves the [[Einstein field equations|3MCZ97SW6V]] with pressureless dust $T_{ab} = \rho\, u_a u_b$, $u = \partial_t$, exactly when
$$\left(\partial_t R\right)^2 = \frac{2M(r)}{R} + 2E(r), \qquad 4\pi\rho = \frac{M'(r)}{R^2\, \partial_r R}.$$
Each shell $r = \text{const}$ of dust moves on its own.
Here $R$ is its areal radius, $M(r)$ the mass inside it, and $E(r)$ its energy per unit mass.

Checks of special cases:
if $M' = 0$, the density vanishes and the metric is the [[Schwarzschild metric|6Y50T68WKY]] of mass $M$ in coordinates of freely falling observers.
If $R(t, r) = a(t)\, r$, $M(r) = M_0 r^3$ and $E(r) = -\frac{k}{2} r^2$ with constants $M_0$ and $k$, the metric becomes $-dt^2 + a^2\left(\frac{dr^2}{1 - kr^2} + r^2 d\Omega^2\right)$, the dust [[Friedmann–Lemaître–Robertson–Walker metric|ECJMS4VDTF]].
The first equation then becomes $\dot a^2 = 2M_0/a - k$, and the second gives $\rho = 3M_0/(4\pi a^3)$, so $\dot a^2 = \frac{8\pi}{3}\rho a^2 - k$, the Friedmann equation for dust.

## Explanations

### L1 human

The Lemaître–Tolman metric describes a ball of dust that is round but not uniform: the density can change with the distance from the centre.
Each spherical shell of dust falls or expands like a stone thrown upwards, with its own energy.
It contains both the expanding uniform universe of cosmology and the empty spacetime around a star as special cases.
It is used to model collapsing clouds and lumpy regions of the universe, and also called the Lemaître–Tolman–Bondi model.
