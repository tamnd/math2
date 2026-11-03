---
tag: 1GNF44P5GN
kind: definition
name: Amphidromic point
msc: [86A05, 76U60]
defines: DYR62DYV08
uses: [Y07010W5HJ]
sources:
  - url: https://en.wikipedia.org/wiki/Amphidromic_point
---

## Definition

Let $\Sigma$ be a sea region and fix one [[tidal constituent|Y07010W5HJ]] with angular frequency $\sigma > 0$.
Write its contribution to the surface elevation as
$$\zeta(x, t) = \operatorname{Re}\big( Z(x)\, e^{-i\sigma t} \big), \qquad x \in \Sigma,$$
where $Z \colon \Sigma \to \C$ is the complex amplitude; equivalently $\zeta = H \cos(\sigma t - G)$ with amplitude $H = \abs{Z}$ and phase $G = \arg Z$.
A point $x_0 \in \Sigma$ is an *amphidromic point* of the constituent if $Z(x_0) = 0$, that is, the amplitude $H(x_0)$ is zero.

## Remarks

Example: $Z(x_1, x_2) = x_1 + i x_2$ near the origin gives $\zeta = \abs{x} \cos(\sigma t - \theta)$, with $\theta$ the polar angle of $x$.
The origin is an amphidromic point, high water occurs at angle $\theta = \sigma t$, and it turns counterclockwise once per period.
Non-example: for $Z(x) = 1 + x_1$ near the origin, $Z(0) = 1 \ne 0$, so the origin is not amphidromic and the tide there has amplitude $1$.
Lines of constant phase $G$, the co-tidal lines, all meet at an amphidromic point where $Z$ has a simple zero, and the phase changes by $2\pi$ around it.
Points on land where the amplitude extrapolates to zero are called degenerate amphidromes.
