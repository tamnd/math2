---
tag: T8QBYVZ545
kind: definition
name: Mindlin–Reissner plate theory
msc: [74K20, 74B05]
defines: M8F0SGSGQW
uses: [782XMC21FH, T8ENJX1905, NWYZ9QBA84, J2GWW1NPTC]
sources:
  - url: https://en.wikipedia.org/wiki/Reissner–Mindlin_plate_theory
---

## Definition

Let a plate occupy $\Omega \times (-h/2, h/2)$ with $\Omega \subset \R^2$, made of an isotropic linear elastic material with [[Young's modulus|T8ENJX1905]] $E$, [[Poisson's ratio|NWYZ9QBA84]] $\nu$ and [[shear modulus|J2GWW1NPTC]] $G$.
Indices $\alpha, \beta, \gamma$ run over $1, 2$ and repeated indices are summed.
Let $D = Eh^3/(12(1 - \nu^2))$ and let $\kappa > 0$ be a shear correction factor.
*Mindlin–Reissner plate theory* is the [[plate theory|782XMC21FH]] with these assumptions, for the bending part.

1. The displacement is $u_\alpha(x, z) = -z \, \theta_\alpha(x)$ and $u_3(x, z) = w(x)$, with independent unknowns $w$, $\theta_1$, $\theta_2$ on $\Omega$.
2. The bending moments and transverse shear forces are
$$M_{\alpha\beta} = -D \left[ \tfrac{1 - \nu}{2} (\partial_\beta \theta_\alpha + \partial_\alpha \theta_\beta) + \nu \, \delta_{\alpha\beta} \, \partial_\gamma \theta_\gamma \right], \qquad Q_\alpha = \kappa G h \, (\partial_\alpha w - \theta_\alpha).$$
3. Under a transverse load $q$ per unit area the equilibrium equations are
$$\partial_\beta M_{\alpha\beta} - Q_\alpha = 0, \qquad \partial_\alpha Q_\alpha + q = 0.$$

## Remarks

Example: if $\theta_\alpha = \partial_\alpha w$ then $Q_\alpha$ in clause 2 is $0$, and the moments are those of Kirchhoff–Love theory.
Letting $\kappa G h \to \infty$ with $Q_\alpha$ fixed forces this, and clause 3 then gives $D \Delta^2 w = q$.

Non-example: a displacement with $u_\alpha$ quadratic in $z$, as in higher-order theories that capture warping of the normals, is not of the form of clause 1.

A common choice of the shear correction factor is $\kappa = 5/6$.
For very thin plates a naive finite element discretisation of this model locks, giving deflections that are far too small, and special elements are used to avoid this.
