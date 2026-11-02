---
tag: ED3DAZVQZ4
kind: example
name: Simons cone
msc: [49Q05, 53A10, 49Q15]
illustrates: [XVSVNP3K9G, NP948D6FR0]
uses: [7TPBQPPN97, PA78NFEPCF, 41X0YW2R9N]
sources:
  - url: https://en.wikipedia.org/wiki/Simons_cone
same_as:
  wikidata: Q133933787
  wikipedia: Simons cone
---

## Example

Write points of $\R^8$ as $(x, y)$ with $x, y \in \R^4$.
The *Simons cone* is the hypersurface
$$C = \set{(x, y) \in \R^4 \times \R^4 : \abs{x} = \abs{y}}.$$
It is a [[cone|7TPBQPPN97]]: if $(x, y) \in C$ and $t > 0$, then $(tx, ty) \in C$.
It is smooth away from the origin, and the origin is its only singular point.

Check that $C \setminus \set{0}$ is a [[minimal surface|41X0YW2R9N]], that is, has [[mean curvature|PA78NFEPCF]] zero.
The cone is the zero set of $u(x, y) = \abs{x}^2 - \abs{y}^2$, and $\nabla u = 2(x, -y)$ vanishes only at the origin.
The unit normal is $\nu = (x, -y)/r$ with $r = \sqrt{\abs{x}^2 + \abs{y}^2}$, and the mean curvature is, up to a constant factor, $\operatorname{div} \nu$.
Since $\operatorname{div}(x, -y) = 4 - 4 = 0$ and $(x, -y) \cdot \nabla (1/r) = -(\abs{x}^2 - \abs{y}^2)/r^3$, one gets $\operatorname{div} \nu = -(\abs{x}^2 - \abs{y}^2)/r^3$, which is $0$ on $C$.

## Remarks

The intersection of $C$ with the unit sphere $S^7$ is the product $S^3(1/\sqrt{2}) \times S^3(1/\sqrt{2})$ of two $3$-spheres of radius $1/\sqrt{2}$, a minimal hypersurface of $S^7$.
James Simons showed in 1968 that $C$ is stable, that is, the second variation of area is nonnegative.
Bombieri, De Giorgi and Giusti proved in 1969 that $C$ is in fact area-minimizing: the region $\set{\abs{x} < \abs{y}}$ minimizes perimeter among all sets that agree with it outside a ball.
So area-minimizing hypersurfaces in $\R^8$ can have isolated singular points, and the dimension bound for the singular set of such hypersurfaces is sharp.
The analogous cones $\set{\abs{x} = \abs{y}}$ with $x, y \in \R^k$ for $k \le 3$ are not area-minimizing.
The cone is the reason why the answer to [[Bernstein's problem|NP948D6FR0]] changes at dimension $8$.

## Explanations

### L1 human

Take two copies of four-dimensional space and look at the points where the distance from the origin in the first copy equals the distance in the second.
This set is a cone in eight dimensions, with its tip at the origin.
It balances its own surface tension perfectly away from the tip, like a soap film.
Surprisingly, it is even the least-area surface with its boundary, so least-area surfaces in eight dimensions can have a sharp point.
