---
tag: SXGWP7S515
kind: definition
name: Electric potential
msc: [78A30, 31B15]
defines: SAEDXNM3Y1
uses: [6XPSV47R56, YZ7Q9DP8RT, 0H7C3T1GJY, 0ABK9V9Y64, DCMFQ01QGS]
sources:
  - url: https://en.wikipedia.org/wiki/Electric_potential
---

## Definition

Let $\varepsilon_0 > 0$ be the vacuum permittivity.
For a system of point [[charges|6XPSV47R56]] $q_1, \dots, q_n$ at distinct points $x_1, \dots, x_n \in \R^3$, the *electric potential* is the function on $\R^3 \setminus \set{x_1, \dots, x_n}$ given by
$$\varphi(x) = \frac{1}{4 \pi \varepsilon_0} \sum_{i=1}^{n} \frac{q_i}{\abs{x - x_i}}.$$
For a bounded, measurable charge density $\rho \colon \R^3 \to \R$ with compact support, the electric potential is the function on $\R^3$ given by
$$\varphi(x) = \frac{1}{4 \pi \varepsilon_0} \int_{\R^3} \frac{\rho(y)}{\abs{x - y}} \, dy.$$

## Remarks

In both cases $E = -\nabla \varphi$, where $E$ is the [[electric field|YZ7Q9DP8RT]] and $\nabla$ is the [[gradient|0ABK9V9Y64]].
So $\varphi$ is a [[scalar potential|0H7C3T1GJY]] of $-E$, normalised by $\varphi(x) \to 0$ as $\abs{x} \to \infty$.
Up to the factor $1/\varepsilon_0$ and a sign convention, the second formula is the [[Newtonian potential|DCMFQ01QGS]] of $\rho$.
Example: for one charge $q$ at the origin, $\varphi(x) = q / (4 \pi \varepsilon_0 \abs{x})$, and $-\nabla \varphi(x) = q x / (4 \pi \varepsilon_0 \abs{x}^3)$ is the Coulomb field.
Non-example: $\psi(x) = \varphi(x) + 1$ also satisfies $E = -\nabla \psi$, but it is not the electric potential of the definition, since it does not vanish at infinity.
The potential difference $\varphi(a) - \varphi(b)$ is the voltage between $a$ and $b$, measured in volts.
