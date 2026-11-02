---
tag: JR2BWZEWH1
kind: statement
role: theorem
name: Ultraparallel theorem
msc: [51M10, 51M09]
uses: [GN4N94GQ0Z, NSYMQMHPDN, RHKSMPBSQ1]
about: [GN4N94GQ0Z]
sources:
  - url: https://en.wikipedia.org/wiki/Ultraparallel_theorem
same_as:
  wikidata: Q7880612
  wikipedia: Ultraparallel theorem
---

## Statement

Let $\ell$ and $m$ be two lines of the [[hyperbolic plane|GN4N94GQ0Z]] that do not meet and do not share an ideal endpoint (ultraparallel lines).
Then there is exactly one line that meets both $\ell$ and $m$ at right angles.

## Remarks

Proof idea in the [[Poincaré half-plane model|RHKSMPBSQ1]]: after an isometry, $\ell$ is the imaginary axis and $m$ is the semicircle with centre $c > 0$ and radius $r$ on the real axis.
Since $m$ neither meets $\ell$ nor ends at $0$ or $\infty$, one has $0 < r < c$.
A line meeting $\ell$ at a right angle is a semicircle centred at $0$, of radius $R$ say.
It meets $m$ at a right angle exactly when $R^2 + r^2 = c^2$, so $R = \sqrt{c^2 - r^2}$ is the only choice.
The common perpendicular realizes the distance between $\ell$ and $m$, and the distance between points of $\ell$ and $m$ grows on both sides of it.
Both hypotheses are needed.
Two lines that meet have no common perpendicular, since with it they would bound a triangle with two right angles and a third positive angle, against the angle sum.
Two lines with a common ideal endpoint (limiting parallels) have no common perpendicular either, and the distance between them tends to $0$ toward that endpoint.

## Explanations

### L1 human

In hyperbolic geometry, two lines that never meet come in two kinds.
Some approach each other forever in one direction; the others separate in both directions.
For the second kind, there is exactly one bridge between them that is perpendicular to both, and it marks the place where the lines are closest.

### L2 human

In the Euclidean plane two parallel lines have infinitely many common perpendiculars, all of the same length.
In the hyperbolic plane the ultraparallel case has exactly one, and the limiting parallel case has none.
This gives a clean classification of pairs of distinct lines: intersecting, limiting parallel, or ultraparallel, the last characterized by a unique common perpendicular.
It is used to define the distance between ultraparallel lines, and to build right-angled hexagons and pants decompositions of hyperbolic surfaces.
