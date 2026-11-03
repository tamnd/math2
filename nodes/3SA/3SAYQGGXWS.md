---
tag: 3SAYQGGXWS
kind: definition
name: Kruskal–Szekeres coordinates
msc: [83C15, 83C57]
defines: 2CCXEC0VR7
uses: [6Y50T68WKY, BY4QYYS788, FW2JKAN14B]
sources:
  - url: https://en.wikipedia.org/wiki/Kruskal–Szekeres_coordinates
---

## Definition

Fix $m > 0$ and use units where the gravitational constant and the speed of light equal $1$.
Let $g$ be the [[Schwarzschild metric|6Y50T68WKY]] of mass $m$ in coordinates $(t, r, \theta, \phi)$ with $r > 2m$.
The *Kruskal–Szekeres coordinates* $(T, X, \theta, \phi)$ on this exterior region are
$$T = \left(\frac{r}{2m} - 1\right)^{1/2} e^{r/4m} \sinh\frac{t}{4m}, \qquad X = \left(\frac{r}{2m} - 1\right)^{1/2} e^{r/4m} \cosh\frac{t}{4m}.$$
They satisfy $X^2 - T^2 = \left(\frac{r}{2m} - 1\right) e^{r/2m}$, and in them
$$g = \frac{32 m^3}{r} e^{-r/2m}\left(-dT^2 + dX^2\right) + r^2\left(d\theta^2 + \sin^2\theta\, d\phi^2\right),$$
where $r$ is now the function of $(T, X)$ defined by $X^2 - T^2 = \left(\frac{r}{2m} - 1\right) e^{r/2m}$.
The *Kruskal extension* is the manifold $\set{(T, X) : T^2 - X^2 < 1} \times S^2$ with this [[Lorentzian metric|BY4QYYS788]].

## Remarks

The exterior chart above is the region $X > \abs{T}$.
On it $X^2 - T^2 > 0$, so $r > 2m$, and $T / X = \tanh(t/4m)$ recovers $t$.

Explicitly, $r = 2m\left(1 + W\!\left((X^2 - T^2)/e\right)\right)$, where $W$ is the principal branch of the [[Lambert W function|FW2JKAN14B]].
This is a smooth positive function on the whole region $T^2 - X^2 < 1$, so the metric is smooth there, also on the horizon $r = 2m$, which is the pair of lines $T = \pm X$.
The hyperbola $T^2 - X^2 = 1$ corresponds to $r = 0$, where the curvature blows up, so it is not part of the manifold.

Non-example: the Schwarzschild coordinates are not defined at $r = 2m$, and the [[Eddington–Finkelstein coordinates|SG9GAYQT4R]] cover only half of the Kruskal extension.

The four regions are the exterior $X > \abs{T}$, a second exterior $X < -\abs{T}$, the black hole $T > \abs{X}$ and the white hole $T < -\abs{X}$.
Radial null curves are the lines $T = \pm X + \text{const}$.
