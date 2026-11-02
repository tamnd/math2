---
tag: Q0GBCB9RA4
kind: example
name: SL(2,R)
msc: ["22E46", "22E15", "20G20"]
instance_of: [7JBRGCVJRB]
uses: [0V9PMN0RBH, X6XGGH5FPW, 0SG74WBFA2, 0CGYNDCWRR]
sources:
  - url: https://en.wikipedia.org/wiki/SL2(R)
same_as:
  wikidata: Q307169
  wikipedia: SL2(R)
---

## Example

The group $SL(2, \R)$ is the [[special linear group|0V9PMN0RBH]] of real $2 \times 2$ matrices with determinant $1$:
$$SL(2, \R) = \set{\begin{pmatrix} a & b \\ c & d \end{pmatrix} : a, b, c, d \in \R, \ ad - bc = 1}.$$
It is a closed subgroup of $GL_2(\R)$ cut out by one equation, so it is a [[Lie group|7JBRGCVJRB]] of dimension $3$.

It acts on the [[upper half-plane|X6XGGH5FPW]] $\mathbb{H} = \set{z \in \C : \operatorname{Im} z > 0}$ by [[Möbius transformations|0SG74WBFA2]]
$$z \mapsto \frac{az + b}{cz + d}.$$
Check that $\mathbb{H}$ is preserved: multiplying numerator and denominator by $c\bar{z} + d$ gives
$$\operatorname{Im} \frac{az + b}{cz + d} = \frac{(ad - bc) \operatorname{Im} z}{\abs{cz + d}^2} = \frac{\operatorname{Im} z}{\abs{cz + d}^2} > 0.$$

## Remarks

The matrices $I$ and $-I$ act as the identity map, and the quotient $PSL(2, \R) = SL(2, \R)/\set{\pm I}$ is the group of orientation-preserving isometries of the hyperbolic plane in the upper half-plane model.
$SL(2, \R)$ is connected but not compact.
Its maximal compact subgroup is the rotation group [[SO(2)|0CGYNDCWRR]], and $SL(2, \R)$ is homeomorphic to $SO(2) \times \R^2$.
So its fundamental group is $\Z$, and it is not simply connected.
Its universal cover is a Lie group with no faithful finite-dimensional representation.
An element $g \ne \pm I$ is called elliptic, parabolic or hyperbolic when $\abs{\tr g}$ is less than, equal to, or greater than $2$.
Its Lie algebra $\mathfrak{sl}(2, \R)$ of trace-zero real $2 \times 2$ matrices is simple, so $SL(2, \R)$ is a simple Lie group.

## Explanations

### L1 human

$SL(2, \R)$ is the group of linear maps of the plane that keep area and orientation.
Rotations, shears such as $\begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix}$, and squeezes such as $\begin{pmatrix} e^t & 0 \\ 0 & e^{-t} \end{pmatrix}$ all belong to it.
The same group also moves the points of the upper half-plane by fractional linear maps, and these are the symmetries of the hyperbolic plane.
It is among the smallest noncompact simple Lie groups, and its study is the entry point to the representation theory of such groups.
