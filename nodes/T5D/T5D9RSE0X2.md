---
tag: T5D9RSE0X2
kind: statement
role: theorem
name: Barbier's theorem
msc: [52A10, 52A38, 53C65]
uses: [B4YD1ZXRVH, 0TH78S7GBZ, 9D5NT00H6G]
about: [B4YD1ZXRVH]
sources:
  - url: https://en.wikipedia.org/wiki/Barbier%27s_theorem
same_as:
  wikidata: Q1188048
  wikipedia: Barbier's theorem
---

## Statement

Let $w > 0$, and let $C$ be a [[curve of constant width|B4YD1ZXRVH]] $w$ in the plane.
Then the [[length|0TH78S7GBZ]] of $C$ is $\pi w$.

## Remarks

Apply the [[Crofton formula|9D5NT00H6G]] to $C$.
A line that meets the interior of the convex body bounded by $C$ meets $C$ in exactly two points.
The lines with normal direction $\theta$ that meet the body form a band of width $w(\theta)$.
So the length of $C$ is $\frac{1}{2} \int_0^\pi 2 \, w(\theta) \, d\theta = \int_0^\pi w \, d\theta = \pi w$.
Example: a circle of diameter $w$ has length $\pi w$, and the Reuleaux triangle of width $w$, made of three arcs of radius $w$ and angle $\pi/3$, also has length $\pi w$.
The hypothesis of constant width is needed: the square of side $1$ has width $1$ in the direction of its sides, but its perimeter is $4$, not $\pi$.

## Explanations

### L1 human

All shapes that have the same width in every direction also have the same perimeter, namely $\pi$ times the width.
So a Reuleaux triangle of width $1$ and a coin of diameter $1$ need exactly the same length of string to go around them.

### L2 human

The proof shows a more general fact: the perimeter of any plane convex body equals the integral of its width over the directions in $[0, \pi)$, which is Cauchy's formula.
Barbier's theorem is the special case of a constant integrand.
Together with the isoperimetric inequality it shows that the disc has the largest area among bodies of constant width $w$; the smallest area is the subject of the Blaschke–Lebesgue theorem.
