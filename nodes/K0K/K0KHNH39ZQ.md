---
tag: K0KHNH39ZQ
kind: definition
name: Maxwell's equations in curved spacetime
msc: [83C50, 35Q61, 78A25]
defines: 5BNCD886T7
uses: [H65N7N36K2, WRZJRJS44W, BY4QYYS788, 5FZDQQHQKM, CAZYGE1T4E, 0E3G0GRPZ6, 0ZHSTAG8ZY, 1Y4WX4XQWJ]
sources:
  - url: https://en.wikipedia.org/wiki/Maxwell%27s_equations_in_curved_spacetime
---

## Definition

Let $(M, g)$ be a four-dimensional [[Lorentzian manifold|BY4QYYS788]] with [[Levi-Civita connection|CAZYGE1T4E]] $\nabla$, and let $\mu_0 > 0$ be the vacuum permeability.
Let $J$ be a vector field on $M$, the four-current.
The unknown is a $2$-form $F$ on $M$, the [[electromagnetic tensor|WRZJRJS44W]].
*Maxwell's equations in curved spacetime* are, in local coordinates,
$$\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu, \qquad \partial_\lambda F_{\mu\nu} + \partial_\mu F_{\nu\lambda} + \partial_\nu F_{\lambda\mu} = 0,$$
where indices are raised with $g$ and $\nabla_\mu$ is the [[covariant derivative|5FZDQQHQKM]].

## Remarks

The second set says that $F$ is a closed [[differential form|0E3G0GRPZ6]], $dF = 0$, with $d$ the [[exterior derivative|0ZHSTAG8ZY]]; it does not involve the metric.
The first set can be written $d \star F = \mu_0 \star J^\flat$, up to a sign that depends on conventions.
Here $\star$ is the [[Hodge star|1Y4WX4XQWJ]] of $g$ and $J^\flat$ is the $1$-form dual to $J$.
In coordinates, $\nabla_\mu F^{\mu\nu} = \frac{1}{\sqrt{-\det g}} \partial_\mu \big( \sqrt{-\det g} \, F^{\mu\nu} \big)$, because $F$ is antisymmetric.
The same antisymmetry gives $\nabla_\nu J^\nu = 0$, conservation of charge on a curved background.

Example: on Minkowski space, where $g = \operatorname{diag}(1, -1, -1, -1)$ in inertial coordinates, the Christoffel symbols vanish and the equations reduce to the [[covariant formulation|H65N7N36K2]] of special relativity.

Non-example: on a Lorentzian manifold, the equation $\partial_\mu F^{\mu\nu} = \mu_0 J^\nu$ with plain partial derivatives is not the right law in general coordinates, since its left side is not a vector field.

When the metric itself is unknown and is coupled to $F$ through the electromagnetic stress–energy tensor, the system becomes the Einstein–Maxwell equations.
