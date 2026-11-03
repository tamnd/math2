---
tag: K3E536PSRJ
kind: example
name: Percus–Yevick approximation
msc: [82D15, 82B21, 45G10]
instance_of: [BSCYBP6AS6]
sources:
  - url: https://en.wikipedia.org/wiki/Percus%E2%80%93Yevick_approximation
same_as:
  wikidata: Q3620962
  wikipedia: Percus–Yevick approximation
---

## Example

Consider a classical fluid in $\R^3$ with number density $\rho$, inverse temperature $\beta$ and a pair potential $u(r)$.
Let $g$ be the [[radial distribution function|FME4G0R7FQ]], $h = g - 1$, and let $c$ be the direct correlation function of the [[Ornstein–Zernike equation|29T4NC87AR]].
The Percus–Yevick approximation is the closure
$$c(r) = g(r) \left(1 - e^{\beta u(r)}\right).$$
With the cavity function $y(r) = g(r) e^{\beta u(r)}$ and the Mayer function $f(r) = e^{-\beta u(r)} - 1$ it reads $c(r) = f(r) \, y(r)$.
Inserted in the Ornstein–Zernike equation it gives
$$y(r_{12}) = 1 + \rho \int_{\R^3} f(r_{13}) \, y(r_{13}) \, h(r_{23}) \, dx_3, \qquad h = (1 + f) \, y - 1,$$
where $r_{ij} = \abs{x_i - x_j}$; this is a [[nonlinear integral equation|BSCYBP6AS6]] for $y$, quadratic in $y$.

Check of the second form: $f y = (e^{-\beta u} - 1) g e^{\beta u} = g (1 - e^{\beta u})$.

## Remarks

For hard spheres of diameter $\sigma$, $g(r) = 0$ for $r < \sigma$ and the closure gives $c(r) = 0$ for $r > \sigma$.
In this case the equation has a known closed-form solution, in which $c$ is a cubic polynomial in $r$ for $r < \sigma$.
With the packing fraction $\eta = \frac{\pi}{6} \rho \sigma^3$, the compressibility route gives the equation of state $\frac{\beta P}{\rho} = \frac{1 + \eta + \eta^2}{(1 - \eta)^3}$, and the virial route gives $\frac{1 + 2\eta + 3\eta^2}{(1 - \eta)^2}$.
The two routes differ because the closure is an approximation.

## Explanations

### L1 human

The Ornstein–Zernike equation alone has two unknown functions, so a second rule is needed to close it.
The Percus–Yevick rule says that the direct correlation is zero wherever the particles do not interact.
For hard balls this rule leads to a formula for the pressure that is close to computer simulations at moderate densities.
