---
tag: F0BJ2BHSZG
kind: statement
role: theorem
name: Fenchel's theorem
msc: [53A04]
uses: [QP9DY5K8QW, 7JQS6VKFEZ, 0D032NSZKY, 06JMR2XWXW, 0K06X9QXDX]
about: [QP9DY5K8QW]
sources:
  - url: https://en.wikipedia.org/wiki/Fenchel%27s_theorem
same_as:
  wikidata: Q5443004
  wikipedia: Fenchel's theorem
---

## Statement

Let $\gamma \colon [a, b] \to \R^3$ be a [[regular|06JMR2XWXW]] [[closed curve|0D032NSZKY]] of class $C^2$ whose derivatives up to order $2$ also agree at $a$ and $b$.
Then the [[total curvature|QP9DY5K8QW]] of $\gamma$ satisfies
$$\int_a^b \kappa(t) \, \norm{\gamma'(t)} \, dt \ge 2\pi.$$
Equality holds if and only if $\gamma$ is a simple closed curve that lies in a plane and bounds a [[convex|0K06X9QXDX]] region of that plane.

## Remarks

The unit tangent $T = \gamma' / \norm{\gamma'}$ is a closed curve on the unit sphere, and its length equals the total curvature.
For each unit vector $v$, the integral of $\ip{T}{v}$ over a period is $\ip{\gamma(b) - \gamma(a)}{v} = 0$.
So $T$ is not contained in any open hemisphere, and a closed curve on the sphere with this property has length at least $2\pi$.
Example: a circle has total curvature exactly $2\pi$, and an ellipse too, since both are plane convex curves.
A figure-eight curve in the plane has total curvature greater than $2\pi$, since it is not simple.
The theorem holds in the same form in $\R^n$ for each $n \ge 2$.
Werner Fenchel proved it in 1929.

## Explanations

### L1 human

Any closed loop in space must turn by at least one full turn in all.
Only flat convex loops, such as a circle or an ellipse, manage with exactly one full turn.
Every other loop wastes some turning.

### L2 human

The proof turns a statement about curves in space into a statement about curves on the sphere, through the tangent indicatrix $T$.
This trick, the Gauss map of a curve, is the one-dimensional model of the Gauss map of a surface.
The [[Fáry–Milnor theorem|B1Z1C8AHVD]] sharpens Fenchel's bound for knotted curves, from $2\pi$ to more than $4\pi$.
