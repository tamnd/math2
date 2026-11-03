---
tag: VQ5Z44PXXR
kind: statement
role: proposition
name: Sverdrup balance
msc: [86A05, 76U05]
uses: [F2D7MXW8V1, 6HZRX3WSQD, 0NF6GQNXMY, CZ1S1P465Y]
about: [F2D7MXW8V1]
sources:
  - url: https://en.wikipedia.org/wiki/Sverdrup_balance
same_as:
  wikidata: Q1144436
  wikipedia: Sverdrup balance
---

## Statement

Consider an ocean of constant depth $H$ on a [[beta plane|F2D7MXW8V1]], with Coriolis parameter $f = f_0 + \beta y$ and $\beta > 0$, and reference density $\rho_0$.
Let $\tau = (\tau^x, \tau^y)$ be the wind stress on the surface, a smooth function of $(x, y)$.
Assume the flow is steady and linear.
So in each layer the [[Coriolis force|6HZRX3WSQD]] is balanced by the horizontal pressure gradient and by the vertical divergence of the stress.
Assume the stress vanishes at the bottom.
Assume also that the vertical velocity vanishes at the surface $z = 0$ and at the bottom $z = -H$.
Let $V(x, y) = \int_{-H}^{0} v \, dz$ be the meridional volume transport per unit width, including the surface Ekman layer.
Then
$$\beta V = \frac{1}{\rho_0} \Big( \frac{\partial \tau^y}{\partial x} - \frac{\partial \tau^x}{\partial y} \Big).$$

## Remarks

Integrating the momentum equations over depth gives $-f V = -\rho_0^{-1} \partial_x P + \rho_0^{-1} \tau^x$ and $f U = -\rho_0^{-1} \partial_y P + \rho_0^{-1} \tau^y$, where $U$ is the zonal transport and $P = \int_{-H}^{0} p \, dz$.
Taking the [[curl|0NF6GQNXMY]] eliminates $P$ and leaves $f (\partial_x U + \partial_y V) + \beta V = \rho_0^{-1} (\partial_x \tau^y - \partial_y \tau^x)$.
The depth-integrated continuity equation with $w = 0$ at top and bottom gives $\partial_x U + \partial_y V = 0$, and the balance follows.

Example: in the northern hemisphere the westerlies blow eastward near latitude $45^\circ$, and the trade winds blow westward near latitude $15^\circ$.
So $\tau^x$ increases with $y$ in between, and the wind-stress curl is negative.
The balance then gives $V < 0$: the interior of the subtropical gyre carries water toward the equator.
The return flow cannot obey the balance, and it occurs in a narrow western boundary current such as the Gulf Stream.

The assumption $\beta \ne 0$ is essential: on an $f$-plane the left side vanishes and the equation gives no information on the transport.

## Explanations

### L1 human

On the rotating Earth, a column of water that moves north or south must change its spin to keep its total spin fixed.
The Sverdrup balance says that the twisting of the ocean by the wind is used up entirely in such north-south motion.
So knowing the winds is enough to predict how much water flows north or south across the interior of an ocean basin.
It is named after Harald Sverdrup.

### L2 human

The balance is the vorticity equation $\beta v = f \, \partial w / \partial z$ of [[geostrophic|CZ1S1P465Y]] flow, integrated over the depth, with the vertical velocity at the base of the Ekman layer given by Ekman pumping.
Given $V$, the zonal transport $U$ follows from continuity by integrating $\partial_x U = -\partial_y V$ westward from the eastern boundary, where $U = 0$.
The interior solution cannot also satisfy the condition at the western boundary, and this mismatch is resolved by the frictional boundary layers of Stommel and Munk.
