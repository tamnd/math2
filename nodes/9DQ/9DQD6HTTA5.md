---
tag: 9DQD6HTTA5
kind: definition
name: Ginzburg–Landau equation
msc: [35Q56, 82D55]
defines: 713MRSZ9XA
uses: [GC5BDZ6QBC, 0NF6GQNXMY, 0ABK9V9Y64, 0299VCW1TH]
sources:
  - url: https://en.wikipedia.org/wiki/Ginzburg–Landau_theory
---

## Definition

Let $\Omega \subseteq \R^3$ be an open set and let $\kappa > 0$ be a constant, the Ginzburg–Landau parameter.
For a function $\psi \colon \Omega \to \C$ and a [[vector field|0299VCW1TH]] $A \colon \Omega \to \R^3$, write $\nabla_A \psi = \nabla \psi - i A \psi$, where $\nabla$ is the [[gradient|0ABK9V9Y64]].
The *Ginzburg–Landau equations* are the system
$$- \nabla_A \cdot \nabla_A \psi = \kappa^2 \big( 1 - \abs{\psi}^2 \big) \psi, \qquad \nabla \times \nabla \times A = \mathrm{Im}\big( \overline{\psi} \, \nabla_A \psi \big),$$
for the unknowns $\psi$, the order parameter, and $A$, the magnetic potential.
Here $\nabla_A \cdot V = \nabla \cdot V - i A \cdot V$ for a vector field $V$ with values in $\C^3$, and $\nabla \times$ is the [[curl|0NF6GQNXMY]].

## Remarks

The equations are the Euler–Lagrange equations of the Ginzburg–Landau energy
$$\mathcal{E}(\psi, A) = \int_\Omega \Big( \tfrac{1}{2} \abs{\nabla_A \psi}^2 + \tfrac{\kappa^2}{4} \big( 1 - \abs{\psi}^2 \big)^2 + \tfrac{1}{2} \abs{\nabla \times A}^2 \Big) dx,$$
written in dimensionless units.
On a bounded domain the natural boundary condition is $\nabla_A \psi \cdot n = 0$.
The energy and the equations are invariant under the gauge change $\psi \mapsto e^{i\chi} \psi$, $A \mapsto A + \nabla \chi$.

Example: $\psi = 1$ and $A = 0$ is a solution: both sides of each equation are $0$.

Non-example: $\psi = 1/2$ and $A = 0$ is not a solution, because the left side of the first equation is $0$ while the right side is $\tfrac{3}{8} \kappa^2 \ne 0$.

Without magnetic field, setting $A = 0$ and dropping the second equation gives the simplified equation $-\Delta \psi = \kappa^2 (1 - \abs{\psi}^2) \psi$.
The name Ginzburg–Landau equation is also used for the time-dependent complex equation $\partial_t \psi = (1 + i\alpha) \Delta \psi + \psi - (1 + i\beta) \abs{\psi}^2 \psi$ of pattern formation.
