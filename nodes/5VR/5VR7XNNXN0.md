---
tag: 5VR7XNNXN0
kind: concept
name: Homotopy continuation for polynomial systems
msc: [65H14, 65H20, 14Q65]
specializes: [5V3GJ84CPQ]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_algebraic_geometry
---

## Summary

Homotopy continuation for polynomial systems computes all isolated solutions of a system of polynomial equations in several complex variables.
It deforms a start system, whose solutions are known, into the target system, and it follows each start solution along the deformation by [[numerical continuation|5V3GJ84CPQ]].
It is the basic algorithm of numerical algebraic geometry, and it is used for systems from kinematics, chemistry and other applications.

## Explanations

### L1 human

Solving many polynomial equations at once is hard, but some systems are easy, such as $x^2 = 1$, $y^3 = 1$.
Homotopy continuation slides the easy system into the hard one step by step.
Each solution of the easy system moves along a path as the equations change, and where the paths end are the solutions of the hard system.
For a system of two equations of degrees $2$ and $3$, one follows $2 \cdot 3 = 6$ paths, and these endpoints include every isolated solution.
