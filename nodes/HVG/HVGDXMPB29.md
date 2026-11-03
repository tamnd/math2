---
tag: HVGDXMPB29
kind: example
name: Quartic interaction
msc: [81T10, 81T08]
instance_of: [W031YNVRE3]
uses: [EGCDMWYKQB, AYCCDQWCJF, FG51Y62J8Y]
sources:
  - url: https://en.wikipedia.org/wiki/Quartic_interaction
same_as:
  wikidata: Q6497970
  wikipedia: Quartic interaction
---

## Example

The *quartic interaction*, or $\phi^4$ theory, is the [[quantum field theory|W031YNVRE3]] of one real scalar field $\phi$ on Minkowski space $\R^{1,d-1}$.
Its Lagrangian density, with mass $m \ge 0$ and coupling $\lambda > 0$, is
$$\mathcal{L} = \tfrac12 \partial_\mu \phi \, \partial^\mu \phi - \tfrac12 m^2 \phi^2 - \tfrac{\lambda}{4!} \phi^4.$$
The Euler–Lagrange equation is the nonlinear [[Klein–Gordon equation|AYCCDQWCJF]] $(\partial_\mu \partial^\mu + m^2)\phi + \tfrac{\lambda}{3!}\phi^3 = 0$.
For $\lambda = 0$ it is the free field.
In Euclidean form, the theory is the formal measure proportional to
$$\exp\left(-\int_{\R^d} \left( \tfrac12 \abs{\nabla\phi}^2 + \tfrac12 m^2\phi^2 + \tfrac{\lambda}{4!}\phi^4 \right) dx\right) \mathcal{D}\phi.$$
Its Gaussian part is the [[Gaussian free field|EGCDMWYKQB]], and $\lambda\phi^4$ is the interaction.

## Remarks

In $d = 2$ and $d = 3$ the theory has been constructed rigorously in [[constructive quantum field theory|FG51Y62J8Y]], and it is a nontrivial interacting theory.
In $d = 4$ it is renormalizable in perturbation theory, with mass, coupling and field strength counterterms.
In $d \ge 4$, continuum limits of the lattice model are Gaussian; this is [[quantum triviality|H0VT0FGP6T]].
Its Feynman rules have one vertex with four legs; the factor $1/4!$ cancels the $4!$ ways of attaching four lines to a vertex.
The lattice version is closely related to the [[Ising model|R0KGM32QN6]], which is its limit as the quartic coupling grows with a fixed minimum of the potential.

## Explanations

### L1 human

The $\phi^4$ theory is the simplest model of particles that interact.
The field has a quadratic part that describes free particles of mass $m$, plus a quartic term that lets two particles scatter off each other.
It is the testing ground for perturbation theory, renormalization and rigorous constructions.
It also describes phase transitions in statistical physics, such as the critical point of a magnet.
