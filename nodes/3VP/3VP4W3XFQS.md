---
tag: 3VP4W3XFQS
kind: definition
name: Couple
msc: [70C20]
defines: 4KSPEPZWP2
uses: [9636MFFSGC, 0SEDGXG9S3]
sources:
  - url: https://en.wikipedia.org/wiki/Couple_(mechanics)
---

## Definition

Let $F \in \R^3$ be nonzero, and let $p_1, p_2 \in \R^3$ be points such that $p_1 - p_2$ is not parallel to $F$.
The pair of forces $F$ acting at $p_1$ and $-F$ acting at $p_2$ is a *couple*.
Its *moment* is the vector
$$M = (p_1 - p_2) \times F,$$
where $\times$ is the [[cross product|0SEDGXG9S3]].

## Remarks

For every reference point $O$, the total [[torque|9636MFFSGC]] of the pair is $(p_1 - O) \times F + (p_2 - O) \times (-F) = M$, so the moment does not depend on $O$.
Its size is $\abs{F} d$, where $d$ is the distance between the two lines of action.

Example: $F = (0, 5, 0)$ at $p_1 = (0.2, 0, 0)$ and $-F$ at $p_2 = (-0.2, 0, 0)$ form a couple with moment $(0.4, 0, 0) \times (0, 5, 0) = (0, 0, 2)$.

Non-example: if $p_1 - p_2$ is parallel to $F$, the two forces act along the same line, and their moment is $0$; they cancel completely and do not form a couple.
Two couples with the same moment have the same effect on a rigid body, so a couple is often identified with its moment, a free vector.
