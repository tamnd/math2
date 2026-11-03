---
tag: NAW7Y8GWFB
kind: definition
name: Kutta condition
msc: [76B10, 76G25]
defines: DSWYGZCGM5
uses: [84K7TEWZ2Z, Q4DVPTBHEE, BTHH4Y71QR]
sources:
  - url: https://en.wikipedia.org/wiki/Kutta_condition
---

## Definition

Let $B$ be a bounded rigid body in the plane, with smooth boundary except at one corner point $T$, the trailing edge.
At $T$ the interior angle is less than $\pi$, possibly $0$ (a cusp).
Consider steady, incompressible and irrotational flows of an inviscid fluid outside $B$, tangent to the boundary of $B$.
Assume that they tend to a given uniform stream far from $B$.
These [[potential flows|84K7TEWZ2Z]] form a one-parameter family, indexed by the [[circulation|BTHH4Y71QR]] $\Gamma$ around $B$.
For all but one value of $\Gamma$ the velocity is unbounded near $T$.
The *Kutta condition* is the requirement that the velocity stays bounded in a neighbourhood of $T$.
It holds for exactly one value of $\Gamma$.

## Remarks

Example: a flat plate of chord $c$ at angle of attack $\alpha$ in a stream of speed $U$.
Map the exterior of a circle conformally onto the exterior of the plate; the [[complex potential|Q4DVPTBHEE]] of the circle flow with circulation $\Gamma$ gives a flow past the plate.
The velocity is bounded at the trailing edge exactly when the rear stagnation point of the circle flow sits at the preimage of the edge, which forces $\abs{\Gamma} = \pi U c \sin\alpha$.
The plate also has a sharp leading edge, where the velocity stays unbounded; the condition is imposed only at the trailing edge.
Non-example: the same flow with $\Gamma = 0$ goes around the sharp trailing edge, and its speed tends to infinity at the edge, so it fails the condition.
At a trailing edge with a positive angle the condition makes $T$ a stagnation point; at a cusp the velocities on the two sides become equal and finite.
