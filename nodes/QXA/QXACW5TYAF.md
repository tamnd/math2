---
tag: QXACW5TYAF
kind: definition
name: Invariant mass
msc: [83A05, 70H40]
defines: H5BXV0V62D
uses: [G49G4R1K04, 67N6B8MJ3X]
sources:
  - url: https://en.wikipedia.org/wiki/Invariant_mass
---

## Definition

Let $(\R^4, \eta)$ be [[Minkowski space|G49G4R1K04]] with $\eta = \operatorname{diag}(-1, 1, 1, 1)$, and let $c$ be the speed of light.
Let a system of particles have [[four-momenta|67N6B8MJ3X]] $p_1, \ldots, p_n$, each future-directed timelike or null, and let $P = p_1 + \cdots + p_n$ be the total four-momentum.
The *invariant mass* of the system is
$$M = \frac{1}{c} \sqrt{-\eta(P, P)}.$$
In an inertial frame where $P = (E/c, \vec P)$, this reads $M^2 c^4 = E^2 - \abs{\vec P}^2 c^2$.

## Remarks

A sum of future-directed timelike or null vectors is future-directed timelike or null, so $-\eta(P, P) \ge 0$ and $M$ is a real number $\ge 0$.
Since $\eta$ is preserved by Lorentz transformations, $M$ does not depend on the inertial frame.
For one particle of mass $m$, $P = m u$ and $M = m$.
Example: two photons with four-momenta $(E/c)(1, 1, 0, 0)$ and $(E/c)(1, -1, 0, 0)$ give $P = (2E/c, 0, 0, 0)$, so $M = 2E/c^2 > 0$ although each photon has mass $0$.
Non-example: the sum $\sum_i \gamma_i m_i$ of the relativistic masses of the particles is not the invariant mass: it equals $E/c^2$, which depends on the frame.
When $M > 0$ there is a frame where $\vec P = 0$, the centre-of-momentum frame, and there $M = E/c^2$.
