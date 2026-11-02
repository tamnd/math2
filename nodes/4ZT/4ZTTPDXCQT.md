---
tag: 4ZTTPDXCQT
kind: definition
name: Affine differential geometry
msc: [53A15]
defines: K5C968HMSN
uses: [0FCHE902D7, 06JMR2XWXW]
sources:
  - url: https://en.wikipedia.org/wiki/Affine_differential_geometry
---

## Definition

Let $n \ge 1$.
The *equi-affine group* of $\R^{n+1}$ is the group of maps $x \mapsto Ax + b$ with $A$ in the [[general linear group|0FCHE902D7]] $GL(n+1, \R)$, $\det A = 1$ and $b \in \R^{n+1}$.
*Affine differential geometry* is the study of the properties of smooth curves and hypersurfaces in $\R^{n+1}$ that are invariant under the equi-affine group.

## Remarks

For a [[regular curve|06JMR2XWXW]] $\gamma \colon I \to \R^2$ with $\det(\gamma', \gamma'') > 0$, the *affine arc length* is
$$\sigma(t) = \int_{t_0}^{t} \det\big(\gamma'(u), \gamma''(u)\big)^{1/3} \, du.$$
It is invariant: if $\Phi(x) = Ax + b$ with $\det A = 1$, then $\det(A\gamma', A\gamma'') = \det(\gamma', \gamma'')$.
For the parabola $\gamma(t) = (t, t^2/2)$, one has $\gamma' = (1, t)$ and $\gamma'' = (0, 1)$, so the determinant is $1$ and the affine arc length from $0$ is $t$.

Euclidean arc length is not an affine invariant.
The shear $(x, y) \mapsto (x + y, y)$ has determinant $1$, and it maps the segment from $(0,0)$ to $(0,1)$, of length $1$, to the segment from $(0,0)$ to $(1,1)$, of length $\sqrt{2}$.

For a nondegenerate hypersurface, the basic invariants are the affine normal vector field and the induced Blaschke metric.
Some authors use the full affine group, with any invertible $A$; then volume is no longer preserved and the invariants change.

## Explanations

### L1 human

Affine differential geometry replaces the rigid motions of Euclidean geometry by the larger group of area- or volume-preserving affine maps.
It asks which features of a curved shape survive all of these maps.
