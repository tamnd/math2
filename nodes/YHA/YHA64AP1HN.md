---
tag: YHA64AP1HN
kind: concept
name: One-parameter subgroup
msc: ["22E15", 22A05]
specializes: [0JYTG5K9Y4]
sources:
  - url: https://en.wikipedia.org/wiki/One-parameter_group
same_as:
  wikidata: Q1308481
  wikipedia: One-parameter group
---

## Summary

A one-parameter subgroup of a topological group $G$ is a continuous [[group homomorphism|0JYTG5K9Y4]] from the additive group $\R$ into $G$.
In a [[Lie group|7JBRGCVJRB]], it is a smooth curve through the identity along which the group law becomes addition of the parameter.
One-parameter subgroups of a Lie group correspond to the tangent vectors at the identity, which is how the exponential map is built.

## Explanations

### L1 human

A one-parameter subgroup is a way to move steadily through a group.
Moving for time $s$ and then for time $t$ is the same as moving for time $s + t$.
Turning a wheel at constant speed is a picture: the rotation after time $t$ is a rotation by the angle $ct$.
In the group of invertible matrices, $t \mapsto e^{tA}$ is a one-parameter subgroup for each square matrix $A$.
For $A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, it gives the rotations by angle $t$ of the plane.
