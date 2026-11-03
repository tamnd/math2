---
tag: X87KPFF17K
kind: statement
role: fact
name: Newtonian limit
msc: ["83C25", "83C05"]
uses: [3MCZ97SW6V, RNRTS8WWNM, AH62KSWA6Y, DWK5N5SKTK, 29WRN5J730, REDZ92MKXX]
about: [3MCZ97SW6V, 29WRN5J730]
sources:
  - url: https://en.wikipedia.org/wiki/Newtonian_limit
same_as:
  wikidata: Q7020536
  wikipedia: Newtonian limit
---

## Statement

Let $G$ be the gravitational constant and $c$ the speed of light.
Let $(M, g)$ be a solution of the [[Einstein field equations|3MCZ97SW6V]] $G_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}$ with zero cosmological constant.
Assume that in coordinates $(x^0, x^1, x^2, x^3) = (ct, x, y, z)$:

1. the field is weak: $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ with $\eta = \mathrm{diag}(-1, 1, 1, 1)$ and $\abs{h_{\mu\nu}} \ll 1$, so only terms linear in $h$ are kept;
2. the field is quasi-static: time derivatives of $h_{\mu\nu}$ are negligible compared with spatial derivatives;
3. the matter moves slowly and has small pressure, so its [[stress–energy tensor|REDZ92MKXX]] is dominated by $T_{00} = \rho c^2$, with $\rho$ the mass density.

Then, up to a choice of coordinates, $g_{00} = -\left(1 + 2\Phi/c^2\right)$, where $\Phi$ solves [[Poisson's equation|DWK5N5SKTK]] $\nabla^2 \Phi = 4\pi G \rho$.
Moreover, a test particle moving along a timelike [[geodesic|RNRTS8WWNM]] with speed $\abs{v} \ll c$ obeys $\frac{d^2 x^i}{dt^2} = -\partial_i \Phi$ to leading order, which is [[Newton's law of gravitation|29WRN5J730]].

## Remarks

The proof uses [[linearized gravity|AH62KSWA6Y]].
For a slow particle, $dx^0/d\tau \approx c$ dominates, so the geodesic equation becomes $\frac{d^2 x^i}{dt^2} \approx -c^2 \Gamma^i_{00} = \frac{c^2}{2} \partial_i h_{00}$, and this is $-\partial_i \Phi$ when $h_{00} = -2\Phi/c^2$.
In the harmonic gauge the linearized $00$ field equation is $\nabla^2 \bar h_{00} = -16\pi G \rho / c^2$ for the trace-reversed perturbation, which gives $\bar h_{00} = -4\Phi/c^2$ and then $h_{00} = -2\Phi/c^2$.

Example: outside a spherical body of mass $M$, $\Phi = -GM/r$, and $g_{00} = -(1 - 2GM/(rc^2))$, which is the time-time component of the Schwarzschild metric.

The slow-motion hypothesis is needed: for light, $v = c$, the spatial components $h_{ij} = -2\Phi \delta_{ij}/c^2$ contribute as much as $h_{00}$.
This is why the bending of light in general relativity is twice the value obtained from Newtonian gravity alone.

## Explanations

### L1 human

General relativity describes gravity as curved spacetime, while Newton describes it as a force.
The Newtonian limit says that, when gravity is weak and everything moves slowly compared with light, the two theories agree.
Only one part of the curvature matters then: the way clocks run at different rates in different places.
That rate difference plays the role of Newton's gravitational potential.

### L2 human

The limit is the first check that any theory of gravity must pass, and it fixes the constant $8\pi G/c^4$ in the Einstein equations.
It is the leading term of the post-Newtonian expansion, whose higher orders give the relativistic corrections tested in the solar system.
The derivation shows that $g_{00}$ alone controls slow motion, while $g_{ij}$ matters for fast particles and light.
