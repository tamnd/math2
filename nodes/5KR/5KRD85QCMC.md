---
tag: 5KRD85QCMC
kind: definition
name: Gauge fixing
msc: [78A25, 70S15]
defines: TXD7MTYQYS
uses: [BQFCNWFV9Q, 8PEMR2J7EF, YZ7Q9DP8RT, XRED3C547P]
sources:
  - url: https://en.wikipedia.org/wiki/Gauge_fixing
---

## Definition

Let $U \subseteq \R^3 \times \R$ be open.
Pairs $(\phi, A)$ of a $C^1$ scalar potential and a $C^1$ [[vector potential|8PEMR2J7EF]] on $U$ determine the [[electric field|YZ7Q9DP8RT]] and the [[magnetic field|XRED3C547P]] by
$$E = -\nabla \phi - \partial_t A, \qquad B = \nabla \times A.$$
A *gauge transformation* replaces $(\phi, A)$ by $(\phi - \partial_t \chi, \; A + \nabla \chi)$ for a $C^2$ function $\chi$ on $U$; it does not change $E$ and $B$.
*Gauge fixing* is the imposition of an additional condition $G(\phi, A) = 0$ on the potentials, the *gauge condition*.
The condition is required to be reachable: every pair of potentials can be brought to satisfy it by a gauge transformation.

## Remarks

A gauge condition is complete if the gauge transformation that achieves it is unique.
Most usual conditions leave a residual freedom, for example by functions $\chi$ that solve a homogeneous equation.
In covariant notation the transformation reads $A^\mu \mapsto A^\mu - \partial^\mu \chi$ for the [[four-potential|BQFCNWFV9Q]].

Example: the Coulomb gauge is $\nabla \cdot A = 0$.
Given any $(\phi, A)$ on $\R^3$ with $\nabla \cdot A$ smooth and decaying, solve the Poisson equation $\Delta \chi = -\nabla \cdot A$; then $\nabla \cdot (A + \nabla \chi) = 0$.

Other common conditions are the Lorenz gauge $\nabla \cdot A + \frac{1}{c^2} \partial_t \phi = 0$, the temporal gauge $\phi = 0$ and the axial gauge $A_3 = 0$.
For the temporal gauge choose $\chi(x, t) = \int_0^t \phi(x, s) \, ds$, which gives $\phi - \partial_t \chi = 0$.

Non-example: the condition $A = 0$ is not a gauge condition, since it forces $B = 0$ and so cannot be reached from potentials of a nonzero magnetic field.
