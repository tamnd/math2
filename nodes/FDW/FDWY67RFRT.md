---
tag: FDWY67RFRT
kind: definition
name: Dynamical billiards
msc: ["37C83", "37A05", "37D40"]
defines: XWMKYE038F
uses: [0XPR1E85W0, 0TVJZYB6SH, 05D5EGMFYV, BBZP1R872N, B232EZ1FMB]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamical_billiards
---

## Definition

Let $Q \subset \R^2$ be a [[compact|0TVJZYB6SH]] connected set whose [[boundary|05D5EGMFYV]] $\partial Q$ is a finite union of smooth curves, called the table.
A *billiard trajectory* in $Q$ is a path $t \mapsto q(t)$ in $Q$ with the following properties:

1. Between two times at which $q(t) \in \partial Q$, the path is a straight segment run at unit speed.
2. At a time when $q(t)$ is a smooth point of $\partial Q$, the velocity after the collision is the mirror image of the velocity before it. The component tangent to $\partial Q$ is kept and the normal component changes sign.

The *billiard flow* is the flow on the unit tangent vectors $(q, v)$, $q \in Q$, $\abs{v} = 1$, that moves $(q, v)$ along its trajectory.
The *billiard map* acts on the pairs $(s, \theta)$.
Here $s$ is the arc-length parameter of a point of $\partial Q$, and $\theta \in (0, \pi)$ is the angle between an inward unit vector and the boundary.
The map sends $(s, \theta)$ to the next collision point and its outgoing angle.
These two [[dynamical systems|BBZP1R872N]] are called *dynamical billiards*.

## Remarks

Example: let $Q$ be the unit disc.
A chord leaving the circle at angle $\theta$ to the tangent subtends the arc $2\theta$ and meets the circle again at the same angle $\theta$.
So the billiard map is $(s, \theta) \mapsto (s + 2\theta \bmod 2\pi, \theta)$, and the angle is a conserved quantity.

Non-example: a trajectory that hits a corner of $\partial Q$, where the boundary has no tangent, is not continued by clause 2.
Such trajectories form a set of measure zero and are left out.

The billiard flow preserves the Liouville measure $dq \, dv$.
The billiard map preserves the [[invariant measure|B232EZ1FMB]] $\sin \theta \, ds \, d\theta$.
The same definitions make sense for tables in $\R^n$ and on Riemannian manifolds, such as the flat torus.
