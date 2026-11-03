---
tag: VZH4A4SC28
kind: definition
name: Massive gravity
msc: [83D05]
defines: Y4SHDZSCZ4
uses: [384JFR3K6X, AH62KSWA6Y, G49G4R1K04, BY4QYYS788]
sources:
  - url: https://en.wikipedia.org/wiki/Massive_gravity
---

## Definition

Work in units with $\hbar = c = 1$ and let $m > 0$.
Let a theory of gravity have a [[Lorentzian metric|BY4QYYS788]] $g$ as its field, and let flat [[Minkowski space|G49G4R1K04]] $\eta$ be a solution.
Write $g = \eta + h$ and keep the terms of second order in $h$ in the action, as in [[linearized gravity|AH62KSWA6Y]].
It is a *massive gravity* theory, with graviton mass $m$, if this gives the *Fierz–Pauli action*
$$S^{(2)} = \int \left[ \mathcal{L}^{(2)}_{\mathrm{EH}}(h) - \frac{m^2}{2}\left( h_{\mu\nu}h^{\mu\nu} - h^2 \right) \right] d^4x.$$
Here $h = \eta^{\mu\nu}h_{\mu\nu}$ and indices are raised with $\eta$.
The quadratic part of the Einstein–Hilbert Lagrangian, with $h$ suitably normalized, is
$$\mathcal{L}^{(2)}_{\mathrm{EH}} = -\frac12 \partial_\lambda h_{\mu\nu}\partial^\lambda h^{\mu\nu} + \partial_\mu h^{\mu\lambda}\partial^\nu h_{\nu\lambda} - \partial_\mu h^{\mu\nu}\partial_\nu h + \frac12 \partial_\lambda h\, \partial^\lambda h.$$

## Remarks

The relative coefficient $-1$ between $h_{\mu\nu}h^{\mu\nu}$ and $h^2$ is the *Fierz–Pauli tuning*: any other choice adds a sixth degree of freedom with negative energy, a ghost.
With the tuning, the field equations describe a massive spin-$2$ field with five polarizations, in contrast with the two of the massless graviton.
Example: the linear Fierz–Pauli theory itself, with $g = \eta + h$ and action $S^{(2)}$, is a massive gravity theory.
Non-example: general relativity has $m = 0$; its linearization has no mass term and only two polarizations.
In the limit $m \to 0$ the linear theory does not reduce to linearized general relativity.
For a given Newtonian mass it predicts $3/4$ of the general-relativistic light deflection: this is the van Dam–Veltman–Zakharov discontinuity.
Vainshtein argued in 1972 that nonlinear effects can restore agreement near massive sources.
Generic nonlinear completions contain the Boulware–Deser ghost; the de Rham–Gabadadze–Tolley theory avoids it by a specific potential built from $g$ and a fixed reference metric.

## Explanations

### L1 human

A theory of massive gravity is one in which, for weak fields, gravity behaves like a field whose particles have a small mass.
The precise form of the mass term matters: only one combination avoids particles with negative energy.
