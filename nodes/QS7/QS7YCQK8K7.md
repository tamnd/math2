---
tag: QS7YCQK8K7
kind: statement
role: fact
name: Equivalence principle
msc: [83C05, 83C10, 53B30]
uses: [63ZKC7AFX2, G49G4R1K04, RRHKMGNKG9, FZBA1HA9ZM, RNRTS8WWNM, SXFTH721QT]
about: [63ZKC7AFX2]
sources:
  - url: https://en.wikipedia.org/wiki/Equivalence_principle
same_as:
  wikidata: Q210546
  wikipedia: Equivalence principle
---

## Statement

Let $(M, g)$ be a [[spacetime|63ZKC7AFX2]] and let $p \in M$.
Then there are local coordinates $x^0, \ldots, x^3$ near $p$, called locally inertial coordinates, such that
$$g_{\mu\nu}(p) = \eta_{\mu\nu} \quad \text{and} \quad \partial_\lambda g_{\mu\nu}(p) = 0 \quad \text{for all } \lambda, \mu, \nu,$$
where $\eta = \operatorname{diag}(-1, 1, 1, 1)$ is the metric of [[Minkowski space|G49G4R1K04]].
In these coordinates all [[Christoffel symbols|FZBA1HA9ZM]] vanish at $p$, so at $p$ the [[geodesic|RNRTS8WWNM]] equation reads $d^2x^\mu/d\tau^2 = 0$, the equation of free motion of special relativity.

## Remarks

This is the mathematical form, in general relativity, of the physical equivalence principle.
In a small enough freely falling laboratory, gravity cannot be detected, and the laws of special relativity hold.
The weak equivalence principle says that the world line of a freely falling test body depends only on its initial position and velocity, not on its mass or composition.
In Newtonian terms, inertial mass equals gravitational mass.
Einstein's equivalence principle adds that all non-gravitational laws of physics take their special-relativistic form in a locally inertial frame.
The proof: take an orthonormal basis $e_0, \ldots, e_3$ of $T_pM$ and use [[normal coordinates|RRHKMGNKG9]] $x \mapsto \exp_p(x^\mu e_\mu)$; in normal coordinates the first derivatives of the metric vanish at $p$.
The second derivatives of $g_{\mu\nu}$ cannot in general be removed: they vanish at $p$ in some coordinates only if the Riemann curvature tensor vanishes at $p$.
So tidal effects, which are measured by curvature, remain detectable in a freely falling laboratory of finite size.

## Explanations

### L1 human

Inside a closed lift that falls freely, everything floats, as if there were no gravity.
Conversely, in a rocket that accelerates in empty space, objects fall to the floor as if there were gravity.
The equivalence principle says that, in a small region, gravity and acceleration cannot be told apart.
Einstein used this to build gravity into the geometry of spacetime.

### L2 human

In the mathematics of general relativity the principle is built in: near any event, spacetime looks like Minkowski space to first order.
This is why the laws of special relativity, written with tensors, can be carried to curved spacetime by replacing partial derivatives with covariant derivatives, the rule of minimal coupling.
The curvature appears only at second order, and it governs the relative motion of nearby free bodies through the [[geodesic deviation equation|SXFTH721QT]].
