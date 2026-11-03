---
tag: X3FZC85THY
kind: example
name: Kerr metric
msc: [83C15, 83C57]
instance_of: [JRV1T69FYJ]
uses: [2NJH36SR8A, 6Y50T68WKY, 5AKNNW3W4Z]
sources:
  - url: https://en.wikipedia.org/wiki/Kerr_metric
same_as:
  wikidata: Q1068747
  wikipedia: Kerr metric
---

## Example

Use units where the gravitational constant and the speed of light equal $1$.
Fix a mass $M > 0$ and a rotation parameter $a \in \R$, and set
$$\Sigma = r^2 + a^2 \cos^2\theta, \qquad \Delta = r^2 - 2Mr + a^2.$$
In [[Boyer–Lindquist coordinates|2NJH36SR8A]] $(t, r, \theta, \phi)$, on the region where $\Delta > 0$ and $\Sigma > 0$, the *Kerr metric* is
$$g = -\left(1 - \frac{2Mr}{\Sigma}\right) dt^2 - \frac{4 M a r \sin^2\theta}{\Sigma}\, dt\, d\phi + \frac{\Sigma}{\Delta}\, dr^2 + \Sigma\, d\theta^2 + \left(r^2 + a^2 + \frac{2 M a^2 r \sin^2\theta}{\Sigma}\right)\sin^2\theta\, d\phi^2.$$
Its [[Ricci curvature|4GTNM0WHDH]] vanishes, so it is a [[vacuum solution|JRV1T69FYJ]] of the Einstein equations.

Checks: the coefficients do not depend on $t$ or $\phi$, so $\partial_t$ and $\partial_\phi$ are [[Killing vector fields|5AKNNW3W4Z]]: the metric is stationary and axisymmetric.
For $a = 0$, $\Sigma = r^2$ and $\Delta = r^2 - 2Mr$, the cross term vanishes and $g$ becomes the [[Schwarzschild metric|6Y50T68WKY]].
For $M = 0$ it is flat Minkowski space in oblate spheroidal coordinates.
The mass is $M$ and the angular momentum is $J = aM$, read off from the behaviour of $g$ for large $r$.

If $a^2 \le M^2$, the zeros of $\Delta$ are $r_\pm = M \pm \sqrt{M^2 - a^2}$.
The surface $r = r_+$ is the [[event horizon|D8NZ32Z3SQ]] and $r = r_-$ is an inner Cauchy horizon.
Between $r_+$ and the surface $r = M + \sqrt{M^2 - a^2\cos^2\theta}$, where $g_{tt}$ changes sign, lies the [[ergosphere|SWZFAXCQMT]].
The curvature blows up where $\Sigma = 0$, that is, on the ring $r = 0$, $\theta = \pi/2$.
If $a^2 > M^2$ there is no horizon.

## Explanations

### L1 human

The Kerr metric describes the spacetime around a rotating black hole, and far away around any rotating mass.
It was found by Roy Kerr in 1963, long after the non-rotating case.
The rotation drags spacetime around with it, so close to the hole nothing can stand still relative to distant stars.
The region where this happens is the ergosphere, which lies outside the horizon and from which energy can in principle be extracted.
Astrophysical black holes are expected to be described by this metric, since they rotate but carry almost no charge.
