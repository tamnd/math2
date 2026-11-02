---
tag: DX8RV2XG6H
kind: statement
role: fact
name: Darcy's law
msc: [76S05, 35Q35]
uses: [0ABK9V9Y64, 0MWV6ZTK6S, 0299VCW1TH, 13CB7V2YM4]
sources:
  - url: https://en.wikipedia.org/wiki/Darcy's_law
same_as:
  wikidata: Q392416
  wikipedia: Darcy's law
---

## Statement

Consider the slow flow of a fluid of viscosity $\mu > 0$ through a porous medium of permeability $k > 0$ that fills a region $\Omega \subseteq \R^3$.
Let $p \colon \Omega \to \R$ be the pressure of the fluid, and neglect gravity.
Let $q \colon \Omega \to \R^3$ be the volumetric flux, the [[vector field|0299VCW1TH]] of the volume of fluid that crosses a unit area per unit time.
Then
$$q = - \frac{k}{\mu} \nabla p.$$
Here $\nabla p$ is the [[gradient|0ABK9V9Y64]] of the pressure.

## Remarks

Darcy's law is an empirical law, found by Henry Darcy from experiments on water flowing through sand.
It can also be derived from the equations of [[Stokes flow|13CB7V2YM4]] by homogenization in a periodic porous structure.
It is valid when the flow is slow, that is, when the Reynolds number of the flow in the pores is small.

For an incompressible fluid without sources, the [[divergence|0MWV6ZTK6S]] of the flux is zero.
With constant $k$ and $\mu$ this gives $\Delta p = 0$, so the pressure is a harmonic function, and boundary values of $p$ determine the flow.
With gravity the law reads $q = -\tfrac{k}{\mu} (\nabla p - \rho g)$, where $\rho$ is the density and $g$ the gravitational acceleration vector.

## Explanations

### L1 human

Water seeps through sand or soil from high pressure to low pressure.
Darcy's law says that the flow rate is proportional to the drop in pressure and to how easily the medium lets fluid through.
It is inversely proportional to the viscosity, that is, to how thick and sticky the fluid is.
It is the analogue for porous media of Ohm's law for electric current and Fourier's law for heat.

### L2 human

Darcy's law turns problems of groundwater, oil reservoirs and filtration into elliptic and parabolic partial differential equations for the pressure.
Combined with conservation of mass for a compressible fluid or a gas, it leads to diffusion equations such as the porous medium equation.
When the permeability varies in space, the pressure solves the divergence-form equation $\nabla \cdot (k \nabla p) = 0$, a standard model of an elliptic equation with variable coefficients.
