---
tag: 8CTSVCSDDS
kind: definition
name: Rheonomous constraint
msc: [70F20, 70G10]
defines: VR3HXNKCZR
uses: [AXA8HN8Y45, Y5DPEB2N70]
sources:
  - url: https://en.wikipedia.org/wiki/Rheonomous
---

## Definition

Consider a system of $N$ point particles with position vector $x \in \R^{3N}$ and time $t$.
A constraint $g(x, \dot x, t) = 0$ is *rheonomous* if $g$ depends explicitly on $t$, that is, if it is not a [[scleronomous constraint|Y5DPEB2N70]].
In particular, a [[holonomic constraint|AXA8HN8Y45]] $f(x, t) = 0$ is rheonomous when $\partial f / \partial t$ is not identically zero.

## Remarks

Example: a pendulum of length $\ell > 0$ whose pivot moves on the vertical axis as $p(t) = (0, 0, a \cos(\omega t))$, with $a \ne 0$ and $\omega \ne 0$, obeys $\abs{x - p(t)}^2 - \ell^2 = 0$, and this function depends on $t$.
Non-example: the same pendulum with a fixed pivot obeys $\abs{x}^2 - \ell^2 = 0$, which has no explicit $t$.
Whether a constraint is rheonomous can depend on the coordinates.
In a frame that rotates with a turning wire, the constraint of a bead on the wire no longer contains $t$, but that frame is not inertial.
