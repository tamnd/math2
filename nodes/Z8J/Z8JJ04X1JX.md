---
tag: Z8JJ04X1JX
kind: statement
role: theorem
name: Synge's theorem
msc: [53C20, 53C21]
uses: [7CBT4SM83Y, 1X42JAA349, S1XK3HXHFX, 913WEQERBE, NSYMQMHPDN, ZB91TH6FKV, TVAGN3D6W5]
about: [1X42JAA349]
sources:
  - url: https://en.wikipedia.org/wiki/Synge%27s_theorem
same_as:
  wikidata: Q3527171
  wikipedia: Synge's theorem
---

## Statement

Let $(M, g)$ be a compact connected [[Riemannian manifold|7CBT4SM83Y]] of dimension $n$ with positive [[sectional curvature|1X42JAA349]].
Then:

1. If $n$ is even and $M$ is [[orientable|913WEQERBE]], then $M$ is simply connected.
2. If $n$ is odd, then $M$ is orientable.

## Remarks

The idea of the proof: if the conclusion fails, there is a nontrivial free homotopy class of loops along which parallel transport has the required orientation behaviour.
Compactness gives a closed [[geodesic|NSYMQMHPDN]] $\gamma$ of minimal length in this class.
A linear-algebra argument shows that [[parallel transport|TVAGN3D6W5]] once around $\gamma$ fixes a unit vector normal to $\gamma$.
Pushing $\gamma$ in the direction of this parallel field decreases length to second order, by the [[second variation formula|ZB91TH6FKV]] and positive curvature, which contradicts minimality.

Example: the real projective plane $\R P^2$ with the round metric has positive curvature, even dimension and fundamental group of order $2$.
It is not orientable, so this does not contradict part 1.
Its orientability hypothesis is therefore needed.
In odd dimensions, $\R P^3$ is orientable, as part 2 says, but it is not simply connected, so part 1 has no odd-dimensional analogue.

## Explanations

### L1 human

Positive curvature makes loops want to shrink.
Synge's theorem says that for compact spaces of even dimension, every loop can in fact be shrunk to a point, once one excludes the twisted, non-orientable cases.
In odd dimensions, it says the space cannot be twisted like a Möbius band.

### L2 human

Synge's theorem is one of the few known topological obstructions to positive sectional curvature.
For instance, it shows that $\R P^2 \times \R P^2$, whose orientable double cover is not simply connected, has no metric of positive curvature.
The proof is the model for later arguments that combine second variation with the holonomy of a closed geodesic, such as Weinstein's fixed point theorem.
