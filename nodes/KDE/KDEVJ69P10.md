---
tag: KDEVJ69P10
kind: example
name: Cubic surface
msc: [14J26, 14J70]
instance_of: [AV2ZAAZXN9]
uses: [AV2ZAAZXN9, ZT9A6JK8QF, RYB6F7JFGV, VQK5HQFYEM]
sources:
  - url: https://en.wikipedia.org/wiki/Cubic_surface
same_as:
  wikidata: Q3505260
  wikipedia: Cubic surface
---

## Example

A *cubic surface* is the zero set in [[projective space|ZT9A6JK8QF]] $\mathbb{P}^3$ of a homogeneous polynomial of degree $3$ in four variables.
A concrete smooth one is the Fermat cubic over $\C$,
$$X = \set{[x : y : z : w] \in \mathbb{P}^3 : x^3 + y^3 + z^3 + w^3 = 0}.$$
It is smooth: the partial derivatives $3x^2, 3y^2, 3z^2, 3w^2$ vanish together only at $x = y = z = w = 0$, which is not a point of $\mathbb{P}^3$.
By the [[adjunction formula|RYB6F7JFGV]], a smooth surface of degree $3$ in $\mathbb{P}^3$ has canonical divisor $K_X = (3 - 4) H = -H$, where $H$ is a plane section.
So $-K_X = H$ is ample, and $X$ is a [[del Pezzo surface|AV2ZAAZXN9]] of degree $K_X^2 = H^2 = 3$.

## Remarks

The Fermat cubic contains the line $\set{x = -y, \ z = -w}$, since then $x^3 + y^3 = 0$ and $z^3 + w^3 = 0$.
More generally, for cube roots of unity $\zeta, \zeta'$ the lines $\set{x = -\zeta y, \ z = -\zeta' w}$ lie on $X$, which gives $9$ lines.
The other two ways of pairing the four variables give $9$ more each.
So there are $27$ lines in all, as the [[twenty-seven lines theorem|VQK5HQFYEM]] predicts.
Every smooth cubic surface over an algebraically closed field is the blow-up of $\mathbb{P}^2$ at six points in general position, so it is a rational surface.
The Clebsch surface, given by $\sum x_i = 0$ and $\sum x_i^3 = 0$ in $\mathbb{P}^4$, is a smooth cubic surface on which all $27$ lines are defined over $\R$.

## Explanations

### L1 human

A cubic surface is the set of solutions of one cubic equation in four homogeneous coordinates.
The Fermat cubic $x^3 + y^3 + z^3 + w^3 = 0$ is the most symmetric example.
It is smooth, it can be parametrized by the plane, and it contains exactly $27$ straight lines, which can be written down by hand.
