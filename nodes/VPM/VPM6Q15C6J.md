---
tag: VPM6Q15C6J
kind: concept
name: Featherstone's algorithm
msc: ["70E55", "70E60"]
sources:
  - url: https://en.wikipedia.org/wiki/Featherstone%27s_algorithm
same_as:
  wikidata: Q5439643
  wikipedia: Featherstone's algorithm
---

## Summary

Featherstone's algorithm, also called the articulated-body algorithm, computes the accelerations of a [[multibody system|87RX5SJ7DJ]] whose joints form a tree.
Given the joint positions, velocities and forces, it finds the joint accelerations with a number of operations proportional to the number of bodies.
Methods that first form and then solve the full mass matrix need a number of operations that grows like the cube of this number.
The algorithm is used in robotics and in physics engines for simulation.

## Explanations

### L1 human

Simulating a robot arm requires, at each small time step, finding how fast each joint speeds up under the motor forces and gravity.
The direct approach writes one big system of equations for all joints together and solves it.
Featherstone's algorithm instead walks along the chain of links, from the base out to the tips, back to the base, and out again.
On the way in, each link learns how the part of the arm beyond it responds to a push.
On the way out, the accelerations follow one joint at a time.
