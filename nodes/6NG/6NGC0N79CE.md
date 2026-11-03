---
tag: 6NGC0N79CE
kind: definition
name: Geometrothermodynamics
msc: [80A10, 53B50, 53D10]
defines: PZS2XQR4YV
uses: [ZTH9SSWCDG, WNSAZD8EZC, RTAVY44P4Z, 1R7ANBHDSN, HKPHRSN3ER]
sources:
  - url: https://en.wikipedia.org/wiki/Geometrothermodynamics
---

## Definition

Let $(\mathcal{T}, \Theta)$ be the thermodynamic phase space of dimension $2n+1$ of the [[contact geometry of thermodynamics|ZTH9SSWCDG]].
It has coordinates $(\Phi, E^a, I_a)$ and the form $\Theta = d\Phi - \sum_a I_a \, dE^a$, and it is a [[contact manifold|WNSAZD8EZC]].
A *geometrothermodynamic structure* on $\mathcal{T}$ is a non-degenerate metric $G$ on $\mathcal{T}$ invariant under the Legendre transformations of $\mathcal{T}$.
These are the changes of coordinates that exchange some pairs $(E^a, I_a)$ and modify $\Phi$ accordingly.
For a system with fundamental relation $\Phi = f(E^1, \dots, E^n)$, let $\varphi \colon \mathcal{E} \to \mathcal{T}$ be the embedding of its equilibrium manifold, a [[Legendrian submanifold|RTAVY44P4Z]] with $\varphi^* \Theta = 0$.
The *thermodynamic metric* of the system is the pull-back $g = \varphi^* G$, a metric on $\mathcal{E}$ in the coordinates $E^a$.

## Remarks

The triple $(\mathcal{T}, \Theta, G)$ is the phase space of geometrothermodynamics, and the pair $(\mathcal{E}, g)$ is its equilibrium space.
The metric $G$ is in general pseudo-Riemannian, so $g$ need not be a [[Riemannian metric|1R7ANBHDSN]].
Legendre invariance of $G$ means that one geometry results from $U$, from the entropy representation or from any free energy.
The metrics are related by the [[Legendre transformation|HKPHRSN3ER]] of coordinates.

Example: take $n = 2$, $\Phi = U$ and $E = (S, V)$.
The equilibrium manifold of a gas is the surface $\set{(U(S, V), S, V, T(S, V), -p(S, V))}$, and $g$ is a $2 \times 2$ metric in $(S, V)$.
For the ideal gas, the metrics used in the literature give zero curvature.

Non-example: the Weinhold metric, the Hessian $\sum_{a,b} \frac{\partial^2 U}{\partial E^a \partial E^b} \, dE^a dE^b$ of the internal energy, is defined from one chosen potential.
It is not invariant under Legendre transformations, and avoiding this dependence on the potential is the motivation for the definition above.
