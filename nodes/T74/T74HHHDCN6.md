---
tag: T74HHHDCN6
kind: definition
name: Energy release rate
msc: [74R10, 74A45]
defines: D2D6BRJA5X
uses: [SNRXGRZWR5, 3E9K1DRNYN, 6W00ZECYT0]
sources:
  - url: https://en.wikipedia.org/wiki/Energy_release_rate_(fracture_mechanics)
---

## Definition

Let an elastic body contain a crack of area $A$, from a one-parameter family of cracks that grow along a given path.
Let the loads be fixed.
Let $u_A$ be the equilibrium displacement of the body with crack of area $A$.
Let $W$ be the [[strain energy density|3E9K1DRNYN]] and $t$ the applied traction.
The potential energy is
$$\Pi(A) = \int_{\Omega} W(\nabla u_A) \, dx - \int_{\partial \Omega} t \cdot u_A \, dS.$$
The *energy release rate* is
$$G = -\frac{d \Pi}{d A}.$$
In a two-dimensional problem of unit thickness with crack length $a$, $G = -d\Pi / da$.

## Remarks

Irwin's relation: for a [[linear elastic|6W00ZECYT0]] isotropic material with Young's modulus $E$ and Poisson's ratio $\nu$, $G = (K_I^2 + K_{II}^2)/E' + K_{III}^2 (1 + \nu)/E$, where $E' = E$ in plane stress and $E' = E / (1 - \nu^2)$ in plane strain.
Example: for a crack of length $2a$ in a wide plate under remote tension $\sigma$ in plane stress, $K_I = \sigma \sqrt{\pi a}$, so $G = \pi \sigma^2 a / E$ at each tip.
Non-example: the potential energy $\Pi$ itself, or the elastic energy of the uncracked body, is not a rate and has different units, energy rather than energy per area.
The same value of $G$ is obtained under fixed displacements, with $\Pi$ then equal to the strain energy alone.

## Explanations

### L1 human

The energy release rate is how much stored energy the body gives up when the crack grows by one unit of area.
