---
tag: VMTSRGGS1A
kind: definition
name: Multipole expansion
msc: [78A30, 31B10]
defines: KE84W5KNT8
uses: [SAEDXNM3Y1, BANHMXD2TD, QFYGJVA996, 3F32Y21HP4]
sources:
  - url: https://en.wikipedia.org/wiki/Multipole_expansion
---

## Definition

Let $\varepsilon_0 > 0$ be the vacuum permittivity.
Let $\rho \colon \R^3 \to \R$ be a bounded, measurable charge density that vanishes outside the ball of radius $R$ centred at $0$.
Let $\varphi$ be its [[electric potential|SAEDXNM3Y1]].
Let $P_l$ be the [[Legendre polynomial|QFYGJVA996]] of degree $l$, and let $\gamma$ be the angle between $x$ and $y$.
For $x \in \R^3$ with $r = \abs{x} > R$, the *multipole expansion* of $\varphi$ is
$$\varphi(x) = \frac{1}{4 \pi \varepsilon_0} \sum_{l=0}^{\infty} \frac{1}{r^{l+1}} \int_{\R^3} \rho(y) \, \abs{y}^l \, P_l(\cos \gamma) \, dy.$$
The $l$-th term is the $2^l$-pole term: monopole for $l = 0$, dipole for $l = 1$, quadrupole for $l = 2$.

## Remarks

The series converges absolutely for $r > R$, since $\abs{P_l} \le 1$ on $[-1, 1]$.
So the $l$-th integral term is at most $(R^l / r^{l+1}) \int \abs{\rho(y)} \, dy$, a geometric bound.
It comes from the expansion $1/\abs{x - y} = \sum_l \abs{y}^l P_l(\cos \gamma) / r^{l+1}$ for $\abs{y} < \abs{x}$.
In Cartesian form the first three terms are
$$\varphi(x) = \frac{1}{4 \pi \varepsilon_0} \left( \frac{Q}{r} + \frac{p \cdot x}{r^3} + \frac{1}{2} \sum_{i,j=1}^{3} Q_{ij} \frac{x_i x_j}{r^5} + \cdots \right),$$
with total charge $Q$, [[dipole moment|BANHMXD2TD]] $p$, and quadrupole moment $Q_{ij} = \int \rho(y) (3 y_i y_j - \abs{y}^2 \delta_{ij}) \, dy$.
Example: charges $+q$ at $(0,0,d/2)$ and $-q$ at $(0,0,-d/2)$ have $Q = 0$ and $p = (0,0,qd)$, so far away $\varphi \approx q d \cos \theta / (4 \pi \varepsilon_0 r^2)$, with $\theta$ the polar angle of $x$.
Non-example: inside the ball, $r < R$, the series need not converge; there one uses the interior expansion in powers $r^l$.
Using the addition theorem, $P_l(\cos \gamma)$ splits into products of [[spherical harmonics|3F32Y21HP4]] of $x$ and of $y$, which gives the spherical multipole moments.
