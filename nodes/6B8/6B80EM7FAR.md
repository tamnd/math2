---
tag: 6B80EM7FAR
kind: definition
name: Eddington–Finkelstein coordinates
msc: [83C15, 83C57]
defines: SG9GAYQT4R
uses: [6Y50T68WKY, BY4QYYS788]
sources:
  - url: https://en.wikipedia.org/wiki/Eddington–Finkelstein_coordinates
---

## Definition

Fix $m > 0$ and use units where the gravitational constant and the speed of light equal $1$.
Let $g$ be the [[Schwarzschild metric|6Y50T68WKY]] of mass $m$ in coordinates $(t, r, \theta, \phi)$ with $r > 2m$.
The *tortoise coordinate* is
$$r_* = r + 2m \ln\left(\frac{r}{2m} - 1\right).$$
The *ingoing Eddington–Finkelstein coordinates* are $(v, r, \theta, \phi)$ with $v = t + r_*$.
In them the metric reads
$$g = -\left(1 - \frac{2m}{r}\right) dv^2 + 2\, dv\, dr + r^2\left(d\theta^2 + \sin^2\theta\, d\phi^2\right).$$
This formula defines a smooth [[Lorentzian metric|BY4QYYS788]] on the larger range $v \in \R$, $r > 0$, which contains the horizon $r = 2m$.
The *outgoing Eddington–Finkelstein coordinates* use $u = t - r_*$ instead, with
$$g = -\left(1 - \frac{2m}{r}\right) du^2 - 2\, du\, dr + r^2\left(d\theta^2 + \sin^2\theta\, d\phi^2\right).$$

## Remarks

Check of the ingoing form: $dr_* = dr / (1 - 2m/r)$, so $dt = dv - dr/(1 - 2m/r)$.
Substituting gives $-(1 - 2m/r)\, dt^2 = -(1 - 2m/r)\, dv^2 + 2\, dv\, dr - dr^2 / (1 - 2m/r)$.
The last term cancels the $dr^2$ term of the Schwarzschild metric, which leaves the formula above.
The determinant of the $(v, r)$ block is $-1$, so the metric is nondegenerate at $r = 2m$.

Non-example: the Schwarzschild coordinates $(t, r, \theta, \phi)$ themselves do not cover the horizon, because $g_{rr} = (1 - 2m/r)^{-1}$ is not defined at $r = 2m$.

The curves $v = \text{const}$, $\theta, \phi$ constant are the ingoing radial null [[geodesics|NSYMQMHPDN]].
The ingoing chart covers the exterior, the horizon and the black hole interior $0 < r < 2m$; the outgoing chart covers the exterior and the white hole region.
