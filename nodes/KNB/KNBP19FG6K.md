---
tag: KNBP19FG6K
kind: statement
role: fact
name: Newton's laws of motion
msc: [70A05, 70F10]
uses: [68W1NWECX8, Q05G0NZDNB, 37Q4BTJMXW]
about: [68W1NWECX8, Q05G0NZDNB]
sources:
  - url: https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion
same_as:
  wikidata: Q38433
  wikipedia: Newton's laws of motion
---

## Statement

Consider point particles described in an [[inertial frame of reference|Q05G0NZDNB]], in the setting of [[classical mechanics|68W1NWECX8]].
Write $m$ for the mass of a particle, $x(t) \in \R^3$ for its position at time $t$, and $p = m \dot x$ for its [[momentum|37Q4BTJMXW]].

1. First law: a particle on which the net force is zero moves with constant velocity.
2. Second law: if $F(t)$ is the net force on a particle at time $t$, then $\dfrac{dp}{dt} = F(t)$; for constant mass this reads $m \ddot x(t) = F(t)$.
3. Third law: if $F_{ij}$ is the force that particle $j$ exerts on particle $i$, then $F_{ji} = -F_{ij}$.

## Remarks

The three laws are the axioms of Newtonian mechanics, not theorems; they are confirmed by experiment within their range of validity.
The first law singles out the inertial frames, and the second law then gives the equations of motion, a system of second-order differential equations.
The third law, together with the second, gives conservation of the total momentum of an isolated system.
The strong form of the third law adds that $F_{ij}$ is parallel to $x_i - x_j$; it gives conservation of angular momentum as well.
Example: a ball of mass $m$ near the ground feels the force $(0, 0, -mg)$, so the second law gives $\ddot x = (0, 0, -g)$.
The ball then moves on a parabola, or on a vertical line if it is thrown straight up or down.
In a rotating frame the second law fails unless fictitious forces are added, which is why the frame must be inertial.

## Explanations

### L1 human

The first law says that things keep moving the way they move unless something pushes them.
The second law says how much a push changes the motion: the same force speeds up a light body more than a heavy one.
The third law says that pushes come in pairs: if you push a wall, the wall pushes back on you just as hard.

### L2 human

The second law turns a mechanical problem into an initial value problem for an ordinary differential equation.
Under mild conditions on the forces, the positions and velocities at one time determine the motion.
From the three laws one derives the conservation laws of momentum, angular momentum and, for conservative forces, energy.
Lagrangian and Hamiltonian mechanics reformulate the same laws in coordinates adapted to constraints and symmetries.
