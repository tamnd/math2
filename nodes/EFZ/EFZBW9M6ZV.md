---
tag: EFZBW9M6ZV
kind: definition
name: Buckley–Leverett equation
msc: [76S05, 76T06, 35L65]
defines: GZQJQGH7VZ
uses: [XN081NCPF5, DX8RV2XG6H, A3Q9SNF86Q]
sources:
  - url: https://en.wikipedia.org/wiki/Buckley%E2%80%93Leverett_equation
---

## Definition

Consider one-dimensional flow of two immiscible incompressible fluids, water and oil, through a homogeneous porous medium of porosity $\phi \in (0, 1)$, neglecting gravity and capillary pressure.
Let $S(x, t) \in [0, 1]$ be the water saturation, and let $u > 0$ be the total Darcy velocity of the two fluids, which is constant in $x$.
Let $k_{rw}(S)$ and $k_{ro}(S)$ be the relative permeabilities and $\mu_w$, $\mu_o$ the viscosities of water and oil, and define the fractional flow function
$$f(S) = \frac{k_{rw}(S) / \mu_w}{k_{rw}(S) / \mu_w + k_{ro}(S) / \mu_o}.$$
The *Buckley–Leverett equation* is the scalar [[conservation law|XN081NCPF5]]
$$\frac{\partial S}{\partial t} + \frac{u}{\phi} \frac{\partial f(S)}{\partial x} = 0.$$

## Remarks

It follows from conservation of water and [[Darcy's law|DX8RV2XG6H]] for each phase: the water flux is $u f(S)$.

Example: with $k_{rw} = S^2$, $k_{ro} = (1 - S)^2$ and $\mu_w = \mu_o$, $f(S) = S^2 / (S^2 + (1 - S)^2)$.
This $f$ increases from $0$ to $1$ and has an inflection point at $S = 1/2$, so it is neither convex nor concave.
For injection of water into a medium with $S = 0$, the entropy solution is a shock from $0$ to a saturation $S^*$ followed by a rarefaction.
The value $S^*$ is fixed by the tangent condition $f(S^*) / S^* = f'(S^*)$, the Welge construction.
Here $S^* = 1/\sqrt{2}$.

Non-example: if capillary pressure is kept, an extra term of the form $\partial_x (D(S) \partial_x S)$ appears, and the equation is parabolic, not a pure hyperbolic conservation law.
