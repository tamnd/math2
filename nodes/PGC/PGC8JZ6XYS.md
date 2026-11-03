---
tag: PGC8JZ6XYS
kind: definition
name: Solar dynamo
msc: [85A30, 76W05]
defines: NPVYXT6WHA
uses: [AFVDBT0K5C, T8JWCBK9M6, X9PZ8RJH90]
sources:
  - url: https://en.wikipedia.org/wiki/Solar_dynamo
---

## Definition

The *solar dynamo* is the [[dynamo|AFVDBT0K5C]] that maintains the large-scale magnetic field of the Sun in its convection zone, against ohmic decay.
In the mean-field formulation, split the velocity and the magnetic field into averages over longitude and fluctuations, $u = U + u'$ and $B = \bar B + b'$.
The mean field $\bar B$ obeys the mean-field induction equation of [[magnetohydrodynamics|T8JWCBK9M6]]:
$$\frac{\partial \bar B}{\partial t} = \nabla \times \left( U \times \bar B + \alpha \bar B \right) + \eta_T \nabla^2 \bar B, \qquad \nabla \cdot \bar B = 0.$$
Here the mean flow $U$ contains the differential rotation and the meridional circulation of the Sun.
The scalar $\alpha$ describes the mean electromotive force of the helical small-scale motions.
The constant $\eta_T > 0$ is the turbulent magnetic diffusivity.
A *solar dynamo model* is a solution of this equation in a spherical shell, with $U$ close to the observed rotation of the Sun.
The solution must not decay and must oscillate in time.

## Remarks

The mean field splits into a toroidal part, along circles of latitude, and a poloidal part, in meridional planes.
The shear of $U$ turns poloidal field into toroidal field, the $\Omega$-effect, and the term $\alpha \bar B$ turns toroidal field into poloidal field, the $\alpha$-effect.
Models with both effects are called $\alpha\Omega$ dynamos.

Example: take a local Cartesian model with constant $\alpha$ and constant shear.
The $\alpha\Omega$ equations have travelling wave solutions, which grow when the product of $\alpha$ and the shear is large enough.
Parker called these dynamo waves, and they model the migration of the sunspot belts toward the equator.

Non-example: take an axisymmetric flow acting on an axisymmetric field, with $\alpha = 0$ and molecular diffusivity in place of $\eta_T$.
By [[Cowling's antidynamo theorem|X9PZ8RJH90]], it cannot sustain the field.
So the non-axisymmetric fluctuations behind $\alpha$ are essential.
