---
tag: V1TJKX965V
kind: definition
name: Multibody system
msc: ["70E55", "70E60"]
defines: 87RX5SJ7DJ
uses: [EZ9P9ERKNE, BCF1EX9W2M, AXA8HN8Y45, 21SZKJ4XCK, EY362KR0KB]
sources:
  - url: https://en.wikipedia.org/wiki/Multibody_system
---

## Definition

A *multibody system* consists of the following data.

1. A finite set of bodies $B_1, \ldots, B_N$, each a [[rigid body|EZ9P9ERKNE]] with given mass and inertia tensor.
2. A finite set of joints, each joining two bodies, or a body and the ground, and constraining their relative position and velocity.
3. Applied forces and torques acting on the bodies, such as gravity, springs, dampers and actuators.

The *topology* of the system is the graph whose vertices are the bodies and the ground and whose edges are the joints.

## Remarks

When the joints give [[holonomic constraints|AXA8HN8Y45]], the configurations form a set of dimension $n$, the number of [[degrees of freedom|21SZKJ4XCK]].
If the graph is a tree, one can use the joint variables as [[generalized coordinates|BCF1EX9W2M]] $q \in \R^n$.
The equations of motion then take the form $M(q)\ddot q + C(q, \dot q) = \tau$, with a symmetric positive definite mass matrix $M(q)$.
If the graph has cycles, the closure of each loop adds algebraic constraints $\Phi(q) = 0$, and the equations become a [[differential-algebraic system|EY362KR0KB]].

Example: a planar double pendulum, two rods joined by a hinge, with the first rod hinged to the ground.
Its graph is a path ground, rod 1, rod 2, which is a tree, and its two hinge angles are generalized coordinates; it has $2$ degrees of freedom.

Non-example: a vibrating elastic beam is not a multibody system.
It is not made of finitely many rigid bodies, and it has infinitely many degrees of freedom.

## Explanations

### L1 human

A multibody system is a set of rigid parts with joints between them.
The joints decide how the parts may move relative to each other, and the forces decide how they actually move.
