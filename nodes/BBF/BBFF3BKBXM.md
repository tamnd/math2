---
tag: BBFF3BKBXM
kind: definition
name: Einstein–Infeld–Hoffmann equations
msc: ["83C10", "70F10"]
defines: FQVH3J95KD
uses: [29WRN5J730, 62SNWC5E45, 7HC8RM1EH9, 3MCZ97SW6V]
sources:
  - url: https://en.wikipedia.org/wiki/Einstein%E2%80%93Infeld%E2%80%93Hoffmann_equations
---

## Definition

Consider $N \ge 2$ point masses with masses $m_1, \dots, m_N > 0$, positions $x_a(t) \in \R^3$, velocities $v_a = \dot x_a$ and accelerations $a_a = \ddot x_a$, in harmonic coordinates with coordinate time $t$.
Write $r_{ab} = \abs{x_a - x_b}$ and $n_{ab} = (x_a - x_b)/r_{ab}$ for $a \ne b$, let $G$ be the gravitational constant and $c$ the speed of light.
Fix an index $a \in \set{1, \dots, N}$.
The *Einstein–Infeld–Hoffmann equations* are
$$\begin{aligned} a_a = {} & \sum_{b \ne a} \frac{G m_b\, n_{ba}}{r_{ab}^2} \Big[ 1 - \frac{4}{c^2} \sum_{d \ne a} \frac{G m_d}{r_{ad}} - \frac{1}{c^2} \sum_{d \ne b} \frac{G m_d}{r_{bd}} + \frac{\abs{v_a}^2}{c^2} + \frac{2\abs{v_b}^2}{c^2} - \frac{4\, v_a \cdot v_b}{c^2} \\ & \qquad - \frac{3}{2c^2} (n_{ab} \cdot v_b)^2 + \frac{1}{2c^2} (x_b - x_a) \cdot a_b \Big] \\ & + \frac{1}{c^2} \sum_{b \ne a} \frac{G m_b}{r_{ab}^2} \big[ n_{ab} \cdot (4 v_a - 3 v_b) \big] (v_a - v_b) + \frac{7}{2c^2} \sum_{b \ne a} \frac{G m_b\, a_b}{r_{ab}}. \end{aligned}$$
All terms of order $c^{-4}$ are dropped.
So in the $c^{-2}$ terms each $a_b$ may be replaced by its Newtonian value $\sum_{d \ne b} G m_d n_{db}/r_{bd}^2$.

## Remarks

The equations are the first [[post-Newtonian|7HC8RM1EH9]] correction to [[Newton's law of gravitation|29WRN5J730]]: when $c \to \infty$ they reduce to $a_a = \sum_{b \ne a} G m_b n_{ba}/r_{ab}^2$.

Example: take a test mass $m_1 \to 0$ moving around a mass $m_2 = M$ at rest at the origin, so $v_2 = 0$ and $a_2 = 0$.
With $r = r_{12}$, $n = n_{12}$ and $v = v_1$, the equations give
$$a_1 = -\frac{GM}{r^2} n \Big[ 1 - \frac{4GM}{rc^2} + \frac{\abs v^2}{c^2} \Big] + \frac{4GM}{r^2c^2} (n \cdot v)\, v,$$
which is the geodesic equation of the Schwarzschild metric in harmonic coordinates, expanded to order $c^{-2}$.

Non-example: the plain Newtonian equations $a_a = \sum_{b \ne a} G m_b n_{ba}/r_{ab}^2$ are not the Einstein–Infeld–Hoffmann equations; they miss the velocity-dependent terms and give no perihelion advance for two bodies.

The equations are also the Euler–Lagrange equations of a Lagrangian for the $N$ bodies, so they conserve energy, momentum and angular momentum to order $c^{-2}$.
They contain no radiation reaction, which first appears at order $c^{-5}$.
