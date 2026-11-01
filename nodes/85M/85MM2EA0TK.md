---
tag: 85MM2EA0TK
kind: object
name: Poincaré disk model
msc: [51M10, 30F45]
instance_of: [0VKD1TP7F3]
sources:
  - url: https://en.wikipedia.org/wiki/Poincar%C3%A9_disk_model
same_as:
  wikidata: Q2617832
  wikipedia: Poincaré disk model
---

## Description

The *Poincaré disk model* of the hyperbolic plane is the [[unit disc|8G5ABXRK85]] $\mathbb{D} = \set{z \in \C : \abs{z} < 1}$ with the Riemannian metric
$$ds = \frac{2\, \abs{dz}}{1 - \abs{z}^2}.$$
The distance between two points is the infimum of the lengths of piecewise smooth curves joining them, which makes $\mathbb{D}$ a [[metric space|0VKD1TP7F3]].
The distance from $0$ to $z$ is
$$d(0, z) = \int_0^{\abs{z}} \frac{2\, dt}{1 - t^2} = \log\frac{1 + \abs{z}}{1 - \abs{z}},$$
attained along the radius, so points near the boundary circle are infinitely far from $0$.
In general, $d(z, w) = 2 \operatorname{artanh} \abs{\dfrac{z - w}{1 - \bar w z}}$.

## Remarks

The metric has constant Gaussian curvature $-1$.
The geodesics are the diameters of $\mathbb{D}$ and the arcs of circles that meet the unit circle at right angles.
The orientation-preserving isometries are the [[Möbius transformations|0SG74WBFA2]] $z \mapsto e^{i\theta}(z - a)/(1 - \bar a z)$ with $\abs{a} < 1$, which are the conformal automorphisms of $\mathbb{D}$.
The model is conformal: hyperbolic angles equal Euclidean angles.
The [[Schwarz–Pick theorem|V1QYA9RW73]] says that every holomorphic self-map of $\mathbb{D}$ does not increase this distance.
The Cayley map $z \mapsto (z - i)/(z + i)$ is an isometry from the Poincaré half-plane model onto the disk model.

## Explanations

### L1 human

The Poincaré disk is a picture of a geometry where the parallel postulate fails.
The whole infinite hyperbolic plane is squeezed into a round disc, and distances grow without bound toward the rim.
Straight lines of this geometry appear as diameters or as circular arcs that hit the rim at right angles.
Through a point off such a line there are infinitely many lines that never meet it.
M. C. Escher's Circle Limit prints show tilings of this disc by congruent figures that look smaller and smaller toward the edge.
