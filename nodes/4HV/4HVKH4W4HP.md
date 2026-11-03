---
tag: 4HVKH4W4HP
kind: definition
name: Maxwell stress tensor
msc: [78A25, 78A30]
defines: ZWVYST76GE
uses: [YZ7Q9DP8RT, XRED3C547P, S3RZRCH0T5, P3PK0Q02CZ, WX302T93TW, 0JX86PSSA9]
sources:
  - url: https://en.wikipedia.org/wiki/Maxwell_stress_tensor
---

## Definition

Let $E$ be the [[electric field|YZ7Q9DP8RT]] and $B$ the [[magnetic field|XRED3C547P]] in vacuum, and let $\varepsilon_0, \mu_0 > 0$ be the vacuum permittivity and permeability.
The *Maxwell stress tensor* is the symmetric [[tensor field|WX302T93TW]] with components
$$\sigma_{ij} = \varepsilon_0 \Big( E_i E_j - \frac{1}{2} \delta_{ij} \abs{E}^2 \Big) + \frac{1}{\mu_0} \Big( B_i B_j - \frac{1}{2} \delta_{ij} \abs{B}^2 \Big), \qquad i, j \in \set{1, 2, 3},$$
where $\delta_{ij}$ is the Kronecker delta.

## Remarks

For $C^1$ solutions of Maxwell's equations with sources $\rho$ and $J$, a computation gives
$$\sum_{j} \partial_j \sigma_{ij} = f_i + \varepsilon_0 \mu_0 \, \partial_t S_i,$$
where $f = \rho E + J \times B$ is the [[Lorentz force|S3RZRCH0T5]] density and $S$ is the [[Poynting vector|P3PK0Q02CZ]].
By the [[divergence theorem|0JX86PSSA9]], the total force on the charges in a bounded region $V$ is
$$F_i = \int_{\partial V} \sum_j \sigma_{ij} n_j \, dA - \varepsilon_0 \mu_0 \frac{d}{dt} \int_V S_i \, dV.$$
For static fields the last term is zero, and the force depends only on the fields on $\partial V$.

Example: for a uniform field $E = (0, 0, E_0)$ and $B = 0$, the tensor is $\sigma = \frac{\varepsilon_0 E_0^2}{2} \operatorname{diag}(-1, -1, 1)$.
So the field pulls with tension $\varepsilon_0 E_0^2 / 2$ along the field lines and pushes with pressure $\varepsilon_0 E_0^2 / 2$ across them; this tension gives the attraction between the plates of a capacitor.

Non-example: the matrix $\varepsilon_0 E_i E_j$ alone is not the stress tensor; the trace terms with $\delta_{ij}$ are needed for the force identity above.

Some books use the opposite sign, so that the tensor is the momentum flux density $-\sigma$.
