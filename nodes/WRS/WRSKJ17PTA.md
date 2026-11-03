---
tag: WRSKJ17PTA
kind: statement
role: proposition
name: Griffith criterion
msc: [74R10, 74A45]
uses: [D2D6BRJA5X, 6W00ZECYT0, T8ENJX1905]
about: [SNRXGRZWR5, D2D6BRJA5X]
sources:
  - url: https://en.wikipedia.org/wiki/Fracture_mechanics
---

## Statement

Let a linear elastic, brittle body contain a crack, and let $G$ be the [[energy release rate|D2D6BRJA5X]] of the crack.
Let $\gamma > 0$ be the surface energy of the material per unit area of new surface.
Griffith's criterion postulates that the crack can grow only if $G \ge 2 \gamma$, and that it grows when $G$ exceeds $2\gamma$.
Consider an infinite plate in plane stress, of an isotropic material with [[Young's modulus|T8ENJX1905]] $E$.
Let it contain a straight through crack of length $2a$, perpendicular to a remote uniaxial tension $\sigma$.
Then $G = \pi \sigma^2 a / E$.
Hence the crack grows when $\sigma$ reaches the critical stress
$$\sigma_f = \sqrt{\frac{2 E \gamma}{\pi a}}.$$
In plane strain the same holds with $E$ replaced by $E / (1 - \nu^2)$, where $\nu$ is Poisson's ratio.

## Remarks

The criterion is an energy balance: the crack grows if the drop in the potential energy of the body pays for the energy of the two new crack faces.
The formula for $G$ follows from the stress intensity factor $K_I = \sigma \sqrt{\pi a}$ of this crack and Irwin's relation $G = K_I^2 / E$.
The critical stress decreases like $a^{-1/2}$: a crack four times as long halves the strength.
For metals, Irwin and Orowan replaced $2\gamma$ by a measured fracture energy $G_c$ that includes plastic work; the form $\sigma_f = \sqrt{E G_c / (\pi a)}$ is unchanged.
The criterion assumes brittle behaviour; when a large plastic zone forms at the tip, the energy balance must include the plastic dissipation.

## Explanations

### L1 human

A crack grows when growing releases more stored elastic energy than it costs to create the new broken surfaces.
For a crack in a big plate this gives a breaking stress that falls with the square root of the crack length.
This explains why glass, which is very strong in theory, breaks at low stresses: it contains tiny cracks.

### L2 human

The Griffith criterion is the founding result of linear elastic fracture mechanics.
In terms of the [[stress intensity factor|8D619PN75J]] it reads $K_I \ge K_{Ic}$, where the [[fracture toughness|BQ0AMNFJRA]] $K_{Ic}$ is a material constant.
Its modern variational form, due to Francfort and Marigo, minimizes the sum of the elastic energy and a surface energy over all possible crack sets.
