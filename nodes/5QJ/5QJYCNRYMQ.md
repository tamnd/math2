---
tag: 5QJYCNRYMQ
kind: concept
name: Bilinear interpolation
msc: [65D05, 41A05]
specializes: [BM703GV34G]
sources:
  - url: https://en.wikipedia.org/wiki/Bilinear_interpolation
same_as:
  wikidata: Q612143
  wikipedia: Bilinear interpolation
---

## Summary

Bilinear interpolation estimates a function of two variables inside a rectangle from its values at the four corners.
It uses the unique function of the form $a + bx + cy + dxy$ that matches the four values.
It is the two-dimensional analogue of linear interpolation and a basic tool for resampling images and gridded data.

## Explanations

### L1 human

Suppose the temperature is known at the four corners of a rectangular field.
To estimate it at a point inside, first interpolate linearly along the bottom edge and along the top edge, and then interpolate linearly between those two results.
Doing it in the other order, first along the vertical edges, gives the same answer.
For example, on the unit square with corner values $0$, $0$, $0$ and $1$ (the last at $(1, 1)$), the estimate at $(x, y)$ is $xy$, so the center gets $1/4$.
