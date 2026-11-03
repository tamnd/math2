---
tag: WYMPWM6GZ2
kind: definition
name: Scleronomous constraint
msc: [70F20, 70G10]
defines: Y5DPEB2N70
uses: [AXA8HN8Y45]
sources:
  - url: https://en.wikipedia.org/wiki/Scleronomous
---

## Definition

Consider a system of $N$ point particles with position vector $x \in \R^{3N}$ and time $t$.
Let $f(x, t) = 0$ be a [[holonomic constraint|AXA8HN8Y45]], with $f$ defined on $U \times J$ for an open set $U \subseteq \R^{3N}$ and an interval $J$.
The constraint is *scleronomous* if $f$ does not depend on $t$, that is, $\partial f / \partial t = 0$ on $U \times J$.
More generally, a constraint $g(x, \dot x, t) = 0$ on positions and velocities is scleronomous if $g$ does not depend on $t$.

## Remarks

Example: the pendulum constraint $\abs{x}^2 - \ell^2 = 0$, with fixed length $\ell > 0$, does not contain $t$, so it is scleronomous.
Non-example: a bead moves on a wire ring of radius $1$, centred at the origin in a vertical plane through the $z$-axis.
The ring turns about the $z$-axis with angular speed $\omega \ne 0$.
The bead obeys $x \sin(\omega t) - y \cos(\omega t) = 0$ and $x^2 + y^2 + z^2 = 1$; the first equation contains $t$ explicitly, so it is not scleronomous.
When all constraints are scleronomous, the positions of the particles can be written as functions $x = x(q)$ of generalized coordinates $q$ alone, without $t$.
