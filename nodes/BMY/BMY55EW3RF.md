---
tag: BMY55EW3RF
kind: concept
name: Submersion
msc: [57R35, 58A05]
sources:
  - url: https://en.wikipedia.org/wiki/Submersion_(mathematics)
same_as:
  wikidata: Q1420023
  wikipedia: Submersion (mathematics)
---

## Summary

A submersion is a smooth map between [[smooth manifolds|F45VQ47GPV]] whose [[differential|6P9PXQDSEN]] is surjective at every point.
Locally it looks like the projection of $\R^m$ onto $\R^n$.
Its fibres are smooth submanifolds, which makes submersions the basic way to cut a manifold into smooth pieces.
Projections of products and of fibre bundles are typical examples.

## Explanations

### L1 human

A submersion is a map that is locally a projection, like the shadow map $(x, y, z) \mapsto (x, y)$ that forgets the height.
Near each point it can move the point in every direction of the target.
Because of this, the set of points that land on a given value is a smooth piece of space, with no pinches.
For example, $f(x, y) = x^2 + y^2$ is a submersion from $\R^2 \setminus \set{0}$ to $(0, \infty)$, and its fibres are the circles around the origin.
