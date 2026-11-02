---
tag: EQ5JSYGWG2
kind: example
name: Helicoid
msc: [53A10]
instance_of: [41X0YW2R9N]
sources:
  - url: https://en.wikipedia.org/wiki/Helicoid
---

## Example

Fix $c > 0$.
For $u \in \R$ and $v \in \R$, let
$$x(u, v) = (v \cos u, \; v \sin u, \; c u).$$
Its image, the helicoid, is swept out by a horizontal line that turns about the $z$-axis at a constant rate while it moves up.
It is a [[minimal surface|41X0YW2R9N]].

Check.
The partial derivatives are $x_u = (-v \sin u, v \cos u, c)$ and $x_v = (\cos u, \sin u, 0)$.
So $E = v^2 + c^2$, $F = 0$ and $G = 1$.
The cross product is $x_u \times x_v = (-c \sin u, c \cos u, -v)$, with length $W = \sqrt{v^2 + c^2}$, and $N = (x_u \times x_v)/W$.
The second derivatives are $x_{uu} = (-v \cos u, -v \sin u, 0)$, $x_{uv} = (-\sin u, \cos u, 0)$ and $x_{vv} = 0$.
So the coefficients of the [[second fundamental form|9KHQR16P1B]] are $e = 0$, $f = c/W$ and $g = 0$.
The [[mean curvature|PA78NFEPCF]] is $H = \dfrac{eG - 2fF + gE}{2(EG - F^2)} = 0$.

## Remarks

The Gaussian curvature is $K = -f^2/(EG) = -c^2/(v^2 + c^2)^2$.
The helicoid is a ruled surface, and together with the plane it is the only ruled minimal surface in $\R^3$.
It is locally isometric to the [[catenoid|6NN1HP54GB]].

## Explanations

### L1 human

Picture a spiral staircase whose steps are thin lines that extend to infinity on both sides of the central pole.
That surface is a helicoid.
The points at a fixed distance from the pole trace out helices, and a soap film can take this shape.
