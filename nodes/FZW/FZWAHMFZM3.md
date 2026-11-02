---
tag: FZWAHMFZM3
kind: statement
role: fact
name: Gauss's principle of least constraint
msc: [70F25, 70H30, 49S05]
uses: [GD776GVZSR]
about: [GD776GVZSR]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss%27s_principle_of_least_constraint
same_as:
  wikidata: Q1477313
  wikipedia: Gauss's principle of least constraint
---

## Statement

Consider $N$ particles with masses $m_i > 0$ and applied forces $F_i$, for $i = 1, \dots, N$, subject to ideal constraints that are holonomic or linear in the velocities.
Fix a time $t$ and the positions and velocities of the particles at time $t$.
Call a family $(b_1, \dots, b_N)$ of vectors of $\R^3$ an *admissible acceleration* if it is compatible with the constraints at these positions and velocities.
Define the *constraint* (Gauss's function)
$$Z(b_1, \dots, b_N) = \sum_{i=1}^{N} m_i \,\Big\lvert b_i - \frac{F_i}{m_i} \Big\rvert^2.$$
Then the actual accelerations $a_i = \ddot r_i(t)$ are the unique minimiser of $Z$ among admissible accelerations.

## Remarks

For such constraints the admissible accelerations form an affine subspace $a + W$, where $W$ is the space of virtual displacements.
On it $Z$ is a strictly convex quadratic function, so it has a unique minimiser.
For $b = a + w$ with $w \in W$, one finds $Z(b) - Z(a) = 2\sum_i (m_i a_i - F_i) \cdot w_i + \sum_i m_i \abs{w_i}^2$.
The linear term vanishes by [[d'Alembert's principle|GD776GVZSR]], so $Z(b) > Z(a)$ when $w \neq 0$.
Example: a single free particle has all accelerations admissible, and the minimiser is $b = F/m$, which is Newton's law.

## Explanations

### L1 human

Without constraints, each particle would accelerate as $F_i/m_i$.
Constraints prevent this.
Gauss's principle says that the real motion deviates from the free motion as little as possible, where the deviation is measured by a mass-weighted sum of squares.

### L2 human

Gauss's principle is a minimum principle at each instant, not a stationarity principle over a whole path like [[Hamilton's principle|FAQ9CH2Z76]].
It is a quadratic program in the accelerations, and it handles nonholonomic constraints linear in the velocities with no extra work.
This makes it useful in the numerical simulation of constrained multibody systems.
It is equivalent to d'Alembert's principle for ideal constraints.
