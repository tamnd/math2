---
tag: 7ZMAJ5RBEY
kind: definition
name: Central configuration
msc: [70F10, 70F15]
defines: HQSVS8HX7F
uses: [62SNWC5E45, 0HNK6KT05K, 29WRN5J730]
sources:
  - url: https://en.wikipedia.org/wiki/Central_configuration
---

## Definition

Let $n \ge 2$, let $G > 0$ be the gravitational constant, let $m_1, \ldots, m_n > 0$ be masses and let $d \ge 1$.
Let $q_1, \ldots, q_n \in \R^d$ be pairwise distinct positions with [[centre of mass|0HNK6KT05K]] $c = \frac{1}{M} \sum_i m_i q_i$, where $M = \sum_i m_i$.
The configuration $(q_1, \ldots, q_n)$ is a *central configuration* if there is a real number $\lambda$ such that
$$\sum_{j \ne i} \frac{G m_j (q_j - q_i)}{\norm{q_j - q_i}^3} = -\lambda\, (q_i - c) \qquad \text{for all } i = 1, \ldots, n.$$
The left side is the acceleration of body $i$ under [[Newton's law of gravitation|29WRN5J730]].

## Remarks

The constant $\lambda$ is always positive.
Central configurations are counted up to translation, rotation and scaling, since these maps send central configurations to central configurations.
Equivalently, they are the critical points of the potential $U = \sum_{i < j} G m_i m_j / \norm{q_i - q_j}$ restricted to configurations with a fixed moment of inertia about the centre of mass.

Example: three equal masses $m = 1$, with $G = 1$, at the vertices of an equilateral triangle of side $s$.
Each body feels two pulls of size $1/s^2$ with an angle of $60^\circ$ between them, so the total pull has size $\sqrt{3}/s^2$ and points to the centre.
The distance to the centre is $s/\sqrt{3}$, so the condition holds with $\lambda = 3/s^3$.
By a result of Lagrange the equilateral triangle is central for any three positive masses.

Non-example: three unit masses on a line at $0$, $1$ and $3$, with $G = 1$, so $c = 4/3$.
The body at $0$ has acceleration $1 + 1/9 = 10/9$, which forces $\lambda = 5/6$.
The body at $1$ has acceleration $-1 + 1/4 = -3/4$, which forces $\lambda = -9/4$.
No single $\lambda$ works, so the configuration is not central.

These configurations give solutions of the [[n-body problem|62SNWC5E45]] in which the shape stays similar to itself.
In the plane, a rigid rotation with angular speed $\sqrt{\lambda}$ about $c$ is a solution, called a relative equilibrium.
