---
tag: SNB562CJDB
kind: statement
role: theorem
name: Work–energy theorem
msc: [70A05, 70F10]
uses: [KNBP19FG6K, 4NMMPYCK2C, 0CDZ684TCD, 0NHGY0N0JB]
about: [C9YCMAPKMT, 0CDZ684TCD]
sources:
  - url: https://en.wikipedia.org/wiki/Work_(physics)
---

## Statement

Let a particle of constant mass $m > 0$ move along a path $x \colon [a, b] \to \R^3$ of class $C^2$.
Let $F(t) = m \ddot x(t)$ be the net force on it, as given by [[Newton's second law|KNBP19FG6K]].
Then the [[work|0CDZ684TCD]] of the net force along the motion equals the change of [[kinetic energy|4NMMPYCK2C]]:
$$\int_a^b F(t) \cdot \dot x(t)\, dt = \tfrac12 m \abs{\dot x(b)}^2 - \tfrac12 m \abs{\dot x(a)}^2.$$

## Remarks

The proof is one line: $\frac{d}{dt}\big(\frac12 m \abs{\dot x}^2\big) = m \ddot x \cdot \dot x = F \cdot \dot x$, and the [[fundamental theorem of calculus|0NHGY0N0JB]] integrates this from $a$ to $b$.
Example: a constant force of size $4$ pushes a body of mass $2$ from rest over a distance $3$ along its direction.
The work is $12$, so the final speed $v$ satisfies $\frac12 \cdot 2 v^2 = 12$, that is, $v = 2\sqrt3$, in SI units.
The theorem concerns the net force; the work of a single force among several does not in general equal the change of kinetic energy.
For a system of particles, the same identity holds when the work of all forces, internal and external, is added up.

## Explanations

### L1 human

The work that the total force does on a body is exactly the kinetic energy that the body gains.
Pushing a cart forward adds energy of motion; braking takes it away.

### L2 human

The theorem is the integrated form of Newton's second law along the velocity.
When the force has a potential energy, the work is the drop of potential energy, and the theorem becomes the conservation of mechanical energy.
It often gives speeds directly, without solving the equations of motion in time.
