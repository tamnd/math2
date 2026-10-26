---
tag: ~cab8d11b
kind: definition
name: Surface integral
msc: [26B15]
defines: ~0c4c4dd7
uses: [~489b93d1, ~df346b27, ~282d16f3, ~97f7a8a9]
sources:
  - url: https://en.wikipedia.org/wiki/Surface_integral
    locator: Surface integrals of scalar fields
  - url: https://en.wikipedia.org/wiki/Surface_integral
    locator: Dependence on parametrization
---

## Definition

Let $r \colon D \to \mathbb{R}^3$ be a [[parametrised surface|~489b93d1]] as in the definition of [[surface area|~df346b27]], let $S = r(D)$, and let $f \colon S \to \mathbb{R}$ be continuous.
The surface integral of $f$ over $S$ is
$$\iint_S f \, dS = \iint_D f\big( r(u, v) \big) \, \| r_u(u, v) \times r_v(u, v) \| \, du \, dv.$$

## Remarks

The expression $dS = \| r_u \times r_v \| \, du \, dv$ is the surface element. With $f = 1$, the integral is the area of $S$.
The value does not depend on the parametrisation of $S$. For a surface made of several pieces, add the integrals over the pieces.
For the graph $z = g(x, y)$ over $D$, $\iint_S f \, dS = \iint_D f(x, y, g(x, y)) \sqrt{1 + g_x^2 + g_y^2} \, dx \, dy$.
Example: on the unit sphere $S$, symmetry gives $\iint_S x^2 \, dS = \iint_S y^2 \, dS = \iint_S z^2 \, dS$. These add up to the area $4\pi$, so $\iint_S z^2 \, dS = 4\pi / 3$.

## Explanations

### L1 human

A surface integral adds up the values of a function over a curved surface, each weighted by a small piece of area.
If $f$ is a mass density per unit area, the surface integral is the total mass of the surface.
