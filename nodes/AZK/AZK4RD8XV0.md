---
tag: AZK4RD8XV0
kind: concept
name: Lifting property
msc: [18A32, 55U35]
sources:
  - url: https://en.wikipedia.org/wiki/Lifting_property
same_as:
  wikidata: Q30672450
  wikipedia: Lifting property
---

## Summary

A morphism $i$ has the left lifting property with respect to a morphism $p$ when every suitable commutative square has a diagonal filler.
The square has $i$ on its left side and $p$ on its right side.
Equivalently, $p$ has the right lifting property with respect to $i$.
Lifting properties define fibrations and cofibrations in homotopy theory and in model categories, and they describe many classes of maps by a single test.
When the filler is always unique, $i$ and $p$ are called orthogonal.

## Explanations

### L1 human

Picture a square of four maps: $u$ along the top, $v$ along the bottom, $i$ on the left and $p$ on the right, with the square commuting.
A lift is a diagonal map from the bottom left corner to the top right corner that keeps both triangles commuting.
In topology, the [[homotopy lifting property|G4QDM01P6J]] is of this kind: a homotopy in the base lifts to the total space once its start is lifted.
In sets, a surjection has the right lifting property with respect to the inclusion of the empty set into a point: every point of the target has a preimage.
