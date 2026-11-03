---
tag: 4NMMPYCK2C
kind: definition
name: Kinetic energy
msc: [70A05, 70F10]
defines: C9YCMAPKMT
uses: [K160D2Z0CS, HFDS8NCJ1A]
sources:
  - url: https://en.wikipedia.org/wiki/Kinetic_energy
---

## Definition

Let a particle of mass $m > 0$ have [[velocity|K160D2Z0CS]] $\dot x(t) \in \R^3$ at time $t$.
Its *kinetic energy* at time $t$ is
$$T(t) = \tfrac12\, m \abs{\dot x(t)}^2,$$
where $\abs{\cdot}$ is the Euclidean norm.
For $N$ particles with masses $m_i$ and velocities $\dot x_i$, the kinetic energy is $T = \sum_{i=1}^{N} \tfrac12 m_i \abs{\dot x_i}^2$.

## Remarks

Example: a particle of mass $2$ with velocity $(1, 2, 2)$ has $\abs{\dot x}^2 = 9$ and kinetic energy $T = 9$.
Non-example: the quantity $m\, \dot x$ is a vector, the [[momentum|HFDS8NCJ1A]] $p$, and not the kinetic energy.
In terms of momentum, $T = \abs{p}^2/(2m)$.
For a system with total mass $M$ and centre-of-mass velocity $V$, the kinetic energy splits as $T = \frac12 M \abs{V}^2 + \sum_i \frac12 m_i \abs{\dot x_i - V}^2$.

## Explanations

### L1 human

Kinetic energy is half the mass times the speed squared.
It is zero only when the body is at rest, and it does not care in which direction the body moves.
