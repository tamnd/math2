---
tag: NCYXJ5GP62
kind: definition
name: Marangoni effect
msc: [76D45, "76E06"]
defines: 26R4JJ2MXQ
uses: [18KXZHVF4M, NM5Q4845Z4, DF0M8YNQ3D]
sources:
  - url: https://en.wikipedia.org/wiki/Marangoni_effect
---

## Definition

Consider a liquid with [[viscosity|NM5Q4845Z4]] $\mu > 0$ in the half-space $z < 0$, below a flat free surface $z = 0$.
Above the surface is a gas of negligible viscosity.
Let $u = (u_1, u_2, u_3)$ be the velocity of the liquid, a solution of the [[Navier–Stokes equations|18KXZHVF4M]].
Let the surface tension $\sigma(x, y)$ be a smooth function on the surface, for instance through its dependence on the temperature or on a surfactant concentration.
The *Marangoni effect* is the tangential stress $\nabla_s\sigma = (\partial_x\sigma, \partial_y\sigma)$ that the surface exerts on the liquid.
It enters the boundary condition at $z = 0$:
$$\mu\,\frac{\partial u_1}{\partial z} = \frac{\partial\sigma}{\partial x}, \qquad \mu\,\frac{\partial u_2}{\partial z} = \frac{\partial\sigma}{\partial y}, \qquad u_3 = 0.$$
A flow driven by this stress is called a Marangoni flow.

## Remarks

Example: let $\sigma(x) = \sigma_0 + \tau x$ with $\tau > 0$ constant, and take a liquid layer $-d < z < 0$ on a solid bottom with the [[no-slip condition|DF0M8YNQ3D]].
The steady shear flow $u = \left(\frac{\tau}{\mu}(z + d), 0, 0\right)$ satisfies the Navier–Stokes equations with constant pressure, vanishes at $z = -d$, and has $\mu\,\partial_z u_1 = \tau = \partial_x\sigma$ at $z = 0$.
So the surface moves towards larger $\sigma$, with speed $\tau d/\mu$.
Non-example: if $\sigma$ is constant, the condition reduces to $\partial_z u_1 = \partial_z u_2 = 0$, the stress-free condition, and there is no Marangoni stress.
For thermal Marangoni convection one uses the Marangoni number $\mathrm{Ma} = -\frac{d\sigma}{dT}\frac{\Delta T\,L}{\mu\alpha}$, with $\Delta T$ a temperature difference, $L$ a length and $\alpha$ the thermal diffusivity.
