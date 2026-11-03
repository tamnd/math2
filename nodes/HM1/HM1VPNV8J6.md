---
tag: HM1VPNV8J6
kind: definition
name: Lattice Boltzmann method
msc: [76M28, 82C40, 65M75]
defines: PMGS1JJPHK
uses: [YQRS1ZMRAC, MH6CSWD7F0, 18KXZHVF4M]
sources:
  - url: https://en.wikipedia.org/wiki/Lattice_Boltzmann_methods
---

## Definition

Let $\Delta x > 0$ and $\Delta t > 0$ be the lattice spacing and the time step, and consider the lattice $\Delta x\, \Z^d$.
Let $c_0, \ldots, c_{q-1} \in \R^d$ be velocities with $c_i \Delta t \in \Delta x\, \Z^d$, and let $w_i > 0$ be weights summing to $1$.
Let $c_s > 0$ be a lattice sound speed such that $\sum_i w_i c_i = 0$ and $\sum_i w_i c_i c_i^T = c_s^2 I$.
The unknowns are populations $f_i(x, t)$ at lattice points $x$ and times $t \in \Delta t\, \N$, with density $\rho = \sum_i f_i$ and momentum $\rho u = \sum_i c_i f_i$.
The equilibrium populations are
$$f_i^{eq} = w_i \rho \left( 1 + \frac{c_i \cdot u}{c_s^2} + \frac{(c_i \cdot u)^2}{2 c_s^4} - \frac{\abs{u}^2}{2 c_s^2} \right).$$
The *lattice Boltzmann method* with BGK collision and relaxation time $\tau > \Delta t / 2$ is the update
$$f_i(x + c_i \Delta t, t + \Delta t) = f_i(x, t) - \frac{\Delta t}{\tau} \big( f_i(x, t) - f_i^{eq}(x, t) \big).$$

## Remarks

The update is a collision step, a discrete version of the [[BGK collision operator|YQRS1ZMRAC]], followed by a streaming step to the neighbouring site.
The collision conserves $\rho$ and $\rho u$ at each site, since $f^{eq}$ has the same zeroth and first moments as $f$.
A Chapman–Enskog expansion shows that, for small $\abs{u}/c_s$, the moments approximate the Navier–Stokes equations with kinematic viscosity $\nu = c_s^2 (\tau - \Delta t / 2)$.

Example: the D2Q9 lattice in two dimensions has $\Delta x = \Delta t = 1$ and $c_s^2 = 1/3$.
It uses $c_0 = (0, 0)$ with $w_0 = 4/9$, the four axis vectors $(\pm 1, 0), (0, \pm 1)$ with weight $1/9$, and the four diagonals $(\pm 1, \pm 1)$ with weight $1/36$.
Check: the weights sum to $4/9 + 4/9 + 4/36 = 1$, and $\sum_i w_i c_{i,1}^2 = 2 \cdot \tfrac19 + 4 \cdot \tfrac1{36} = \tfrac13$.

Non-example: the D2Q5 lattice, with only the rest and the four axis velocities, lacks the fourth-order isotropy needed for the Navier–Stokes equations.
It is used instead for advection–diffusion problems.
