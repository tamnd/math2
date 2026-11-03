---
tag: 4ZC4ZEBQRJ
kind: definition
name: Rayleigh–Taylor instability
msc: ["76E17"]
defines: 3ETBXHDWBM
uses: [84K7TEWZ2Z, H028A17Z55]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh–Taylor_instability
---

## Definition

Consider two inviscid incompressible fluids at rest, the lower one in $z < 0$ with density $\rho_1$ and the upper one in $z > 0$ with density $\rho_2$.
Gravity $g > 0$ acts in the direction $-z$, and the interface $z = 0$ has surface tension $\sigma \ge 0$.
Perturb the interface to $z = \eta(x, t)$ and linearise the Euler equations, with [[potential flow|84K7TEWZ2Z]] in each layer.
The *Rayleigh–Taylor instability* is the exponential growth in time of a normal mode $\eta = \hat\eta \, e^{ikx + st}$, $k > 0$, $s > 0$, of this linear problem.

## Remarks

The normal modes satisfy
$$s^2 = \frac{g k (\rho_2 - \rho_1) - \sigma k^3}{\rho_1 + \rho_2}.$$
So the wavenumber $k$ is unstable exactly when $\rho_2 > \rho_1$ and $k^2 < g (\rho_2 - \rho_1) / \sigma$, with every $k > 0$ unstable when $\sigma = 0$.

Example: with $\sigma = 0$ and heavy fluid on top, the growth rate is $s = \sqrt{A g k}$, where $A = (\rho_2 - \rho_1) / (\rho_2 + \rho_1)$ is the Atwood number.
Non-example: if $\rho_2 < \rho_1$, the light fluid on top, then $s^2 < 0$ for every $k$, and the modes are oscillating interfacial gravity waves, not growing ones.

By the equivalence principle, the same instability occurs at an interface accelerated with acceleration $a$ directed from the light fluid towards the heavy fluid, with $g$ replaced by $a$.
The configuration is the special case $U_1 = U_2 = 0$ of the Kelvin–Helmholtz problem.
