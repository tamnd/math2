---
tag: GBEY10W50T
kind: statement
role: proposition
name: Energy–momentum relation
msc: [83A05, 70H40]
uses: [67N6B8MJ3X, H5BXV0V62D, G49G4R1K04]
about: [67N6B8MJ3X]
sources:
  - url: https://en.wikipedia.org/wiki/Energy–momentum_relation
same_as:
  wikidata: Q3502299
  wikipedia: Energy–momentum relation
---

## Statement

Let a particle of mass $m \ge 0$ have energy $E$ and momentum $\vec p$ in an inertial frame, and let $c$ be the speed of light.
Then
$$E^2 = \abs{\vec p}^2 c^2 + m^2 c^4.$$

## Remarks

The [[four-momentum|67N6B8MJ3X]] is $p = (E/c, \vec p)$, and its Minkowski square is $\eta(p, p) = -m^2 c^2$, where $\eta = \operatorname{diag}(-1, 1, 1, 1)$ is the metric of [[Minkowski space|G49G4R1K04]].
Writing out $-E^2/c^2 + \abs{\vec p}^2 = -m^2c^2$ gives the relation.
For $m > 0$ one can check it directly: $E = \gamma m c^2$ and $\vec p = \gamma m \vec v$ give $E^2 - \abs{\vec p}^2c^2 = \gamma^2 m^2 c^4 (1 - \abs{\vec v}^2/c^2) = m^2 c^4$.
For a photon, $m = 0$ and the relation reduces to $E = \abs{\vec p} c$.
For a particle at rest it gives $E = mc^2$.
For small momentum, $E = mc^2 \sqrt{1 + \abs{\vec p}^2/(m^2c^2)} \approx mc^2 + \abs{\vec p}^2/(2m)$, the rest energy plus the Newtonian kinetic energy.
The same relation holds for a system, with $m$ replaced by its [[invariant mass|H5BXV0V62D]] and $E$, $\vec p$ by its total energy and momentum.

## Explanations

### L1 human

Energy and momentum of a particle are tied together by its mass.
Think of a right triangle with legs $mc^2$ and $\abs{\vec p} c$: the energy $E$ is the hypotenuse.
A particle at rest has only the leg $mc^2$; a particle without mass, like a photon, has only the leg $\abs{\vec p}c$.

### L2 human

The relation is the statement that the four-momentum lies on the mass shell, the hyperboloid $\eta(p, p) = -m^2c^2$ with $p^0 > 0$.
It is used constantly in collision kinematics, for example to find the energy threshold of a reaction from the [[invariant mass|H5BXV0V62D]] of the initial state.
In quantum mechanics it leads, with $E \to i\hbar \partial_t$ and $\vec p \to -i\hbar\nabla$, to the Klein–Gordon equation.
