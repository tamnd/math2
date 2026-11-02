---
tag: RHKSMPBSQ1
kind: example
name: Poincaré half-plane model
msc: [51M10, 30F45]
instance_of: [GN4N94GQ0Z]
uses: [X6XGGH5FPW, Q61VFHCH2J, NSYMQMHPDN, 0SG74WBFA2]
sources:
  - url: https://en.wikipedia.org/wiki/Poincar%C3%A9_half-plane_model
same_as:
  wikidata: Q2534886
  wikipedia: Poincaré half-plane model
---

## Example

The *Poincaré half-plane model* is the [[upper half-plane|X6XGGH5FPW]] $\mathbb{H} = \set{(x, y) \in \R^2 : y > 0}$ with the [[Riemannian metric|Q61VFHCH2J]]
$$ds^2 = \frac{dx^2 + dy^2}{y^2}.$$
Its [[geodesics|NSYMQMHPDN]], the lines of the geometry, are the vertical half-lines and the semicircles centred on the $x$-axis.
The distance between $(x_1, y_1)$ and $(x_2, y_2)$ is given by
$$\cosh d = 1 + \frac{(x_2 - x_1)^2 + (y_2 - y_1)^2}{2 y_1 y_2}.$$

Check of the distance on the $y$-axis: the length of the segment from $(0, 1)$ to $(0, e)$ is $\int_1^e dy/y = 1$.
The formula gives $\cosh d = 1 + (e - 1)^2/(2e) = (e^2 + 1)/(2e) = \cosh 1$, so $d = 1$ as well.

Check of the hyperbolic parallel axiom: take the line $x = 0$ and the point $(1, 1)$.
The vertical line $x = 1$ does not meet it.
The semicircle centred at $(2, 0)$ through $(1, 1)$ has radius $\sqrt 2$, so it stays in $x \ge 2 - \sqrt 2 > 0$ and does not meet it either.
So $\mathbb{H}$ is a model of [[hyperbolic geometry|GN4N94GQ0Z]].

## Remarks

The metric has constant Gaussian curvature $-1$.
The orientation-preserving isometries are the [[Möbius transformations|0SG74WBFA2]] $z \mapsto (az + b)/(cz + d)$ with $a, b, c, d \in \R$ and $ad - bc = 1$, written with $z = x + iy$.
So the group of these isometries is $\mathrm{PSL}_2(\R)$.
The model is conformal: hyperbolic angles equal Euclidean angles.

## Explanations

### L1 human

The half-plane model draws the whole hyperbolic plane inside the region above a horizontal line.
Distances grow as you approach that line, so the line itself is infinitely far away.
The straight lines of the geometry look like vertical rays and half-circles standing on the boundary line.
