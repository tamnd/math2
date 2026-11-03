---
tag: HGZA2K3ZXD
kind: definition
name: Kelvin wave
msc: [76U60, 86A05, 86A10]
defines: QERM9Y9QSJ
uses: [NT73Y95RY5, 287Z5PMWY5, F2D7MXW8V1, MT3A0DDAA8]
sources:
  - url: https://en.wikipedia.org/wiki/Kelvin_wave
---

## Definition

Consider a layer of mean depth $H > 0$ with gravitational acceleration $g$ and Coriolis parameter $f(y)$.
Its [[shallow water equations|NT73Y95RY5]] linearised about rest are
$$\partial_t u - f v = -g \, \partial_x \eta, \qquad \partial_t v + f u = -g \, \partial_y \eta, \qquad \partial_t \eta + H (\partial_x u + \partial_y v) = 0.$$
Here $(u, v)$ is the velocity and $\eta$ the surface displacement.
Let $c = \sqrt{g H}$.
A *Kelvin wave* is a solution with $v \equiv 0$ that is bounded and decays away from the line $y = 0$.

1. *Coastal Kelvin wave.* On an [[f-plane|287Z5PMWY5]] with $f = f_0 > 0$ and a wall at $y = 0$ bounding the fluid $y > 0$, it is
$$\eta = F(x - c t) \, e^{-y / L_d}, \qquad u = \frac{g}{c} \eta, \qquad L_d = \frac{c}{f_0},$$
for any smooth bounded profile $F$.
2. *Equatorial Kelvin wave.* On the equatorial [[beta plane|F2D7MXW8V1]] with $f = \beta y$, $\beta > 0$, and no wall, it is
$$\eta = F(x - c t) \, e^{-\beta y^2 / (2c)}, \qquad u = \frac{g}{c} \eta.$$

## Remarks

Check of the coastal case: with $v = 0$ the first and third equations give the non-dispersive wave $\eta = F(x - ct)$, $u = (g / c) \eta$.
The second equation becomes $f_0 u = -g \, \partial_y \eta$, that is $\partial_y \eta = -(f_0 / c) \eta$, which gives the decay $e^{-y / L_d}$ over the [[deformation radius|MT3A0DDAA8]] $L_d$.
The same computation with $f = \beta y$ gives $\partial_y \eta = -(\beta y / c) \eta$ and the Gaussian profile of the equatorial wave, with width $\sqrt{c / \beta}$.

So the coastal wave in the northern hemisphere moves with the coast on its right, and the equatorial wave moves eastward.

Example: for the deep ocean, $H = 4000$ m gives $c \approx 198$ m/s and, with $f_0 = 10^{-4}$ s$^{-1}$, an offshore decay scale of about $2000$ km.

Non-example: the profile $F(x + ct) e^{-y / L_d}$, moving in the opposite direction, is not a solution: the cross-wall balance would require $\partial_y \eta = +(f_0 / c) \eta$, which grows away from the wall and is unbounded.

In a stratified fluid the same forms hold for each vertical mode, with $c$ replaced by the internal gravity wave speed of the mode.
