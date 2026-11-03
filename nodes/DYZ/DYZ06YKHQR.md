---
tag: DYZ06YKHQR
kind: definition
name: Electric field
msc: [78A30, 78A25]
defines: YZ7Q9DP8RT
uses: [6XPSV47R56, 4RM18X9CXG, 0299VCW1TH]
sources:
  - url: https://en.wikipedia.org/wiki/Electric_field
---

## Definition

Let $\varepsilon_0 > 0$ be the vacuum permittivity.
For a system of point [[charges|6XPSV47R56]] $q_1, \dots, q_n$ at distinct points $x_1, \dots, x_n \in \R^3$, the *electric field* is the [[vector field|0299VCW1TH]] on $\R^3 \setminus \set{x_1, \dots, x_n}$ given by
$$E(x) = \frac{1}{4 \pi \varepsilon_0} \sum_{i=1}^{n} q_i \, \frac{x - x_i}{\abs{x - x_i}^3}.$$
For a bounded, measurable charge density $\rho \colon \R^3 \to \R$ with compact support, the electric field is the vector field on $\R^3$ given by
$$E(x) = \frac{1}{4 \pi \varepsilon_0} \int_{\R^3} \rho(y) \, \frac{x - y}{\abs{x - y}^3} \, dy.$$

## Remarks

By [[Coulomb's law|4RM18X9CXG]], a test charge $q$ at rest at $x$ feels the force $q E(x)$.
Example: a single charge $q$ at the origin has the field $E(x) = q x / (4 \pi \varepsilon_0 \abs{x}^3)$, of size $\abs{q} / (4 \pi \varepsilon_0 r^2)$ at distance $r = \abs{x}$.
Non-example: the field $q x / (4 \pi \varepsilon_0 \abs{x}^2)$ is not the field of a point charge in $\R^3$.
It decays like $1/r$ instead of $1/r^2$.
For a bounded density with compact support the integral converges absolutely, since $\abs{x - y}^{-2}$ is integrable near $y = x$ in $\R^3$, and $E$ is continuous.
The unit of the electric field is the volt per metre, equal to the newton per coulomb.
