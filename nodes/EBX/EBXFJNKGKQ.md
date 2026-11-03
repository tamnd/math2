---
tag: EBXFJNKGKQ
kind: definition
name: Torque
msc: [70C20, 70A05]
defines: 9636MFFSGC
uses: [0SEDGXG9S3]
sources:
  - url: https://en.wikipedia.org/wiki/Torque
---

## Definition

Let a force $F \in \R^3$ act at a point with position $p \in \R^3$, and let $O \in \R^3$ be a reference point.
The *torque*, or *moment*, of $F$ about $O$ is
$$\tau_O = (p - O) \times F,$$
where $\times$ is the [[cross product|0SEDGXG9S3]].
For forces $F_1, \dots, F_k$ acting at points $p_1, \dots, p_k$, the total torque about $O$ is $\sum_{i=1}^{k} (p_i - O) \times F_i$.

## Remarks

The size of the torque is $\abs{\tau_O} = \abs{p - O}\, \abs{F} \sin\varphi$, where $\varphi$ is the angle between $p - O$ and $F$.
Its direction is the axis of the turning it tends to cause, by the right-hand rule.

Example: $O = 0$, $p = (0.8, 0, 0)$ and $F = (0, 10, 0)$ give $\tau_O = (0, 0, 8)$, a turning about the vertical axis.

Non-example: a force along the line through $O$ and $p$, such as $F = (-10, 0, 0)$ above, has zero torque about $O$, although it is not zero.
Changing the reference point gives $\tau_{O'} = \tau_O + (O - O') \times \sum_i F_i$, so the total torque does not depend on the reference point when the total force is zero.
