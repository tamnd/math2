---
tag: PGPW2Y7GPD
kind: statement
role: theorem
name: Gauss's spherical harmonic analysis of the geomagnetic field
msc: [86A25, 31B05, 33C55]
uses: [NDPHH8SR3E, S8RG6N1PRT, 3F32Y21HP4, VPJCSVRY6S, 0H7C3T1GJY, 0JX86PSSA9]
about: [Z13HPJFV1F, 3F32Y21HP4]
sources:
  - url: https://en.wikipedia.org/wiki/Earth%27s_magnetic_field
---

## Statement

Let $0 < r_1 < a < r_2$, and use spherical coordinates $(r, \theta, \phi)$ with colatitude $\theta$ and longitude $\phi$.
Let $B$ be a smooth vector field on the shell $S = \set{x \in \R^3 : r_1 < \abs{x} < r_2}$ with $\nabla \times B = 0$ and $\nabla \cdot B = 0$ on $S$, and with zero flux through the sphere $\abs{x} = a$.
Let $P_n^m$ be the Schmidt semi-normalised [[associated Legendre functions|VPJCSVRY6S]].
Then:

1. There are unique real numbers $g_n^m, h_n^m, q_n^m, s_n^m$, for $n \ge 1$ and $0 \le m \le n$, with $h_n^0 = s_n^0 = 0$, such that $B = -\nabla V$ on $S$.
Here
$$V = a \sum_{n=1}^{\infty} \sum_{m=0}^{n} \Bigl[ \Bigl(\frac{a}{r}\Bigr)^{n+1} \bigl(g_n^m \cos m\phi + h_n^m \sin m\phi\bigr) + \Bigl(\frac{r}{a}\Bigr)^{n} \bigl(q_n^m \cos m\phi + s_n^m \sin m\phi\bigr) \Bigr] P_n^m(\cos\theta).$$
The series converges uniformly on every closed subshell of $S$.
2. The coefficients are determined by the values of $B$ on any single sphere $\abs{x} = c$ with $r_1 < c < r_2$.
3. If $B$ extends to a field with $\nabla \times B = 0$ and $\nabla \cdot B = 0$ on $\set{\abs{x} > r_1}$ that tends to $0$ at infinity, then all $q_n^m$ and $s_n^m$ vanish.

## Remarks

Proof idea: the shell is simply connected and $B$ is curl-free, so $B = -\nabla V$ for a [[scalar potential|0H7C3T1GJY]] $V$, and $\nabla \cdot B = 0$ makes $V$ a solution of [[Laplace's equation|S8RG6N1PRT]].
A harmonic function on a shell expands in solid [[spherical harmonics|3F32Y21HP4]] $r^n Y_n^m$ and $r^{-n-1} Y_n^m$.
The constant term does not affect $B$.
The term $1/r$ would give a flux $\ne 0$ through the sphere, so the zero-flux hypothesis removes it.
By the [[divergence theorem|0JX86PSSA9]] this hypothesis holds when $B$ is divergence-free on the whole ball $\abs{x} < r_2$, as for any magnetic field.
On the sphere $r = c$, the radial component $B_r$ gets the factor $(n+1)$ from internal terms and $-n$ from external terms.
The horizontal components get the same sign from both, so measuring all components separates the two parts.
The $g_n^m, h_n^m$ are the internal Gauss coefficients, and the $q_n^m, s_n^m$ the external ones.
In geomagnetism $a = 6371.2$ km is the reference radius, and the dipole terms $g_1^0, g_1^1, h_1^1$ are by far the largest.

## Explanations

### L1 human

Above the Earth's surface and below the ionosphere there are almost no electric currents, so the magnetic field there comes from a potential that satisfies Laplace's equation.
Such a potential can be written as a sum of standard patterns, the spherical harmonics, each with one number in front, the Gauss coefficients.
Gauss showed how to compute these numbers from measurements around the globe, and found that nearly all of the field comes from inside the Earth.

### L2 human

This is the basis of every global model of the geomagnetic field, such as the [[International Geomagnetic Reference Field|YKKYJFPXYG]].
The degree $n$ term of the internal field decays like $r^{-(n+2)}$, so the dipole $n = 1$ dominates far away.
Higher degrees describe smaller features, and they grow when the field is continued downward toward the core.
The separation into internal and external parts follows from the different radial dependence.
The same idea appears in the exterior and interior Dirichlet problems for the Laplace equation.
The squared size of the coefficients of degree $n$, summed over $m$ and weighted by $n + 1$, gives the Lowes–Mauersberger power spectrum of the field.
