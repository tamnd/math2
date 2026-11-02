---
tag: 7Z3VD04JGX
kind: definition
name: Zonoid
msc: [52A21, 52A20]
defines: ZMZZ2QRFTZ
uses: [437FSG3419, Z5SA6A67KF, F79WYYC07C, 1H92CYA4ZC]
sources:
  - url: https://en.wikipedia.org/wiki/Zonoid
---

## Definition

Let $n \ge 1$.
A *zonoid* in $\R^n$ is a [[convex body|437FSG3419]] $Z$ that is the limit of a sequence of [[zonotopes|Z5SA6A67KF]] in $\R^n$.
The limit is taken in the [[Hausdorff distance|F79WYYC07C]].
Here a zonotope is a Minkowski sum $[a_1, b_1] + \cdots + [a_m, b_m]$ of finitely many closed segments.

## Remarks

Equivalently, the [[support function|1H92CYA4ZC]] of $Z$ has the form $h_Z(x) = x \cdot a + \int_{S^{n-1}} \abs{x \cdot v} \, d\mu(v)$.
Here $a \in \R^n$, and $\mu$ is a finite even Borel measure on the unit sphere $S^{n-1}$.
Example: the closed unit ball $B$ of $\R^n$ is a zonoid.
Its support function is $h_B(x) = \abs{x}$, and by rotation invariance $\int_{S^{n-1}} \abs{x \cdot v} \, d\sigma(v) = c_n \abs{x}$ for the normalized surface measure $\sigma$ and a constant $c_n > 0$, so $\mu = \sigma / c_n$ works with $a = 0$.
Non-example: a triangle in $\R^2$ is not a zonoid.
Each zonotope is symmetric about a point, this property passes to Hausdorff limits, and a triangle has no centre of symmetry.
In $\R^2$ every convex body with a centre of symmetry is a zonoid; in $\R^3$ the regular octahedron is a centrally symmetric convex body that is not a zonoid.
Some authors also call lower-dimensional Hausdorff limits of zonotopes, such as single segments, zonoids; here a zonoid is required to have nonempty interior, like every convex body.
