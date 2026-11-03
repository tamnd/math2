---
tag: VZC1GWAEP5
kind: definition
name: Coulomb gas method
msc: [82B28, 82B20, 81T40]
defines: X02M521M51
uses: [PAEME5EQRM, EGCDMWYKQB, 0CV69WDRXW]
sources:
  - url: https://en.wikipedia.org/wiki/Coulomb_gas
---

## Definition

Let $a > 0$ be a hard-core radius, $K > 0$ a coupling and $z > 0$ a fugacity.
Let $D \subset \R^2$ be a bounded region.
A configuration of the *two-dimensional Coulomb gas* in $D$ is a family of points $x_1, \dots, x_m \in D$ with charges $q_1, \dots, q_m \in \set{-1, +1}$.
It is required that $\sum_i q_i = 0$ and $\abs{x_i - x_j} \ge a$ for $i \ne j$.
The energy of the configuration is
$$E = -K \sum_{1 \le i < j \le m} q_i q_j \log \frac{\abs{x_i - x_j}}{a}.$$
The grand [[partition function|0CV69WDRXW]] of the gas is
$$Z = \sum_{m \ge 0} \frac{z^m}{(m/2)!^2} \int e^{-E} \, dx_1 \cdots dx_m.$$
Here $m$ runs over even numbers, and the charges are $q_1 = \cdots = q_{m/2} = +1$ and $q_{m/2 + 1} = \cdots = q_m = -1$.
The integral runs over admissible positions, and the factorials remove the labelling of charges of equal sign.
The *Coulomb gas method* applies to a two-dimensional [[lattice model|PAEME5EQRM]].
It writes the partition function or the correlation functions of the model as those of such a Coulomb gas, exactly or up to irrelevant terms.
Equivalently, it writes them as those of a [[Gaussian free field|EGCDMWYKQB]] with point charges.
It then derives the critical behaviour of the model from this Gaussian theory.

## Remarks

The function $-\log \abs{x}$ is, up to the factor $2\pi$, the Green function of the Laplacian in the plane, so $E$ is the electrostatic energy of the charges in two dimensions.
Two charges of the same sign repel and two of opposite sign attract.

Example: in the Villain form of the [[XY model|J53AT590R9]], the vortices of the spin field carry integer charges.
Its partition function factors into a Gaussian spin-wave part and a Coulomb gas of vortices, with coupling proportional to the spin coupling.
A pair of charges $\pm 1$ at distance $r$ has weight $(r/a)^{-K}$, so the mean square distance of a single pair, $\int_a^\infty r^2 \, r^{-K} \, r \, dr$, is finite exactly when $K > 4$.
This is the scaling argument of Kosterlitz and Thouless for the binding of vortex pairs at low temperature.

Non-example: a gas of charges in three dimensions with the Coulomb energy $\sum_{i < j} q_i q_j / \abs{x_i - x_j}$ is not a two-dimensional Coulomb gas.
Its interaction is not logarithmic, and the method in the above form does not apply to it.

The method was used by Bernard Nienhuis to predict exact critical exponents of the $O(n)$ loop models, and the connective constant $\sqrt{2 + \sqrt 2}$ of the hexagonal lattice.
