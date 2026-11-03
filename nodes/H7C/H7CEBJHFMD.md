---
tag: H7CEBJHFMD
kind: definition
name: Kirchhoff–Love plate theory
msc: [74K20, 74B05]
defines: 9E6E0SCEYA
uses: [782XMC21FH, T8ENJX1905, NWYZ9QBA84, AS7WQTM99W]
sources:
  - url: https://en.wikipedia.org/wiki/Kirchhoff–Love_plate_theory
---

## Definition

Let a plate occupy $\Omega \times (-h/2, h/2)$ with $\Omega \subset \R^2$.
Let it be made of an isotropic linear elastic material with [[Young's modulus|T8ENJX1905]] $E$ and [[Poisson's ratio|NWYZ9QBA84]] $\nu$.
Indices $\alpha, \beta$ run over $1, 2$, and repeated indices are summed.
*Kirchhoff–Love plate theory* is the [[plate theory|782XMC21FH]] with these assumptions.

1. The displacement is $u_\alpha(x, z) = u^0_\alpha(x) - z \, \partial_\alpha w(x)$ and $u_3(x, z) = w(x)$ for $x \in \Omega$ and $\abs{z} < h/2$.
2. The stress is in a state of [[plane stress|AS7WQTM99W]] parallel to the mid-plane.
3. The bending moments are $M_{\alpha\beta} = \int_{-h/2}^{h/2} z \, \sigma_{\alpha\beta} \, dz$, which gives
$$M_{\alpha\beta} = -D \left[ (1 - \nu) \, \partial_\alpha \partial_\beta w + \nu \, \delta_{\alpha\beta} \, \Delta w \right], \qquad D = \frac{E h^3}{12 (1 - \nu^2)}.$$
4. Under a transverse load $q$ per unit area, equilibrium reads $\partial_\alpha \partial_\beta M_{\alpha\beta} + q = 0$.

## Remarks

Clauses 3 and 4 give the [[biharmonic plate equation|X1SGK619VJ]] $D \Delta^2 w = q$, since $\partial_\alpha \partial_\beta \partial_\alpha \partial_\beta w = \Delta^2 w$.
Example: $w(x_1, x_2) = c\,(x_1^2 + x_2^2)$ gives $M_{11} = M_{22} = -2cD(1 + \nu)$ and $M_{12} = 0$, a state of uniform bending with $q = 0$.

Non-example: a displacement with $u_\alpha = -z \, \theta_\alpha$ where $\theta_\alpha \ne \partial_\alpha w$ violates clause 1, because the normals do not stay normal; it belongs to [[Mindlin–Reissner plate theory|M8F0SGSGQW]].

The transverse shear strains vanish under clause 1, yet the shear forces $Q_\alpha = \partial_\beta M_{\alpha\beta}$ are not zero; this inconsistency is harmless for thin plates.
At a free edge the theory can impose only two conditions, the vanishing of the normal moment and of the Kirchhoff effective shear force.
