---
tag: X9PZ8RJH90
kind: statement
role: theorem
name: Cowling's antidynamo theorem
msc: [76W05, 86A25]
uses: [AFVDBT0K5C, T8JWCBK9M6]
about: [AFVDBT0K5C]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamo_theory
---

## Statement

Let $V \subset \R^3$ be a bounded region with smooth boundary that is symmetric under rotations about the $z$-axis.
Assume $V$ is filled with a fluid of constant magnetic diffusivity $\eta > 0$ and surrounded by an insulator.
Let $\mathbf{u}$ be a smooth velocity field on $V$, tangent to $\partial V$ and symmetric under rotations about the $z$-axis.
Let $\mathbf{B}$ be a solution of the [[kinematic dynamo problem|AFVDBT0K5C]] for $\mathbf{u}$ that is symmetric under rotations about the $z$-axis.
Then the magnetic energy $\int_{\R^3} \abs{\mathbf{B}(x, t)}^2 \, dx$ tends to $0$ as $t \to \infty$.
In short, an axisymmetric magnetic field cannot be maintained by dynamo action.

## Remarks

In cylindrical coordinates $(s, \varphi, z)$ write $\mathbf{B} = \nabla \times (A \, \mathbf{e}_\varphi) + B_\varphi \mathbf{e}_\varphi$, a poloidal part and a toroidal part.
The poloidal potential $A$ satisfies an advection–diffusion equation with no source term, so it decays.
The toroidal part $B_\varphi$ has a source, the shearing of the poloidal field by the rotation $u_\varphi$, but this source decays with $A$, so $B_\varphi$ decays too.
Thomas Cowling proved the original steady version in 1933 by looking at a point where the poloidal field vanishes: there the current cannot be sustained by $\mathbf{u} \times \mathbf{B}$.
The theorem shows that the axisymmetric part of the geomagnetic field must be maintained by non-axisymmetric motions.

## Explanations

### L1 human

The Earth's magnetic field looks roughly like that of a bar magnet along the rotation axis.
One might hope that a flow symmetric about the axis could create such a field.
Cowling's theorem says no: a field that is exactly symmetric about an axis always dies out.
So the motions of the Earth's core must break the symmetry.

### L2 human

It is the first and best-known antidynamo theorem of [[dynamo theory|AFVDBT0K5C]].
The proof is a decoupling argument: axisymmetry splits the induction equation into a scalar equation for the poloidal flux and a forced equation for the toroidal field.
The poloidal part has no way to be regenerated from the toroidal part, which is the missing link of a dynamo cycle.
Mean-field dynamo theory restores this link by averaging small non-axisymmetric motions into an effective term, the alpha effect.
