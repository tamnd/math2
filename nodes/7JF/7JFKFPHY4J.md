---
tag: 7JFKFPHY4J
kind: definition
name: Light cone
msc: [83A05, 53B30]
defines: JZ9ADDZX8D
uses: [G49G4R1K04, PNEFDF4Z03]
sources:
  - url: https://en.wikipedia.org/wiki/Light_cone
---

## Definition

Let $(V, \eta)$ be [[Minkowski space|G49G4R1K04]] with signature $(-, +, +, +)$ and coordinates $(x^0, x^1, x^2, x^3)$, and let $p$ be an event.
The *light cone* of $p$ is the set
$$C(p) = \set{q : \eta(q - p, q - p) = 0},$$
the events at [[spacetime interval|PNEFDF4Z03]] zero from $p$.
Its *future light cone* is the part with $q^0 \ge p^0$ and its *past light cone* the part with $q^0 \le p^0$.

## Remarks

Example: with $c = 1$, the event $q = (2, 1, 1, \sqrt{2})$ lies on the future light cone of the origin.
Check: $-4 + 1 + 1 + 2 = 0$ and $q^0 = 2 > 0$.
Non-example: $q = (1, 2, 0, 0)$ is not on the light cone of the origin, since $-1 + 4 = 3 \ne 0$; it is spacelike separated from it.
The events $q$ with $\eta(q - p, q - p) < 0$ and $q^0 > p^0$ form the interior of the future cone, the *chronological future* of $p$.
The light cone is preserved by every Lorentz transformation, and in a Lorentzian manifold the same construction is made in each tangent space.
