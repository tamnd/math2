---
tag: WZ42B0SAVM
kind: problem
name: Kakeya needle problem
msc: [28A75, 52A38]
uses: [2Z2QVWZ262]
about: [6PEN7AKC7M]
sources:
  - url: https://en.wikipedia.org/wiki/Kakeya_set
history:
  posed_by: "Sōichi Kakeya"
  first_stated: "1917"
---

## Problem

A needle is a line segment of length $1$ in the plane $\R^2$.
Find the smallest area, in the sense of [[Lebesgue measure|2Z2QVWZ262]], of a region $R \subset \R^2$ with the following property.
The needle can be moved continuously inside $R$ so that it ends in its starting position with its two ends exchanged.

## Remarks

The problem is solved, and the answer is that there is no positive minimum.
Abram Besicovitch showed that for every $\varepsilon > 0$ there is a region of area less than $\varepsilon$ in which the needle can be turned around.
His construction builds on a set of measure zero that contains a unit segment in every direction, an example of a [[Kakeya set|6PEN7AKC7M]].
If $R$ is required to be convex, the minimum exists: it is the equilateral triangle of height $1$, of area $1/\sqrt{3}$, a result of Julius Pál.

## Explanations

### L1 human

Imagine a stick of length one lying on a table, and you must turn it to face the other way while keeping it inside a painted region.
A disc of diameter one works, with area about $0.785$, and a triangle of height one does better.
Surprisingly, with clever back-and-forth moves the painted region can be made as small in area as you like.
