---
tag: K5WHKRZ2SQ
kind: definition
name: Electrostatic energy
msc: [78A30, 31B15]
defines: 2G4KXD6SE8
uses: [6XPSV47R56, SAEDXNM3Y1, YZ7Q9DP8RT]
sources:
  - url: https://en.wikipedia.org/wiki/Electric_potential_energy
---

## Definition

Let $\varepsilon_0 > 0$ be the vacuum permittivity.
For point [[charges|6XPSV47R56]] $q_1, \dots, q_n$ at distinct points $x_1, \dots, x_n \in \R^3$, the *electrostatic energy* is
$$W = \frac{1}{4 \pi \varepsilon_0} \sum_{1 \le i < j \le n} \frac{q_i q_j}{\abs{x_i - x_j}}.$$
For a bounded, measurable charge density $\rho$ with compact support and [[electric potential|SAEDXNM3Y1]] $\varphi$, the electrostatic energy is
$$W = \frac{1}{2} \int_{\R^3} \rho(x) \, \varphi(x) \, dx.$$

## Remarks

For a density as above, with [[electric field|YZ7Q9DP8RT]] $E$, integration by parts gives the field form
$$W = \frac{\varepsilon_0}{2} \int_{\R^3} \abs{E(x)}^2 \, dx.$$
In particular $W \ge 0$ for a continuous distribution, with equality only when $\rho = 0$ almost everywhere.
The point-charge formula leaves out the infinite self-energy of each point charge, so it can be negative.
Example: charges $q$ and $-q$ at distance $d$ have $W = -q^2 / (4 \pi \varepsilon_0 d) < 0$.
Example: a ball of radius $R$ with uniform total charge $Q$ has $W = 3 Q^2 / (20 \pi \varepsilon_0 R)$.
Non-example: the sum over all ordered pairs $i \ne j$ without the factor $\tfrac12$ is not $W$; it counts each pair twice.
