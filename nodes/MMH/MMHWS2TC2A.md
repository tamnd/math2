---
tag: MMHWS2TC2A
kind: problem
name: Danzer set
msc: [52C17, 52A37, 52C23]
uses: [437FSG3419, 2Z2QVWZ262]
about: [437FSG3419]
sources:
  - url: https://en.wikipedia.org/wiki/Danzer_set
same_as:
  wikidata: Q65121675
  wikipedia: Danzer set
history:
  posed_by: "Ludwig Danzer"
  first_stated: "1965"
---

## Problem

Let $d \ge 2$.
A set $D \subseteq \R^d$ is a *Danzer set* if it meets every [[convex body|437FSG3419]] in $\R^d$ of volume $1$, where volume is [[Lebesgue measure|2Z2QVWZ262]].
Is there a Danzer set $D$ of bounded density?
This means that there is a constant $C$ such that every ball of radius $r \ge 1$ contains at most $C r^d$ points of $D$.

## Remarks

Ludwig Danzer asked the question; it is listed as a problem of Danzer in the proceedings of a convexity colloquium held in Copenhagen in 1965.
The question is open.
Bambah and Woods showed in 1971 that a finite union of lattices is never a Danzer set.
They also constructed Danzer sets with at most $C r^d \log^{d-1} r$ points in a ball of radius $r$, by overlaying rectangular grids of different shapes.
Solomon and Weiss gave a construction with $O(r^d \log r)$ points, and they showed that the vertex sets of substitution tilings, such as Penrose tilings, are not Danzer sets.

## Explanations

### L1 human

Can one scatter points in the plane, not too densely, so that every convex shape of area one contains at least one of them?
Very long and thin shapes are the difficulty: they can slip between the points of any grid.
Adding a little more than a constant density of points is known to be enough.
Whether bounded density suffices is open.
