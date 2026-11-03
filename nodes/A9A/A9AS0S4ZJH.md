---
tag: A9AS0S4ZJH
kind: definition
name: Kinematics
msc: [70B05, 70B10, 70B15]
defines: T08CJT9E1E
uses: [68W1NWECX8, K160D2Z0CS, Q8D2JWY8G6, 2FTZ7D8Z0F]
sources:
  - url: https://en.wikipedia.org/wiki/Kinematics
---

## Definition

*Kinematics* is the branch of [[classical mechanics|68W1NWECX8]] that studies the motion of points, bodies and systems of bodies as functions of time.
It makes no reference to the masses involved or to the forces that cause the motion.
Its objects are:

1. the positions of points as functions of time, given in a frame of reference, together with their [[velocities|K160D2Z0CS]], [[accelerations|Q8D2JWY8G6]] and higher derivatives;
2. the orientations of bodies as functions of time, together with their [[angular velocities|2FTZ7D8Z0F]] and angular accelerations;
3. the relations that geometric constraints, such as joints and linkages, impose between these quantities.

## Remarks

Example: a point with constant acceleration $a$, initial position $x_0$ and initial velocity $v_0$ is at $x(t) = x_0 + v_0 t + \frac12 a t^2$.
This statement is kinematic: it follows from integrating twice, with no forces involved.
Non-example: the statement that a ball under gravity has acceleration $-g$ in the vertical direction is not kinematic, because it comes from a law of force; it belongs to dynamics.
Kinematics of points is the subject of MSC class 70B05, rigid body kinematics of 70B10, and the kinematics of robots and mechanisms of 70B15.
