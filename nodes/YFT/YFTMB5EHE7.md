---
tag: YFTMB5EHE7
kind: definition
name: Jerk
msc: [70B05]
defines: ES59TGRGN7
uses: [Q8D2JWY8G6, 04TKTF8KDK]
sources:
  - url: https://en.wikipedia.org/wiki/Jerk_(physics)
---

## Definition

Let $I \subseteq \R$ be an open interval of times, and let $x \colon I \to \R^3$ give the position of a point particle in a fixed frame of reference.
Assume $x$ is twice differentiable on $I$, with [[acceleration|Q8D2JWY8G6]] $a = \ddot x$, and that $a$ is differentiable at $t \in I$.
The *jerk* of the particle at time $t$ is the vector
$$j(t) = \dot a(t) = x^{(3)}(t),$$
the third [[derivative|04TKTF8KDK]] of the position.

## Remarks

Example: for $x(t) = (t^3, 0, 0)$, the acceleration is $a(t) = (6t, 0, 0)$ and the jerk is the constant vector $(6, 0, 0)$.
Non-example: the change of acceleration $a(t_2) - a(t_1)$ is not the jerk; it must be divided by $t_2 - t_1$ and the limit taken.
For uniform circular motion with angular speed $\omega$ and position $x(t)$ relative to the centre, $j(t) = -\omega^2 \dot x(t)$, which is nonzero although the speed is constant.
The SI unit of jerk is $\mathrm{m/s^3}$.
