---
tag: 2G5DNV8MK4
kind: definition
name: Degrees of freedom
msc: [70G10, 70F20]
defines: 21SZKJ4XCK
uses: [MGYKGP7PW3, BCF1EX9W2M]
sources:
  - url: https://en.wikipedia.org/wiki/Degrees_of_freedom_(mechanics)
---

## Definition

Consider a mechanical system with holonomic constraints whose [[configuration space|MGYKGP7PW3]] $Q$ is a smooth manifold.
The *number of degrees of freedom* of the system is the dimension $n$ of $Q$.
Equivalently, it is the number of [[generalized coordinates|BCF1EX9W2M]] $q_1, \dots, q_n$ needed to describe the configurations near any point of $Q$.

## Remarks

Example: $N$ point particles in $\R^3$ with $k$ independent holonomic constraints have $3N - k$ degrees of freedom.
A planar double pendulum has $2$ particles in the plane, so $4$ coordinates, and $2$ rod constraints; it has $4 - 2 = 2$ degrees of freedom.
Non-example: a set of positions that is not a manifold, such as two crossing lines, has no well-defined dimension near the crossing.
There the count of degrees of freedom is not defined.
If the system also has $m$ independent nonholonomic constraints on the velocities, it has $n - m$ independent velocities.
Some authors call $n - m$ the number of degrees of freedom and keep $n$ as the number of generalized coordinates.
