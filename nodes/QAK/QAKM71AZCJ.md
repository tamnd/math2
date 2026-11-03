---
tag: QAKM71AZCJ
kind: definition
name: Baroclinic instability
msc: ["76E20", 76U60, 86A10]
defines: 2SVQ4JN85Y
uses: [8Z4QBWTWVR, F2D7MXW8V1, 73GW90ST91]
sources:
  - url: https://en.wikipedia.org/wiki/Baroclinity
---

## Definition

Consider the [[quasi-geostrophic equations|8Z4QBWTWVR]] on a [[beta plane|F2D7MXW8V1]] with Coriolis parameter $f_0 + \beta y$ and buoyancy frequency $N(z) > 0$.
The domain is periodic in $x$, with $0 \le z \le H$ and walls or decay in $y$.
Let $U(y, z)$ be a steady zonal basic flow, in [[thermal wind|73GW90ST91]] balance with a basic buoyancy $B$ such that $f_0 \, \partial_z U = -\partial_y B$.
The basic flow is *unstable* if the linearised equations admit a normal mode $\psi' = \operatorname{Re}[\hat\psi(y, z) e^{i k (x - c t)}]$ with $k$ real and $\operatorname{Im} c > 0$.
The instability is *baroclinic* when the growth of such modes is supplied by the vertical shear $\partial_z U$.
Then the eddies gain energy from the available potential energy of the basic state.
They do so through a buoyancy flux $\overline{v' b'}$ directed down the basic buoyancy gradient.

## Remarks

The growth rate of the mode is $k \operatorname{Im} c$.
The contrasting case is barotropic instability, in which the eddies draw energy from the horizontal shear $\partial_y U$ of the basic flow.

Example: in the [[Eady model|KBCEHH0H7N]], $U = \Lambda z$ on an f-plane with constant $N$ and rigid lids at $z = 0$ and $z = H$.
All wavelengths longer than about $2.6 \, N H / f_0$ grow, the fastest with growth rate about $0.31 \, f_0 \Lambda / N$.

Non-example: a uniform flow $U = U_0$ has no vertical shear and no horizontal buoyancy gradient.
It has no available potential energy to release, and on an f-plane every normal mode has real $c$.

The Charney–Stern theorem gives necessary conditions for such an instability in terms of the gradient of the basic quasi-geostrophic potential vorticity.
