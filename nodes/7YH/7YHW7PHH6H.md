---
tag: 7YHW7PHH6H
kind: problem
name: Topology optimization
msc: [74P15, 49Q10, 74P05]
uses: [WWQJQXJECK, S2BBZPAFDR, GC5BDZ6QBC]
about: [WWQJQXJECK]
sources:
  - url: https://en.wikipedia.org/wiki/Topology_optimization
same_as:
  wikidata: Q2443456
  wikipedia: Topology optimization
history:
  posed_by: "Martin P. Bendsøe and Noboru Kikuchi"
  first_stated: "1988"
---

## Problem

Let $D \subseteq \R^d$ be a bounded open design region with Lipschitz boundary, and let $0 < V < \abs{D}$ be a volume bound.
Let $A$ be the elasticity tensor of a given isotropic elastic material, and let $f \in L^2(D; \R^d)$ be a load.
For a measurable set $\omega \subseteq D$ let $\chi_\omega$ be its indicator function, and fix a small $\varepsilon > 0$.
Let $u_\omega \in H^1(D; \R^d)$ be the displacement that solves the linear elasticity system $-\operatorname{div}\big((\chi_\omega + \varepsilon (1 - \chi_\omega)) A \, e(u)\big) = f$ in $D$, where $e(u) = \frac12 (\nabla u + \nabla u^{T})$.
The boundary conditions are $u = 0$ on a part of $\partial D$ of positive surface measure and zero traction on the rest.
The *minimum compliance topology optimization problem* is to find a set $\omega$ with $\abs{\omega} \le V$ that minimizes the compliance $\int_D f \cdot u_\omega \, dx$.

## Remarks

The material occupies $\omega$, and a very weak material of stiffness $\varepsilon$ fills the rest of $D$ so that the equation stays elliptic.
Unlike classical [[shape optimization|WWQJQXJECK]], no topology of $\omega$ is fixed in advance: holes may appear or disappear.
In general this problem has no minimizer: minimizing sequences develop finer and finer mixtures of material and void.
Bendsøe and Kikuchi replaced the sets $\omega$ by composite materials with a microstructure, given by homogenization, and this relaxed problem has solutions.
A widely used simpler method replaces $\chi_\omega$ by a density $\rho \colon D \to [0, 1]$ and the stiffness by $\rho^p A$ with $p > 1$, which pushes $\rho$ toward the values $0$ and $1$.
The resulting discrete problems are solved by gradient methods with adjoint sensitivities, as in [[optimal control of partial differential equations|S2BBZPAFDR]].

## Explanations

### L1 human

Topology optimization asks where to put material inside a box so that a structure is as stiff as possible for a given amount of material.
The answer may have holes, struts and branches that no designer fixed in advance.
Computers solve such problems by giving each small cell of the box a density between $0$ and $1$ and improving the densities step by step.
The results often look like bones or trees, and they are used to design light parts for aircraft and cars.
