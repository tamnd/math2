---
tag: S3RZRCH0T5
kind: statement
role: fact
name: Lorentz force
msc: [78A35, 78A25]
uses: [6XPSV47R56, YZ7Q9DP8RT, XRED3C547P, 0N5N15HWZ7]
about: [YZ7Q9DP8RT, XRED3C547P]
sources:
  - url: https://en.wikipedia.org/wiki/Lorentz_force
same_as:
  wikidata: Q172137
  wikipedia: Lorentz force
---

## Statement

Let $E$ and $B$ be the [[electric field|YZ7Q9DP8RT]] and the [[magnetic field|XRED3C547P]] in a region of $\R^3$.
Let a point [[charge|6XPSV47R56]] $q$ be at the point $x$ at time $t$, with velocity $v$.
Then the electromagnetic force on the charge is
$$F = q \, \big( E(x, t) + v \times B(x, t) \big),$$
where $\times$ is the [[cross product|0N5N15HWZ7]].

## Remarks

The Lorentz force law is a law of physics, not a theorem; together with Maxwell's equations it is the basis of classical electrodynamics.
The magnetic part does no work, since $(v \times B) \cdot v = 0$; so a magnetic field changes the direction of motion but not the speed.
Example: in a uniform field $B$ with $E = 0$, a particle of mass $m$ moving perpendicular to $B$ with speed $u$ follows a circle.
Its radius is $m u / (\abs{q} \abs{B})$ and its angular frequency is $\abs{q} \abs{B} / m$, the cyclotron frequency.
For a current density $J$, the force per unit volume is $\rho E + J \times B$, with charge density $\rho$.

## Explanations

### L1 human

The Lorentz force tells how electric and magnetic fields push a charged particle.
The electric part pushes along the field, whether the particle moves or not.
The magnetic part acts only on moving charges and pushes sideways, at right angles to both the motion and the field.

### L2 human

With Newton's second law, $m \dot v = q (E + v \times B)$ gives the equations of motion of charged particles, used for cyclotrons, mass spectrometers and plasmas.
For constant crossed fields with $\abs{E} < c \abs{B}$, the particle drifts with the velocity $E \times B / \abs{B}^2$.
In special relativity the law becomes covariant, with the electromagnetic tensor acting on the four-velocity, and $m \dot v$ replaced by the rate of change of relativistic momentum.
