---
tag: ATYY0AV9CN
kind: example
name: Saint Venant–Kirchhoff model
msc: [74B20]
instance_of: [ZHK2EVRD90]
uses: [3E9K1DRNYN, MRANPXATRD, 80737NDZ4V]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperelastic_material
---

## Example

The *Saint Venant–Kirchhoff model* is the [[hyperelastic material|ZHK2EVRD90]] with the [[strain energy density function|3E9K1DRNYN]] below.
$$W = \frac{\lambda}{2}(\tr E)^2 + \mu \tr(E^2), \qquad E = \tfrac12(F^T F - I).$$
Here $F$ is the deformation gradient, $E$ is the [[Green–Lagrange strain tensor|MRANPXATRD]] and $\lambda, \mu$ are the [[Lamé parameters|80737NDZ4V]].
Its second Piola–Kirchhoff stress is $S = \partial W / \partial E = \lambda (\tr E) I + 2\mu E$.
Check: $W$ depends on $F$ only through $F^T F$, so $W(QF) = W(F)$ for every rotation $Q$, and the model is frame-indifferent.
For small displacement gradients $E$ is close to the small strain, and the model reduces to isotropic linear elasticity.
It behaves badly under strong compression: as $F \to 0$, $E \to -\tfrac12 I$ and $W$ stays finite.
So the energy does not prevent a volume element from being crushed to zero volume.

## Explanations

### L1 human

This model takes Hooke's law of linear elasticity and applies it to a strain measure that is correct for large rotations.
It is the simplest way to handle bodies that rotate a lot while their strains stay small, such as long thin beams and plates.
It is not a good model for large compressions.
