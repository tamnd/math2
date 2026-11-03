---
tag: HFDS8NCJ1A
kind: definition
name: Momentum
msc: [70A05, 70F10]
defines: 37Q4BTJMXW
uses: [SH7J0X3NCC, K160D2Z0CS]
sources:
  - url: https://en.wikipedia.org/wiki/Momentum
---

## Definition

Let a particle of mass $m > 0$ move with [[velocity|K160D2Z0CS]] $\dot x(t) \in \R^3$ at time $t$.
Its *momentum* at time $t$ is the vector
$$p(t) = m\, \dot x(t).$$
For a [[Newtonian system|SH7J0X3NCC]] of $N$ point particles with masses $m_i$ and velocities $\dot x_i(t)$, the *total momentum* is $P(t) = \sum_{i=1}^{N} m_i \dot x_i(t)$.

## Remarks

Example: a particle of mass $2$ with position $x(t) = (3t, t^2, 0)$ has velocity $(3, 2t, 0)$ and momentum $p(t) = (6, 4t, 0)$.
Non-example: the quantity $m \abs{\dot x}^2/2$ is a scalar, the kinetic energy, and not the momentum.
With $M = \sum_i m_i$ and the centre of mass $X = \frac{1}{M}\sum_i m_i x_i$, the total momentum is $P = M \dot X$.
Some texts call $p$ the linear momentum, to separate it from angular momentum.
Newton's second law reads $\dot p = F$, where $F$ is the net force.

## Explanations

### L1 human

Momentum is "mass times velocity".
It adds up over the parts of a system, and the total momentum moves as if all the mass sat at the centre of mass.
