---
tag: 1NNFAMQ54B
kind: example
name: Hénon–Heiles system
msc: [70H07, 37N05, 85A05]
instance_of: [0EDKGA2FAK]
uses: [0EDKGA2FAK, 0262JP0NV9, 60TDCPY4Z4, 3ZZSXKM16Z, DBKXCGDKTD, 0N8NGKDZDZ]
sources:
  - url: https://en.wikipedia.org/wiki/H%C3%A9non%E2%80%93Heiles_system
same_as:
  wikidata: Q5964294
  wikipedia: Hénon–Heiles system
---

## Example

The *Hénon–Heiles system* is the [[Hamiltonian system|0EDKGA2FAK]] on $\R^4$ with coordinates $(x, y, p_x, p_y)$ and Hamiltonian
$$H = \frac{1}{2} \left( p_x^2 + p_y^2 \right) + \frac{1}{2} \left( x^2 + y^2 \right) + x^2 y - \frac{1}{3} y^3.$$
Its equations of motion are
$$x'' = -x - 2 x y, \qquad y'' = -y - x^2 + y^2.$$
The energy $H$ is a [[first integral|0262JP0NV9]].
The potential $V(x, y) = \frac{1}{2}(x^2 + y^2) + x^2 y - \frac{1}{3} y^3$ has a minimum at the origin and three saddle [[equilibrium points|0N8NGKDZDZ]] at $(0, 1)$ and $\left( \pm \frac{\sqrt{3}}{2}, -\frac{1}{2} \right)$.
Check at $(0, 1)$: $\partial_x V = x + 2 x y = 0$ and $\partial_y V = y + x^2 - y^2 = 1 - 1 = 0$, and $V(0, 1) = \frac{1}{2} - \frac{1}{3} = \frac{1}{6}$.
The value of $V$ is $\frac{1}{6}$ at all three saddles, so for energies $0 < E < \frac{1}{6}$ the motion near the origin stays in a bounded triangular region.

## Remarks

Michel Hénon and Carl Heiles introduced the system in 1964.
It was a model for the motion of a star in the gravitational field of a galaxy with an axis of symmetry.
They studied it numerically with a [[Poincaré section|60TDCPY4Z4]] on the energy surface.
At low energies most orbits lie on smooth invariant curves, as the [[KAM theorem|3ZZSXKM16Z]] predicts near an integrable system.
As the energy approaches $\frac{1}{6}$, the regular region shrinks and most of the section is filled by [[chaotic|DBKXCGDKTD]] orbits.
The system became a standard test case for chaos in Hamiltonian systems with two degrees of freedom.

## Explanations

### L1 human

The Hénon–Heiles system describes a ball rolling in a bowl that is round at the bottom and has the shape of a rounded triangle higher up.
With little energy the ball moves in regular, repeating patterns.
With more energy its path becomes irregular and unpredictable, although nothing random is in the equations.
It was one of the first clear computer pictures of chaos in a mechanical system.
