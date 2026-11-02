---
tag: V2SBN1FNQV
kind: concept
name: Epsilon-net of a set system
msc: [52C45, 68U05, 05D05]
sources:
  - url: https://en.wikipedia.org/wiki/Ε-net_(computational_geometry)
same_as:
  wikidata: Q8083987
  wikipedia: Ε-net (computational geometry)
---

## Summary

An $\varepsilon$-net of a [[family of sets|0C21Q694AG]] is a subset of the ground set that meets every large member of the family.
Here large means that the member holds at least an $\varepsilon$ fraction of the points.
It is a small sample that is guaranteed to hit every heavy range.
The $\varepsilon$-net theorem of Haussler and Welzl says that families of [[VC dimension|KCFXR9K3GD]] $d$ have $\varepsilon$-nets of size $O\big(\frac{d}{\varepsilon} \log \frac{d}{\varepsilon}\big)$, independent of the number of points.
This makes $\varepsilon$-nets a central tool in computational geometry and learning theory.

## Explanations

### L1 human

Suppose there are many points in the plane and many possible regions, such as all half-planes.
An $\varepsilon$-net is a handful of the points chosen so that every region containing a fair share of all points contains at least one chosen point.
For example, take $100$ points on a line, with intervals as the ranges.
The points in positions $10, 20, \dots, 100$ form a $1/10$-net: any interval with at least $10$ of the points contains one of these.
A random sample of the right size works with high probability when the regions are simple.
This is unrelated to the $\varepsilon$-nets of metric spaces, which cover a space by small balls.
