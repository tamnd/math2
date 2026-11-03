---
tag: FDP9G4BCMF
kind: definition
name: Ffowcs Williams–Hawkings equation
msc: [76Q05]
defines: W0ZTN95BMW
uses: [J31W7DJ90H, 85WZYYHZYS, 09C4JP7Y0M, 0KPHENZ5S7]
sources:
  - url: https://en.wikipedia.org/wiki/Aeroacoustics
---

## Definition

Consider a compressible fluid in $\R^3$ with density $\rho$, velocity $u$, pressure $p$ and viscous stress tensor $\tau_{ij}$.
Let $\rho_0$, $p_0$, $c_0$ be the constant density, pressure and speed of sound of the fluid at rest.
Let a closed surface move in the fluid, given as the zero set of a smooth function $f(x, t)$.
Assume $f > 0$ outside the surface and $\abs{\nabla f} = 1$ on it.
Let $n = \nabla f$ be the outward unit normal, $v_n$ the normal velocity of the surface and $u_n = u \cdot n$ the normal velocity of the fluid.
Let $H$ be the [[Heaviside function|09C4JP7Y0M]] and $\delta$ the [[Dirac delta|0KPHENZ5S7]].
Set $\rho' = \rho - \rho_0$, $P_{ij} = (p - p_0) \delta_{ij} - \tau_{ij}$, and let $T_{ij}$ be the Lighthill stress tensor of [[Lighthill's acoustic analogy|J31W7DJ90H]].
The *Ffowcs Williams–Hawkings equation* is the equation, in the sense of distributions,
$$\left( \frac{1}{c_0^2} \frac{\partial^2}{\partial t^2} - \Delta \right) \big( c_0^2 \rho' H(f) \big) = \frac{\partial}{\partial t} \big[ Q \, \delta(f) \big] - \frac{\partial}{\partial x_i} \big[ L_i \, \delta(f) \big] + \frac{\partial^2}{\partial x_i \partial x_j} \big[ T_{ij} H(f) \big],$$
where $Q = \rho_0 v_n + \rho (u_n - v_n)$ and $L_i = P_{ij} n_j + \rho u_i (u_n - v_n)$, with summation over repeated indices.

## Remarks

The equation follows from the mass and momentum equations of the fluid outside the surface, written for the generalised functions $\rho' H(f)$ and $\rho u_i H(f)$.
The surface terms come from the derivatives of $H(f)$.
The three terms on the right are the thickness (monopole), loading (dipole) and quadrupole sources.
Outside the source region $c_0^2 \rho'$ equals the acoustic pressure $p'$.

Example: for a solid surface the fluid does not cross the boundary, so $u_n = v_n$.
The sources then reduce to $Q = \rho_0 v_n$ and $L_i = P_{ij} n_j$, the force per unit area that the surface exerts on the fluid.

Special case: when no surface is present, so that $H(f) = 1$ everywhere, the surface terms vanish and the equation reduces to Lighthill's equation.
