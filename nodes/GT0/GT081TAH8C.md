---
tag: GT081TAH8C
kind: definition
name: Impulse
msc: [70A05, 70F10]
defines: CW0ZBRQSPA
uses: [0QM4TXT3DR, HFDS8NCJ1A, KNBP19FG6K]
sources:
  - url: https://en.wikipedia.org/wiki/Impulse_(physics)
---

## Definition

Let $F \colon [t_0, t_1] \to \R^3$ be an integrable force acting on a particle during the time interval $[t_0, t_1]$.
The *impulse* of $F$ over $[t_0, t_1]$ is the vector
$$J = \int_{t_0}^{t_1} F(t)\, dt,$$
where the [[integral|0QM4TXT3DR]] is taken component by component.

## Remarks

If $F$ is the net force on a particle of constant mass, [[Newton's second law|KNBP19FG6K]] gives $J = p(t_1) - p(t_0)$, the change of [[momentum|HFDS8NCJ1A]].
Example: the constant force $F = (10, 0, 0)$ over $[0, 0.5]$ has impulse $J = (5, 0, 0)$.
For a particle of mass $1$ at rest at $t = 0$, its velocity at $t = 0.5$ is then $(5, 0, 0)$.
Non-example: the line integral $\int F \cdot dx$ along the path is a scalar, the work, and not the impulse; it integrates over the path rather than over time.
The unit of impulse is the newton-second, the same as the unit of momentum.

## Explanations

### L1 human

Impulse adds up a force over the time it acts.
It is exactly the change of momentum it causes, whatever the shape of the force in time.
