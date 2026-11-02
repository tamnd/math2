---
tag: EMVDSQJM8S
kind: definition
name: Total curvature
msc: [53A04]
defines: QP9DY5K8QW
uses: [7JQS6VKFEZ, 06JMR2XWXW, 0D032NSZKY]
sources:
  - url: https://en.wikipedia.org/wiki/Total_curvature
---

## Definition

Let $\gamma \colon [a, b] \to \R^n$ be a [[regular|06JMR2XWXW]] curve of class $C^2$ with [[curvature|7JQS6VKFEZ]] $\kappa$.
The *total curvature* of $\gamma$ is
$$\int_a^b \kappa(t) \, \norm{\gamma'(t)} \, dt,$$
that is, the integral of $\kappa$ with respect to arc length.
For a plane curve with signed curvature $k$, the *total signed curvature* is $\int_a^b k(t) \, \norm{\gamma'(t)} \, dt$.

## Remarks

Example: the circle $\gamma(t) = (r \cos t, r \sin t)$, $t \in [0, 2\pi]$, has $\kappa = 1/r$ and $\norm{\gamma'} = r$, so its total curvature is $2\pi$.
Non-example: the boundary of a square is a [[closed curve|0D032NSZKY]] that is not of class $C^2$, so the definition does not apply.
For convex polygons one uses instead the sum of the exterior angles, which is again $2\pi$.
The total curvature does not change under a regular reparametrisation or a rigid motion.
For a closed regular plane curve, the total signed curvature equals $2\pi$ times the turning number of the curve.
