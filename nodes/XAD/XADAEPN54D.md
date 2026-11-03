---
tag: XADAEPN54D
kind: concept
name: Lagrange multipliers for constraints
msc: [70H03, 70F20, 70H45]
specializes: [47JMCBM3VJ]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange_multiplier
  - url: https://en.wikipedia.org/wiki/Lagrangian_mechanics
---

## Summary

In mechanics, Lagrange multipliers let one write the equations of motion of a constrained system in redundant coordinates, without first solving the constraints.
Each [[holonomic constraint|AXA8HN8Y45]] adds one unknown function of time, its multiplier, to the [[Lagrange equations|BEM454AYTT]].
The multipliers measure the forces that the constraints exert, such as the tension in a pendulum rod.
This is the dynamical version of the [[method of Lagrange multipliers|0VKKP8X6Q6]] for constrained extrema.
See the [[definition|PP54N0QDWF]].

## Explanations

### L1 human

A bead on a wire, or a mass on a rigid rod, cannot move freely: a constraint holds it on a curve or a surface.
One way is to choose coordinates that fit the constraint, such as an angle for the pendulum.
The other way is to keep ordinary Cartesian coordinates and add an unknown force that keeps the body on the constraint.
The multiplier is the size of this force, and it is found together with the motion.
For a pendulum in Cartesian coordinates, the multiplier gives the tension of the rod at each moment.
