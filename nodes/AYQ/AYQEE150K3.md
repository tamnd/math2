---
tag: AYQEE150K3
kind: definition
name: Relativistic mechanics
msc: [83A05, 70H40]
defines: ZBD683ZDDX
uses: [G49G4R1K04, Z788G6MJ9E, YG74WHC3S9, Y59V040THG, 67N6B8MJ3X]
sources:
  - url: https://en.wikipedia.org/wiki/Relativistic_mechanics
---

## Definition

Let $(\R^4, \eta)$ be [[Minkowski space|G49G4R1K04]] with inertial coordinates $x = (ct, \vec x)$ and $\eta = \operatorname{diag}(-1, 1, 1, 1)$, where $c$ is the speed of light.
*Relativistic mechanics* of a point particle is the following model.

1. A particle of mass $m > 0$ is a future-directed timelike [[world line|Z788G6MJ9E]] $\tau \mapsto x(\tau)$, parametrised by [[proper time|YG74WHC3S9]] $\tau$.
2. Its [[four-velocity|Y59V040THG]] is $u = dx/d\tau$, so $\eta(u, u) = -c^2$, and its [[four-momentum|67N6B8MJ3X]] is $p = m u$.
3. A force on the particle is a four-vector $F(\tau)$ along the world line with $\eta(F, u) = 0$, called the four-force.
4. The equation of motion is
$$\frac{dp}{d\tau} = F.$$

## Remarks

In an inertial frame write $\vec v = d\vec x/dt$, $\gamma = 1/\sqrt{1 - \abs{\vec v}^2/c^2}$ and $F = \gamma(\vec f \cdot \vec v / c, \vec f)$ for a three-force $\vec f$.
Then the equation of motion becomes $\frac{d}{dt}(\gamma m \vec v) = \vec f$ and $\frac{d}{dt}(\gamma m c^2) = \vec f \cdot \vec v$, because $d\tau = dt/\gamma$.
Example: a free particle has $F = 0$, so $p$ is constant and the world line is a straight line; with $\vec v = 0$ it gives $p = (mc, \vec 0)$.
Non-example: a four-vector $F$ with $\eta(F, u) \ne 0$ is not an admissible force, because $\frac{d}{d\tau}\eta(p, p) = 2m\,\eta(F, u)$ would change the value $\eta(p, p) = -m^2c^2$, and so the mass.
For small speeds $\gamma \approx 1$, and the first equation reduces to Newton's second law $m \, d\vec v/dt = \vec f$.
