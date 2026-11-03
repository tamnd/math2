---
tag: D18YD1WKVS
kind: definition
name: Rigid body
msc: ["70E15", 70B10]
defines: EZ9P9ERKNE
uses: [0C95TG69SG, 0CGYNDCWRR]
sources:
  - url: https://en.wikipedia.org/wiki/Rigid_body
---

## Definition

Let $B$ be a set of labels for material points, and let $I \subseteq \R$ be an interval of times.
Let a motion assign to each $X \in B$ and each $t \in I$ a position $x_X(t) \in \R^3$.
The system is a *rigid body* if, for all $X, Y \in B$, the [[Euclidean distance|0C95TG69SG]] $\abs{x_X(t) - x_Y(t)}$ does not depend on $t \in I$.

## Remarks

Suppose the motion is continuous in $t$ and the positions at a time $t_0 \in I$ do not all lie in one plane.
Then for each $t$ there are a unique $R(t)$ in the [[special orthogonal group|0CGYNDCWRR]] $SO(3)$ and a unique $b(t) \in \R^3$ with $x_X(t) = R(t)\, x_X(t_0) + b(t)$ for all $X \in B$.
So the configuration of a rigid body is a point of $SE(3)$, a space of dimension $6$.

Example: let $X$ range over the unit cube and let $R_z(t)$ be the rotation by the angle $t$ about the $x_3$-axis.
Then $x_X(t) = R_z(t)\, X + (0, 0, t)$ is a rigid body moving by a screw motion; the distances are kept because $R_z(t)$ is orthogonal.

Non-example: $x_X(t) = (1 + t) X$ for $t \ge 0$ is a uniform expansion; two points at distance $d$ at time $0$ are at distance $(1 + t) d$ at time $t$, so this is not a rigid body.
In continuum mechanics, a body is rigid when its deformation gradient is a rotation at every point and time.
