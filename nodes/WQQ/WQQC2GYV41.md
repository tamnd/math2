---
tag: WQQC2GYV41
kind: definition
name: Munk's wind-driven circulation model
msc: [86A05, 76U05, 35Q86]
defines: A112WAXBF0
uses: [VQ5Z44PXXR, PV3B8PR3XJ, F2D7MXW8V1, E66111XRRA, NM5Q4845Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Ocean_gyre
---

## Definition

Consider a homogeneous ocean of constant depth $H$ and density $\rho_0$ in a bounded basin $D$ of a [[beta plane|F2D7MXW8V1]] with $\beta > 0$.
Let $\psi$ be the [[stream function|E66111XRRA]] of the depth-averaged velocity, $u = -\partial_y \psi$ and $v = \partial_x \psi$.
Let $\tau$ be the wind stress on the surface and $A_H > 0$ a lateral eddy [[viscosity|NM5Q4845Z4]].
*Munk's model* is the boundary value problem
$$\beta \frac{\partial \psi}{\partial x} = \frac{1}{\rho_0 H} \Big( \frac{\partial \tau^y}{\partial x} - \frac{\partial \tau^x}{\partial y} \Big) + A_H \nabla^4 \psi \quad \text{in } D,$$
with $\psi = 0$ on $\partial D$ (no flow through the coast) and $\partial \psi / \partial n = 0$ on $\partial D$ (no slip).
The length $\delta_M = (A_H / \beta)^{1/3}$ is the *Munk boundary layer width*.

## Remarks

Example: in a boundary layer at a western wall $x = 0$, the equation reduces to $\beta \psi_x = A_H \psi_{xxxx}$.
Its exponential solutions $e^{\lambda x}$ satisfy $\lambda^3 = \delta_M^{-3}$, so $\lambda \in \set{1, e^{2\pi i/3}, e^{-2\pi i/3}} \cdot \delta_M^{-1}$.
The two roots with negative real part give decaying solutions $e^{-x/(2\delta_M)} \cos\big(\sqrt{3} x / (2 \delta_M)\big)$ and $e^{-x/(2\delta_M)} \sin\big(\sqrt{3} x / (2 \delta_M)\big)$, enough to meet both boundary conditions at the western wall.
At an eastern wall only one decaying root is available, so the eastern layer is weaker and cannot carry the return flow.

Non-example: [[Stommel's model|PV3B8PR3XJ]] has bottom friction $-\varepsilon \nabla^2 \psi$ instead of lateral friction $A_H \nabla^4 \psi$.
It is a second-order problem, it takes only the condition $\psi = 0$, and its boundary layer has width $\varepsilon / \beta$.

Away from the boundaries the friction term is small, and $\psi$ follows the [[Sverdrup balance|VQ5Z44PXXR]].
With free-slip walls, the condition $\partial \psi / \partial n = 0$ is replaced by $\nabla^2 \psi = 0$.
