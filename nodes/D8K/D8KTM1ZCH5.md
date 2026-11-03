---
tag: D8KTM1ZCH5
kind: definition
name: Ideal MHD equations
msc: [76W05, 35Q35, 76X05]
defines: ZSA13P8P81
uses: [T8JWCBK9M6, RW0JK9VDZE, 9BWWD4QK8Y, 8RA7AMWSAF]
sources:
  - url: https://en.wikipedia.org/wiki/Magnetohydrodynamics
---

## Definition

Let $\mu_0 > 0$ be the magnetic permeability and $\gamma > 1$ the adiabatic index of a gas.
Let $\rho(x, t) > 0$, $\mathbf{u}(x, t)$, $p(x, t)$ and $\mathbf{B}(x, t)$ be the density, velocity, pressure and magnetic field on a region of $\R^3$.
The *ideal MHD equations* are the system:

1. $\partial_t \rho + \nabla \cdot (\rho \mathbf{u}) = 0$;
2. $\rho \left( \partial_t \mathbf{u} + (\mathbf{u} \cdot \nabla) \mathbf{u} \right) = -\nabla p + \frac{1}{\mu_0} (\nabla \times \mathbf{B}) \times \mathbf{B}$;
3. $\partial_t \mathbf{B} = \nabla \times (\mathbf{u} \times \mathbf{B})$;
4. $\left( \partial_t + \mathbf{u} \cdot \nabla \right) \left( p \rho^{-\gamma} \right) = 0$;
5. $\nabla \cdot \mathbf{B} = 0$.

## Remarks

They are the equations of [[magnetohydrodynamics|T8JWCBK9M6]] with zero viscosity, zero magnetic diffusivity and adiabatic thermodynamics.
Clause 5 is a constraint on the initial data: clause 3 gives $\partial_t (\nabla \cdot \mathbf{B}) = 0$, so it holds for all time once it holds at $t = 0$.
The Lorentz force splits as
$$\frac{1}{\mu_0} (\nabla \times \mathbf{B}) \times \mathbf{B} = -\nabla \frac{\abs{\mathbf{B}}^2}{2 \mu_0} + \frac{1}{\mu_0} (\mathbf{B} \cdot \nabla) \mathbf{B},$$
a magnetic pressure plus a magnetic tension along field lines.
Example: constant $\rho$, $p$ and $\mathbf{B}$ with $\mathbf{u} = 0$ is a solution; every term with a derivative vanishes.
Non-example: the resistive induction equation $\partial_t \mathbf{B} = \nabla \times (\mathbf{u} \times \mathbf{B}) + \eta \Delta \mathbf{B}$ with $\eta > 0$ is not ideal.
With $\mathbf{B} = 0$ the system reduces to the compressible [[Euler equations|RW0JK9VDZE]].
The system can be written in [[conservation form|8RA7AMWSAF]] for mass, momentum, total energy and magnetic flux.
