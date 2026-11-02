---
tag: 2DC88BMQVX
kind: example
name: Horocycle flow
msc: [37D40, 37A17]
instance_of: [116TPXR5FS]
uses: [0V9PMN0RBH, X6XGGH5FPW, BTYF5Y5PFY, 5TKBSHY6VC]
sources:
  - url: https://en.wikipedia.org/wiki/Horocycle
---

## Example

Let $G = \mathrm{PSL}_2(\R)$, the quotient of the [[special linear group|0V9PMN0RBH]] $\mathrm{SL}_2(\R)$ by $\set{\pm I}$.
As in [[geodesic flow on a locally symmetric space|5TKBSHY6VC]], identify $G$ with the unit tangent bundle of the [[upper half-plane|X6XGGH5FPW]] $\mathbb{H}$.
Then the geodesic flow is $g \mapsto g a_t$, with $a_t$ the class of $\operatorname{diag}(e^{t/2}, e^{-t/2})$.
Let $h_s$ be the class of $\begin{pmatrix} 1 & s \\ 0 & 1 \end{pmatrix}$.
The (stable) horocycle flow is $\psi_s(g) = g h_s$, for $s \in \R$.
For a [[lattice|BTYF5Y5PFY]] $\Gamma \subseteq G$, it descends to $\Gamma \backslash G$, because left and right multiplications commute.

Check of the name and of the link with the geodesic flow.
A matrix computation gives $a_{-t} h_s a_t = h_{e^{-t} s}$.
Hence $g h_s a_t = g a_t h_{e^{-t}s}$, so the geodesic orbits of $g$ and of $g h_s$ approach each other as $t \to +\infty$.
So the orbits of $\psi$ are the stable leaves of the geodesic flow.
They project to horocycles in $\mathbb{H}$: circles tangent to the boundary, and horizontal lines.

## Remarks

When $\Gamma$ is cocompact, Hedlund proved that the horocycle flow on $\Gamma \backslash G$ is minimal: every orbit is dense.
Furstenberg proved that it is then uniquely ergodic, with the Haar measure as the only invariant probability measure.
The relation $a_{-t} h_s a_t = h_{e^{-t}s}$ shows that the geodesic flow renormalises the horocycle flow.
The horocycle flow has zero entropy, in contrast with the geodesic flow, which is an Anosov flow.

## Explanations

### L1 human

On the hyperbolic plane, a horocycle is a curve that looks like a circle of infinite radius, touching the boundary at one point.
The horocycle flow slides a unit vector along such a curve, keeping it perpendicular to the curve.
Two vectors on the same horocycle, when pushed forward along geodesics, come closer and closer.
On a closed hyperbolic surface every horocycle orbit spreads evenly over the whole space, which makes this flow a model of rigid, slowly mixing motion.
