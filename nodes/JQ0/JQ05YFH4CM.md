---
tag: JQ05YFH4CM
kind: definition
name: Water waves
msc: [76B15, 76B07]
defines: R9WC0Z7Z69
uses: [84K7TEWZ2Z, 470A1RJWBP, S8RG6N1PRT, 2JZ0C15A9C]
sources:
  - url: https://en.wikipedia.org/wiki/Wind_wave
---

## Definition

Let $g > 0$ be the acceleration of gravity and $h > 0$ the depth of the undisturbed water.
Use coordinates $(x, z)$ with $x \in \R^d$ horizontal ($d = 1$ or $2$) and $z$ vertical, the bottom at $z = -h$.
The *water wave problem* asks for two functions.
The first is $\eta(x, t)$, the elevation of the free surface.
The second is $\phi(x, z, t)$, the [[velocity potential|470A1RJWBP]], defined on the fluid domain $\{-h < z < \eta(x, t)\}$.
They must satisfy:

1. $\Delta \phi = 0$ in the fluid domain, where $\Delta$ is the Laplacian in $(x, z)$.
2. $\partial_z \phi = 0$ on the bottom $z = -h$.
3. $\partial_t \eta + \nabla_x \phi \cdot \nabla_x \eta = \partial_z \phi$ on $z = \eta(x, t)$ (kinematic condition).
4. $\partial_t \phi + \tfrac{1}{2}\abs{\nabla \phi}^2 + g \eta = 0$ on $z = \eta(x, t)$ (dynamic condition).

A solution describes *water waves*: the motion of an [[incompressible|2JZ0C15A9C]], inviscid fluid in irrotational motion, with velocity $\nabla \phi$, below a free surface at constant pressure.

## Remarks

Example: $\eta = 0$, $\phi = 0$ is the state of rest, and it satisfies all four clauses, since every term in them vanishes.
Non-example: the pair $\eta = a\cos(kx)$, $\phi = 0$ with $a \neq 0$, $k \neq 0$ satisfies clauses 1 to 3 but fails clause 4, since $g\eta \neq 0$; a raised surface cannot stay at rest.
Clause 1 is [[Laplace's equation|S8RG6N1PRT]], which expresses incompressibility of a [[potential flow|84K7TEWZ2Z]].
Clause 4 is the Bernoulli equation at the surface, where the pressure equals the constant atmospheric pressure, absorbed into $\phi$.
With surface tension $\sigma$ and density $\rho$, clause 4 gains the term $-\frac{\sigma}{\rho}\nabla_x \cdot \left(\frac{\nabla_x \eta}{\sqrt{1 + \abs{\nabla_x \eta}^2}}\right)$ on the left side.
For deep water one replaces clause 2 by $\nabla \phi \to 0$ as $z \to -\infty$.
