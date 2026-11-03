---
tag: T6N6M1BXCZ
kind: definition
name: Plane stress
msc: [74B05, 74K20]
defines: AS7WQTM99W
uses: [KG2XWEMJ30]
sources:
  - url: https://en.wikipedia.org/wiki/Plane_stress
---

## Definition

Let $\sigma$ be a [[Cauchy stress tensor|KG2XWEMJ30]] field on a region of $\R^3$, and let $e_1, e_2, e_3$ be an orthonormal basis.
The field $\sigma$ is in *plane stress* with respect to the plane spanned by $e_1, e_2$ if at every point
$$\sigma_{13} = \sigma_{23} = \sigma_{33} = 0.$$
Equivalently, $\sigma e_3 = 0$: the traction on every plane normal to $e_3$ vanishes.

## Remarks

Example: uniaxial tension $\sigma = s \, e_1 \otimes e_1$ is in plane stress, since its only nonzero component is $\sigma_{11}$.

Non-example: the hydrostatic stress $\sigma = -p I$ with $p \ne 0$ is not in plane stress for any plane, since $\sigma e_3 = -p e_3 \ne 0$ for every unit vector $e_3$.

In the usual two-dimensional theory one also assumes that $\sigma_{11}, \sigma_{12}, \sigma_{22}$ do not depend on $x_3$.
For an isotropic linear elastic material with Young's modulus $E$ and Poisson's ratio $\nu$, plane stress gives the out-of-plane strain $\varepsilon_{33} = -\frac{\nu}{E} (\sigma_{11} + \sigma_{22})$, which is not zero in general.
Plane stress is exact only in special cases; for thin plates loaded in their plane it is an approximation that improves as the thickness decreases.
