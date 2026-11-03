---
tag: JVV91TAA9M
kind: definition
name: Magnetohydrodynamics
msc: [76W05, 76X05, 85A30]
defines: T8JWCBK9M6
uses: [18KXZHVF4M, 9BWWD4QK8Y, 2JZ0C15A9C, 0NF6GQNXMY, 0MWV6ZTK6S]
sources:
  - url: https://en.wikipedia.org/wiki/Magnetohydrodynamics
---

## Definition

Consider an [[incompressible|2JZ0C15A9C]] fluid in a region of $\R^3$ with constant density $\rho > 0$, dynamic viscosity $\mu \ge 0$ and electrical conductivity $\sigma > 0$.
Let $\mu_0$ be the magnetic permeability of vacuum and $\eta = 1/(\mu_0 \sigma)$ the magnetic diffusivity.
*Magnetohydrodynamics* (MHD) is the model in which the velocity $\mathbf{u}(x, t)$, the pressure $p(x, t)$ and the magnetic field $\mathbf{B}(x, t)$ satisfy
$$\rho \left( \frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u} \cdot \nabla) \mathbf{u} \right) = -\nabla p + \mu \Delta \mathbf{u} + \mathbf{J} \times \mathbf{B}, \qquad \mathbf{J} = \frac{1}{\mu_0} \nabla \times \mathbf{B},$$
$$\frac{\partial \mathbf{B}}{\partial t} = \nabla \times (\mathbf{u} \times \mathbf{B}) + \eta \Delta \mathbf{B},$$
$$\nabla \cdot \mathbf{u} = 0, \qquad \nabla \cdot \mathbf{B} = 0.$$
Here $\mathbf{J}$ is the current density and $\mathbf{J} \times \mathbf{B}$ the Lorentz force per unit volume.
The second line is the *induction equation*.

## Remarks

The model follows from [[Maxwell's equations|9BWWD4QK8Y]] by dropping the displacement current, which is valid for speeds much smaller than the speed of light.
One adds Ohm's law $\mathbf{J} = \sigma (\mathbf{E} + \mathbf{u} \times \mathbf{B})$ in the moving fluid.
Eliminating the electric field $\mathbf{E}$ gives the induction equation, after using $\nabla \times (\nabla \times \mathbf{B}) = -\Delta \mathbf{B}$ when $\nabla \cdot \mathbf{B} = 0$.
Example: if $\mathbf{B} \equiv 0$, the equations reduce to the incompressible [[Navier–Stokes equations|18KXZHVF4M]].
Another example: a fluid at rest, $\mathbf{u} = 0$, in a uniform field $\mathbf{B} = B_0 \mathbf{e}_z$ with constant pressure is a solution, since $\nabla \times \mathbf{B} = 0$ and $\Delta \mathbf{B} = 0$.
Non-example: a field $\mathbf{B}$ with $\nabla \cdot \mathbf{B} \ne 0$ is not admissible, even if it solves the induction equation.
The magnetic Reynolds number $\mathrm{Rm} = U L / \eta$ compares advection of the field by the flow with its diffusion; the limit $\eta = 0$, $\mu = 0$ gives incompressible ideal MHD.
The compressible version adds the continuity equation and an energy equation.
