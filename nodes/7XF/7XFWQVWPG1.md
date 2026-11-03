---
tag: 7XFWQVWPG1
kind: statement
role: theorem
name: Bernoulli's principle
msc: [76A02, 76B99]
uses: [ZJH90RWYQ5, RW0JK9VDZE, ZWF8B7T5NX, B3SXT9TWFA, 470A1RJWBP]
about: [ZJH90RWYQ5]
sources:
  - url: https://en.wikipedia.org/wiki/Bernoulli%27s_principle
same_as:
  wikidata: Q181328
  wikipedia: Bernoulli's principle
---

## Statement

Let a fluid of constant density $\rho > 0$ flow in an open set $\Omega \subseteq \R^3$ with velocity $u$ and pressure $p$, both smooth.
Assume the flow is [[inviscid|ZJH90RWYQ5]] and the body force per unit mass is $f = -\nabla \Phi$ for a smooth potential $\Phi$.

1. If the flow is steady, then the Bernoulli function
$$H = \frac{p}{\rho} + \frac{\abs{u}^2}{2} + \Phi$$
is constant along each [[streamline|ZWF8B7T5NX]].
2. If the flow is steady and irrotational, that is $\nabla \times u = 0$, then $H$ is constant in all of $\Omega$ when $\Omega$ is connected.
3. Assume the flow is irrotational with [[velocity potential|470A1RJWBP]] $\varphi$, so $u = \nabla \varphi$, and $\Omega$ is connected.
The flow need not be steady.
Then
$$\frac{\partial \varphi}{\partial t} + \frac{\abs{u}^2}{2} + \frac{p}{\rho} + \Phi = C(t)$$
for a function $C$ of time alone.

## Remarks

The proof uses the identity $(u \cdot \nabla) u = \nabla (\abs{u}^2 / 2) - u \times \omega$, where $\omega = \nabla \times u$ is the [[vorticity|B3SXT9TWFA]].
With it, the steady [[Euler equations|RW0JK9VDZE]] become $\nabla H = u \times \omega$.
The right side is orthogonal to $u$, so $u \cdot \nabla H = 0$ and $H$ is constant along streamlines.
If $\omega = 0$, then $\nabla H = 0$ everywhere.

Example: water leaves a small hole at depth $h$ below the free surface of a large tank.
Along a streamline from the surface (speed about $0$, atmospheric pressure, $\Phi = g h$) to the jet (atmospheric pressure, $\Phi = 0$), part 1 gives the speed $\sqrt{2 g h}$ (Torricelli's law).

Without the inviscid hypothesis the result fails.
In steady viscous flow through a straight pipe, the speed along each streamline is constant while the pressure drops, so $H$ decreases downstream.

There is a version for steady compressible barotropic flow, with $p / \rho$ replaced by $\int dp / \rho$.

## Explanations

### L1 human

Along the path of a fluid parcel, pressure and speed trade off: where the fluid moves faster, the pressure is lower.
This explains why a shower curtain is pulled inward and how a Venturi tube measures speed.
It is an energy balance: pressure, motion and height together keep a fixed total when friction is negligible.

### L2 human

Bernoulli's principle is a first integral of the steady Euler equations.
It turns the momentum equation into an algebraic relation between pressure and speed, so once the velocity of a potential flow is known, the pressure follows at once.
This is how one computes forces in potential flow, for example in the Kutta–Joukowski theorem and in d'Alembert's paradox.
The relation $\nabla H = u \times \omega$ links it to [[Crocco's theorem|1JE4AC4QFF]], which is its thermodynamic version for compressible flow.
