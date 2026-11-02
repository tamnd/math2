---
tag: CD6SMMZSW8
kind: concept
name: Holomorphically convex hull
msc: ["32E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Function_of_several_complex_variables
---

## Summary

Let $K$ be a compact subset of an open set $D \subseteq \C^n$.
Its holomorphically convex hull is the set of points of $D$ where no [[holomorphic function|507C34W0ZT]] on $D$ beats, in absolute value, its maximum on $K$.
It is the analogue of the convex hull, with holomorphic functions in place of linear functions.
Whether these hulls stay away from the boundary of $D$ decides whether $D$ is a domain of holomorphy.

## Explanations

### L1 human

The closed [[convex hull|0FQSDC2EQ2]] of a compact set consists of the points that every closed half-space containing the set also contains.
The holomorphic hull replaces half-spaces by the regions $\abs{f} \le c$ for holomorphic functions $f$.
For the unit circle in $\C$, the hull is the closed unit disc.
By the maximum principle, no holomorphic function on $\C$ can be larger inside the disc than on the circle.
If the origin is removed from the domain, the hull of the circle is just the circle, because the function $1/z$ is larger inside.
So the hull depends on the domain $D$ as well as on $K$.
