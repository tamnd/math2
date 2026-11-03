---
tag: T0ZXBPN5XR
kind: definition
name: Dupuit–Forchheimer assumption
msc: [76S05, 86A05]
defines: 4JHXH2E83Q
uses: [DX8RV2XG6H, 64DSSBPT5E, DGVNNYKBHC]
sources:
  - url: https://en.wikipedia.org/wiki/Dupuit–Forchheimer_assumption
---

## Definition

Consider an unconfined aquifer of hydraulic conductivity $K > 0$ on a horizontal impermeable base $z = 0$, with water table at height $z = h(x, y, t) > 0$.
The *Dupuit–Forchheimer assumption* states that:

1. the hydraulic head is constant on each vertical line, so it equals $h(x, y, t)$ at every depth;
2. hence, by [[Darcy's law|DX8RV2XG6H]], the flow is horizontal with specific discharge $-K \nabla h$, the same at every depth, where $\nabla = (\partial_x, \partial_y)$.

The discharge per unit width is then $-K h \nabla h$.
Conservation of mass gives the *Boussinesq equation*
$$S_y \frac{\partial h}{\partial t} = \nabla \cdot (K h \nabla h) + N.$$
Here $S_y > 0$ is the specific yield and $N$ is the recharge rate.

## Remarks

Example: steady flow in a strip $0 \le x \le L$ between water levels $h(0) = h_1$ and $h(L) = h_2$, with no recharge.
The discharge per unit width $q = -K h \, dh/dx$ is constant, so $h^2$ is linear in $x$, and
$$q = \frac{K (h_1^2 - h_2^2)}{2 L}, \qquad h(x)^2 = h_1^2 - (h_1^2 - h_2^2) \frac{x}{L}.$$
This is Dupuit's formula; the discharge it gives is known to be exact for this geometry, although the water table shape is not.

Non-example: near a pumping well the water table drops steeply and the flow has a strong vertical part, so clause 1 fails.
The assumption also ignores the seepage face that forms at the well.

The Boussinesq equation with $N = 0$ and constant $K$ is $\partial_t h = \frac{K}{2 S_y} \nabla^2 (h^2)$, a [[porous medium equation|DGVNNYKBHC]] with exponent $2$.
It is the nonlinear counterpart of the [[groundwater flow equation|64DSSBPT5E]] of a confined aquifer.
