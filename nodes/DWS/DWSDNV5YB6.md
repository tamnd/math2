---
tag: DWSDNV5YB6
kind: definition
name: Boyer–Lindquist coordinates
msc: [83C15, 83C57]
defines: 2NJH36SR8A
uses: [BY4QYYS788, 5AKNNW3W4Z]
sources:
  - url: https://en.wikipedia.org/wiki/Boyer–Lindquist_coordinates
---

## Definition

Use geometrized Gaussian units.
Fix real parameters $M$ (mass), $a$ (rotation) and $Q$ (charge), and set
$$\Sigma = r^2 + a^2\cos^2\theta, \qquad \Delta = r^2 - 2Mr + a^2 + Q^2.$$
Let $t \in \R$, $\theta \in (0, \pi)$, $\phi$ an angle of period $2\pi$, and $r$ in an interval where $\Delta \ne 0$ and $\Sigma \ne 0$.
*Boyer–Lindquist coordinates* are coordinates $(t, r, \theta, \phi)$ in which the [[Lorentzian metric|BY4QYYS788]] reads
$$g = -\frac{\Delta - a^2\sin^2\theta}{\Sigma}\, dt^2 - \frac{2a\sin^2\theta\,(r^2 + a^2 - \Delta)}{\Sigma}\, dt\, d\phi + \frac{(r^2 + a^2)^2 - \Delta a^2 \sin^2\theta}{\Sigma}\sin^2\theta\, d\phi^2 + \frac{\Sigma}{\Delta}\, dr^2 + \Sigma\, d\theta^2.$$
This is the Kerr–Newman metric; $Q = 0$ gives the Kerr metric.

## Remarks

Example: for $M = Q = 0$, $\Delta = r^2 + a^2$, the cross term vanishes, and
$$g = -dt^2 + \frac{\Sigma}{r^2 + a^2}\, dr^2 + \Sigma\, d\theta^2 + (r^2 + a^2)\sin^2\theta\, d\phi^2.$$
This is flat Minkowski space written with $x = \sqrt{r^2 + a^2}\sin\theta\cos\phi$, $y = \sqrt{r^2 + a^2}\sin\theta\sin\phi$, $z = r\cos\theta$, the oblate spheroidal coordinates.
For $Q = 0$ one checks $\frac{\Delta - a^2\sin^2\theta}{\Sigma} = 1 - \frac{2Mr}{\Sigma}$ and $r^2 + a^2 - \Delta = 2Mr$, which gives the usual form of the [[Kerr metric|X3FZC85THY]].

Non-example: the Kerr–Schild coordinates of the Kerr spacetime are not Boyer–Lindquist coordinates.
In them the metric is flat Minkowski space plus a multiple of $\ell \otimes \ell$ for a null covector $\ell$, and it has several off-diagonal terms besides $dt\, d\phi$.

The coordinates fail where $\Delta = 0$, which are the horizons $r_\pm = M \pm \sqrt{M^2 - a^2 - Q^2}$, and on the axis $\sin\theta = 0$.
The fields $\partial_t$ and $\partial_\phi$ are [[Killing vector fields|5AKNNW3W4Z]], because no coefficient depends on $t$ or $\phi$.
