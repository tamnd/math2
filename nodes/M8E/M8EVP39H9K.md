---
tag: M8EVP39H9K
kind: definition
name: Cahn–Hilliard–Navier–Stokes diffuse interface model
msc: [76T06, 35Q35]
defines: 10WBPH9ANN
uses: [DKN15NVKSB, 18KXZHVF4M, A3Q9SNF86Q, 2JZ0C15A9C, P1KWMQG4NZ]
sources:
  - url: https://en.wikipedia.org/wiki/Cahn%E2%80%93Hilliard_equation
---

## Definition

Let $\Omega \subseteq \R^d$ with $d \in \set{2, 3}$ be a domain filled with two immiscible [[incompressible|2JZ0C15A9C]] fluids of the same constant density $\rho > 0$.
Let $\varepsilon > 0$ be a small length and let $F(\phi) = \frac{1}{4} (\phi^2 - 1)^2$ be the double-well potential.
Let $M > 0$ be the mobility, $\eta > 0$ the viscosity, and $\lambda > 0$ a constant proportional to the surface tension.
The unknowns are the velocity $u$, the pressure $p$, the phase field $\phi$ and the chemical potential $\mu$.
The *Cahn–Hilliard–Navier–Stokes model* is the system
$$\rho \left( \frac{\partial u}{\partial t} + (u \cdot \nabla) u \right) = -\nabla p + \nabla \cdot \big( 2 \eta \, D u \big) + \mu \nabla \phi,$$
$$\nabla \cdot u = 0,$$
$$\frac{\partial \phi}{\partial t} + u \cdot \nabla \phi = \nabla \cdot (M \nabla \mu),$$
$$\mu = \lambda \left( \frac{1}{\varepsilon^2} F'(\phi) - \Delta \phi \right),$$
where $D u = \frac{1}{2} (\nabla u + \nabla u^T)$ is the [[strain rate tensor|P1KWMQG4NZ]].

## Remarks

Without flow ($u = 0$), the last two equations are the [[Cahn–Hilliard equation|DKN15NVKSB]].
The term $\mu \nabla \phi$ is the capillary force; it differs from $-\phi \nabla \mu$ by a gradient, which can be absorbed in the pressure.
With the boundary conditions $u = 0$ and $\partial_n \phi = \partial_n \mu = 0$, smooth solutions dissipate the total energy
$$E = \int_\Omega \frac{\rho}{2} \abs{u}^2 + \lambda \left( \frac{1}{2} \abs{\nabla \phi}^2 + \frac{1}{\varepsilon^2} F(\phi) \right) dx.$$

Example: $u = 0$, constant $p$ and $\phi = \tanh\!\big(x_1 / (\sqrt{2} \varepsilon)\big)$ on $\R^d$ is a steady solution: this $\phi$ satisfies $F'(\phi) = \varepsilon^2 \phi''$, so $\mu = 0$, and then all four equations hold.
It describes a flat interface of thickness of order $\varepsilon$.

Non-example: the system without the term $\mu \nabla \phi$ is not the model; the fluids then feel no surface tension, and the energy identity fails.

Versions for fluids of different densities exist, but they need extra terms to keep the energy law.
