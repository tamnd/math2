---
tag: C68BDNFQ7N
kind: definition
name: Contact mechanics
msc: [74M15, 74M10, 74B05]
defines: T0R3FBPTJ2
uses: [JRD6BDKT1X, KG2XWEMJ30, QFQAB091MQ]
sources:
  - url: https://en.wikipedia.org/wiki/Contact_mechanics
---

## Definition

*Contact mechanics* is the part of [[solid mechanics|JRD6BDKT1X]] that studies deformable bodies which may touch along part of their boundaries.
On the possible contact surface $\Gamma_c$ let $g$ be the gap between the bodies measured along the normal $n$.
Let $p = -n \cdot \sigma n$ be the contact pressure, where $\sigma$ is the [[Cauchy stress|KG2XWEMJ30]].
A contact problem is a boundary value problem of solid mechanics with the following conditions on $\Gamma_c$:

1. non-penetration: $g \ge 0$,
2. no adhesion: $p \ge 0$,
3. complementarity: $g \, p = 0$, so pressure acts only where the gap is closed,
4. a law for the tangential traction, for example zero traction (frictionless contact) or a friction law such as Coulomb's.

## Remarks

Example: a linear elastic body pressed against a rigid flat obstacle without friction.
Its equilibrium equations together with clauses 1 to 4, with zero tangential traction, form the [[Signorini problem|QFQAB091MQ]].

Non-example: a body glued to a rigid support.
There the displacement is prescribed on the whole surface and the traction may pull as well as push.
So clauses 1 to 3 are replaced by an equality, and the problem is an ordinary boundary value problem.

Clauses 1 to 3 are the Signorini conditions, also called the Hertz–Signorini–Moreau conditions.
Adhesive contact, as in the [[JKR model|98BMFJ17D9]], relaxes clause 2.
