---
tag: PJWK0PKN6Q
kind: concept
name: Lie derivative
msc: [53A45, 58A10]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_derivative
same_as:
  wikidata: Q579267
  wikipedia: Lie derivative
---

## Summary

The Lie derivative measures how a [[tensor field|WX302T93TW]] changes along the flow of a vector field $X$.
It is defined without any extra structure such as a metric or a connection.
On functions it is the directional derivative, and on vector fields it is the [[Lie bracket|68FGQEBD6J]].
A tensor field is invariant under the flow of $X$ exactly when its Lie derivative along $X$ is zero.

## Explanations

### L1 human

Imagine a fluid flowing on a surface, and some quantity painted on the surface, such as a field of arrows.
Carry the painted field back along the flow for a short time and compare it with the field that is already there.
The rate of change of this comparison is the Lie derivative.
For the rotation field $X = -y \, \partial_x + x \, \partial_y$ in the plane and the function $f = x^2 + y^2$, one gets $X f = 0$.
This says that $f$ does not change under rotations about the origin.
