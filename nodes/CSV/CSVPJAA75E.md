---
tag: CSVPJAA75E
kind: problem
name: Two-body problem
msc: [70F05, 70F15]
uses: [29WRN5J730, 0HNK6KT05K, X5G1A3A4VR, TYXD1T6FRX, 62SNWC5E45, 00HJCMC2CD]
about: [62SNWC5E45, TYXD1T6FRX]
sources:
  - url: https://en.wikipedia.org/wiki/Two-body_problem
same_as:
  wikidata: Q232976
  wikipedia: Two-body problem
history:
  posed_by: "Isaac Newton"
  first_stated: "1687"
---

## Problem

Let $G > 0$ be the gravitational constant and let $m_1, m_2 > 0$ be masses.
Let the positions $x_1(t), x_2(t) \in \R^3$ satisfy [[Newton's law of universal gravitation|29WRN5J730]]
$$m_1 x_1'' = \frac{G m_1 m_2 (x_2 - x_1)}{\norm{x_2 - x_1}^3}, \qquad m_2 x_2'' = \frac{G m_1 m_2 (x_1 - x_2)}{\norm{x_1 - x_2}^3}.$$
Given initial positions with $x_1(0) \neq x_2(0)$ and initial velocities, determine the motion of the two bodies.

## Remarks

The problem is solved completely.
Let $M = m_1 + m_2$, let $R = (m_1 x_1 + m_2 x_2) / M$ be the [[centre of mass|0HNK6KT05K]] and let $r = x_2 - x_1$ be the relative position.
Adding the two equations gives $R'' = 0$, so the centre of mass moves on a straight line at constant speed.
Subtracting them gives
$$r'' = - \frac{G M \, r}{\norm{r}^3},$$
which is the [[Kepler problem|TYXD1T6FRX]] with $k = G M$.
Equivalently, $\mu r'' = - G m_1 m_2 \, r / \norm{r}^3$, where $\mu = m_1 m_2 / M$ is the [[reduced mass|X5G1A3A4VR]].
So $r$ moves on a [[conic section|00HJCMC2CD]] with a focus at $0$, or on a line through $0$ when the angular momentum is zero.
Then $x_1 = R - \frac{m_2}{M} r$ and $x_2 = R + \frac{m_1}{M} r$, so each body moves on a scaled copy of the relative orbit around the centre of mass.

The two-body problem is the case $n = 2$ of the [[n-body problem|62SNWC5E45]], while for $n \ge 3$ there is no general solution by elementary formulas.
Newton solved it in the Principia of 1687.

## Explanations

### L1 human

Two bodies, such as a star and a planet, pull on each other by gravity.
Their common balance point moves in a straight line, and each body circles around it.
Seen from one body, the other moves on an ellipse, a parabola or a hyperbola, just as if the first were fixed.
