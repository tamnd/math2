---
tag: BE0FDGYK91
kind: example
name: Double pendulum
msc: [70K55, 70H07, 37N05]
instance_of: [0EDKGA2FAK]
uses: [0EDKGA2FAK, DBKXCGDKTD, NJ1FJSNK6A, 0262JP0NV9]
sources:
  - url: https://en.wikipedia.org/wiki/Double_pendulum
same_as:
  wikidata: Q1243208
  wikipedia: Double pendulum
---

## Example

Let $g > 0$ be the acceleration of gravity, and let $m_1, m_2, \ell_1, \ell_2 > 0$.
A point mass $m_1$ hangs from a fixed pivot on a massless rod of length $\ell_1$.
A second point mass $m_2$ hangs from the first mass on a massless rod of length $\ell_2$.
Both rods move without friction in a vertical plane.
Let $\theta_1$ and $\theta_2$ be the angles of the rods from the downward vertical.
The Lagrangian is
$$L = \frac{m_1 + m_2}{2} \ell_1^2 \theta_1'^2 + \frac{m_2}{2} \ell_2^2 \theta_2'^2 + m_2 \ell_1 \ell_2 \theta_1' \theta_2' \cos(\theta_1 - \theta_2) + (m_1 + m_2) g \ell_1 \cos \theta_1 + m_2 g \ell_2 \cos \theta_2.$$
Check: the second mass is at $(\ell_1 \sin \theta_1 + \ell_2 \sin \theta_2, \, -\ell_1 \cos \theta_1 - \ell_2 \cos \theta_2)$.
Its squared speed is $\ell_1^2 \theta_1'^2 + \ell_2^2 \theta_2'^2 + 2 \ell_1 \ell_2 \theta_1' \theta_2' \cos(\theta_1 - \theta_2)$, which gives the kinetic terms.
The Legendre transform of $L$ makes the double pendulum a [[Hamiltonian system|0EDKGA2FAK]] with two degrees of freedom.

## Remarks

The energy is a [[first integral|0262JP0NV9]], but no second independent first integral is known, and the chaotic motion described below indicates that there is none.
For small energies the motion is close to a superposition of two normal modes of the linearised system.
For larger energies numerical studies show [[chaotic|DBKXCGDKTD]] motion, with a positive [[Lyapunov exponent|NJ1FJSNK6A]] and a sensitive dependence on initial conditions.
So two double pendulums started from almost the same state soon move in completely different ways.

## Explanations

### L1 human

A double pendulum is one pendulum hanging from the end of another.
For small swings it moves in a regular way.
Started high, it flips and tumbles in an unpredictable pattern, and a tiny change of the start gives a completely different motion.
It is one of the simplest mechanical systems that shows chaos.
