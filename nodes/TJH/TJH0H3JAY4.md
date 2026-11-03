---
tag: TJH0H3JAY4
kind: definition
name: F-plane
msc: [76U60, 86A10, 86A05]
defines: 287Z5PMWY5
uses: [6HZRX3WSQD]
sources:
  - url: https://en.wikipedia.org/wiki/F-plane
---

## Definition

Let a planet rotate with angular speed $\Omega$, and fix a reference latitude $\varphi_0$.
The *f-plane* at $\varphi_0$ is the model that writes the equations of motion in flat coordinates $x$ (east), $y$ (north) and $z$ (up).
In it the [[Coriolis|6HZRX3WSQD]] parameter is the constant $f_0 = 2 \Omega \sin \varphi_0$.

## Remarks

Only the vertical component of the rotation vector is kept, so the horizontal Coriolis acceleration is $f_0 \, \mathbf{k} \times \mathbf{u}$, with $\mathbf{k}$ the upward unit vector and $\mathbf{u}$ the horizontal velocity.
The f-plane is the beta plane with $\beta = 0$.

Example: at $\varphi_0 = 45^\circ$ on the Earth, $\Omega = 7.292 \times 10^{-5}$ s$^{-1}$ gives $f_0 \approx 1.03 \times 10^{-4}$ s$^{-1}$.
Unforced frictionless flow $\partial_t \mathbf{u} = -f_0 \mathbf{k} \times \mathbf{u}$ on the f-plane gives inertial oscillations, in which $\mathbf{u}$ rotates with period $2 \pi / \abs{f_0}$, about $17$ hours at $45^\circ$.

Non-example: a model with $f = f_0 + \beta y$ and $\beta \ne 0$ is not an f-plane; it supports Rossby waves, which the f-plane does not.
