---
tag: BB23EKZ2QS
kind: statement
role: proposition
name: Bondi accretion
msc: [85A30, 76N15]
uses: [RW0JK9VDZE, SN4J6KP03C, 9YTGKNPMCP]
about: [RW0JK9VDZE, 9YTGKNPMCP]
sources:
  - url: https://en.wikipedia.org/wiki/Bondi_accretion
same_as:
  wikidata: Q4941412
  wikipedia: Bondi accretion
---

## Statement

Let a point mass $M$ be at rest in an infinite gas that is at rest at infinity with density $\rho_\infty$ and [[sound speed|SN4J6KP03C]] $c_\infty$.
Assume the flow is steady, spherically symmetric and inviscid.
Assume it obeys the [[Euler equations|RW0JK9VDZE]] with the Newtonian gravity of $M$ only, with gravitational constant $G$.
Assume it is [[polytropic|9YTGKNPMCP]], with pressure $p \propto \rho^\gamma$ and $1 \le \gamma < 5/3$.
Then among the inflow solutions there is exactly one that passes smoothly from subsonic flow at large radius to supersonic flow near the mass.
It reaches the local sound speed $c_s(r_s)$ at the sonic radius $r_s = G M / (2 c_s(r_s)^2)$.
Its mass accretion rate is
$$\dot M = 4\pi \lambda_\gamma \, \frac{G^2 M^2 \rho_\infty}{c_\infty^3}, \qquad \lambda_\gamma = \frac{1}{4} \left( \frac{2}{5 - 3\gamma} \right)^{\frac{5 - 3\gamma}{2(\gamma - 1)}},$$
with $\lambda_1 = e^{3/2}/4$ understood as the limit $\gamma \to 1$.

## Remarks

Let $v$ be the inflow speed and $c_s$ the local sound speed.
Steady spherical flow conserves the mass flux $4\pi r^2 \rho v$ and, for $\gamma > 1$, the Bernoulli constant $\frac{v^2}{2} + \frac{c_s^2}{\gamma - 1} - \frac{GM}{r}$.
For $\gamma = 1$ the middle term is $c_s^2 \ln \rho$.
Combining them gives $\big(v - \frac{c_s^2}{v}\big) \frac{dv}{dr} = \frac{2 c_s^2}{r} - \frac{GM}{r^2}$, so a smooth transonic solution must have $v = c_s$ exactly where $r = GM/(2c_s^2)$.
Evaluating the two conserved quantities at the sonic point and at infinity fixes $c_s(r_s)$ in terms of $c_\infty$ and then $\dot M$.
Example: for $\gamma = 4/3$ one gets $\lambda_{4/3} = \frac{1}{4} \cdot 2^{3/2} \approx 0.707$, and for isothermal gas $\lambda_1 \approx 1.12$.
At $\gamma = 5/3$ the sonic radius moves to $r = 0$ and the formula gives $\lambda_{5/3} = 1/4$ as a limit; for $\gamma > 5/3$ there is no transonic solution.

## Explanations

### L1 human

A star or black hole sitting in a cloud of gas pulls in the gas around it.
Far away the gas moves slowly, and close in it falls faster than sound.
Bondi found the unique smooth flow joining these two regions and the rate at which it feeds the central mass.
The rate grows like the mass squared and falls steeply with the temperature of the gas.

### L2 human

The natural length scale is the Bondi radius $GM/c_\infty^2$, inside which the gravity of the mass dominates the thermal energy of the gas.
The formula is the standard estimate of the feeding rate of black holes in galactic nuclei.
For a mass moving through gas at relative speed $v$, the Bondi–Hoyle interpolation replaces $c_\infty^2$ by $c_\infty^2 + v^2$.
The problem is the inflow counterpart of the [[Parker solar wind model|GMWEA8Q83B]], whose transonic outflow has the same mathematical structure.
Gas with angular momentum cannot fall in radially and forms an [[accretion disk|6ADKW56QGV]] instead.
