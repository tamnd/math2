---
tag: W0B0BBAH35
kind: concept
name: Universally closed morphism
msc: [14A15]
sources:
  - url: https://en.wikipedia.org/wiki/Proper_morphism
---

## Summary

A morphism of schemes is universally closed if it stays a closed map of topological spaces after every base change.
Being closed alone is too weak a condition, because the product topology is not the Zariski topology of a fibre product.
Universal closedness is the topological half of the definition of a proper morphism.

## Explanations

### L1 human

A closed map sends closed sets to closed sets.
For schemes one asks more: the map must stay closed even after one adds extra parameters to the base.
The map from the affine line to a point is closed, since the image of anything is the point or empty.
After one adds a parameter, it becomes the projection of the plane to a line.
This projection sends the hyperbola $xy = 1$ onto the line with the origin removed, which is not closed.
So the affine line is not universally closed over a point, which reflects the missing point at infinity.
