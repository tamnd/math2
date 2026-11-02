---
tag: 8SETG842RX
kind: example
name: Apollonian gasket
msc: [52C26, 28A80, 52C15]
illustrates: [S360JBEYKD]
uses: [060W5CBZP6, SSNFTHZ6YJ]
sources:
  - url: https://en.wikipedia.org/wiki/Apollonian_gasket
same_as:
  wikidata: Q1184368
  wikipedia: Apollonian gasket
---

## Example

Start with four [[circles|060W5CBZP6]], one enclosing the other three, that are pairwise tangent at six distinct points.
The three inner circles and the outer circle bound four curvilinear triangles.
Into each such curvilinear triangle, insert the unique circle inside it tangent to its three sides.
This creates three new curvilinear triangles.
Repeat forever.
The *Apollonian gasket* is the family of all circles obtained, or the closure of their union.
Apart from the outer circle, which encloses the others, the circles have disjoint interiors, so they form a [[circle packing|S360JBEYKD]].
For the curvatures, take the outer circle with negative sign.
By Descartes' circle theorem, four pairwise tangent circles with curvatures $k_1, k_2, k_3, k_4$ satisfy $(k_1 + k_2 + k_3 + k_4)^2 = 2(k_1^2 + k_2^2 + k_3^2 + k_4^2)$.
Check with the start $(-1, 2, 2, 3)$: an outer circle of radius $1$, two circles of radius $\tfrac12$ and one of radius $\tfrac13$; then $6^2 = 36 = 2(1 + 4 + 4 + 9)$.
Each new circle replaces one curvature $k_4$ by $2(k_1 + k_2 + k_3) - k_4$, so in this gasket all curvatures are integers.

## Remarks

The leftover set, the complement in the outer disc of all open discs, has area zero.
Its [[Hausdorff dimension|SSNFTHZ6YJ]] is about $1.3057$, strictly between $1$ and $2$, so it is a fractal.

## Explanations

### L1 human

Draw three coins that touch each other in pairs, and a large circle around them touching all three.
Fill every curved triangular gap with the largest circle that fits, then fill the smaller gaps, and keep going forever.
The picture becomes a lace of ever smaller circles, the Apollonian gasket.
With a good start, such as curvatures $-1, 2, 2, 3$, every circle in the picture has a whole-number curvature.
