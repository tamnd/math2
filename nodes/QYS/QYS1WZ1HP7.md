---
tag: QYS1WZ1HP7
kind: definition
name: Advection–diffusion equation
msc: [76R50, 35Q35]
defines: DG49VBBT91
uses: [VP2HN86VAG, 2JZ0C15A9C, 0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Convection%E2%80%93diffusion_equation
---

## Definition

Let $\Omega \subseteq \R^n$ be open, let $u \colon \Omega \times (0, T) \to \R^n$ be a given velocity field, let $D > 0$ be the diffusivity, and let $R$ be a given source term.
The *advection–diffusion equation* for an unknown scalar $c(x, t)$ is
$$\frac{\partial c}{\partial t} + \nabla \cdot (u c) = \nabla \cdot (D \nabla c) + R.$$
When $D$ is constant and the flow is [[incompressible|2JZ0C15A9C]], that is $\nabla \cdot u = 0$, it becomes
$$\frac{\partial c}{\partial t} + u \cdot \nabla c = D \, \Delta c + R,$$
where $\Delta$ is the [[Laplacian|0E0B6RA8K0]].

## Remarks

Example: in one dimension with constant $u = U$, constant $D$ and $R = 0$, the function
$$c(x, t) = \frac{1}{\sqrt{4 \pi D t}} \exp\!\left( -\frac{(x - U t)^2}{4 D t} \right), \quad t > 0,$$
is a solution.
Indeed $c(x, t) = G(x - U t, t)$ where $G$ solves the [[heat equation|VP2HN86VAG]] $G_t = D G_{yy}$, and then $c_t + U c_x = G_t = D c_{xx}$.

Non-example: with $u = U \ne 0$, the heat kernel $G(x, t)$ itself is not a solution, since $G_t + U G_x - D G_{xx} = U G_x \ne 0$.

For $u = 0$ the equation is the heat equation, and for $D = 0$ it is the transport equation.
When $c$ is a temperature, $D$ is the thermal diffusivity.
