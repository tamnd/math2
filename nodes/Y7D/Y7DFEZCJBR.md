---
tag: Y7DFEZCJBR
kind: definition
name: Nonholonomic system
msc: [70F25, 70G45]
defines: PTRV0QFSB9
uses: [AXA8HN8Y45, BCF1EX9W2M, K160D2Z0CS, 5Q4BHBFXJY]
sources:
  - url: https://en.wikipedia.org/wiki/Nonholonomic_system
---

## Definition

Consider a mechanical system with [[generalized coordinates|BCF1EX9W2M]] $q = (q_1, \dots, q_n)$ in an open set $V \subseteq \R^n$ and time $t$.
Let $a_{ji}$ and $b_j$ be smooth functions of $(q, t)$, for $1 \le j \le m$ and $1 \le i \le n$, such that the $m \times n$ matrix $(a_{ji})$ has rank $m$ everywhere.
Suppose the motion obeys the $m$ constraints, linear in the generalized velocities,
$$\sum_{i=1}^n a_{ji}(q, t)\, \dot q_i + b_j(q, t) = 0, \qquad j = 1, \dots, m.$$
The system is *nonholonomic* if this family is not equivalent to a family of [[holonomic constraints|AXA8HN8Y45]].
This means: there are no smooth functions $f_1(q, t), \dots, f_m(q, t)$ such that, near each point, a motion obeys the constraints exactly when each $f_j(q(t), t)$ is constant.

## Remarks

Example: a skate on the plane has coordinates $(x, y, \theta)$, and the blade forbids sideways motion: $\dot x \sin\theta - \dot y \cos\theta = 0$.
The allowed velocities at each point are spanned by $X = (\cos\theta, \sin\theta, 0)$ and $Y = (0, 0, 1)$, and their Lie bracket $[Y, X] = (-\sin\theta, \cos\theta, 0)$ is not in that span.
By the [[Frobenius theorem|5Q4BHBFXJY]] the constraint is not integrable, so the skate is nonholonomic.
Non-example: the constraint $\dot x \cos y - x \sin y\, \dot y = 0$ on the plane is $\frac{d}{dt}(x \cos y) = 0$, equivalent to the holonomic constraint $x \cos y = c$.
For scleronomous constraints with $b_j = 0$, nonholonomic means that the distribution of allowed velocities is not involutive.
