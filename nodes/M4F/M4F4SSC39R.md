---
tag: M4F4SSC39R
kind: definition
name: Displacement thickness
msc: [76D10]
defines: 6DZC6HPDH2
uses: [YCFPD0GE5G]
sources:
  - url: https://en.wikipedia.org/wiki/Boundary_layer_thickness
---

## Definition

Consider a two-dimensional incompressible [[boundary layer|YCFPD0GE5G]] along the wall $y = 0$, with tangential velocity $u(x, y)$ and outer speed $U(x) > 0$.
Assume that $1 - u(x, \cdot) / U(x)$ is integrable on $(0, \infty)$.
The *displacement thickness* at $x$ is
$$\delta^*(x) = \int_0^\infty \Big( 1 - \frac{u(x, y)}{U(x)} \Big) dy.$$
The *momentum thickness* is the companion quantity $\theta(x) = \int_0^\infty \frac{u}{U} \big( 1 - \frac{u}{U} \big) dy$, and $H = \delta^* / \theta$ is the *shape factor*.

## Remarks

Example: for the linear profile $u = U y / \delta$ for $0 \le y \le \delta$ and $u = U$ for $y > \delta$, one gets $\delta^* = \int_0^\delta (1 - y / \delta) \, dy = \delta / 2$ and $\theta = \int_0^\delta \frac{y}{\delta}\big(1 - \frac{y}{\delta}\big) dy = \delta / 6$, so $H = 3$.

Non-example: a profile with $u = U (1 - (1 + y)^{-1})$ tends to $U$ too slowly: $1 - u / U = (1 + y)^{-1}$ is not integrable, so $\delta^*$ is not defined.

The mass flux deficit $\int_0^\infty (U - u) \, dy$ equals $U \delta^*$.
For the Blasius layer $\delta^* \approx 1.72 \sqrt{\nu x / U}$ and $H \approx 2.59$.
