---
tag: SQHGJ9C0QE
kind: concept
name: Carleson measure
msc: [30H10, 42B35]
sources:
  - url: https://en.wikipedia.org/wiki/Carleson_measure
same_as:
  wikidata: Q5041178
  wikipedia: Carleson measure
---

## Summary

A Carleson measure is a positive measure on the [[unit disc|8G5ABXRK85]] with a size bound near the boundary.
Its mass in each box touching the boundary is at most a constant times the length of the box.
Carleson showed that these are exactly the measures $\mu$ for which the [[Hardy space|PNNNFJVF6W]] $H^p$ embeds continuously into $L^p(\mu)$.
They appear in the [[corona theorem|WMGA92P2G4]], in interpolation problems and in the duality between $H^1$ and [[BMO|QJYTXFT8Y4]].

## Explanations

### L1 human

Picture a small arc $I$ on the circle and the "box" in the disc that sits just inside it, of depth equal to the length of $I$.
A measure is Carleson if each such box carries mass at most a constant times the length of $I$.
Area measure on the disc is Carleson, since a box of side $\ell$ has area about $\ell^2$, which is at most a constant times $\ell$.
A measure that piles too much mass close to one boundary point is not Carleson.
The condition is exactly what is needed to integrate $\abs{f}^p$ against $\mu$ when $f$ is in $H^p$.
