---
tag: 6RKB5XJRDC
kind: definition
name: Harmonic coordinate condition
msc: ["83C05", "35Q75", "35L70"]
defines: PPB51F8QVK
uses: [D1SYF8F8RQ, PAGN759BNR, Z8XNDJSCJS, K83HM845A8]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_coordinate_condition
---

## Definition

Let $(M, g)$ be a [[Lorentzian manifold|D1SYF8F8RQ]] of dimension $n + 1$, and let $\square_g$ be its [[Laplace–Beltrami operator|PAGN759BNR]], the wave operator
$$\square_g f = \frac{1}{\sqrt{\abs{\det g}}} \, \partial_\alpha \Bigl( \sqrt{\abs{\det g}} \, g^{\alpha\beta} \partial_\beta f \Bigr).$$
Local coordinates $(x^0, \dots, x^n)$ on an open set $U \subseteq M$ satisfy the *harmonic coordinate condition* if
$$\square_g x^\mu = 0 \quad \text{on } U \text{ for each } \mu = 0, \dots, n.$$

## Remarks

Equivalent forms are $\partial_\alpha \bigl( \sqrt{\abs{\det g}} \, g^{\alpha\mu} \bigr) = 0$ and $g^{\alpha\beta} \Gamma^\mu_{\alpha\beta} = 0$ for each $\mu$, where $\Gamma^\mu_{\alpha\beta}$ are the [[Christoffel symbols|Z8XNDJSCJS]].
This follows from $\square_g x^\mu = -g^{\alpha\beta} \Gamma^\mu_{\alpha\beta}$.
In harmonic coordinates the [[Ricci tensor|K83HM845A8]] is $R_{\mu\nu} = -\tfrac12 g^{\alpha\beta} \partial_\alpha \partial_\beta g_{\mu\nu} + Q_{\mu\nu}(g, \partial g)$, with $Q_{\mu\nu}$ quadratic in the first derivatives.
So the vacuum equations $R_{\mu\nu} = 0$ become a quasilinear hyperbolic system for $g_{\mu\nu}$.
Example: inertial coordinates on Minkowski space are harmonic, since all Christoffel symbols vanish.
Non-example: in Minkowski space with spatial spherical coordinates $(t, r, \theta, \varphi)$, the function $r$ is not harmonic, since $\square r = \Delta r = 2/r \ne 0$ for the flat metric of signature $(-,+,+,+)$.
Harmonic coordinates exist near any point: one solves the wave equation $\square_g x^\mu = 0$ with suitable initial values.

## Explanations

### L1 human

Harmonic coordinates are coordinates that are themselves solutions of the wave equation of the spacetime.
