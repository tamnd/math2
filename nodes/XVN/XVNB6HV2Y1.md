---
tag: XVNB6HV2Y1
kind: statement
role: theorem
name: Blaschke–Lebesgue theorem
msc: [52A10, 52A40, 52A38]
uses: [B4YD1ZXRVH, KMNV11B91V, T5D9RSE0X2]
about: [B4YD1ZXRVH]
sources:
  - url: https://en.wikipedia.org/wiki/Blaschke%E2%80%93Lebesgue_theorem
same_as:
  wikidata: Q4925292
  wikipedia: Blaschke–Lebesgue theorem
---

## Statement

Let $w > 0$, and let $K$ be a plane convex body of constant width $w$.
So $K$ is bounded by a [[curve of constant width|B4YD1ZXRVH]] $w$.
Then the area of $K$ is at least $\frac{\pi - \sqrt{3}}{2} w^2$.
Equality holds if and only if $K$ is a [[Reuleaux triangle|KMNV11B91V]] of width $w$.

## Remarks

One classical route approximates $K$ by Reuleaux polygons of width $w$, which are bodies of constant width bounded by finitely many circular arcs of radius $w$.
For Reuleaux polygons one shows that the area can be lowered by deforming the polygon towards a Reuleaux triangle, and a limit argument finishes the proof.
Example: a disc of diameter $w$ has area $\frac{\pi}{4} w^2 \approx 0.785 \, w^2$, while the Reuleaux triangle has area $\frac{\pi - \sqrt{3}}{2} w^2 \approx 0.705 \, w^2$.
The constant width hypothesis is needed: a segment of length $w$ has diameter $w$ and area $0$.

## Explanations

### L1 human

Among all shapes that have the same width $w$ in every direction, the Reuleaux triangle uses the least area.
It is the "thinnest" such shape, while the round disc is the "fattest".

### L2 human

The maximum among bodies of constant width $w$ is the disc, which follows from [[Barbier's theorem|T5D9RSE0X2]] and the isoperimetric inequality, since all such bodies have perimeter $\pi w$.
The minimum is much harder, and the Blaschke–Lebesgue theorem identifies it.
In three dimensions the question of the body of constant width with least volume is open.
