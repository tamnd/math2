---
tag: GSTG1NVYWW
kind: concept
name: Moreau envelope
msc: [90C25, 49J52, 52A41]
sources:
  - url: https://en.wikipedia.org/wiki/Moreau_envelope
same_as:
  wikidata: Q115978756
  wikipedia: Moreau envelope
---

## Summary

The Moreau envelope of a convex function is a smooth convex function that approximates it from below.
Its value at a point is the least value of the function plus a quadratic penalty for moving away from that point.
It has the same minimizers and minimum value as the original function, and its gradient is given by the [[proximal operator|E239APE78P]].
It was introduced by Jean-Jacques Moreau and is a basic tool of nonsmooth convex optimization.

## Explanations

### L1 human

Take a function with corners, such as the absolute value.
Roll a parabola-shaped smoothing over it: at each point, allow a short step to a lower value, paying a quadratic price for the distance moved.
The result has the corners rounded off but keeps the same lowest point.
For the absolute value one gets the Huber function, which is quadratic near $0$ and linear far away.
