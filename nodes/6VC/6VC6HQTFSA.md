---
tag: 6VC6HQTFSA
kind: concept
name: Sheaf of differentials
msc: [14F10, 14F06]
sources:
  - url: https://en.wikipedia.org/wiki/Cotangent_sheaf
same_as:
  wikidata: Q19596510
  wikipedia: Cotangent sheaf
---

## Summary

The sheaf of relative differentials $\Omega_{X/Y}$ of a morphism of schemes $X \to Y$ is the sheaf version of the module of [[Kähler differentials|7HCFARHG7D]].
On an affine piece $\operatorname{Spec} B \to \operatorname{Spec} A$ it is given by the $B$-module $\Omega_{B/A}$.
For a smooth variety it is a vector bundle, the cotangent bundle, whose dual is the tangent bundle.
Its exterior powers give the sheaves of differential forms, and the top one is the [[canonical bundle|W05VYY4HBR]].

## Explanations

### L1 human

On a manifold, the cotangent bundle collects the differentials $df$ of functions at every point.
The sheaf of differentials does the same on a scheme, using only algebra: $d$ is linear and satisfies the product rule.
On the affine plane with coordinates $x, y$, every differential is $g \, dx + h \, dy$ with polynomial $g, h$.
On a curve defined by $f(x, y) = 0$, there is one extra relation $\partial_x f \, dx + \partial_y f \, dy = 0$.
At smooth points this leaves a module of rank one, the cotangent line of the curve.
