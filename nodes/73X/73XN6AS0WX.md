---
tag: 73XN6AS0WX
kind: example
name: Enneper surface
msc: [53A10]
instance_of: [41X0YW2R9N]
sources:
  - url: https://en.wikipedia.org/wiki/Enneper_surface
---

## Example

For $(u, v) \in \R^2$, let
$$x(u, v) = \left(u - \frac{u^3}{3} + u v^2, \; -v + \frac{v^3}{3} - u^2 v, \; u^2 - v^2\right).$$
Its image is the Enneper surface.
It is a [[minimal surface|41X0YW2R9N]].

Check.
The partial derivatives are $x_u = (1 - u^2 + v^2, \, -2uv, \, 2u)$ and $x_v = (2uv, \, -1 + v^2 - u^2, \, -2v)$.
A direct computation gives $E = G = (1 + u^2 + v^2)^2$ and $F = 0$, so $x$ is a conformal immersion.
The second derivatives are $x_{uu} = (-2u, -2v, 2)$ and $x_{vv} = (2u, 2v, -2)$, so $x_{uu} + x_{vv} = 0$.
For a conformal parametrization this means that the [[mean curvature|PA78NFEPCF]] vanishes.

## Remarks

In the [[Weierstrass–Enneper parameterization|YWV6J23AP6]], this surface has data $f = 2$ and $g(z) = z$ on $\C$, with $z = u + iv$.
The surface is complete, but it is not embedded: it intersects itself.
Its Gauss map is the inverse stereographic projection of $g(z) = z$, which covers the sphere once except for one point, so its total curvature is $-4\pi$.

## Explanations

### L1 human

Near the origin the Enneper surface looks like a saddle.
Farther out its edges fold over and pass through each other.
It is one of the simplest minimal surfaces after the plane, the catenoid and the helicoid, and its formula is just a polynomial.
