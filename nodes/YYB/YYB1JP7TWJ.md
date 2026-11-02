---
tag: YYB1JP7TWJ
kind: example
name: Bunimovich stadium
msc: ["37C83", "37A25"]
instance_of: [XWMKYE038F]
uses: [XWMKYE038F, GX9Q2PYNZE]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamical_billiards
---

## Example

Let $a > 0$ and $r > 0$.
The *Bunimovich stadium* is the table $Q \subset \R^2$ made of the rectangle $[-a, a] \times [-r, r]$ and two half-discs of radius $r$.
The half-discs are centred at $(-a, 0)$ and $(a, 0)$ and sit on the short sides of the rectangle.
Its boundary consists of two parallel segments of length $2a$ and two semicircles of radius $r$.
These pieces have a common tangent at the four junctions, so the boundary is a $C^1$ curve.
The table is compact with piecewise smooth boundary, so it carries a [[billiard|XWMKYE038F]] flow.

## Remarks

Bunimovich proved that the billiard in the stadium is ergodic for every $a > 0$.
This was a surprise, because the boundary has no dispersing part: the semicircles are focusing and the segments are flat, unlike the [[Sinai billiard|GX9Q2PYNZE]].
The mechanism is defocusing: a beam focused by a semicircle passes through a focal point and spreads out again before the next reflection, if the free path is long enough.
For $a = 0$ the table is a disc and the billiard is integrable, so the length $a > 0$ of the straight parts is essential.
The stadium also has a family of periodic orbits bouncing between the two flat sides; they fill a set of zero measure, so they do not contradict ergodicity.

## Explanations

### L1 human

Take a round table, cut it in half, and pull the halves apart, joining them with two straight sides; the result looks like a running track.
A ball on a round table keeps the same angle forever, but on the stadium the motion becomes chaotic.
Almost every shot eventually explores the whole table, spending time in each region in proportion to its area.
The stadium is a standard example in the study of quantum chaos.
