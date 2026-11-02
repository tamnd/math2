---
tag: A5T30ZHVGH
kind: statement
role: theorem
name: Minimum total potential energy principle
msc: [74G65, 74B05, 49S05]
uses: [M4CEZ5K9HP, SJZX81A783, 0KX66CZMBB, 85KK79FCN5, PQ25NHV0KS]
about: [PQ25NHV0KS]
sources:
  - url: https://en.wikipedia.org/wiki/Minimum_total_potential_energy_principle
same_as:
  wikidata: Q6865491
  wikipedia: Minimum total potential energy principle
---

## Statement

Let $\Omega \subset \R^3$ be a bounded connected open set with Lipschitz boundary $\partial\Omega = \overline{\Gamma_D} \cup \overline{\Gamma_N}$, where $\Gamma_D$ and $\Gamma_N$ are disjoint and $\Gamma_D$ has positive surface measure.
Let $\varepsilon(v) = \tfrac12(\nabla v + \nabla v^T)$ be the linearised strain of a displacement $v \colon \Omega \to \R^3$.
Let $\mathsf{C}$ be a bounded measurable elasticity tensor field that is symmetric and uniformly [[positive definite|0KX66CZMBB]] on symmetric $3 \times 3$ matrices.
Let $f \in L^2(\Omega)^3$ be the body force and $g \in L^2(\Gamma_N)^3$ the surface traction.
Let $V = \set{v \in H^1(\Omega)^3 : v = 0 \text{ on } \Gamma_D}$, the admissible displacements, and define the total potential energy
$$\Pi(v) = \frac12 \int_\Omega \mathsf{C}\varepsilon(v) : \varepsilon(v)\, dx - \int_\Omega f \cdot v \, dx - \int_{\Gamma_N} g \cdot v \, dS.$$
Then:

1. $\Pi$ has exactly one minimiser $u$ on $V$.
2. A displacement $u \in V$ minimises $\Pi$ on $V$ if and only if $u$ is a [[weak solution|SJZX81A783]] of the equilibrium equations below.
   Here $\nu$ is the outward unit normal.
   $$-\operatorname{div}(\mathsf{C}\varepsilon(u)) = f \text{ in } \Omega, \quad u = 0 \text{ on } \Gamma_D, \quad (\mathsf{C}\varepsilon(u))\nu = g \text{ on } \Gamma_N.$$

## Remarks

The functional $\Pi$ is a strictly convex quadratic functional on the [[Sobolev space|M4CEZ5K9HP]] $V$.
Korn's inequality, together with $\abs{\Gamma_D} > 0$, shows that the strain energy controls the $H^1$ norm on $V$, so the [[Lax–Milgram theorem|85KK79FCN5]] gives existence and uniqueness.
For a convex quadratic functional, minimisers are exactly the points where the first variation vanishes, and the first variation of $\Pi$ is the weak form of equilibrium.
Without $\abs{\Gamma_D} > 0$, the body can move rigidly: $\Pi$ is unchanged along rigid motions when the loads are balanced, so uniqueness fails, and $\Pi$ is unbounded below when they are not.
Example in one dimension: a bar $[0, \ell]$ with stiffness $k > 0$, clamped at $0$ and pulled by a force $P$ at $\ell$, has $\Pi(v) = \tfrac{k}{2}\int_0^\ell v'^2\,dx - P v(\ell)$, whose minimiser is $u(x) = Px/k$.
The same idea, that stable equilibria minimise the total potential energy, holds for conservative systems more generally.
It is the basis of the finite element method in structural mechanics.

## Explanations

### L1 human

An elastic body at rest under loads takes the shape that makes its total potential energy as small as possible.
This energy is the energy stored by deforming the body minus the work done by the loads.
A ball rolls to the bottom of a bowl for the same reason.

### L2 human

The principle is the variational form of linear elasticity, and it is a model case of the direct method of the [[calculus of variations|PQ25NHV0KS]].
It replaces a system of partial differential equations by the minimisation of a convex functional.
Restricting the minimisation to a finite-dimensional space of trial displacements gives the Ritz and finite element approximations, and the convexity gives their convergence.
