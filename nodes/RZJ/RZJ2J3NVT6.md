---
tag: RZJ2J3NVT6
kind: definition
name: Electromagnetic four-potential
msc: [78A25, 83A05]
defines: BQFCNWFV9Q
uses: [SAEDXNM3Y1, 8PEMR2J7EF, WRZJRJS44W, YZ7Q9DP8RT, XRED3C547P]
sources:
  - url: https://en.wikipedia.org/wiki/Electromagnetic_four-potential
---

## Definition

Work in Minkowski space with coordinates $x^0 = ct, x^1, x^2, x^3$ and metric $\eta = \operatorname{diag}(1, -1, -1, -1)$.
Let $\phi$ be a scalar potential and $A$ a [[vector potential|8PEMR2J7EF]] for the electromagnetic field.
So $\phi$ and $A$ are $C^1$ functions with
$$E = -\nabla \phi - \frac{\partial A}{\partial t}, \qquad B = \nabla \times A,$$
where $E$ is the [[electric field|YZ7Q9DP8RT]] and $B$ the [[magnetic field|XRED3C547P]].
The *electromagnetic four-potential* is the four-vector field
$$A^\mu = \Big( \frac{\phi}{c}, A_1, A_2, A_3 \Big), \qquad \mu = 0, 1, 2, 3.$$

## Remarks

Lowering the index gives $A_\mu = (\phi / c, -A_1, -A_2, -A_3)$, and the [[electromagnetic tensor|WRZJRJS44W]] is
$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu.$$
For instance $F_{0i} = \frac{1}{c} \big( -\partial_t A_i - \partial_i \phi \big) = E_i / c$.
In static situations $\phi$ is the [[electric potential|SAEDXNM3Y1]] of electrostatics.

Example: a charge $q$ at rest at the origin has the four-potential $A^\mu = \big( \frac{q}{4 \pi \varepsilon_0 c \abs{x}}, 0, 0, 0 \big)$, which gives the Coulomb field and $B = 0$.

Non-example: for the uniform magnetic field $B = (0, 0, B_0)$ with $B_0 \neq 0$, no four-potential with spatial part $A = 0$ exists, since then $\nabla \times A = 0 \neq B$; one can take $A = \frac{B_0}{2} (-y, x, 0)$ instead.

For any $C^2$ function $\chi$, the four-potential $A^\mu - \partial^\mu \chi$, that is $\phi - \partial_t \chi$ and $A + \nabla \chi$, gives the same fields.
