---
tag: 6NN1HP54GB
kind: example
name: Catenoid
msc: [53A10]
instance_of: [41X0YW2R9N]
sources:
  - url: https://en.wikipedia.org/wiki/Catenoid
---

## Example

For $u \in \R$ and $v \in \R$, let
$$x(u, v) = (\cosh v \cos u, \; \cosh v \sin u, \; v).$$
Its image, the catenoid, is the [[surface of revolution|NE09EDK19V]] obtained by rotating the catenary $r = \cosh z$ about the $z$-axis.
It is a [[minimal surface|41X0YW2R9N]].

Check.
The partial derivatives are $x_u = (-\cosh v \sin u, \cosh v \cos u, 0)$ and $x_v = (\sinh v \cos u, \sinh v \sin u, 1)$.
So $E = \cosh^2 v$, $F = 0$ and $G = \sinh^2 v + 1 = \cosh^2 v$, and the parametrization is conformal.
For a conformal parametrization, $x_{uu} + x_{vv} = 2 E H N$, where $H$ is the mean curvature and $N$ the unit normal.
Here $x_{uu} = (-\cosh v \cos u, -\cosh v \sin u, 0)$ and $x_{vv} = (\cosh v \cos u, \cosh v \sin u, 0)$, so $x_{uu} + x_{vv} = 0$ and $H = 0$.

## Remarks

The principal curvatures are $\pm 1/\cosh^2 v$, and the Gaussian curvature is $K = -1/\cosh^4 v$.
Apart from pieces of planes, the catenoids are the only minimal surfaces of revolution.
The catenoid is locally isometric to the [[helicoid|EQ5JSYGWG2]], and one can be bent into the other through a family of minimal surfaces.

## Explanations

### L1 human

Dip two parallel circular rings into soapy water and pull them a little apart.
The soap film between them forms a tube with a narrow waist: that is a catenoid.
Its profile is the catenary, the curve of a hanging chain.
