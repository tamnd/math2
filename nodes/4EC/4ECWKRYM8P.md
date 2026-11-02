---
tag: 4ECWKRYM8P
kind: definition
name: Dirac equation
msc: [35Q41, 35Q40]
defines: XNZX7VXXR2
uses: [GC5BDZ6QBC, A38B1QFK20, 09EGC6F8PT]
sources:
  - url: https://en.wikipedia.org/wiki/Dirac_equation
---

## Definition

Write points of $\R^4$ as $x = (x^0, x^1, x^2, x^3)$ with $x^0 = t$, and let $\eta = \mathrm{diag}(1, -1, -1, -1)$.
Let $\gamma^0, \gamma^1, \gamma^2, \gamma^3$ be complex $4 \times 4$ matrices with
$$\gamma^\mu \gamma^\nu + \gamma^\nu \gamma^\mu = 2 \eta^{\mu\nu} I \quad \text{for all } \mu, \nu \in \set{0, 1, 2, 3}.$$
Let $m \ge 0$ be a constant, the mass.
The *Dirac equation* is the [[partial differential equation|GC5BDZ6QBC]]
$$\Big( i \sum_{\mu=0}^{3} \gamma^\mu \partial_\mu - m \Big) \psi = 0$$
for an unknown function $\psi \colon \R^4 \to \C^4$, where $\partial_\mu$ is the [[partial derivative|09EGC6F8PT]] in $x^\mu$.
Units are chosen with $\hbar = c = 1$.

## Remarks

The matrices $\gamma^\mu$ generate a representation of the [[Clifford algebra|A38B1QFK20]] of $(\R^4, \eta)$.
A standard choice is the Dirac representation, in which $\gamma^0 = \mathrm{diag}(1, 1, -1, -1)$.

Example: in the Dirac representation, $\psi(x) = e^{-imt} (1, 0, 0, 0)$ is a solution.
Indeed $\psi$ depends only on $t$, and $i \gamma^0 \partial_t \psi = i \gamma^0 (-im) \psi = m \gamma^0 \psi = m \psi$, since $(1, 0, 0, 0)$ is an eigenvector of $\gamma^0$ for the eigenvalue $1$.

Non-example: for $m > 0$, $\psi(x) = e^{imt} (1, 0, 0, 0)$ is not a solution, because $i \gamma^0 \partial_t \psi - m \psi = -2m \psi \ne 0$.

Applying the operator $i \gamma^\nu \partial_\nu + m$ to the equation and using the anticommutation relations gives $(\partial_t^2 - \Delta + m^2) \psi = 0$, the Klein–Gordon equation for each component.
