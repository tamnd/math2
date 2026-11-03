---
tag: VY6Y9ZE2GH
kind: definition
name: Electrohydrodynamics
msc: [76W05, 78A30]
defines: JYVW94GVS5
uses: [18KXZHVF4M, DWK5N5SKTK, 2JZ0C15A9C]
sources:
  - url: https://en.wikipedia.org/wiki/Electrohydrodynamics
---

## Definition

Consider an [[incompressible|2JZ0C15A9C]] fluid in a region of $\R^3$ with constant density $\rho$ and viscosity $\mu$, electric permittivity $\varepsilon(x, t) > 0$ and electrical conductivity $\sigma(x, t) \ge 0$.
*Electrohydrodynamics* (EHD) is the model in which the velocity $\mathbf{u}$, the pressure $p$, the free charge density $q$ and the electric potential $\phi$ satisfy:

1. the [[Navier–Stokes equations|18KXZHVF4M]] with electric body force, $\rho (\partial_t \mathbf{u} + (\mathbf{u} \cdot \nabla) \mathbf{u}) = -\nabla p + \mu \Delta \mathbf{u} + q \mathbf{E} - \frac{1}{2} \abs{\mathbf{E}}^2 \nabla \varepsilon$, and $\nabla \cdot \mathbf{u} = 0$;
2. electrostatics, $\mathbf{E} = -\nabla \phi$ and $\nabla \cdot (\varepsilon \mathbf{E}) = q$;
3. charge conservation, $\partial_t q + \nabla \cdot (q \mathbf{u} + \sigma \mathbf{E}) = 0$.

## Remarks

The force in clause 1 is the Korteweg–Helmholtz force without the electrostriction term, which can be absorbed into the pressure for an incompressible fluid.
The current in clause 3 is convection of charge plus Ohmic conduction; models of ionised gases replace $\sigma \mathbf{E}$ by a mobility term and add diffusion.
Clause 2 is a [[Poisson equation|DWK5N5SKTK]] for $\phi$; magnetic forces and induction are neglected, which is the electrostatic limit.
Example: a fluid at rest with constant $\varepsilon$, no free charge and a uniform field $\mathbf{E}$ is a solution with constant pressure, since the electric force vanishes.
Non-example: a liquid metal driven by a magnetic field obeys [[magnetohydrodynamics|T8JWCBK9M6]], where the force is $\mathbf{J} \times \mathbf{B}$ and is not electrostatic.
The leaky dielectric model of G. I. Taylor and J. R. Melcher is a special case.
It has two such fluids with constant $\varepsilon$ and $\sigma$ in each, and free charge only on their interface.
