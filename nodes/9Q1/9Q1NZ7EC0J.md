---
tag: 9Q1NZ7EC0J
kind: definition
name: Celestial mechanics
msc: [70F15, 70F10, 85A04]
defines: RCC89W11XQ
uses: [29WRN5J730, 62SNWC5E45, TYXD1T6FRX, 0EDKGA2FAK]
sources:
  - url: https://en.wikipedia.org/wiki/Celestial_mechanics
---

## Definition

*Celestial mechanics* is the study of the motion of bodies that interact through gravity.
Its standard model consists of point masses $m_1, \ldots, m_n > 0$ at positions $x_1(t), \ldots, x_n(t) \in \R^3$.
They move according to [[Newton's law of universal gravitation|29WRN5J730]],
$$m_i \, x_i'' = \sum_{j \neq i} \frac{G m_i m_j (x_j - x_i)}{\norm{x_j - x_i}^3}, \qquad i = 1, \ldots, n,$$
where $G > 0$ is the gravitational constant.
The field also covers simplified models derived from this one, such as restricted problems in which some masses are negligible, and corrections for extended bodies.

## Remarks

The equations above define the [[n-body problem|62SNWC5E45]], a [[Hamiltonian system|0EDKGA2FAK]].
For $n = 2$ they reduce to the [[Kepler problem|TYXD1T6FRX]], whose bounded orbits are ellipses.
The motion of the Moon around the Earth under the pull of the Sun is a question of celestial mechanics.
The fall of a stone through the air is not a typical question of the field.
There gravity is a constant force, and air friction dominates the analysis.
Relativistic corrections are treated in relativistic celestial mechanics, which uses general relativity instead of Newton's law.

## Explanations

### L1 human

Celestial mechanics is Newton's mechanics applied to the sky.
Its objects are bodies that attract each other by gravity, and its task is to predict and understand their paths.
