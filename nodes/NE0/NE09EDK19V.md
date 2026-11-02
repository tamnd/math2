---
tag: NE09EDK19V
kind: example
name: Surface of revolution
msc: [53A05]
instance_of: [6080X3FAD4]
sources:
  - url: https://en.wikipedia.org/wiki/Surface_of_revolution
---

## Example

Let $s \mapsto (r(s), z(s))$, for $s$ in an open interval $I$, be a smooth regular curve in the $xz$-plane.
Assume that it is parametrized by [[arc length|0TH78S7GBZ]] and that $r(s) > 0$ for all $s$.
Rotating it about the $z$-axis gives the surface of revolution
$$x(s, \theta) = (r(s) \cos\theta, \; r(s) \sin\theta, \; z(s)), \qquad s \in I, \ \theta \in \R.$$
The partial derivatives are $x_s = (r' \cos\theta, r' \sin\theta, z')$ and $x_\theta = (-r \sin\theta, r \cos\theta, 0)$.
They are orthogonal, $\abs{x_s} = 1$ because $r'^2 + z'^2 = 1$, and $\abs{x_\theta} = r > 0$.
So $x$ is an immersion, and if the profile curve is a homeomorphism onto its image then the image of $x$ is a [[regular surface|6080X3FAD4]].
The [[first fundamental form|MAJ3DH7MZS]] is $ds^2 + r(s)^2 \, d\theta^2$.
The meridians ($\theta$ constant) and the parallels ($s$ constant) are lines of curvature, and the [[Gaussian curvature|SQVQ5DQT6W]] is
$$K = -\frac{r''(s)}{r(s)}.$$

## Remarks

For $r(s) = \cos s$ and $z(s) = \sin s$ with $s \in (-\pi/2, \pi/2)$, one gets the unit sphere without its poles, and $K = \cos s / \cos s = 1$.
Rotating a circle that does not meet the axis gives a torus.
Rotating a catenary gives the [[catenoid|6NN1HP54GB]], and rotating a tractrix gives the [[pseudosphere|44WEBQSKEY]].

## Explanations

### L1 human

Take a curve drawn in a half-plane and spin it around the edge line of the half-plane.
It sweeps out a surface, like a vase on a potter's wheel.
Spheres, cylinders, cones and doughnuts all arise this way.
Because of the symmetry, the curvature of such a surface depends only on the profile curve.
