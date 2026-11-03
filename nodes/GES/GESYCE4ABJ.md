---
tag: GESYCE4ABJ
kind: statement
role: corollary
name: Theorema Egregium and the impossibility of a distortion-free map
msc: [53A05, 86A30]
uses: [YKSA8SJ81V, SQVQ5DQT6W, P9CM4GQ2T0, R9YWQS15AA, Y2C8D9VC7D]
about: [Y2C8D9VC7D, YKSA8SJ81V]
sources:
  - url: https://en.wikipedia.org/wiki/Theorema_Egregium
---

## Statement

Let $S$ be a [[sphere|P9CM4GQ2T0]] of radius $R > 0$ in $\R^3$, and let $U \subseteq S$ be a nonempty open set.
Then there is no smooth map $P \colon U \to \R^2$ that is a [[local isometry|R9YWQS15AA]].
In particular, no [[map projection|Y2C8D9VC7D]] of $U$ preserves the lengths of all curves in $U$.

## Remarks

The [[Gaussian curvature|SQVQ5DQT6W]] of $S$ is $1/R^2$ at every point, and that of the plane is $0$.
By the [[Theorema Egregium|YKSA8SJ81V]], a local isometry preserves Gaussian curvature, so it would give $1/R^2 = 0$, a contradiction.
The same argument works for any open piece of an ellipsoid, whose Gaussian curvature is positive everywhere.
The hypothesis of positive curvature is needed: a cylinder has curvature $0$, and the map $(\cos u, \sin u, v) \mapsto (u, v)$ for $0 < u < 2\pi$ is a local isometry onto a plane strip.
So a cylinder can be unrolled without distortion, but no part of a sphere can be flattened that way.

## Explanations

### L1 human

Every flat map of the Earth, however small the region, distorts some distances.
The reason is that the sphere is curved in a way that can be detected from inside it, by measuring lengths and angles.
For example, a triangle on a sphere has angle sum larger than $180^\circ$, while a flat triangle has exactly $180^\circ$.
A map that kept all lengths would also keep angle sums, which is impossible.

### L2 human

This is why map makers must choose which property to keep.
A projection can be conformal, like the [[Mercator projection|DRQJ0R4HJQ]], or equal-area, but not isometric.
The local distortion that each projection must have is measured by [[Tissot's indicatrix|RCMYJPDMGJ]].
For small regions the distortion is small, which is why city maps look accurate.
