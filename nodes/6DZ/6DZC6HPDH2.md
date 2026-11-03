---
tag: 6DZC6HPDH2
kind: concept
name: Displacement thickness
msc: [76D10]
sources:
  - url: https://en.wikipedia.org/wiki/Boundary_layer_thickness
---

## Summary

The displacement thickness of a [[boundary layer|YCFPD0GE5G]] measures how far the slowed fluid near the wall pushes the outer flow away from the wall.
Move the wall into the flow until a frictionless flow carries the same mass flux as the real one; the displacement thickness is this distance.
The edge of the layer is vague, but the displacement thickness is a precise integral of the velocity profile.
It is used to correct inviscid calculations for the presence of the layer.

## Explanations

### L1 human

Near a wall the fluid moves slower than the main stream, so less fluid gets through than if the stream ran at full speed right up to the wall.
Imagine the wall were thicker and the stream ran at full speed up to the new wall.
The displacement thickness is the extra thickness that gives the same missing flow.
For a linear speed profile that rises from zero to full speed over a height $\delta$, it is $\delta / 2$.
