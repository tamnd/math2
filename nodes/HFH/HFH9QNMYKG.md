---
tag: HFH9QNMYKG
kind: definition
name: Electric dipole moment
msc: [78A30]
defines: BANHMXD2TD
uses: [6XPSV47R56]
sources:
  - url: https://en.wikipedia.org/wiki/Electric_dipole_moment
---

## Definition

Fix an origin in $\R^3$.
For a system of point [[charges|6XPSV47R56]] $q_1, \dots, q_n$ at points $x_1, \dots, x_n \in \R^3$, the *electric dipole moment* is the vector
$$p = \sum_{i=1}^{n} q_i \, x_i.$$
For an integrable charge density $\rho \colon \R^3 \to \R$ with $\int \abs{y} \abs{\rho(y)} \, dy < \infty$, the electric dipole moment is
$$p = \int_{\R^3} y \, \rho(y) \, dy.$$

## Remarks

If the origin moves to $a$, the moment becomes $p - Q a$, where $Q$ is the total charge.
So $p$ does not depend on the origin exactly when $Q = 0$.
Example: charges $+q$ at $(0,0,d/2)$ and $-q$ at $(0,0,-d/2)$ give $p = (0, 0, qd)$, for any choice of origin, since $Q = 0$.
Non-example: a single charge $q \ne 0$ has no intrinsic dipole moment, since its moment $q x_1$ changes with the origin and vanishes when the origin is at $x_1$.
A dipole of moment $p$ in a uniform field $E$ feels the torque $p \times E$ and has potential energy $-p \cdot E$.
The SI unit is the coulomb metre.
