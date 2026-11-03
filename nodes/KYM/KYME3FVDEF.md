---
tag: KYME3FVDEF
kind: definition
name: Geodynamo
msc: [86A25, 76W05]
defines: 19AESAFHF9
uses: [AFVDBT0K5C, T8JWCBK9M6, Z13HPJFV1F]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamo_theory
---

## Definition

Let $V$ be the Earth's liquid outer core, a spherical shell filled with an electrically conducting fluid of magnetic diffusivity $\eta > 0$.
Let $\mathbf{u}$ be the velocity of the fluid and $\mathbf{B}$ the magnetic field.
In [[magnetohydrodynamics|T8JWCBK9M6]], $\mathbf{B}$ obeys the induction equation
$$\frac{\partial \mathbf{B}}{\partial t} = \nabla \times (\mathbf{u} \times \mathbf{B}) + \eta \nabla^2 \mathbf{B}, \qquad \nabla \cdot \mathbf{B} = 0.$$
Couple this equation with the equations of buoyancy-driven convection of the fluid in a frame rotating with the Earth.
Let $L$ be the depth of the shell, so that $L^2/\eta$ is the free decay time of a field.
The *geodynamo* is the regime of this coupled system in the core in which the field is self-sustained.
This means that $\mathbf{B}$ does not decay to zero over times much longer than $L^2/\eta$.

## Remarks

A dynamo needs the magnetic Reynolds number $Rm = UL/\eta$, with $U$ a typical speed, to exceed a critical value; in the core $Rm$ is of order $10^3$.
Not every flow works: Cowling's antidynamo theorem rules out an axisymmetric field maintained by dynamo action, so the geodynamo field is not exactly axisymmetric.
A non-example is a field left in a core at rest ($\mathbf{u} = 0$): the induction equation reduces to the diffusion equation and the field decays.
The first self-consistent numerical geodynamo with a spontaneous reversal was published by Glatzmaier and Roberts in 1995.
See [[dynamo theory|AFVDBT0K5C]] for the general theory and the [[Earth's magnetic field|Z13HPJFV1F]] for the observed field.
