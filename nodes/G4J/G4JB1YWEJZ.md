---
tag: G4JB1YWEJZ
kind: example
name: Couette flow
msc: [76D05, 76D07]
illustrates: [18KXZHVF4M]
uses: [18KXZHVF4M, DF0M8YNQ3D, NM5Q4845Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Couette_flow
same_as:
  wikidata: Q1114429
  wikipedia: Couette flow
---

## Example

Consider a fluid of density $\rho > 0$ and dynamic [[viscosity|NM5Q4845Z4]] $\mu > 0$ between two parallel plates $y = 0$ and $y = h$, with $h > 0$.
The lower plate is at rest and the upper plate moves in the $x$-direction with constant speed $U$.
*Plane Couette flow* is
$$u = \Big( \frac{U y}{h}, 0, 0 \Big), \qquad p = p_0,$$
with $p_0$ a constant.

Check: $u$ depends only on $y$ and points in the $x$-direction, so $\nabla \cdot u = 0$ and $(u \cdot \nabla) u = (U y / h) \, \partial_x u = 0$.
Also $\Delta u = 0$ since $u$ is linear, and $\nabla p = 0$.
So the steady [[Navier–Stokes equations|18KXZHVF4M]] $\rho (u \cdot \nabla) u = -\nabla p + \mu \Delta u$ hold.
At $y = 0$ the velocity is $0$ and at $y = h$ it is $(U, 0, 0)$, so the [[no-slip condition|DF0M8YNQ3D]] holds on both plates.

## Remarks

The shear stress $\mu \, \partial_y u_1 = \mu U / h$ is the same at every height.
Measuring the force needed to drag the upper plate gives $\mu$, which is the principle of a Couette viscometer.
With an added constant pressure gradient $\partial_x p = -G$ the flow becomes $u_1 = \frac{U y}{h} + \frac{G}{2 \mu} y (h - y)$, a sum of Couette and Poiseuille flow.
The rotating version between two coaxial cylinders is [[Taylor–Couette flow|6Q0X0W9F11]].

## Explanations

### L1 human

Put a thin layer of honey between two plates and slide the top plate.
The honey right at each plate moves with that plate, and in between the speed changes evenly from bottom to top.
This straight-line speed profile is the simplest viscous flow there is.
