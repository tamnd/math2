---
tag: P1G0M3S8QV
kind: concept
name: Bicubic interpolation
msc: [65D05, 65D07, 41A05]
specializes: [BM703GV34G]
sources:
  - url: https://en.wikipedia.org/wiki/Bicubic_interpolation
same_as:
  wikidata: Q611705
  wikipedia: Bicubic interpolation
---

## Summary

Bicubic interpolation builds a smooth surface over a rectangular grid from values and derivatives at the grid points.
On each cell it uses a polynomial $\sum_{i,j=0}^{3} a_{ij} x^i y^j$, fixed by the values, the two first partial derivatives and the mixed derivative at the four corners.
The patches join with continuous first derivatives, giving smoother results than [[bilinear interpolation|5QJYCNRYMQ]], which is why it is common in image resampling.

## Explanations

### L1 human

Bilinear interpolation produces visible creases along grid lines because its slopes jump there.
Bicubic interpolation also matches slopes at the grid points, so neighboring patches meet smoothly.
Each patch is a cubic in each direction, with sixteen coefficients determined by sixteen pieces of corner data.
When the derivatives are unknown, as in image processing, they are estimated from neighboring values by finite differences.
