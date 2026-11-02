---
tag: 5XVEF5DKAG
kind: concept
name: Inverse mean curvature flow
msc: ["53E10", "53C21"]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_mean_curvature_flow
same_as:
  wikidata: Q6060395
  wikipedia: Inverse mean curvature flow
---

## Summary

Inverse mean curvature flow is a geometric evolution of hypersurfaces.
Each point moves outward along the unit normal, with speed equal to the reciprocal of the [[mean curvature|PA78NFEPCF]].
It needs a hypersurface with positive mean curvature.
Under this flow the area of the hypersurface grows exponentially in time.
Huisken and Ilmanen used a weak form of this flow to prove the Riemannian Penrose inequality for a connected horizon.

## Explanations

### L1 human

Think of a closed surface that expands outward.
Where the surface is strongly curved it moves slowly, and where it is nearly flat it moves fast.
This is the opposite of mean curvature flow, where curved parts move fastest and the surface shrinks.
A round sphere of radius $r$ in $\R^3$ has mean curvature $2/r$ (with $H$ the sum of the principal curvatures), so it expands with speed $r/2$.
Its radius is then $r_0 e^{t/2}$ at time $t$, and its area is $e^t$ times the initial area.
