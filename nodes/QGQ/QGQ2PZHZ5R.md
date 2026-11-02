---
tag: QGQ2PZHZ5R
kind: definition
name: Singular point of an algebraic variety
msc: [14B05, 14A10]
defines: D86X15A8WS
uses: [HV6YBS0YDH, E7A5DHFT01, 36X2WTHYCB, JERVQT4C12, 047NDTEPCV, 09EGC6F8PT, 63XXTF6B5M, MZ02BKPHJA]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_point_of_an_algebraic_variety
---

## Definition

Let $X$ be an [[algebraic variety|HV6YBS0YDH]] over an algebraically closed field $k$ and let $p \in X$.
The point $p$ is *nonsingular* (or smooth) if $\dim_k T_p X = \dim X$, where $T_p X$ is the [[Zariski tangent space|E7A5DHFT01]] and $\dim X$ is the [[dimension|36X2WTHYCB]] of $X$.
Otherwise $\dim_k T_p X > \dim X$, and $p$ is a *singular point* of $X$.
The variety $X$ is *nonsingular* if it has no singular point.

## Remarks

Jacobian criterion: let $X \subseteq k^n$ be an [[affine variety|JERVQT4C12]] of dimension $d$ with $I(X) = (f_1, \dots, f_r)$.
Then $p$ is nonsingular if and only if the [[Jacobian matrix|047NDTEPCV]] $\left(\frac{\partial f_j}{\partial x_i}(p)\right)$ has rank $n - d$.
Algebraic form: $p$ is nonsingular if and only if the [[local ring|MZ02BKPHJA]] of $X$ at $p$ is a [[regular local ring|63XXTF6B5M]].
The singular points of $X$ form a closed subset different from $X$.

Example: for $X = V(f) \subseteq k^2$ with $f = y^2 - x^2(x + 1)$, a curve of dimension $1$, the [[partial derivatives|09EGC6F8PT]] are $\partial f / \partial x = -3x^2 - 2x$ and $\partial f / \partial y = 2y$.
Assume $\operatorname{char} k \ne 2$.
Both vanish together with $f$ only at $(0, 0)$, so the origin is the only singular point.

Non-example: on the circle $V(x^2 + y^2 - 1)$ with $\operatorname{char} k \ne 2$, the gradient $(2x, 2y)$ vanishes only at $(0, 0)$, which is not on the circle, so the circle has no singular point.
